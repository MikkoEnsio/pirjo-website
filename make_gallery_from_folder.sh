#!/bin/zsh

# ============================================================================
# make_gallery_from_folder.sh
#
# Purpose
# -------
# Generate one gallery page for the Pirjo website from images stored in:
#
#   src/assets/images/photos/<gallery-slug>/
#
# The generated page is written to:
#
#   src/gallery/photos/<gallery-slug>/index.md
#
# This script follows the exact working gallery structure already verified in
# the project (Smoke, Suomenlinna, Ferry Trip Views). That means it creates:
#
# - the thumbnail grid
# - the full lightbox HTML block
# - gallery-specific JavaScript image and title arrays
# - lightbox navigation functions
#
# Why this exact structure is needed
# ----------------------------------
# The current site does not use a generic shared lightbox variable.
# Each gallery page needs its own full lightbox setup, including gallery-
# specific array names in JavaScript.
#
# Fixed project conventions
# -------------------------
# 1. Photos are always read only from:
#      src/assets/images/photos/<gallery-slug>/
#
# 2. Gallery pages are always written only to:
#      src/gallery/photos/<gallery-slug>/index.md
#
# 3. If a gallery slug contains hyphens, those must NOT be used directly in
#    JavaScript variable names. Therefore the script also needs a JS variable
#    root, e.g.:
#
#      slug:   ferry-trip-views
#      jsroot: ferryTripViews
#
# Usage
# -----
# Run from the project root:
#
#   zsh tools/make_gallery_from_folder.sh tulips "Tulips" tulips
#
#   zsh tools/make_gallery_from_folder.sh ferry-trip-views "Ferry Trip Views" ferryTripViews
#
# Arguments
# ---------
# $1 = gallery slug
# $2 = gallery title
# $3 = JavaScript variable root
#
# Notes
# -----
# - Image order follows filename order in the folder.
# - Visible titles/captions are derived from filenames:
#     extension removed
#     "_" replaced with spaces
#     "-" replaced with spaces
# - If you rename files in Finder, run this script again to update the page.
# - This script assumes the gallery images are already in the correct folder.
#
# ============================================================================

set -e

if [ $# -lt 3 ]; then
  echo "Usage:"
  echo "  zsh tools/make_gallery_from_folder.sh <gallery-slug> <Gallery Title> <js-variable-root>"
  echo
  echo "Examples:"
  echo '  zsh tools/make_gallery_from_folder.sh tulips "Tulips" tulips'
  echo '  zsh tools/make_gallery_from_folder.sh ferry-trip-views "Ferry Trip Views" ferryTripViews'
  exit 1
fi

SLUG="$1"
TITLE="$2"
JSROOT="$3"

IMAGE_DIR="src/assets/images/photos/$SLUG"
PAGE_DIR="src/gallery/photos/$SLUG"
PAGE_FILE="$PAGE_DIR/index.md"

mkdir -p "$PAGE_DIR"

if ! find "$IMAGE_DIR" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \) | grep -q .; then
  echo "No image files found in $IMAGE_DIR"
  exit 1
fi

cat > "$PAGE_FILE" <<EOF
---
title: $TITLE
layout: base.njk
---
# $TITLE

<div class="gallery-grid">
EOF

i=0
for img in "$IMAGE_DIR"/*; do
  [ -f "$img" ] || continue
  case "${img:l}" in
    *.jpg|*.jpeg|*.png|*.webp) ;;
    *) continue ;;
  esac

  filename="$(basename "$img")"
  alt="${filename%.*}"
  alt="${alt//_/ }"
  alt="${alt//-/ }"

  cat >> "$PAGE_FILE" <<EOF
  <a href="#" onclick="openLightbox($i); return false;"><img src="/assets/images/photos/$SLUG/$filename" alt="$alt"></a>
EOF

  i=$((i+1))
done

cat >> "$PAGE_FILE" <<EOF
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
  const ${JSROOT}Images = [
EOF

first=1
for img in "$IMAGE_DIR"/*; do
  [ -f "$img" ] || continue
  case "${img:l}" in
    *.jpg|*.jpeg|*.png|*.webp) ;;
    *) continue ;;
  esac

  filename="$(basename "$img")"

  if [ $first -eq 1 ]; then
    first=0
  else
    echo "," >> "$PAGE_FILE"
  fi

  printf '    "/assets/images/photos/%s/%s"' "$SLUG" "$filename" >> "$PAGE_FILE"
done

cat >> "$PAGE_FILE" <<EOF

  ];

  const ${JSROOT}Titles = [
EOF

first=1
for img in "$IMAGE_DIR"/*; do
  [ -f "$img" ] || continue
  case "${img:l}" in
    *.jpg|*.jpeg|*.png|*.webp) ;;
    *) continue ;;
  esac

  filename="$(basename "$img")"
  alt="${filename%.*}"
  alt="${alt//_/ }"
  alt="${alt//-/ }"

  if [ $first -eq 1 ]; then
    first=0
  else
    echo "," >> "$PAGE_FILE"
  fi

  printf '    "%s"' "$alt" >> "$PAGE_FILE"
done

cat >> "$PAGE_FILE" <<EOF

  ];

  let currentImageIndex = 0;

  function updateLightbox() {
    const lightboxImage = document.getElementById("lightbox-image");
    const lightboxCaption = document.getElementById("lightbox-caption");
    lightboxImage.src = ${JSROOT}Images[currentImageIndex];
    lightboxImage.alt = ${JSROOT}Titles[currentImageIndex];
    lightboxCaption.textContent = ${JSROOT}Titles[currentImageIndex];
  }

  function openLightbox(index) {
    currentImageIndex = index;
    updateLightbox();
    document.getElementById("lightbox").style.display = "flex";
  }

  function closeLightbox(event) {
    if (event) event.stopPropagation();
    document.getElementById("lightbox").style.display = "none";
  }

  function prevImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex - 1 + ${JSROOT}Images.length) % ${JSROOT}Images.length;
    updateLightbox();
  }

  function nextImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex + 1) % ${JSROOT}Images.length;
    updateLightbox();
  }

  function lightboxBackgroundClick(event) {
    if (event.target.id === "lightbox") {
      closeLightbox();
    }
  }

  document.addEventListener("keydown", function(event) {
    const lightbox = document.getElementById("lightbox");
    if (lightbox.style.display !== "flex") return;

    if (event.key === "Escape") closeLightbox();
    if (event.key === "ArrowLeft") {
      currentImageIndex = (currentImageIndex - 1 + ${JSROOT}Images.length) % ${JSROOT}Images.length;
      updateLightbox();
    }
    if (event.key === "ArrowRight") {
      currentImageIndex = (currentImageIndex + 1) % ${JSROOT}Images.length;
      updateLightbox();
    }
  });
</script>
EOF

echo "Created $PAGE_FILE from images in $IMAGE_DIR"
