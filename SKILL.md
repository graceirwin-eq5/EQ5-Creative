---
name: eq5-slides
description: "Use this skill whenever creating Equals 5 branded presentations, pitch decks, campaign proposals, or client-facing slide decks. Trigger on any request involving EQ5 slides, decks, or presentations. Uses standard PowerPoint layouts (Title, Content, Two-Column, Blank) styled with the EQ5 dual-theme system (Midnight Navy dark + Lavender Frost light). Inter typography, brand color palette, logo + Confidential footer on every slide."
---

# Equals 5 — Branded Slide Skill

## Quick Reference

| Task | Action |
|------|--------|
| Create branded deck | Follow [Colors](#colors) + [Layouts](#standard-layouts), generate with PptxGenJS |
| Edit existing deck | `python -m markitdown deck.pptx` to extract, rebuild with brand rules |
| Visual QA | Convert to images, check against [QA Checklist](#qa-checklist) |

---

## Brand System

### Dual-Theme Architecture

Every slide is either **Dark** or **Light**:

| Theme | When to use | Ratio |
|-------|-------------|-------|
| **Dark** (Midnight Navy) | Equals 5 as subject — product, platform, capabilities, CTA, hero | ~70% |
| **Light** (Lavender Frost) | External context — market, clients, team, data tables, comparisons | ~30% |

### Colors

**No `#` prefix** — PptxGenJS corrupts files with `#`.

#### Dark Theme

| Token | Hex | Usage |
|-------|-----|-------|
| `MIDNIGHT` | `0B1525` | Slide background |
| `BRAND_BLUE` | `3079E9` | CTAs, accent shapes, chart primary |
| `BRAND_CYAN` | `00C8C8` | Headline accent words, data highlights |
| `SLATE` | `6577A5` | Muted labels, dividers, footer text |
| `WHITE` | `FFFFFF` | Primary text |
| `CARD_DARK` | `0F1D33` | Card/container backgrounds |

**Transparency shortcuts:** Body text = `FFFFFF` with `transparency: 30`. Footer = `FFFFFF` with `transparency: 60`.

#### Light Theme

| Token | Hex | Usage |
|-------|-----|-------|
| `LIGHT_BG` | `F5F0FA` | Slide background base |
| `DARK_TEXT` | `1A1A2E` | Headlines |
| `BODY_DARK` | `4A4A6A` | Body text |
| `CARD_BORDER` | `E8E4F0` | Card borders, dividers |
| `TABLE_HEADER` | `4A5578` | Table header row fill |
| `TABLE_ROW_ALT` | `F0EDF5` | Alternating table row fill |

#### Shared Accents

| Token | Hex | Usage |
|-------|-----|-------|
| `PINK_ACCENT` | `FF3366` | Error / prohibition icons |
| `GREEN_CHECK` | `00CC66` | Checkmarks, positive states |

### Typography

**Font:** Inter (all weights). Fallback: Calibri.

| Element | Weight | Size | Dark Color | Light Color |
|---------|--------|------|------------|-------------|
| Title | Extra Bold (800) | 44pt | `FFFFFF` | `1A1A2E` |
| Title accent word | Extra Bold (800) | 44pt | `00C8C8` | `00C8C8` |
| Subtitle | Bold (700) | 24pt | `FFFFFF` trans 30 | `4A4A6A` |
| Body | Regular (400) | 16pt | `FFFFFF` trans 30 | `4A4A6A` |
| Bold callout | Bold (700) | 16pt | `FFFFFF` | `1A1A2E` |
| Bullet heading | Bold (700) | 16pt | `FFFFFF` | `1A1A2E` |
| Bullet description | Regular (400) | 13pt | `FFFFFF` trans 30 | `4A4A6A` |
| Stat number | Extra Bold (800) | 60pt | `00C8C8` | `1A1A2E` |
| Stat label | Medium (500) | 12pt | `6577A5` | `4A4A6A` |
| Tagline | Regular (400) | 12pt | `6577A5` | `4A4A6A` |
| Table header | Bold (700) | 11pt | `FFFFFF` on `4A5578` fill | `FFFFFF` on `4A5578` fill |
| Table cell | Regular (400) | 10pt | `FFFFFF` | `1A1A2E` |
| Footer | Regular (400) | 8pt | `FFFFFF` trans 60 | `6577A5` trans 60 |

All titles use `charSpacing: -0.5`. Hero titles use `charSpacing: -1`.

### Logo

**Source:** `https://equals5.com/i/logo.svg` — download and convert to PNG.

```bash
curl -o eq5_logo.svg https://equals5.com/i/logo.svg
# White logo — for dark slides
npx sharp-cli -i eq5_logo.svg -o eq5_logo_white.png --width 400
# Dark logo — for light slides (tint to MIDNIGHT)
npx sharp-cli -i eq5_logo.svg -o eq5_logo_dark.png --width 400 --tint "rgb(11,21,37)"
```

**Placement:** Top-left on every slide (`x: 0.3, y: 0.2, w: 0.6, h: 0.35`). White on dark, dark on light.

### Trademark Rules

First mention: **Equals 5™**, **Uni 5™**, **Personi-5™**, **Identi-5™**. Always numeral `5`, never "Five" (except logo wordmark).

### Messaging Rules

| Always | Never |
|--------|-------|
| "100% deterministic" / "100% NPI-level" | "97% accuracy" (spec docs only) |
| "Verify" for Uni 5 Stage 1 | "Enrich" externally |
| Lead with "Doctors Are People Too" | Position as generic programmatic vendor |
| Include CCPA/CPRA with data claims | Omit compliance language |

---

## Slide Chrome

Every slide gets exactly two persistent elements: the **logo** and the **Confidential footer**. Nothing else.

```javascript
function applyChrome(slide, { theme = "dark" }) {
  // Logo — top-left
  const logoData = theme === "dark" ? logoWhiteBase64 : logoDarkBase64;
  slide.addImage({ data: logoData, x: 0.3, y: 0.2, w: 0.6, h: 0.35 });

  // Confidential footer — bottom-left
  slide.addText("Confidential", {
    x: 0.3, y: 5.2, w: 1.5, h: 0.3,
    fontFace: "Inter", fontSize: 8,
    color: theme === "dark" ? "FFFFFF" : "6577A5",
    transparency: 60
  });
}
```

---

## Background Generation

### Dark Background

```javascript
const { createCanvas } = require("canvas");
const fs = require("fs");

function generateDarkBg(width = 1920, height = 1080) {
  const canvas = createCanvas(width, height);
  const ctx = canvas.getContext("2d");

  ctx.fillStyle = "#0B1525";
  ctx.fillRect(0, 0, width, height);

  // Subtle cyan glow — bottom-right
  const glow = ctx.createRadialGradient(
    width * 0.75, height * 0.8, 0,
    width * 0.75, height * 0.8, width * 0.5
  );
  glow.addColorStop(0, "rgba(0, 200, 200, 0.06)");
  glow.addColorStop(1, "rgba(0, 200, 200, 0)");
  ctx.fillStyle = glow;
  ctx.fillRect(0, 0, width, height);

  return canvas.toBuffer("image/png");
}

fs.writeFileSync("bg_dark.png", generateDarkBg());
```

### Light Background

```javascript
function generateLightBg(width = 1920, height = 1080) {
  const canvas = createCanvas(width, height);
  const ctx = canvas.getContext("2d");

  // Lavender gradient base
  const base = ctx.createLinearGradient(0, 0, width, height);
  base.addColorStop(0, "#F8F5FF");
  base.addColorStop(0.5, "#F5F0FA");
  base.addColorStop(1, "#F0EBF5");
  ctx.fillStyle = base;
  ctx.fillRect(0, 0, width, height);

  // Pink glow — top-left
  const pink = ctx.createRadialGradient(
    width * 0.05, height * 0.15, 0,
    width * 0.05, height * 0.15, width * 0.35
  );
  pink.addColorStop(0, "rgba(220, 180, 220, 0.25)");
  pink.addColorStop(1, "rgba(220, 180, 220, 0)");
  ctx.fillStyle = pink;
  ctx.fillRect(0, 0, width, height);

  // Subtle grid overlay
  ctx.strokeStyle = "rgba(200, 190, 215, 0.2)";
  ctx.lineWidth = 0.5;
  for (let x = 0; x <= width; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
  }
  for (let y = 0; y <= height; y += 40) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
  }

  return canvas.toBuffer("image/png");
}

fs.writeFileSync("bg_light.png", generateLightBg());
```

**Dependency:** `npm install canvas`

---

## Standard Layouts

All slides are 16:9 (`LAYOUT_16x9` = 10" × 5.625"). Every layout maps to a standard PowerPoint pattern. Each layout works in both Dark and Light themes — just swap colors and backgrounds.

### Helper: Accent Word Coloring

Many titles highlight one word in `BRAND_CYAN`. This helper builds multi-run text:

```javascript
function titleRuns(title, accentWord, theme = "dark") {
  const baseColor = theme === "dark" ? "FFFFFF" : "1A1A2E";
  if (!accentWord) return [{ text: title, options: { color: baseColor, bold: true } }];

  const parts = title.split(accentWord);
  const runs = [];
  parts.forEach((part, i) => {
    if (part) runs.push({ text: part, options: { color: baseColor, bold: true } });
    if (i < parts.length - 1) runs.push({ text: accentWord, options: { color: "00C8C8", bold: true } });
  });
  return runs;
}
```

---

### 1. Title Slide

Standard centered title + subtitle. Used for deck openers and section dividers.

```
┌─────────────────────────────┐
│ [logo]                      │
│                             │
│        TAGLINE (small)      │
│     TITLE (44pt, bold)      │
│     subtitle (16pt)         │
│                             │
│                Confidential │
└─────────────────────────────┘
```

```javascript
function addTitleSlide(pres, { title, accentWord, subtitle, tagline, theme = "dark" }) {
  const slide = pres.addSlide();
  slide.background = { data: theme === "dark" ? bgDarkBase64 : bgLightBase64 };
  applyChrome(slide, { theme });

  if (tagline) {
    slide.addText(tagline, {
      x: 1, y: 1.6, w: 8, h: 0.3,
      fontFace: "Inter", fontSize: 12,
      color: theme === "dark" ? "6577A5" : "4A4A6A",
      align: "center"
    });
  }

  slide.addText(titleRuns(title, accentWord, theme), {
    x: 1, y: 1.9, w: 8, h: 1.5,
    fontFace: "Inter", fontSize: 44, align: "center", valign: "middle", charSpacing: -1
  });

  if (subtitle) {
    slide.addText(subtitle, {
      x: 1.5, y: 3.5, w: 7, h: 0.6,
      fontFace: "Inter", fontSize: 16, align: "center",
      color: theme === "dark" ? "FFFFFF" : "4A4A6A",
      transparency: theme === "dark" ? 30 : 0
    });
  }
  return slide;
}
```

---

### 2. Title + Content

Title top-left, body content below. The workhorse layout for any text-heavy slide.

```
┌─────────────────────────────┐
│ [logo]                      │
│ TITLE (36pt)                │
│                             │
│ Body text / bullet list     │
│ spanning the full width     │
│                             │
│ Confidential                │
└─────────────────────────────┘
```

```javascript
function addContentSlide(pres, { title, accentWord, body, theme = "dark" }) {
  const slide = pres.addSlide();
  slide.background = { data: theme === "dark" ? bgDarkBase64 : bgLightBase64 };
  applyChrome(slide, { theme });

  slide.addText(titleRuns(title, accentWord, theme), {
    x: 0.6, y: 0.7, w: 8.8, h: 0.8,
    fontFace: "Inter", fontSize: 36, charSpacing: -0.5
  });

  slide.addText(body, {
    x: 0.6, y: 1.7, w: 8.8, h: 3.3,
    fontFace: "Inter", fontSize: 16, valign: "top",
    color: theme === "dark" ? "FFFFFF" : "4A4A6A",
    transparency: theme === "dark" ? 30 : 0,
    lineSpacingMultiple: 1.4
  });
  return slide;
}
```

---

### 3. Two-Column (Text + Image)

Title top-left, left column for text, right column for an image. The standard layout for narrative and feature slides.

```
┌─────────────────────────────┐
│ [logo]                      │
│ TITLE (36pt)                │
│                             │
│ Body text    │  [IMAGE]     │
│ on the left  │              │
│              │              │
│ Confidential                │
└─────────────────────────────┘
```

```javascript
function addTwoColSlide(pres, { title, accentWord, body, imagePath, theme = "dark" }) {
  const slide = pres.addSlide();
  slide.background = { data: theme === "dark" ? bgDarkBase64 : bgLightBase64 };
  applyChrome(slide, { theme });

  slide.addText(titleRuns(title, accentWord, theme), {
    x: 0.6, y: 0.7, w: 4.2, h: 0.8,
    fontFace: "Inter", fontSize: 36, charSpacing: -0.5
  });

  slide.addText(body, {
    x: 0.6, y: 1.7, w: 4.2, h: 3.3,
    fontFace: "Inter", fontSize: 16, valign: "top",
    color: theme === "dark" ? "FFFFFF" : "4A4A6A",
    transparency: theme === "dark" ? 30 : 0,
    lineSpacingMultiple: 1.4
  });

  if (imagePath) {
    slide.addImage({
      path: imagePath,
      x: 5.2, y: 0.7, w: 4.4, h: 4.5,
      sizing: { type: "contain", w: 4.4, h: 4.5 }
    });
  }
  return slide;
}
```

---

### 4. Bullet List

Title top-left, structured bullet list below. Each bullet has a **bold heading** and lighter description.

```
┌─────────────────────────────┐
│ [logo]                      │
│ TITLE (36pt)                │
│                             │
│ • Heading 1                 │
│   Description text          │
│ • Heading 2                 │
│   Description text          │
│ Confidential                │
└─────────────────────────────┘
```

```javascript
function addBulletSlide(pres, { title, accentWord, items, imagePath, theme = "dark" }) {
  // items = [{ heading: "...", desc: "..." }, ...]
  const slide = pres.addSlide();
  slide.background = { data: theme === "dark" ? bgDarkBase64 : bgLightBase64 };
  applyChrome(slide, { theme });

  const textW = imagePath ? 4.2 : 8.8;

  slide.addText(titleRuns(title, accentWord, theme), {
    x: 0.6, y: 0.7, w: textW, h: 0.8,
    fontFace: "Inter", fontSize: 36, charSpacing: -0.5
  });

  const headColor = theme === "dark" ? "FFFFFF" : "1A1A2E";
  const descColor = theme === "dark" ? "FFFFFF" : "4A4A6A";
  const descTrans = theme === "dark" ? 30 : 0;

  let curY = 1.8;
  items.forEach((item) => {
    slide.addText(item.heading, {
      x: 0.6, y: curY, w: textW, h: 0.35,
      fontFace: "Inter", fontSize: 16, bold: true, color: headColor,
      bullet: true
    });
    if (item.desc) {
      slide.addText(item.desc, {
        x: 1.0, y: curY + 0.35, w: textW - 0.4, h: 0.45,
        fontFace: "Inter", fontSize: 13, color: descColor, transparency: descTrans
      });
      curY += 0.95;
    } else {
      curY += 0.5;
    }
  });

  if (imagePath) {
    slide.addImage({
      path: imagePath, x: 5.2, y: 0.7, w: 4.4, h: 4.5,
      sizing: { type: "contain", w: 4.4, h: 4.5 }
    });
  }
  return slide;
}
```

---

### 5. Stats

Title + subtitle top, then a row of big numbers with labels below. Typically Dark theme.

```
┌─────────────────────────────┐
│ [logo]                      │
│ TITLE (36pt)                │
│ Subtitle (16pt)             │
│                             │
│  0.65%    85%     63%       │
│  Avg CTR  Match   Reach     │
│ Confidential                │
└─────────────────────────────┘
```

```javascript
function addStatsSlide(pres, { title, accentWord, subtitle, stats, theme = "dark" }) {
  // stats = [{ value: "85%", label: "Avg Match" }, ...]
  const slide = pres.addSlide();
  slide.background = { data: theme === "dark" ? bgDarkBase64 : bgLightBase64 };
  applyChrome(slide, { theme });

  slide.addText(titleRuns(title, accentWord, theme), {
    x: 0.6, y: 0.7, w: 8.8, h: 0.8,
    fontFace: "Inter", fontSize: 36, charSpacing: -0.5
  });

  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.6, y: 1.5, w: 8.8, h: 0.5,
      fontFace: "Inter", fontSize: 16,
      color: theme === "dark" ? "FFFFFF" : "4A4A6A",
      transparency: theme === "dark" ? 30 : 0
    });
  }

  const count = stats.length;
  const colW = 8.8 / count;
  const startX = 0.6;
  const statY = 2.8;

  stats.forEach((stat, i) => {
    const x = startX + i * colW;

    slide.addText(stat.value, {
      x, y: statY, w: colW, h: 1.2,
      fontFace: "Inter", fontSize: 60, bold: true,
      color: theme === "dark" ? "00C8C8" : "1A1A2E",
      align: "center"
    });

    slide.addText(stat.label, {
      x, y: statY + 1.2, w: colW, h: 0.5,
      fontFace: "Inter", fontSize: 12,
      color: theme === "dark" ? "6577A5" : "4A4A6A",
      align: "center"
    });
  });
  return slide;
}
```

---

### 6. Table

Title top-left, styled data table. Branded header row, alternating fills. Typically Light theme.

```
┌─────────────────────────────┐
│ [logo]                      │
│ TITLE (36pt)                │
│                             │
│ ┌────┬────┬────┬────┐      │
│ │ Hd │ Hd │ Hd │ Hd │      │
│ ├────┼────┼────┼────┤      │
│ │    │    │    │    │      │
│ └────┴────┴────┴────┘      │
│ Confidential                │
└─────────────────────────────┘
```

```javascript
function addTableSlide(pres, { title, accentWord, headers, rows, theme = "light" }) {
  const slide = pres.addSlide();
  slide.background = { data: theme === "dark" ? bgDarkBase64 : bgLightBase64 };
  applyChrome(slide, { theme });

  slide.addText(titleRuns(title, accentWord, theme), {
    x: 0.6, y: 0.7, w: 8.8, h: 0.8,
    fontFace: "Inter", fontSize: 36, charSpacing: -0.5
  });

  const tableRows = [];

  // Header
  tableRows.push(headers.map(h => ({
    text: h, options: {
      fontFace: "Inter", fontSize: 11, bold: true, color: "FFFFFF",
      fill: { color: "4A5578" }, align: "center", valign: "middle"
    }
  })));

  // Data rows
  rows.forEach((row, rIdx) => {
    tableRows.push(row.map(cell => ({
      text: cell, options: {
        fontFace: "Inter", fontSize: 10,
        color: theme === "dark" ? "FFFFFF" : "1A1A2E",
        fill: { color: rIdx % 2 === 0 ? (theme === "dark" ? "0F1D33" : "FFFFFF") : (theme === "dark" ? "0B1525" : "F0EDF5") },
        align: "center", valign: "middle"
      }
    })));
  });

  slide.addTable(tableRows, {
    x: 0.6, y: 1.7, w: 8.8,
    border: { type: "solid", color: theme === "dark" ? "1A2540" : "E8E4F0", pt: 0.5 },
    rowH: 0.4, autoPage: false
  });
  return slide;
}
```

---

### 7. Blank (Custom Content)

Background + chrome only. Use for grids (client logos, team photos), diagrams, or any freeform layout. Place elements manually.

```javascript
function addBlankSlide(pres, { theme = "dark" }) {
  const slide = pres.addSlide();
  slide.background = { data: theme === "dark" ? bgDarkBase64 : bgLightBase64 };
  applyChrome(slide, { theme });
  return slide;
}
```

**Example — Client logo grid on blank light slide:**

```javascript
const slide = addBlankSlide(pres, { theme: "light" });

slide.addText("Clients", {
  x: 0, y: 0.7, w: 10, h: 0.8,
  fontFace: "Inter", fontSize: 40, bold: true, color: "1A1A2E",
  align: "center", charSpacing: -0.5
});

const cols = 5, cardW = 1.6, cardH = 0.7, gapX = 0.2, gapY = 0.15;
const gridW = cols * cardW + (cols - 1) * gapX;
const startX = (10 - gridW) / 2;

logos.forEach((logo, i) => {
  const x = startX + (i % cols) * (cardW + gapX);
  const y = 1.8 + Math.floor(i / cols) * (cardH + gapY);

  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w: cardW, h: cardH,
    fill: { color: "FFFFFF" }, rectRadius: 0.08,
    shadow: { type: "outer", blur: 4, offset: 1, angle: 135, color: "000000", opacity: 0.06 }
  });
  slide.addImage({
    path: logo.path, x: x + 0.15, y: y + 0.1, w: cardW - 0.3, h: cardH - 0.2,
    sizing: { type: "contain", w: cardW - 0.3, h: cardH - 0.2 }
  });
});
```

**Example — Team photo cards on blank light slide:**

```javascript
const slide = addBlankSlide(pres, { theme: "light" });

slide.addText(titleRuns("Our Leadership Team", "Team", "light"), {
  x: 0, y: 0.7, w: 10, h: 0.8,
  fontFace: "Inter", fontSize: 40, align: "center", charSpacing: -0.5
});

const cardW = 2.6, gap = 0.3;
const totalW = members.length * cardW + (members.length - 1) * gap;
const startX = (10 - totalW) / 2;

members.forEach((m, i) => {
  const x = startX + i * (cardW + gap);
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y: 1.7, w: cardW, h: 3.3,
    fill: { color: "FFFFFF" }, rectRadius: 0.12,
    line: { color: "E8E4F0", width: 0.75 }
  });
  slide.addImage({ path: m.photoPath, x: x + 0.2, y: 1.9, w: cardW - 0.4, h: 2.2, sizing: { type: "cover", w: cardW - 0.4, h: 2.2 } });
  slide.addText(m.name, { x, y: 4.2, w: cardW, h: 0.35, fontFace: "Inter", fontSize: 14, bold: true, color: "1A1A2E", align: "center" });
  slide.addText(m.role, { x, y: 4.5, w: cardW, h: 0.3, fontFace: "Inter", fontSize: 11, color: "6577A5", align: "center" });
});
```

---

## Setup & Dependencies

```bash
npm install -g pptxgenjs
npm install canvas
pip install "markitdown[pptx]" Pillow --break-system-packages
```

---

## Scaffold: Example Deck

```javascript
const pptxgen = require("pptxgenjs");
const fs = require("fs");

// Prerequisites: run Background Generation code first to create bg_dark.png and bg_light.png
// Prerequisites: run Logo commands first to create eq5_logo_white.png and eq5_logo_dark.png
// Prerequisites: define applyChrome(), titleRuns(), and all addXxxSlide() functions above

// Load assets
const bgDarkBase64 = "image/png;base64," + fs.readFileSync("bg_dark.png").toString("base64");
const bgLightBase64 = "image/png;base64," + fs.readFileSync("bg_light.png").toString("base64");
const logoWhiteBase64 = "image/png;base64," + fs.readFileSync("eq5_logo_white.png").toString("base64");
const logoDarkBase64 = "image/png;base64," + fs.readFileSync("eq5_logo_dark.png").toString("base64");

let pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Equals 5";
pres.title = "Campaign Proposal";

// 1. Hero (Dark) — ™ on first mention of trademarked names
addTitleSlide(pres, {
  title: "Precisely Target HCPs",
  accentWord: "Target",
  subtitle: "Equals 5™ reaches physicians on Social Media and anywhere on internet, by NPI number.",
  tagline: "your journey to reach physicians",
  theme: "dark"
});

// 2. Two-Column narrative (Dark)
addTwoColSlide(pres, {
  title: "Doctors Are Changing",
  accentWord: "Changing",
  body: "Traditional creative formats and channels are no longer performing.\n\nDoctors are getting younger and spend most of their time on non-professional channels.",
  imagePath: "illustration.png",
  theme: "dark"
});

// 3. Content slide (Light)
addContentSlide(pres, {
  title: "Why Social Media?",
  body: "Doctors are people too. They spend an average of 45 minutes per day on Social and other non-professional channels, compared to just 3 minutes on endemic medical networks.\n\nBy treating HCPs as consumers, we can reach them where they actually spend their time.",
  theme: "light"
});

// 4. Stats (Dark)
addStatsSlide(pres, {
  title: "Equals 5 Reached",
  accentWord: "Reached",
  subtitle: "467,000 HCPs on Social across 25 physician specialities",
  stats: [
    { value: "0.65%", label: "Avg CTR" },
    { value: "85%", label: "Avg List Match" },
    { value: "63%", label: "Avg Target Reach" }
  ],
  theme: "dark"
});

// 5. Bullet list with image (Dark)
addBulletSlide(pres, {
  title: "Campaign Management",
  accentWord: "Management",
  items: [
    { heading: "Upload & Create Audiences", desc: "Upload NPI lists or build custom HCP audiences by Specialty, Location and Demographics." },
    { heading: "Manage Creative", desc: "Streamline creative set-up across multiple channels from one interface." },
    { heading: "Activate Channels", desc: "Onboard audiences on all channels without separate media platforms." },
    { heading: "Launch Campaigns", desc: "One-click activation across all ad networks." }
  ],
  imagePath: "platform_screenshot.png",
  theme: "dark"
});

// 6. Data table (Light)
addTableSlide(pres, {
  title: "Channels",
  headers: ["Network", "Match Rate", "Avg. Daily Time", "NPI Targeting", "NPI Reporting"],
  rows: [
    ["Facebook", "78%", "33 min", "Yes", "Exclusive for EQ5"],
    ["Instagram", "78%", "53 min", "Yes", "Exclusive for EQ5"],
    ["LinkedIn", "46%", "8 min", "Yes", "Through EQ5 Pixel"],
    ["Twitter", "33%", "35 min", "Yes", "Through EQ5 Pixel"],
    ["Reddit", "45%", "24 min", "Yes", "Through EQ5 Pixel"]
  ],
  theme: "light"
});

// 7. Closing (Dark) — include compliance language with data claims
addTitleSlide(pres, {
  title: "Let's Reach Your HCPs",
  subtitle: "100% deterministic. 100% NPI-level. 20+ channels.\nAll campaigns are CCPA/CPRA compliant.\n\ninfo@equals5.com  |  (201) 305-0150  |  equals5.com",
  theme: "dark"
});

pres.writeFile({ fileName: "EQ5_Proposal.pptx" });
```

---

## QA Checklist

### Brand

- [ ] Dual-theme used — Dark for EQ5 content, Light for external context
- [ ] No `#` prefix on hex values
- [ ] Inter font throughout (fallback: Calibri)
- [ ] Logo top-left on every slide (white on dark, dark on light)
- [ ] "Confidential" footer bottom-left on every slide
- [ ] Headline accent words in `00C8C8`
- [ ] ™ on first mention of trademarked names
- [ ] "100% deterministic" / "100% NPI-level" — never "97% accuracy"
- [ ] Privacy compliance (CCPA/CPRA) mentioned with data claims

### Visual

- [ ] Dark backgrounds are `0B1525` Midnight Navy
- [ ] Light backgrounds show lavender gradient with grid pattern
- [ ] Text is readable on both themes (no low-contrast)
- [ ] Images use `contain` or `cover` — no stretching
- [ ] Minimum 0.5" margins
- [ ] Stat numbers legible at 60pt
- [ ] Tables have header fill (`4A5578`) and alternating rows

### Content

- [ ] Client/brand names spelled correctly
- [ ] Stats match latest proof points
- [ ] No placeholder text remaining

---

## File Naming

`EQ5-[Deal ID]-[Partner]-[Pharma]-[Brand].pptx`

Example: `EQ5-1042-Relevate-Pfizer-Ibrance.pptx`

---

*Equals 5 Inc. © 2026. All Rights Reserved.*
