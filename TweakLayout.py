#!/usr/bin/env python3
"""
Pirjo Pesonen Website — Appearance Tweaking Script
====================================================
Uncomment the function call you want, change the value, then run:
    python3 tweak.py

The script modifies base.njk and the change affects ALL pages immediately.
Rebuild the site with: npm run serve
"""

import re

BASE_NJK = "src/_includes/base.njk"

def read():
    with open(BASE_NJK, "r") as f:
        return f.read()

def write(content):
    with open(BASE_NJK, "w") as f:
        f.write(content)
    print(f"Updated {BASE_NJK} — rebuild with: npm run serve")

# ============================================================
# BACKGROUND COLOR
# Current: #888888 (medium grey)
# ============================================================
def change_background(color):
    content = read()
    content = re.sub(r'background-color: #[0-9a-fA-F]+;', f'background-color: {color};', content)
    write(content)
    print(f"Background color changed to: {color}")

# ============================================================
# BODY FONT SIZE
# Current: inherited (Arial default ~16px)
# ============================================================
def change_font_size(px):
    content = read()
    if 'font-size:' in content and 'body {' in content:
        content = re.sub(r'(body \{[^}]*?)font-size: \d+px;', f'\\1font-size: {px}px;', content)
    else:
        content = content.replace('font-family: Arial, sans-serif;', f'font-family: Arial, sans-serif;\n      font-size: {px}px;')
    write(content)
    print(f"Font size changed to: {px}px")

# ============================================================
# BODY FONT FAMILY
# Current: Arial, sans-serif
# Options: "Georgia, serif" | "Arial, sans-serif" | "Helvetica, sans-serif"
# ============================================================
def change_font_family(family):
    content = read()
    content = re.sub(r'font-family: .+?;', f'font-family: {family};', content)
    write(content)
    print(f"Font family changed to: {family}")

# ============================================================
# BODY MARGIN (space around all content)
# Current: 40px
# ============================================================
def change_body_margin(px):
    content = read()
    content = re.sub(r'margin: \d+px;', f'margin: {px}px;', content, count=1)
    write(content)
    print(f"Body margin changed to: {px}px")

# ============================================================
# BODY TOP PADDING (space below navigation bar)
# Current: 120px
# ============================================================
def change_top_padding(px):
    content = read()
    content = re.sub(r'padding-top: \d+px;', f'padding-top: {px}px;', content)
    write(content)
    print(f"Top padding changed to: {px}px")

# ============================================================
# NAVIGATION FONT SIZE
# Current: 25px
# ============================================================
def change_nav_font_size(px):
    content = read()
    content = re.sub(r'(\.site-nav \{[^}]*?)font-size: \d+px;', f'\\1font-size: {px}px;', content)
    write(content)
    print(f"Nav font size changed to: {px}px")

# ============================================================
# NAVIGATION TOP POSITION
# Current: 60px
# ============================================================
def change_nav_top(px):
    content = read()
    content = re.sub(r'(\.site-nav \{[^}]*?)top: \d+px;', f'\\1top: {px}px;', content)
    write(content)
    print(f"Nav top position changed to: {px}px")

# ============================================================
# GALLERY GRID COLUMNS
# Current: 3
# ============================================================
def change_gallery_columns(n):
    content = read()
    content = re.sub(
        r'(\.gallery-grid \{[^}]*?)grid-template-columns: [^;]+;',
        f'\\1grid-template-columns: repeat({n}, 1fr);',
        content
    )
    write(content)
    print(f"Gallery columns changed to: {n}")

# ============================================================
# CATEGORY GRID COLUMNS
# Current: 3
# ============================================================
def change_category_columns(n):
    content = read()
    content = re.sub(
        r'(\.category-grid \{[^}]*?)grid-template-columns: [^;]+;',
        f'\\1grid-template-columns: repeat({n}, 1fr);',
        content
    )
    write(content)
    print(f"Category columns changed to: {n}")

# ============================================================
# GALLERY GAP (space between images)
# Current: 12px
# ============================================================
def change_gallery_gap(px):
    content = read()
    content = re.sub(
        r'(\.gallery-grid \{[^}]*?)gap: \d+px;',
        f'\\1gap: {px}px;',
        content
    )
    write(content)
    print(f"Gallery gap changed to: {px}px")

# ============================================================
# CATEGORY CARD TITLE FONT SIZE
# Current: 28px
# ============================================================
def change_card_title_size(px):
    content = read()
    content = re.sub(
        r'(\.category-card span \{[^}]*?)font-size: \d+px;',
        f'\\1font-size: {px}px;',
        content
    )
    write(content)
    print(f"Card title size changed to: {px}px")

# ============================================================
# TEXT COLOR
# Current: white
# ============================================================
def change_text_color(color):
    content = read()
    content = re.sub(r'(body \{[^}]*?)color: \w+;', f'\\1color: {color};', content)
    write(content)
    print(f"Text color changed to: {color}")


# ============================================================
# ============================================================
# MAKE YOUR CHANGES BELOW
# Uncomment one or more lines, change the value, run the script
# ============================================================
# ============================================================

# change_background("#888888")       # background color
# change_font_size(16)               # body text size in pixels
# change_font_family("Arial, sans-serif")  # font family
# change_body_margin(40)             # margin around content in pixels
# change_top_padding(120)            # space below nav bar in pixels
# change_nav_font_size(25)           # navigation text size
# change_nav_top(60)                 # navigation distance from top
# change_gallery_columns(3)          # number of columns in galleries
# change_category_columns(3)         # number of columns in category grids
# change_gallery_gap(12)             # gap between gallery images in pixels
# change_card_title_size(28)         # category card title size
# change_text_color("white")         # main text color

print("No changes made — uncomment a line above to make a change.")
