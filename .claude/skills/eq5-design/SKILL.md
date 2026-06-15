---
name: eq5-design
description: >
  EQ5 brand design system — sourced directly from equals5.com's live CSS.
  Load this skill whenever building or editing any EQ5 asset: presentation slides,
  hub pages, client portals, reports, emails, or any visual output. Use it to make
  design decisions about color, typography, layout, components, and spacing so
  everything feels like a native extension of equals5.com. Trigger on any request
  involving visual design, layout, slide building, hub page creation, color choices,
  font decisions, card design, or "make it look like the website."
---

# EQ5 Design System

Source of truth: **equals5.com** (extracted from live CSS — `css/main.css`).

Every visual output for Equals 5 — slides, hub pages, portals, reports — should feel like it belongs on the website. This file gives you the exact tokens and patterns to make that happen without guessing.

---

## Brand Foundation

### Color Palette

| Token | Value | Use |
|-------|-------|-----|
| `--bg` | `#0a1020` | Page / slide background (dark navy) |
| `--surface` | `#272f46` | Cards, tabs, raised elements |
| `--surface-deep` | `#253b62` | Deeper card layer, blob accents |
| `--blue` | `#3571cb` | Gradient start, interactive blue |
| `--cyan` | `#01b0b0` | Gradient end, accent, active states |
| `--cyan-alt` | `#06acb3` | Active borders, highlights |
| `--muted` | `#8a95b1` | Body text, captions, secondary labels |
| `--border` | `rgba(255,255,255,.1)` | Subtle dividers and borders |
| `--white` | `#fff` | Primary text on dark bg |
| `--off-white` | `#f3f7ff` | Light section backgrounds |

### The Gradient

The EQ5 brand gradient is the single most recognizable design element. Use it on text, buttons, borders, bars, and accents.

**Horizontal (default):**
```css
linear-gradient(93.8deg, #3571cb 0, #01b0b0 100%)
```

**Angled (alternate / cards):**
```css
linear-gradient(291.19deg, #3571cb 3.36%, #01b0b0 88.05%)
```

**Vertical blob accent (background decoration):**
```css
linear-gradient(180deg, #253b62 0, #492040 100%)
```

**Gradient text — the website's signature move:**
```css
background: linear-gradient(93.8deg, #3571cb 0, #01b0b0 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```
Use on h1, h2, hero numbers, highlighted stats, and any text that needs brand emphasis.
The website automatically applies gradient to `h2 span`, `h3 span`, `h4 span` — so any word inside a heading can be gradient by wrapping in `<span>`.

---

## Typography

### Typeface
**Alliance No.1** — EQ5's custom font, loaded via `@font-face`.

Available weights: 300 (Light), 500 (Medium), 700 (Bold), 800 (ExtraBold), 900 (Black).
Italic variants available for all weights.

When Alliance No.1 isn't available (e.g., email), fall back to: `system-ui, -apple-system, 'Segoe UI', sans-serif`.

### Type Scale (desktop)

| Level | Size | Line Height | Weight | Letter Spacing | Notes |
|-------|------|-------------|--------|----------------|-------|
| Hero H1 | 128px | 128px | 800 | −0.02em | Homepage only |
| H1 | 72px | 72px | 800 | −0.02em | Page titles |
| H2 | 72px | 72px | 800 | −0.02em | Section headers |
| H2 (alt) | 96px | 96px | 800 | −0.02em | Large stat sections |
| H3 | 48px | 48px | 800 | −0.02em | Sub-headers, card titles |
| H4 | 32px | 32px | 700–800 | −0.02em | Feature labels |
| H5/Label | 24px | 24px | 700 | − | Tertiary labels |
| Body | 18px | 24px | 400–500 | − | Paragraphs, color: `#8a95b1` |
| Small | 16px | 20px | 400 | − | Captions, footer |
| Micro | 14px | 18px | 400 | − | Tags, meta labels |
| Data label | 21px | 24px | 400 | − | Menlo monospace, pill format |

**Critical rule: letter-spacing is always `−0.02em` on all headings H1–H4.** This tight tracking is what gives EQ5 headlines their authority. Never skip it.

---

## Components

### CTA Button
```css
height: 52px;
line-height: 52px;
padding: 0 40px;
border-radius: 8px;
background: linear-gradient(93.8deg, #3571cb 0, #01b0b0 100%);
color: #fff;
font-size: 16px;
font-weight: 700;
font-family: 'Alliance No.1';
border: none;
text-decoration: none;
```
On dark or gradient backgrounds, buttons can also be outlined: `background: transparent; border: 2px solid rgba(255,255,255,.5)`.

### Cards / Tiles
```css
background: #272f46;
border-radius: 8px;
box-shadow: 0 12px 40px rgba(0,0,0,.16);
padding: 24px;
```
Use `border-radius: 12px` for larger cards with more content. Use `border-radius: 30px–48px` for full section/panel containers.

For cards with gradient accent: add a `4px` left border using the gradient, or a top-edge gradient tab.

### Stat / Data Pills (Monospace)
```css
display: inline-block;
padding: 5px 17px;
background: #fff;
border-radius: 42px;
font-family: Menlo, monospace;
font-size: 21px;
line-height: 24px;
color: #272f46;
```
Use for NPI counts, CTR figures, and performance metrics inline with body copy.

### Section Containers
- **Dark panel**: `background: #0a1020; border-radius: 48px;` (rounded large panels)
- **Card surface**: `background: #272f46; border-radius: 12px–30px;`
- **Tabs / chips**: `background: #272f46; border-radius: 8px; height: 44px;`
- **Active tab/chip**: `border: 2px solid #06acb3;`

### Decorative Blobs (background accents)
Positioned absolutely behind content, blurred, using the purple-navy gradient:
```css
background: linear-gradient(180deg, #253b62 0, #492040 100%);
border-radius: 50%;
filter: blur(80px);
opacity: 0.6;
```
Use 2–3 blobs per dark section, positioned at corners, to add depth without competing with content.

---

## Layout Rules

### Spacing Rhythm
- Section vertical padding: `100px–120px` (desktop)
- Card internal padding: `24px–40px`
- Gap between cards in a grid: `12px–24px`
- Headline margin-bottom before body copy: `24px–38px`

### Grid Patterns
- **2-col**: equal halves `1fr 1fr` — used for feature text + visual pairs
- **3-col**: `repeat(3, 1fr)` — used for problem cards, platform tiles
- **4-col**: `repeat(4, 1fr)` — metric stats, small feature icons
- **Asymmetric**: `1fr 1.4fr` or `0.8fr 1fr 0.8fr` — highlight center column (common on data slides)

### Background Hierarchy
Dark pages use layered depth:
1. `#0a1020` — base
2. `#272f46` — raised surface (cards)
3. `#253b62` — deepest accent (inside cards or blob overlays)

Light sections (`.white_bg`) use `#f3f7ff` or `#fff` with `#272f46` text.

---

## Slide-Specific Guidance

When building NSM or presentation slides (1280×720px canvas):

- **Background**: always `#0a1020`
- **Headline**: Alliance No.1, weight 800–900, `letter-spacing: −0.02em`, gradient text via `-webkit-background-clip`
- **Gradient variable shorthand** already defined in the deck: `var(--gradient)` = `linear-gradient(-28deg, #3079E9 8%, #00D3D3 88%)` — close match to the site, use this for consistency within existing slides
- **Slide surface cards**: `background: rgba(255,255,255,0.04)–0.08; border: 1px solid rgba(48,121,233,0.25); border-radius: 12px–16px`
- **Highlight card** (center hero): `background: linear-gradient(135deg, rgba(48,121,233,0.1), rgba(0,211,211,0.07)); border: 2px solid rgba(0,211,233,0.45)`
- **Accent bar** (left edge of slide): 3px gradient bar, top to bottom
- **Card accent tab** (top of highlighted card): gradient pill, 8px font, white text, positioned absolute at top center

---

## Do / Don't

**Do:**
- Apply `letter-spacing: −0.02em` to every heading
- Use gradient text for the most important number or word on every slide/section
- Use `#8a95b1` for all secondary/caption text (never pure white for body)
- Round corners generously — 8px minimum, 30px+ for full panels
- Use `Alliance No.1` weight 900 for the biggest numbers (revenue, stats)

**Don't:**
- Use flat solid blue (#3571cb) alone without the gradient — the brand lives in the gradient
- Use white text at full opacity for body copy — it reads as harsh; `#8a95b1` is the correct muted tone
- Skip letter-spacing on headlines — it's the single most distinctive typographic choice on the site
- Use a white background without intentional reason — the brand is dark-first

---

## Quick Reference Cheat Sheet

```
Background:    #0a1020
Surface:       #272f46
Gradient:      linear-gradient(93.8deg, #3571cb 0, #01b0b0 100%)
Gradient text: background: [gradient]; -webkit-background-clip:text; -webkit-text-fill-color:transparent
Font:          Alliance No.1 (fallback: system-ui sans-serif)
Headline:      weight 800, letter-spacing −0.02em
Body text:     18px/24px, color #8a95b1
Card radius:   8px (chips) / 12px (cards) / 30–48px (panels)
Button:        52px tall, 0 40px padding, border-radius 8px, gradient bg
```
