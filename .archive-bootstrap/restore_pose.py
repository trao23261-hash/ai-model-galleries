"""One-time restoration of the owner's verified public pose archive."""
import base64, concurrent.futures, hashlib, io, json, os, pathlib, subprocess, time, urllib.parse, zipfile
ROOT=pathlib.Path.cwd()
BOOT=ROOT/'.archive-bootstrap'
blob=base64.b64decode((BOOT/'pose-metadata.zip.b64').read_text(), validate=True)
with zipfile.ZipFile(io.BytesIO(blob)) as z:
    for n in z.namelist():
        p=pathlib.PurePosixPath(n)
        if not n.startswith('pose/') or p.is_absolute() or '..' in p.parts:
            raise RuntimeError('Unsafe archive path')
    z.extractall(ROOT)
manifest=json.loads((ROOT/'pose/asset-manifest.json').read_text())['items']
expected=json.loads((ROOT/'pose/expected-files.json').read_text())
config=BOOT/'curl.conf'
with config.open('w') as f:
    for i,item in enumerate(manifest):
        if i: f.write("next\n")
        url=item['source_url']; u=urllib.parse.urlsplit(url)
        rel=pathlib.PurePosixPath(item['local_target_path'])
        if u.scheme!='https' or u.netloc!='ai-pose-gallery.pages.dev' or '..' in rel.parts or rel.is_absolute():
            raise RuntimeError('Unexpected asset origin/path')
        p=ROOT/'pose'/rel; p.parent.mkdir(parents=True,exist_ok=True)
        f.write('fail\nsilent\nshow-error\nretry = 3\nretry-delay = 2\nconnect-timeout = 20\nmax-time = 90\nurl = '+json.dumps(url)+'\noutput = '+json.dumps(str(p))+'\n')
start=time.time()
# No account credentials sent to the source website. Strictly public URLs only.
subprocess.run(['curl','--parallel','--parallel-max','4','--parallel-immediate','--fail','--silent','--show-error','--retry','3','--retry-delay','2','--connect-timeout','20','--max-time','90','--config',str(config)],check=True)
bad=[]
for x in expected:
    p=ROOT/x['repository_path']
    if not p.is_file():bad.append(x['repository_path']+':missing');continue
    d=p.read_bytes()
    sha=hashlib.sha256(d).hexdigest()
    gitsha=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()
    if len(d)!=x['bytes'] or sha!=x['sha256'] or gitsha!=x['git_blob_sha']:bad.append(x['repository_path']+':mismatch')
if bad:raise RuntimeError(json.dumps(bad))
report={'status':'verified','source_url':'https://ai-pose-gallery.pages.dev/','verified_files':len(expected),'verified_bytes':sum(x['bytes'] for x in expected),'images':len(manifest),'missing_or_mismatched':0,'elapsed_seconds':round(time.time()-start,1),'coverage':'All listed files from the captured public frontend; excludes unknown backend/build/unlinked files.'}
(ROOT/'pose/github-upload-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report))

