#!/usr/bin/env python3

from pathlib import Path
import json
import re
import sys

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

def natural_key(name):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', name)]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 make_gallery_json.py <folder-name>")
        print("Example: python3 make_gallery_json.py ice-detail")
        sys.exit(1)

    folder = sys.argv[1]
    root = Path(".").resolve()
    image_dir = root / "src" / "assets" / "images" / "photos" / folder
    output_file = root / "src" / "data" / f"{folder}-gallery.json"

    if not image_dir.exists():
        print(f"Missing folder: {image_dir}")
        sys.exit(1)

    files = sorted(
        [p.name for p in image_dir.iterdir()
         if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS],
        key=natural_key
    )

    if not files:
        print(f"No image files found in: {image_dir}")
        sys.exit(1)

    title = folder.replace("-", " ").replace("_", " ").title()

    data = {
        "slug": folder,
        "title": title,
        "folder": folder,
        "images": files
    }

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    print(f"Wrote: {output_file}")
    print(f"Found {len(files)} images in folder '{folder}':")
    for name in files:
        print(" ", name)

if __name__ == "__main__":
    main()
