# Equals 5 — Style Guide

> Tone of voice, writing guidelines, visual identity, and brand standards
> *See also: `reference/EQ5_Messaging.md` for positioning, product suite, and core messaging*

---

## Tone of Voice

### Personality Attributes

| Attribute | Description |
|---|---|
| **Precise** | Data-driven, specific, metric-backed claims. No vague promises. |
| **Pioneering** | First-to-market positioning; innovative and forward-looking. |
| **Approachable** | Professional but never stuffy. "Doctors Are People Too" extends to how EQ5 communicates. |
| **Confident** | Assertive about capabilities without being arrogant. Let the numbers speak. |
| **Compliant** | Privacy and regulatory compliance is woven into every message — never an afterthought. |

### Writing Style Guidelines

Lead with outcomes and results, not features. Use concrete numbers (e.g., "142 pharma brands across 66 clients" not "hundreds of brands"). Avoid jargon overload — explain terms like "NPI" and "non-endemic" when writing for broader audiences. Maintain confidence: "100% NPI-Level Targeting" and "100% NPI-Level Data" are definitive claims backed by the platform's architecture.

---

## Boilerplates

### Boilerplate (Short)

> Equals 5 is the leading All-in-One Healthcare Marketing Platform, enabling pharmaceutical companies and agencies to precisely target and engage healthcare professionals on 20+ social media, programmatic, and professional channels — with 100% NPI-level targeting and reporting. Equals 5 has delivered campaigns across 142 pharmaceutical brands for 66 pharma clients and 42 agency and publisher partners.

### Boilerplate (Long)

> Equals 5 is a pioneering provider of marketing and media buying solutions for the Pharma and Life Sciences industries. The Equals 5 All-in-One Healthcare Marketing Platform enables brands to easily set up and launch HCP marketing campaigns on 20+ channels in one place, using a unique 100% NPI-level targeting technology to precisely reach the HCPs on their target lists and gather NPI-level reporting data on all engagements. Equals 5 has delivered campaigns across 142 pharmaceutical brands for 66 pharma clients — including Top 20 global pharma companies — and 42 agency and publisher partners, spanning 28+ therapeutic categories with deep expertise in oncology, neurology, rare disease, and immunology. All platform features are fully compliant with privacy regulations, including CCPA and CPRA.

---

## Visual Identity

### Logo

The primary Equals 5 logo consists of two elements:

**Icon Mark:** A stylized **=5** monogram — three horizontal bars forming the "equals" symbol stacked above a bold numeral **5**.

**Wordmark:** "EQUALS FIVE" set in uppercase, bold sans-serif (Inter Bold).

**Logo Source:** [equals5.com/i/logo.svg](https://equals5.com/i/logo.svg)

**Usage Rules:**
- The logo should always appear with adequate clear space around it
- Preferred placement: top-left on dark backgrounds
- The icon mark may be used independently as a favicon or app icon
- The wordmark should not be separated from the icon mark in formal brand communications

**Minimum Sizes:**
- Icon mark: 24px minimum height
- Full logo (icon + wordmark): 120px minimum width

**File Formats:** Maintain logo files in SVG (primary, for web and digital), PNG with transparency (for presentations and documents), and PDF (for print applications).

### Color Palette

#### Primary Colors

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| **Midnight Navy** | `#0A1020` | 10, 16, 32 | Primary background, dark themes |
| **Brand Blue** | `#3079E9` | 48, 121, 233 | Primary accent, CTA elements |
| **Brand Cyan** | `#00D3D3` | 0, 211, 211 | Gradient endpoint, highlights, data viz |

#### Secondary Colors

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| **Slate Blue** | `#6577A5` | 101, 119, 165 | Secondary buttons, muted UI elements |
| **White** | `#FFFFFF` | 255, 255, 255 | Primary text on dark backgrounds, clean backgrounds |
| **White (30% opacity)** | `rgba(255,255,255,0.3)` | — | Subtle labels, disclaimers |
| **Dark Gray / Near-Black** | — | — | Body copy and secondary text on light backgrounds |

#### Brand Gradient

```
Direction: ~28° (bottom-left to top-right)
Start: #3079E9 (Brand Blue) at ~8%
End:   #00D3D3 (Brand Cyan) at ~88%
```

**CSS:**
```css
background: linear-gradient(-28deg, #3079E9 8%, #00D3D3 88%);
```

This gradient is used for hero text, primary headlines, and key brand moments.

#### Glow Effect

A subtle cyan glow is applied to brand headlines and key typographic elements:

```css
text-shadow: 0px 0px 15px rgba(0, 211, 211, 0.32);
```

### Typography

#### Primary Typeface: Inter

Inter is the brand's primary typeface, chosen for its clarity, professionalism, and excellent screen readability across digital and print applications.

| Weight | CSS Value | Usage |
|--------|-----------|-------|
| **Extra Bold (800)** | `font-weight: 800` | Hero headlines, brand statements |
| **Bold (700)** | `font-weight: 700` | Section headers, subheadlines, emphasis |
| **Medium (500)** | `font-weight: 500` | Body labels, captions, descriptors |

#### Typographic Styles

**Hero Headline** — Inter Extra Bold (800), ~108px, Brand Gradient fill, tracking -1px, cyan glow text shadow.

**Subheadline** — Inter Bold (700), ~48px, white, leading 1.1, tracking -0.48px.

**Descriptor / Label** — Inter Medium (500), ~12px, white at 30% opacity, tracking 1.2px, uppercase.

### Visual Language

**Background Treatment:** The brand uses a rich, deep Midnight Navy (`#0A1020`) as the primary background. This dark canvas allows the gradient and glow effects to create visual depth and convey technological sophistication.

**Geometric Elements:** Decorative geometric shapes — large circles and angular forms — appear as subtle overlays using mix-blend-mode: overlay. These elements add dimension without competing with content, reinforcing the data/tech aesthetic.

**Gradient Mesh / Atmospheric Effects:** Soft, ambient color washes (pink, blue, purple) appear in the background to create depth and visual interest. Used sparingly — should never overpower the primary brand colors.

**Corner Radius:** Cards and containers use `40px` border radius for a modern, approachable feel.

### Application: Dark Theme (Primary)

| Element | Value |
|---------|-------|
| Background | Midnight Navy `#0A1020` |
| Headlines | Brand Gradient text fill with glow |
| Body text | White |
| CTAs | Brand Blue `#3079E9` or Gradient fill |
| Secondary actions | Slate Blue `#6577A5` |

### Imagery Style

**Photography:** Diverse, professional headshots representing physicians of varied backgrounds, conveying the "Doctors Are People Too" concept — approachable, human, relatable.

**UI/Product Mockups:** Clean platform screenshots showing dashboards, NPI-level reporting, and campaign activation interfaces.

**Illustrations & Icons:** Minimal, modern line-style illustrations for conceptual diagrams (e.g., the data graph, channel maps).

**Data Visualizations:** Charts and stats presented in bold, clean layouts that emphasize performance metrics.

---

## Awards & Recognition

| Award | Date |
|---|---|
| **PM360 2024 Silver Award** — HCP Education category | January 2025 |
| **Baleon Capital Strategic Investment** — Growth equity for platform advancement and AI-powered solutions | February 2025 |

---

## Internal Reference

### File Naming Convention

All project files follow the standard: `EQ5-[Deal ID]-[Partner]-[Pharma]-[Brand]`

Example: `EQ5-1042-Relevate-Pfizer-Ibrance`

### Brand Assets Location

| Asset | Location |
|---|---|
| Logo SVG | [equals5.com/i/logo.svg](https://equals5.com/i/logo.svg) |
| Branded Assets Folder | [Google Drive — Branded](https://drive.google.com/drive/folders/1aoO01yLelLTpHVz0SpXQQT2K3Nh0mAJi) |
| Figma Brand Book | [Figma — Brandbook](https://www.figma.com/design/MoIYxNnhadZgmS7uFXr4Bf/Brandbook) |

---

*Equals 5 Inc. © 2026. All Rights Reserved.*
*Last updated: February 2026*
