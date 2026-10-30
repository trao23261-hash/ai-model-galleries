"""One-shot, verified archive uploader. Requires a reviewed upload-plan.json."""
import base64, gzip, hashlib, io, json, pathlib, subprocess, time, urllib.parse, zipfile
ROOT=pathlib.Path.cwd(); BOOT=ROOT/'.archive-bootstrap'

def run(*args):
    return subprocess.run(args,check=True)

def safe_path(name, prefix):
    p=pathlib.PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or not name.startswith(prefix+'/'):
        raise ValueError('Unsafe path: '+name)
    return ROOT/p

def verify(x):
    p=safe_path(x['repository_path'],plan['directory'])
    d=p.read_bytes()
    if len(d)!=x['bytes'] or hashlib.sha256(d).hexdigest()!=x['sha256'] or hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()!=x['git_blob_sha']:
        raise ValueError('Content mismatch: '+x['repository_path'])

plan=json.loads(gzip.decompress(base64.b64decode((BOOT/'upload-plan.gz.b64').read_text(),validate=True)))
assert plan['directory'] in ('portrait','costume')
assert plan['host']=='ai-'+plan['directory']+'-gallery.pages.dev'
expected=plan['files']; bypath={x['repository_path']:x for x in expected}
assert len(bypath)==len(expected)
blob=base64.b64decode(''.join((BOOT/n).read_text() for n in plan['metadata_parts']),validate=True)
with zipfile.ZipFile(io.BytesIO(blob)) as z:
    for n in z.namelist():safe_path(n,plan['directory'])
    z.extractall(ROOT)
run('git','config','user.name','github-actions[bot]')
run('git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com')
start=time.time()
for bi,batch in enumerate(plan['batches'],1):
    assert sum(bypath[n]['bytes'] for n in batch)<=750_000_000
    config=BOOT/'curl.conf'; downloads=[]
    for name in batch:
        x=bypath[name]; p=safe_path(name,plan['directory'])
        if p.is_file():
            verify(x)
            continue
        u=urllib.parse.urlsplit(x['source_url'])
        if u.scheme!='https' or u.netloc not in (plan['host'],'fonts.gstatic.com'):raise ValueError('Unexpected origin')
        p.parent.mkdir(parents=True,exist_ok=True)
        downloads.append('fail\nsilent\nshow-error\nretry = 3\nretry-delay = 2\nconnect-timeout = 20\nmax-time = 90\nurl = '+json.dumps(x['source_url'])+'\noutput = '+json.dumps(str(p))+'\n')
    if downloads:
        config.write_text('next\n'.join(downloads))
        run('curl','--parallel','--parallel-max','4','--parallel-immediate','--config',str(config))
    for name in batch:verify(bypath[name])
    names=BOOT/'add-files'; names.write_bytes(b'\0'.join(n.encode() for n in batch)+b'\0')
    run('git','add','--pathspec-from-file='+str(names),'--pathspec-file-nul')
    if subprocess.run(['git','diff','--cached','--quiet']).returncode:
        run('git','commit','-m',f"Archive verified {plan['directory']} assets batch {bi}/{len(plan['batches'])}")
        run('git','push','origin','HEAD:main')
    print(json.dumps({'batch':bi,'total':len(plan['batches']),'status':'verified and pushed'}),flush=True)
for x in expected:verify(x)
report={'status':'verified','verified_files':len(expected),'verified_bytes':sum(x['bytes'] for x in expected),'missing_or_mismatched':0,'elapsed_seconds':round(time.time()-start,1),'coverage':'All listed files from captured public frontend; excludes unknown backend/build/unlinked files.'}
(ROOT/plan['directory']/'github-upload-verification.json').write_text(json.dumps(report,indent=2)+'\n')
run('git','add',plan['directory']+'/')
run('git','rm','-r','.archive-bootstrap/')
run('git','commit','-m','Complete verified '+plan['directory']+' archive and remove bootstrap inputs')
run('git','push','origin','HEAD:main')
print(json.dumps(report),flush=True)
