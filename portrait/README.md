# AI portrait gallery: public static-site archive

Source: https://ai-portrait-gallery.pages.dev/
Capture date: 2026-10-30 UTC.

This directory preserves the site's publicly served HTML, CSS, JavaScript, catalog, original PNGs, WebP thumbnails, a ranking API response snapshot and Google Fonts resources. It does not contain private backend source, server configuration, deployment history or unpublished files.

## Open locally
Serve this directory using a standard static HTTP server, then open `index-offline.html`. For example, Python's built-in `python -m http.server 8000` from this directory. `index.html` is the unchanged original and retains the external Google Fonts reference. `index-offline.html` substitutes the downloaded font CSS, whose font URLs were rewritten to local filenames. Offline HTML also removes remote preconnect hints, keeps its home link on the offline entry, and loads the offline-only application copy described below. No image pixels or source image metadata have been modified.

The site's 1,499 catalog records cover 893 face and 606 styling entries, each with original PNG and WebP thumbnail. Its sections, hair filters, lightbox and 60-at-a-time lazy pagination are client-side states in one page. Capturing all records and references covers those states without creating fictitious server pages.

## Limitations and provenance
- Original `assets/app.js` is unchanged. Offline-only `assets/app-offline.js` disables `/api/hit` telemetry and loads the captured `snapshots/api_ranking` rather than calling a backend.
- Ranking is a capture-time snapshot, not a live service. The original built-in `data/ranking.js` fallback is also preserved.
- `robots.txt` and `sitemap.xml` returned the homepage HTML rather than actual robots or sitemap data; their responses are preserved in `snapshots` as evidence, not claimed as site indexes.
- Third-party social/community links remain external. They are not part of this archive.
- Completeness is bounded to discoverable public files referenced by the inspected page, CSS, JavaScript and full catalog at capture time. No claim is made about unpublished or unlinked server files.

## License and owner notices
The source declares images CC0 1.0 and fictitious AI-generated persons. It permits commercial use, editing and reference use, and says attribution is optional. It separately asks visitors to refrain from redistributing/reposting the image data itself, and prohibits impersonation or uses contrary to public order/morals. Preserve the original notices in `index.html` and respect the owner's request; this archive is intended for the user's private reference, not public republication. The site's CC0 statement about images is not a separate blanket license assertion for every piece of website code or third-party font.

Original Japanese image redistribution courtesy request: 「画像データそのものの再配布・転載はご遠慮ください（お願い）。」
CC0 link published by source: https://creativecommons.org/publicdomain/zero/1.0/deed.ja

`asset-manifest.json` records each image URL, path, byte length and SHA-256. `font-manifest.json` records downloaded fonts. `image-inventory.json` is a parsed copy of the public catalog. All 2,998 images passed SHA-256 recording and full decoding; zero missing files or catalog dimension mismatches. See `checkpoint.json`, `coverage-summary.json`, and `browser-qa.json`. `source-manifest.json` covers original front-end files and captured responses.
