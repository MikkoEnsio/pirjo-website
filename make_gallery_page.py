#!/usr/bin/env python3

from pathlib import Path
import re
import sys

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".JPG", ".JPEG", ".PNG", ".WEBP", ".GIF"}

def natural_key(name):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', name)]

def pretty_title(filename):
    stem = Path(filename).stem
    text = stem.replace("_", " ").replace("-", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:1].upper() + text[1:] if text else stem

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 make_gallery_page.py <folder-name> <page-title>")
        print('Example: python3 make_gallery_page.py ice-detail "Ice detail"')
        sys.exit(1)

    folder = sys.argv[1]
    page_title = sys.argv[2]

    root = Path(".").resolve()
    image_dir = root / "src" / "assets" / "images" / "photos" / folder
    output_dir = root / "src" / "gallery" / "photos" / folder
    output_file = output_dir / "index.md"

    if not image_dir.exists():
        print(f"Missing folder: {image_dir}")
        sys.exit(1)

    files = sorted(
        [p.name for p in image_dir.iterdir()
         if p.is_file() and p.suffix in IMAGE_EXTENSIONS],
        key=natural_key
    )

    # Usually cover image should not appear inside the gallery itself
    files = [f for f in files if f.lower() != "cover.jpg" and f.lower() != "cover.jpeg"
             and f.lower() != "cover.png" and f.lower() != "cover.webp"]

    if not files:
        print(f"No gallery image files found in: {image_dir}")
        sys.exit(1)

    grid_lines = []
    image_lines = []
    title_lines = []

    for i, name in enumerate(files):
        img_path = f"/assets/images/photos/{folder}/{name}"
        alt = pretty_title(name)

        grid_lines.append(
            f'  <a href="#" onclick="openLightbox({i}); return false;"><img src="{img_path}" alt="{alt}"></a>'
        )
        comma = "," if i < len(files) - 1 else ""
        image_lines.append(f'    "{img_path}"{comma}')
        title_lines.append(f'    "{alt}"{comma}')

    js_name = re.sub(r'[^A-Za-z0-9_]', '_', folder) + "Images"
    js_titles = re.sub(r'[^A-Za-z0-9_]', '_', folder) + "Titles"

    content = f'''---
title: {page_title}
layout: base.njk
---
# {page_title}

<div class="gallery-grid">
{chr(10).join(grid_lines)}
</div>

<div id="lightbox" class="lightbox" onclick="lightboxBackgroundClick(event)">
  <button type="button" class="lightbox-close" onclick="closeLightbox(event)">×</button>
  <button type="button" class="lightbox-prev" onclick="prevImage(event)">‹</button>

  <div class="lightbox-content" onclick="event.stopPropagation()">
    <img id="lightbox-image" class="lightbox-image" src="" alt="">
    <div id="lightbox-caption" class="lightbox-caption"></div>
  </div>

  <button type="button" class="lightbox-next" onclick="nextImage(event)">›</button>
</div>

<script>
  const {js_name} = [
{chr(10).join(image_lines)}
  ];

  const {js_titles} = [
{chr(10).join(title_lines)}
  ];

  let currentImageIndex = 0;

  function updateLightbox() {{
    const lightboxImage = document.getElementById("lightbox-image");
    const lightboxCaption = document.getElementById("lightbox-caption");
    lightboxImage.src = {js_name}[currentImageIndex];
    lightboxImage.alt = {js_titles}[currentImageIndex];
    lightboxCaption.textContent = {js_titles}[currentImageIndex];
  }}

  function openLightbox(index) {{
    currentImageIndex = index;
    updateLightbox();
    document.getElementById("lightbox").style.display = "flex";
  }}

  function closeLightbox(event) {{
    if (event) event.stopPropagation();
    document.getElementById("lightbox").style.display = "none";
  }}

  function prevImage(event) {{
    event.stopPropagation();
    currentImageIndex = (currentImageIndex - 1 + {js_name}.length) % {js_name}.length;
    updateLightbox();
  }}

  function nextImage(event) {{
    event.stopPropagation();
    currentImageIndex = (currentImageIndex + 1) % {js_name}.length;
    updateLightbox();
  }}

  function lightboxBackgroundClick(event) {{
    if (event.target.id === "lightbox") {{
      closeLightbox();
    }}
  }}

  document.addEventListener("keydown", function(event) {{
    const lightbox = document.getElementById("lightbox");
    if (lightbox.style.display !== "flex") return;

    if (event.key === "Escape") closeLightbox();
    if (event.key === "ArrowLeft") {{
      currentImageIndex = (currentImageIndex - 1 + {js_name}.length) % {js_name}.length;
      updateLightbox();
    }}
    if (event.key === "ArrowRight") {{
      currentImageIndex = (currentImageIndex + 1) % {js_name}.length;
      updateLightbox();
    }}
  }});
</script>
'''

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file.write_text(content, encoding="utf-8")

    print(f"Wrote: {output_file}")
    print(f"Used {len(files)} images from: {image_dir}")
    for name in files:
        print(" ", name)

if __name__ == "__main__":
    main()
