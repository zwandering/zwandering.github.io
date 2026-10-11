This is the source code to Jon Barron's public academic website: https://jonbarron.info/. You are welcome to clone this code for your own personal use, just please attribute the source to the original website or to this repo. If you do clone this website, feel free to add an attribution link to your own downstream website in index.html if you want.

## Profile photo

The homepage shows a random photo from `images/profile/` on every visit. The
candidates are listed in `images/profile/photos.txt`, one file name per line.

To add or remove photos:

1. Put the image files (jpg / png / webp / gif / avif) in `images/profile/`.
2. Run `./scripts/update_profile_photos.sh` to regenerate `photos.txt`.
3. Commit both the photos and `photos.txt`.

If the list cannot be loaded (for example when opening `index.html` directly
from disk), the page falls back to `images/profile/me_2.jpg`.
