# Pirjo Pesonen Website — Project Documentation

Last updated: March 14, 2026

## What this project is

A personal artist website for Pirjo Pesonen, a Finnish ceramics artist and photographer based in Helsinki. Built with Eleventy (static site generator). The site replaces an existing Wix site at https://www.pirjopesonen.com/

The site is maintained by Pirjo's husband (not a programmer). AI assistance (Claude) is used for all technical work.

---

## The core ideology

Pirjo drops images into a folder, pushes a button, and the gallery updates automatically. No editing of code or templates ever needed to add new images.

---

## Current hosting

- Local development only so far (localhost:8080)
- Deployment target: Netlify + GitHub (not yet set up)
- Output goes to `dist/` folder

---

## CRITICAL — Correct commands

```bash
# Start local development server (ALWAYS use this, not npx directly)
npm run serve

# Build without serving
npm run build

# These are defined in package.json as:
# "build": "npx @11ty/eleventy --input=src --output=dist"
# "serve": "npx @11ty/eleventy --serve --input=src --output=dist"
```

**Important:** Always use `npm run serve` not `npx @11ty/eleventy --serve` — the npm script includes the required `--input=src --output=dist` flags.

---

## Folder structure

```
Pirjo_Website_Project/
├── src/
│   ├── _includes/
│   │   ├── base.njk          # Main HTML template, contains all CSS
│   │   ├── nav.njk           # Navigation bar
│   │   ├── gallery.njk       # Reusable gallery template (exists but not used)
│   │   └── series-index.njk  # NOT used — hardcoded HTML approach used instead
│   ├── _data/
│   │   └── galleries.js      # Auto-reads images (exists but not currently used)
│   ├── assets/
│   │   └── images/
│   │       ├── home/         # Home page image
│   │       ├── artist/       # Artist portrait
│   │       ├── tableware-ceramics/    # DONE — fully working
│   │       │   ├── little-boxes/
│   │       │   ├── jars/
│   │       │   ├── small-bowls/
│   │       │   ├── vase/
│   │       │   ├── morning-bowl/
│   │       │   ├── dishes-and-bowls/
│   │       │   ├── candle-holders/
│   │       │   └── aroma-candle-holder/
│   │       ├── unique-ceramics/       # TODO — folders exist, need images
│   │       │   ├── sculptural-vases/
│   │       │   ├── autumn-plates/
│   │       │   ├── fruit-plates/
│   │       │   ├── new-beginnings/
│   │       │   ├── gull-plates/
│   │       │   ├── big-rooster-and-hens/
│   │       │   ├── vase-red-clay/
│   │       │   ├── jar/
│   │       │   ├── green-bowl/
│   │       │   ├── wall-sconce/
│   │       │   └── rattle-beans/
│   │       ├── art/                   # TODO — folders exist, need images
│   │       │   ├── invisible-moments/
│   │       │   ├── ice-cellar/
│   │       │   ├── paikka-platsen-the-place/
│   │       │   ├── bubblegum-boys/
│   │       │   ├── air-tubes/
│   │       │   ├── whats-next-guldagergaard/
│   │       │   ├── fairytales-and-true-stories/
│   │       │   ├── it-blows/
│   │       │   ├── feuilles-mortes/
│   │       │   ├── pillow-talk/
│   │       │   ├── sketches-of-sorrow/
│   │       │   ├── flying-gulls/
│   │       │   ├── pure-misery/
│   │       │   ├── at-the-factory/
│   │       │   ├── useless-things/
│   │       │   ├── young-girl/
│   │       │   └── sounds/
│   │       └── photos/                # DONE — fully working
│   │           ├── ice/
│   │           ├── tulips/
│   │           ├── suomenlinna/
│   │           ├── smoke/
│   │           ├── ferry-trip-views/
│   │           ├── silence-exhibition-2022/
│   │           └── ice-detail/
│   ├── gallery/
│   │   ├── index.md                    # MY ART landing page (needs improvement)
│   │   ├── tableware-ceramics/
│   │   │   ├── index.md                # DONE — shows 8 series thumbnails
│   │   │   └── [8 series]/index.md     # DONE — all working with lightbox
│   │   ├── unique-ceramics/
│   │   │   ├── index.md                # TODO
│   │   │   └── [11 series]/index.md    # TODO
│   │   ├── art/
│   │   │   ├── index.md                # TODO
│   │   │   └── [17 series]/index.md    # TODO
│   │   └── photos/                     # DONE
│   ├── artist/index.md
│   ├── contact/index.md
│   └── index.md
├── Site Files/               # Raw working images from Pirjo
├── dist/                     # Built site output (generated, don't edit)
├── eleventy.config.js
├── package.json
└── PROJECT.md
```

---

## How galleries work — THE CORRECT APPROACH

**Important lesson learned:** Eleventy liquid templates cannot resolve data references from frontmatter. The reliable approach is hardcoded HTML in index.md files.

### Level 1 — MY ART page (/gallery/)
Currently a plain text list. TODO: build a visual grid with category cover images.

### Level 2 — Category index page (e.g. /gallery/tableware-ceramics/)
Hardcoded HTML grid of series thumbnails. See tableware-ceramics/index.md as the model.

```html
---
title: Tableware Ceramics
layout: base.njk
---
# Tableware Ceramics

<div class="category-grid">
  <a class="category-card" href="/gallery/tableware-ceramics/little-boxes/">
    <img src="/assets/images/tableware-ceramics/little-boxes/cover.jpg" alt="Little Boxes">
    <span>Little Boxes</span>
  </a>
  ...more series...
</div>
```

### Level 3 — Series page (e.g. /gallery/tableware-ceramics/little-boxes/)
Hardcoded HTML grid + lightbox JavaScript. See any working tableware series as model.
Images listed in: HTML img tags + JavaScript galleryImages array + galleryTitles array.

---

## Adding new images — workflow

1. Put images in correct series folder e.g. `src/assets/images/tableware-ceramics/little-boxes/`
2. Name must be web-safe: lowercase, hyphens instead of spaces, no Finnish characters
3. Add one image named exactly `cover.jpg` per series
4. Update the series `index.md` to include the new image
5. Run `npm run serve` to rebuild

### Rename script (fixes Finnish characters, run from project root)
```bash
python3 << 'ENDOFFILE'
import os, unicodedata

base = "src/assets/images/tableware-ceramics"  # change folder as needed

def clean(name):
    name = unicodedata.normalize('NFC', name)
    result = ""
    for c in name:
        if c in 'äå': result += 'a'
        elif c == 'ö': result += 'o'
        elif c in 'ÄÅ': result += 'a'
        elif c == 'Ö': result += 'o'
        else: result += c
    return result

for series in os.listdir(base):
    series_path = os.path.join(base, series)
    if not os.path.isdir(series_path): continue
    for filename in os.listdir(series_path):
        new_name = clean(filename)
        if new_name != filename:
            os.rename(os.path.join(series_path, filename), os.path.join(series_path, new_name))
            print(f"Fixed: {filename} → {new_name}")
print("Done!")
ENDOFFILE
```

---

## What is done

- [x] Home page
- [x] Artist/Myself page
- [x] Navigation with dropdown
- [x] All photo galleries (7 series, fully working)
- [x] Tableware ceramics — all 8 series working with lightbox
- [x] Unique ceramics — all 11 series working with lightbox
- [x] Art — all 17 series working with lightbox
- [x] MY ART landing page — hero image + 4 category thumbnails
- [x] Content padding fixed so nothing overlaps navigation bar
- [x] Correct build commands established (npm run serve)

## What is next

1. Blog — markdown based, one .md file per post, Giscus comments later
2. Appearance tweaks — focal point tool for thumbnail cropping
3. Git + GitHub setup
4. Netlify deployment

---

## How to start a new Claude session

Paste this file at the start with:
"Here is the project documentation for the Pirjo Pesonen website. Please read it and help me continue where we left off."

Then describe what you want to work on next.

---

## Working style — how Sams likes to work

This section helps Claude get up to speed quickly on how to collaborate effectively.

**Background**
- Sams is a scientist, not a programmer
- Works on Mac, comfortable with Finder and Terminal basics
- Uses Claude as co-pilot — Claude handles syntax, Sams makes decisions
- Previously used GPT for this project, now uses Claude

**Communication style**
- Prefers short, direct responses — no unnecessary explanation
- Asks one thing at a time, likes to confirm before moving on
- Describes visual changes in physical terms ("move down 3cm", "decrease by 70%")
- Says "OK" or "good" to confirm things worked — then move on
- Sometimes types quickly with small errors — interpret charitably
- Finnish is his native language, writes in English

**Working habits**
- Makes backups frequently — always offer a backup at key milestones
- Likes to understand what commands do, not just copy blindly
- Prefers to test one thing at a time before moving to the next
- Uses Terminal and Finder together naturally
- Keeps this conversation open while working — minimizes rather than closes

**Technical preferences**
- Always use `npm run serve` not `npx @11ty/eleventy --serve`
- Prefers Python scripts saved to files over long heredoc commands
- Scripts should always print clear confirmation when done
- Always verify with a check command after making changes

**What to always do**
- Offer backup before any significant code change
- Give check command after every change
- Keep explanations short unless asked for more
- When something doesn't work, ask for Terminal output before guessing

---

## Useful commands

```bash
# Start server
npm run serve

# Make backup
cp -r /Users/sams/Pirjo_Website_Project /Users/sams/Pirjo_Website_Project_backup_NAME

# Check series contents
for dir in src/assets/images/tableware-ceramics/*/; do echo "--- $dir ---"; ls "$dir"; done

# Check project state
echo "=== TABLEWARE ===" && ls src/assets/images/tableware-ceramics/ && echo "=== UNIQUE ===" && ls src/assets/images/unique-ceramics/ && echo "=== ART ===" && ls src/assets/images/art/
```
