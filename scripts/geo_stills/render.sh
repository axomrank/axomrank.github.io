#!/usr/bin/env bash
# Render every still in stills.js to content/media/<name>.webp at 960×540 with headless Chrome.
# Needs the local server (python3 -m http.server 8770 from the repo root). Safe to rerun.
set -euo pipefail
cd "$(dirname "$0")/../.."
OUT="${TMPDIR:-/home/angsuman/extra_spac/tmp}/geo-stills"; mkdir -p "$OUT"
for n in $(node -e "global.window={};global.document={addEventListener(){},body:null,getElementById(){return null}};require('./app/geofigure.js');global.GEOFIG=window.GEOFIG;require('./scripts/geo_stills/stills.js');console.log(Object.keys(window.STILLS).join(' '))"); do
  png="$OUT/$(echo "$n" | tr / _).png"
  google-chrome --headless=new --disable-gpu --hide-scrollbars --window-size=960,540 --virtual-time-budget=3000 --screenshot="$png" "http://localhost:8770/scripts/geo_stills/still.html?n=$n" >/dev/null 2>&1
  python3 -c "from PIL import Image;im=Image.open('$png').convert('RGB');w=im.width;im.crop((0,0,w,round(w*9/16))).resize((960,540),Image.LANCZOS).save('content/media/$n.webp',quality=88);import os;p='content/media/$n@480.webp';os.path.exists(p) and os.remove(p)"
  echo "rendered $n"
done
