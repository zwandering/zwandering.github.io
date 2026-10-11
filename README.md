This is the source code to Jon Barron's public academic website: https://jonbarron.info/. You are welcome to clone this code for your own personal use, just please attribute the source to the original website or to this repo. If you do clone this website, feel free to add an attribution link to your own downstream website in index.html if you want.

## Profile photo

The homepage shows a random photo from `images/self/` on every visit, with a
caption like `2024 at Hangzhou` underneath. The candidates are listed in
`images/self/photos.json`:

```json
[
  { "file": "Hangzhou_2024.jpg", "year": 2024, "place": "Hangzhou" },
  { "file": "Hawaii_2025.jpg",   "year": 2025, "place": "Hawaii" }
]
```

To add or remove photos:

1. Put the image files (jpg / png / webp / gif / avif) in `images/self/`.
   Keep them web-sized (around 2000 px on the long edge, a few hundred KB).
2. Run `./scripts/update_profile_photos.py`. It adds new files to
   `photos.json` with an empty year/place and drops entries whose file is gone.
3. Fill in `year` and `place` for the new entries.
4. Commit both the photos and `photos.json`.

If the list cannot be loaded (for example when opening `index.html` directly
from disk), the page falls back to `images/self/Hangzhou_2024.jpg`.
