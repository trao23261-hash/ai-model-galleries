# COSTUME-DB-01 public-site backup

Source: https://ai-costume-gallery.pages.dev/ — captured 2026-10-30 UTC.
The requester confirmed ownership before bulk acquisition resumed.

## Open the archive

Serve this directory with a static HTTP server and open `offline/index.html` (for example `python3 -m http.server 8000`, then http://localhost:8000/offline/).

- `original/index.html` preserves the exact public homepage, inline CSS, JavaScript, META and complete D catalog.
- `original/png/`: original PNGs; `original/img/`: display WebP images; `original/thumbs/`: WebP thumbnails. No pixels have been modified or images recompressed.
- `offline/index.html` rewrites paths to those same original binaries, removes the external analytics script, and adds `.morebtn[hidden]{display:none!important}` to repair the original CSS overriding the paginator hidden flag (which otherwise leaves negative remaining counts visible). Original HTML remains byte-for-byte unchanged. No duplicated binary mirror.
- `items.json` is the parsed complete 1,407-entry catalog. Each entry refers to three images, totaling 4,221 references.
- Source notices and third-party community/author links remain intact. External links are not mirrored.

## Coverage and limitations

This is one HTML application, not a collection of server-generated pages. Category/search states and 120-at-a-time pagination are rendered in-browser from the complete catalog. All catalog references are included in the verified archive. This does not recover private build tools, backend implementation, deployment settings, unpublished files or historical versions. Arbitrary unlinked server files cannot be claimed complete.

Original external Cloudflare analytics is retained as provenance when downloaded but is not executed by the offline mirror. Inline SVG icons and CSS are already part of the original HTML; no web fonts are requested by the page.

## Ownership, notices and content

Original notice: 「画像の一括ダウンロード（自動取得を含む）・再配布・転載・販売は禁止です。」

The site restricts bulk acquisition and redistribution to ordinary visitors. The requester explicitly confirmed ownership; this backup does not grant a new public license. The original notices also allow free individual reference/commercial creative use, disclaim warranties and ask users to check third-party rights.

The site describes AI-generated fictional clothing-only reference images without people, including seasonal clothing, party wear, lingerie and swimwear. The description is not a guarantee of exhaustive semantic review; file decoding verifies data integrity. No sexual content was generated or embellished for this archival task.

## Verification

All 4,221 images passed complete Pillow decoding and SHA-256 hashing, with zero missing files. All 4,221 rewritten offline image references resolve. `manifest.json` records original source URL/path/size/SHA; `asset-manifest.json` records image formats/dimensions; `missing-items.json` is empty. `browser-qa.json` documents representative successful UI tests and the offline-only paginator fix. `robots.txt` and `sitemap.xml` return identical homepage fallback; `auxiliary-manifest.json` records that evidence without storing duplicate HTML.
