# POSE-DB-01 public-site backup

Source: https://ai-pose-gallery.pages.dev/
Snapshot: 2026-10-30 UTC. The requester confirmed ownership of this website before bulk image acquisition resumed.

## Open the gallery

Serve this directory with a static HTTP server, then open `offline/index.html`. For example: `python3 -m http.server 8000` and browse `http://localhost:8000/offline/`.

- `original/index.html` is the exact downloaded homepage, with inline CSS, JavaScript and all public gallery metadata unchanged.
- `original/img/` contains the 1,439 original PNG image references.
- `original/thumbs/` contains the corresponding 1,439 JPEG thumbnails.
- `offline/index.html` uses the same original image files without duplicates and omits external Cloudflare analytics. Only paths and the analytics tag differ from the original page.
- `original/beacon.min.js` preserves the linked third-party analytics script for completeness; it is not run by the offline copy.
- `asset-manifest.json` records every image URL, local path, HTTP status, byte size, SHA-256 and decoded dimensions.
- `manifest.json` records the homepage and external script.
- `missing-assets.json` and `coverage-summary.json` state verification and coverage.

## Scope and fidelity

The captured page enumerates 1,439 image records, each with an original and thumbnail. It is a single HTML application: filters, card/pose views and angle/lightbox navigation are client-side states, not separate HTML pages. There are no other internal HTML links. `robots.txt` and `sitemap.xml` both return the same homepage fallback rather than index documents.

This backup covers the deployed public frontend and all image URLs it enumerates. It does not recover original private build tooling, backend code, deployment configuration, unlisted server files or historical versions. Full coverage of arbitrary unknown server files cannot be asserted.

## Rights and content

The original site's notices remain intact, including its restrictions on bulk image download and redistribution. The requester confirmed ownership; this backup does not grant other people a new license. External links and attribution are retained. The linked Cloudflare script is third-party material, not source-site-owned code.

The site describes faceless grey mannequin line drawings. Its metadata includes ordinary, suggestive and intimate pose categories. A category name alone does not establish an image's visual content. Automated decoding checks file integrity, not a complete semantic content review.
