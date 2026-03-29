#!/usr/bin/env python3
"""
Pirjo Pesonen — Thumbnail Crop Editor
======================================
Double-click this file to start.

What happens automatically:
  1. The website builder starts in the background
  2. The crop editor opens in your browser
  3. The live website opens in another tab

How to adjust a thumbnail:
  - Click on any thumbnail to open the crop editor for that photo
  - Drag the photo around to choose which part shows in the square thumbnail
  - Click "Save this crop" when happy
  - Click "Save All Changes" to write everything to the website files
  - Wait a few seconds, then refresh the website tab to see the result

To stop: close the browser tabs, then close this window.
"""

import os, re, json, threading, webbrowser, subprocess, time, sys
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT        = 8765
SITE_PORT   = 8080
GALLERY_DIR = "src/gallery"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ── Read gallery images ────────────────────────────────────────────────────

def find_pages():
    pages = []
    for root, dirs, files in os.walk(GALLERY_DIR):
        depth = root.replace(GALLERY_DIR, "").count(os.sep)
        if depth < 2:
            continue
        for fname in files:
            if fname == "index.md":
                path = os.path.join(root, fname)
                images = extract_images(path)
                if images:
                    rel = os.path.relpath(root, GALLERY_DIR)
                    title = rel.replace("/", " › ").replace("-", " ").title()
                    pages.append({"path": path, "title": title, "images": images})
    pages.sort(key=lambda p: p["path"])
    return pages

def extract_images(md_path):
    with open(md_path) as f:
        content = f.read()
    images = []
    for m in re.finditer(r'<img\s[^>]*src="([^"]+)"[^>]*>', content):
        tag = m.group(0)
        src = m.group(1)
        if 'id="lightbox-image"' in tag or not src.startswith('/assets/'):
            continue
        pos_match = re.search(r'object-position:\s*([^;"]+)', tag)
        position = pos_match.group(1).strip() if pos_match else "50% 50%"
        images.append({"src": src, "position": position})
    return images

# ── Save positions ─────────────────────────────────────────────────────────

def apply_positions(md_path, positions):
    with open(md_path) as f:
        content = f.read()
    img_tags = [m for m in re.finditer(r'<img\s[^>]*src="([^"]+)"[^>]*>', content)
                if 'id="lightbox-image"' not in m.group(0)
                and m.group(1).startswith('/assets/')]
    if len(img_tags) != len(positions):
        return False, f"Image count mismatch in {md_path}"
    for m, pos in reversed(list(zip(img_tags, positions))):
        tag = m.group(0)
        tag = re.sub(r'object-position:\s*[^;"]+;?\s*', '', tag)
        tag = re.sub(r'\s*style="\s*"', '', tag)
        if 'style="' in tag:
            tag = tag.replace('style="', f'style="object-position: {pos}; ', 1)
        else:
            tag = tag.replace('<img ', f'<img style="object-position: {pos};" ', 1)
        content = content[:m.start()] + tag + content[m.end():]
    with open(md_path, 'w') as f:
        f.write(content)
    return True, "ok"

# ── HTML ───────────────────────────────────────────────────────────────────

def build_html(pages):
    pages_json = json.dumps(pages)
    site_url   = f"http://localhost:{SITE_PORT}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pirjo — Crop Editor</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: Arial, sans-serif; background: #1a1a1a; color: #eee; padding: 24px 24px 100px; }}
  h1 {{ font-size: 24px; margin-bottom: 4px; }}
  .subtitle {{ color: #888; font-size: 14px; margin-bottom: 16px; }}
  .tip {{
    background: #2a2a2a; border: 1px solid #444; border-radius: 8px;
    padding: 12px 16px; margin-bottom: 10px; font-size: 14px;
    line-height: 1.8; color: #bbb;
  }}
  .tip strong {{ color: #fff; }}
  .site-link {{
    display: inline-block; margin-bottom: 24px;
    background: #1a3a1a; border: 1px solid #4caf50; border-radius: 6px;
    padding: 7px 14px; color: #7cfc00; font-size: 13px; text-decoration: none;
  }}
  .series {{ margin-bottom: 32px; }}
  .series-title {{
    font-size: 13px; font-weight: bold; color: #999;
    margin-bottom: 10px; padding-bottom: 5px;
    border-bottom: 1px solid #333; text-transform: uppercase; letter-spacing: 0.06em;
  }}
  .grid {{ display: flex; flex-wrap: wrap; gap: 12px; }}
  .card {{ display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; }}
  .thumb {{
    width: 120px; height: 120px; overflow: hidden;
    border: 2px solid #444; border-radius: 3px;
    transition: border-color 0.15s;
  }}
  .card:hover .thumb {{ border-color: #888; }}
  .thumb.changed {{ border-color: #7cfc00; }}
  .thumb img {{
    width: 100%; height: 100%;
    object-fit: cover; pointer-events: none; display: block;
  }}
  .img-name {{ font-size: 10px; color: #555; max-width: 120px; text-align: center; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}

  /* Modal */
  .overlay {{
    display: none; position: fixed; inset: 0;
    background: rgba(0,0,0,0.88); z-index: 100;
    align-items: center; justify-content: center;
  }}
  .overlay.open {{ display: flex; }}
  .modal {{
    background: #222; border: 1px solid #555; border-radius: 10px;
    padding: 24px; max-width: 380px; width: 95vw;
  }}
  .modal h2 {{ font-size: 15px; margin-bottom: 3px; color: #eee; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .modal .hint {{ font-size: 13px; color: #777; margin-bottom: 14px; }}

  .crop-frame {{
    width: 320px; height: 320px;
    overflow: hidden; border: 3px solid #7cfc00;
    border-radius: 4px; position: relative;
    cursor: grab; user-select: none; margin: 0 auto 16px;
  }}
  .crop-frame:active {{ cursor: grabbing; }}
  .crop-frame img {{
    position: absolute;
    pointer-events: none;
    display: block;
  }}

  .modal-btns {{ display: flex; gap: 10px; justify-content: flex-end; }}
  .btn {{ padding: 9px 20px; border-radius: 6px; border: none; font-size: 14px; cursor: pointer; font-weight: bold; }}
  .btn-save {{ background: #4caf50; color: white; }}
  .btn-save:hover {{ background: #66bb6a; }}
  .btn-cancel {{ background: #333; color: #ccc; border: 1px solid #555; }}
  .btn-cancel:hover {{ background: #444; }}

  .save-bar {{
    position: fixed; bottom: 0; left: 0; right: 0;
    background: #111; border-top: 1px solid #333;
    padding: 12px 24px; display: flex; align-items: center; gap: 16px; z-index: 99;
  }}
  .save-all-btn {{
    background: #4caf50; color: white; border: none;
    padding: 11px 28px; font-size: 15px; border-radius: 6px;
    cursor: pointer; font-weight: bold;
  }}
  .save-all-btn:hover {{ background: #66bb6a; }}
  .save-all-btn:disabled {{ background: #555; cursor: default; }}
  .status {{ font-size: 14px; color: #888; }}
  .changed-count {{ color: #7cfc00; font-weight: bold; }}
  .ok  {{ color: #7cfc00; }}
  .err {{ color: #ff6b6b; }}
</style>
</head>
<body>

<h1>Thumbnail Crop Editor</h1>
<p class="subtitle">Pirjo Pesonen Website</p>

<div class="tip">
  <strong>How to use:</strong> Click any thumbnail to open it for editing.
  Drag the photo inside the green frame to choose what shows in the thumbnail.
  Click <strong>Save this crop</strong>, then when all done click <strong>Save All Changes</strong>.
</div>

<a class="site-link" href="{site_url}" target="_blank">🌐 Open website →</a>

<div id="gallery"></div>

<div class="overlay" id="overlay">
  <div class="modal">
    <h2 id="modal-title">Adjust crop</h2>
    <p class="hint">Drag the photo to reposition it inside the green frame.</p>
    <div class="crop-frame" id="crop-frame">
      <img id="crop-img" src="" alt="">
    </div>
    <div class="modal-btns">
      <button class="btn btn-cancel" onclick="closeModal()">Cancel</button>
      <button class="btn btn-save" onclick="saveCrop()">Save this crop</button>
    </div>
  </div>
</div>

<div class="save-bar">
  <button class="save-all-btn" id="save-btn" onclick="saveAll()">💾 Save All Changes</button>
  <span class="status">Changed: <span class="changed-count" id="count">0</span> photos &nbsp; <span id="save-status"></span></span>
</div>

<script>
const pages = {pages_json};
const original = {{}};
const current  = {{}};

const FRAME = 320;
let modalKey = null;
let imgNatW = 0, imgNatH = 0;
let imgDisplayW = 0, imgDisplayH = 0;
let imgX = 0, imgY = 0;
let dragging = false;
let dragStartX, dragStartY, dragStartImgX, dragStartImgY;

function key(pi, ii) {{ return pi + '_' + ii; }}

function buildGallery() {{
  const gallery = document.getElementById('gallery');
  pages.forEach((page, pi) => {{
    const sec = document.createElement('div');
    sec.className = 'series';
    sec.innerHTML = `<div class="series-title">${{page.title}}</div>`;
    const grid = document.createElement('div');
    grid.className = 'grid';
    page.images.forEach((img, ii) => {{
      const k = key(pi, ii);
      original[k] = img.position;
      current[k]  = img.position;
      const card = document.createElement('div');
      card.className = 'card';
      card.title = 'Click to adjust crop';
      const thumb = document.createElement('div');
      thumb.className = 'thumb';
      thumb.id = 'thumb-' + k;
      const imgEl = document.createElement('img');
      imgEl.src = img.src;
      imgEl.style.objectPosition = img.position;
      thumb.appendChild(imgEl);
      const name = document.createElement('div');
      name.className = 'img-name';
      name.textContent = img.src.split('/').pop().replace(/\\.[^.]+$/, '');
      card.appendChild(thumb);
      card.appendChild(name);
      card.addEventListener('click', () => openModal(pi, ii));
      grid.appendChild(card);
    }});
    sec.appendChild(grid);
    gallery.appendChild(sec);
  }});
}}

function openModal(pi, ii) {{
  const k = key(pi, ii);
  modalKey = k;
  const img = pages[pi].images[ii];
  document.getElementById('modal-title').textContent =
    pages[pi].title + ' — ' + img.src.split('/').pop().replace(/\\.[^.]+$/, '');
  const cropImg = document.getElementById('crop-img');
  cropImg.onload = () => {{
    imgNatW = cropImg.naturalWidth;
    imgNatH = cropImg.naturalHeight;
    // Scale so shorter side fills the frame
    const scale = Math.max(FRAME / imgNatW, FRAME / imgNatH);
    imgDisplayW = Math.round(imgNatW * scale);
    imgDisplayH = Math.round(imgNatH * scale);
    // Set initial position from saved object-position
    const parts = current[k].split(' ');
    const px = parseFloat(parts[0]) / 100;
    const py = parseFloat(parts[1] !== undefined ? parts[1] : parts[0]) / 100;
    imgX = -Math.round((imgDisplayW - FRAME) * px);
    imgY = -Math.round((imgDisplayH - FRAME) * py);
    applyTransform();
  }};
  cropImg.src = img.src;
  document.getElementById('overlay').classList.add('open');
}}

function applyTransform() {{
  const img = document.getElementById('crop-img');
  img.style.width  = imgDisplayW + 'px';
  img.style.height = imgDisplayH + 'px';
  img.style.left   = imgX + 'px';
  img.style.top    = imgY + 'px';
}}

function clamp(v, lo, hi) {{ return Math.max(lo, Math.min(hi, v)); }}

const frame = document.getElementById('crop-frame');

frame.addEventListener('mousedown', e => {{
  dragging = true;
  dragStartX = e.clientX; dragStartY = e.clientY;
  dragStartImgX = imgX; dragStartImgY = imgY;
  e.preventDefault();
}});
window.addEventListener('mousemove', e => {{
  if (!dragging) return;
  imgX = clamp(dragStartImgX + e.clientX - dragStartX, -(imgDisplayW - FRAME), 0);
  imgY = clamp(dragStartImgY + e.clientY - dragStartY, -(imgDisplayH - FRAME), 0);
  applyTransform();
}});
window.addEventListener('mouseup', () => dragging = false);

frame.addEventListener('touchstart', e => {{
  const t = e.touches[0];
  dragging = true;
  dragStartX = t.clientX; dragStartY = t.clientY;
  dragStartImgX = imgX; dragStartImgY = imgY;
  e.preventDefault();
}}, {{passive: false}});
window.addEventListener('touchmove', e => {{
  if (!dragging) return;
  const t = e.touches[0];
  imgX = clamp(dragStartImgX + t.clientX - dragStartX, -(imgDisplayW - FRAME), 0);
  imgY = clamp(dragStartImgY + t.clientY - dragStartY, -(imgDisplayH - FRAME), 0);
  applyTransform();
}}, {{passive: false}});
window.addEventListener('touchend', () => dragging = false);

function saveCrop() {{
  const ox = imgDisplayW - FRAME;
  const oy = imgDisplayH - FRAME;
  const px = ox > 0 ? Math.round((-imgX / ox) * 100) : 50;
  const py = oy > 0 ? Math.round((-imgY / oy) * 100) : 50;
  const pos = px + '% ' + py + '%';
  current[modalKey] = pos;
  const thumb = document.getElementById('thumb-' + modalKey);
  if (thumb) {{
    thumb.querySelector('img').style.objectPosition = pos;
    thumb.classList.toggle('changed', pos !== original[modalKey]);
  }}
  updateCount();
  closeModal();
}}

function closeModal() {{
  document.getElementById('overlay').classList.remove('open');
  modalKey = null;
}}

document.getElementById('overlay').addEventListener('click', e => {{
  if (e.target === document.getElementById('overlay')) closeModal();
}});

function updateCount() {{
  document.getElementById('count').textContent =
    Object.keys(current).filter(k => current[k] !== original[k]).length;
}}

function saveAll() {{
  const btn = document.getElementById('save-btn');
  const statusEl = document.getElementById('save-status');
  btn.disabled = true; btn.textContent = 'Saving…'; statusEl.textContent = '';
  const payload = {{}};
  pages.forEach((page, pi) => {{
    payload[page.path] = page.images.map((_, ii) => current[key(pi, ii)]);
  }});
  fetch('/save', {{
    method: 'POST',
    headers: {{'Content-Type': 'application/json'}},
    body: JSON.stringify(payload)
  }})
  .then(r => r.json())
  .then(data => {{
    if (data.ok) {{
      statusEl.className = 'ok';
      statusEl.textContent = '✓ Saved! Wait a few seconds, then refresh the website tab.';
      Object.keys(current).forEach(k => original[k] = current[k]);
      document.querySelectorAll('.thumb.changed').forEach(t => t.classList.remove('changed'));
      updateCount();
    }} else {{
      statusEl.className = 'err';
      statusEl.textContent = '✗ Error: ' + data.error;
    }}
    btn.disabled = false; btn.textContent = '💾 Save All Changes';
  }})
  .catch(() => {{
    statusEl.className = 'err';
    statusEl.textContent = '✗ Could not save. Is AdjustCrops.py still running?';
    btn.disabled = false; btn.textContent = '💾 Save All Changes';
  }});
}}

buildGallery();
</script>
</body>
</html>
"""

# ── HTTP handler ───────────────────────────────────────────────────────────

class Handler(BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        pass

    def do_GET(self):
        if self.path in ("/", "/editor"):
            pages = find_pages()
            html = build_html(pages)
            self._respond(200, "text/html; charset=utf-8", html.encode())
        elif self.path.startswith("/assets/"):
            candidates = [
                os.path.join("dist", self.path.lstrip("/")),
                self.path.lstrip("/"),
                os.path.join("src", self.path.lstrip("/")),
            ]
            file_path = next((p for p in candidates if os.path.exists(p)), None)
            if file_path:
                ext = os.path.splitext(file_path)[1].lower().lstrip(".")
                mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg",
                        "png": "image/png", "gif": "image/gif"}.get(ext, "application/octet-stream")
                with open(file_path, "rb") as f:
                    self._respond(200, mime, f.read())
            else:
                self._respond(404, "text/plain", b"Not found")
        else:
            self._respond(404, "text/plain", b"Not found")

    def do_POST(self):
        if self.path == "/save":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                all_positions = json.loads(body)
                errors = []
                for md_path, positions in all_positions.items():
                    ok, msg = apply_positions(md_path, positions)
                    if not ok:
                        errors.append(msg)
                result = {"ok": not errors}
                if errors:
                    result["error"] = "; ".join(errors)
            except Exception as e:
                result = {"ok": False, "error": str(e)}
            self._respond(200, "application/json", json.dumps(result).encode())

    def _respond(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

# ── Start npm run serve ────────────────────────────────────────────────────

def start_site_builder():
    print("  Starting website builder...")
    npm = "npm"
    if sys.platform == "darwin":
        for path in ["/usr/local/bin/npm", "/opt/homebrew/bin/npm"]:
            if os.path.exists(path):
                npm = path
                break
    subprocess.Popen(
        [npm, "run", "serve"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(4)

# ── Main ───────────────────────────────────────────────────────────────────

def main():
    print()
    print("=" * 50)
    print("   Pirjo — Thumbnail Crop Editor")
    print("=" * 50)
    start_site_builder()
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"  Crop editor: http://localhost:{PORT}")
    print(f"  Website:     http://localhost:{SITE_PORT}")
    print()
    print("  Opening browser tabs...")
    print("  Close this window when finished.")
    print("=" * 50)

    def open_tabs():
        time.sleep(1)
        webbrowser.open(f"http://localhost:{PORT}")
        time.sleep(1)
        webbrowser.open(f"http://localhost:{SITE_PORT}")

    threading.Thread(target=open_tabs, daemon=True).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")

if __name__ == "__main__":
    main()
