---
name: Banking demand forecast
description: A soft, rounded count chart that says Low, Medium or High demand in its own teal.
colors:
  field: "#F3F4F1"
  paper: "#FFFFFF"
  ink: "#1B1B1B"
  muted: "#5E6266"
  line: "#E3E4DF"
  track: "#ECEDE8"
  tint: "#E1EEF0"
  bar-rest: "#D9DBD5"
  class-low: "#5E98A5"
  class-medium: "#2C6F7B"
  class-high: "#0F3A44"
  error-ink: "#C23B22"
  error-bg: "#FCEDEA"
  error-line: "#F2C4BA"
typography:
  display:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "clamp(56px, 6.6vw, 96px)"
    fontWeight: 500
    lineHeight: 0.96
    letterSpacing: "-0.045em"
  figure-hero:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "min(112px, 36cqi)"
    fontWeight: 500
    lineHeight: 0.86
    letterSpacing: "-0.06em"
    fontFeature: "tnum"
  figure:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "48px"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.04em"
    fontFeature: "tnum"
  headline:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "22px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "15px"
    fontWeight: 600
  body:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  lead:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: 1.5
  pill:
    fontFamily: "Urbanist, sans-serif"
    fontSize: "13px"
    fontWeight: 500
rounded:
  field: "16px"
  card: "24px"
  panel: "32px"
  pill: "999px"
spacing:
  page: "20px"
  card: "24px"
  panel: "28px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "0 8px 0 26px"
    height: "56px"
  button-quiet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0 16px"
    height: "40px"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    height: "52px"
  segmented:
    backgroundColor: "{colors.field}"
    textColor: "{colors.muted}"
    rounded: "{rounded.pill}"
    padding: "4px"
  segmented-selected:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "9px 12px"
  nav-link:
    textColor: "{colors.muted}"
    rounded: "{rounded.pill}"
    padding: "9px 18px"
  nav-link-current:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
  pill:
    backgroundColor: "{colors.field}"
    textColor: "{colors.muted}"
    typography: "{typography.pill}"
    rounded: "{rounded.pill}"
    padding: "5px 12px"
  trust-pill:
    backgroundColor: "{colors.tint}"
    textColor: "{colors.class-high}"
    rounded: "{rounded.pill}"
    padding: "7px 16px 7px 10px"
  card:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.card}"
    padding: "22px 24px 24px"
  panel:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.panel}"
    padding: "{spacing.panel}"
  forecast-tile-medium:
    backgroundColor: "{colors.class-medium}"
    textColor: "{colors.paper}"
    rounded: "{rounded.card}"
  forecast-tile-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error-ink}"
    rounded: "{rounded.card}"
  pipeline:
    backgroundColor: "{colors.class-high}"
    textColor: "{colors.paper}"
    rounded: "{rounded.card}"
    padding: "28px 32px 30px"
---

# Design System: Banking demand forecast

## Overview

**Creative North Star: "The Count Chart"**

A light, rounded dashboard on a pale field where every answer is a count and a class. White cards and panels sit softly on the field; one ink colour carries text and the primary action; the three demand classes are the only chroma, each a step on one teal ramp. The answer is told as a sentence ("NN.N% chance of Medium demand") on a tile filled with that class's teal.

Playful in motion, sober in palette: words rise from masks, cards float in on a back-ease, bars grow and the probability counts up, yet nothing is coloured that does not mean a class, an error or the ink. Product truth (scope, test contract, responsible-use wording) lives in PRODUCT.md.

Light theme only; the approved comp (design/demo.html) pins it and `.streamlit/config.toml` sets `base = "light"`.

**Key Characteristics:**
- Pale field, white paper, near-black ink; teal only for classes and focus.
- Big rounded panels (32px), cards (24px), fields (16px); every control a pill.
- Large medium-weight Urbanist with tight negative tracking and tabular figures.
- Soft teal-tinted shadow; hover pools a shadow in the card's own colour.
- Motion everywhere, all behind `prefers-reduced-motion: no-preference`.

## Colors

A near-neutral warm-grey ground with a single three-step teal ramp that means "demand class".

### Primary
- **Class Medium, Harbour Teal** (class-medium): the Medium class, the default forecast tile, focus outlines (2px, 3px offset), links, the footer wordmark, and Streamlit's `primaryColor`.

### Secondary
- **Class Low, Shallow Teal** (class-low): the Low class wherever it appears (hero pill, bars, forecast tile, threshold band).
- **Class High, Deep Teal** (class-high): the High class; also the pipeline loader surface and the text on tint pills.

### Neutral
- **Field** (field): page ground, pill and segmented-track fill, dropzone hover.
- **Paper** (paper): cards, panels, fields, quiet buttons; white text on teal and ink.
- **Ink** (ink): all primary text, the Predict button, current nav pill, highlighted last-quarter bars and chart annotations.
- **Muted** (muted): labels, hints, axis text, inactive nav and segments, field hover border.
- **Line** (line): field borders, chart gridlines, the dashed idle outline.
- **Track** (track): empty probability tracks and unselected threshold bands.
- **Tint** (tint): trust pill, "Predicted" tag, text selection.
- **Bar at rest** (bar-rest): monthly bars outside Aug-Oct.

### Error
- **Error ink / Error wash / Error line** (error-ink, error-bg, error-line): the error tile, failed check, failed pipeline step, negative-count bars. Never used for anything but invalid input.

### Named Rules
**The Own Teal Rule.** Low, Medium and High are always shown in their own teal (class-low, class-medium, class-high), on every surface: hero pill, probability bar, forecast tile, threshold band. A class never borrows another's colour, and no other hue stands in for a class.

**The Ink Action Rule.** The primary action is ink, not teal. Teal means a class; ink means "do this".

## Typography

**Display Font:** Urbanist (Google Fonts, 400-700), sans-serif fallback
**Body Font:** Urbanist
**Label/Mono Font:** Urbanist; code spans use the platform monospace

**Character:** One geometric sans throughout. Size and tracking make the hierarchy: display and figures run large at weight 500 with tight negative tracking; titles and emphasis step up to 600.

### Hierarchy
- **Display** (500, clamp(56px, 6.6vw, 96px), 0.96, -0.045em): the hero headline only, max 8em wide. 52px under 860px, 40px under 560px. The footer wordmark uses the same voice larger (clamp(56px, 10.5vw, 156px), -0.055em) in class-medium.
- **Figure, hero** (500, up to 112px scaled by container, 0.86, -0.06em): the forecast probability.
- **Figure** (500, 48px, 1, -0.04em): card numbers, "No forecast yet" (46px), pipeline status. A 15px muted 500 unit follows inline.
- **Headline** (600, 22px, 1.3, -0.015em): panel and section titles ("Input", "Prediction", reference sections).
- **Statement** (600, up to 40px, -0.035em): the class name in "chance of <Class> demand".
- **Title** (600, 15px): card titles in the card top row.
- **Lead** (400, 20px, 1.7): hero sentence, max 30em.
- **Body** (400, 16px): default; long prose capped at 82ch.
- **Label** (500, 14px): widget labels, hints, segment labels, nav, buttons (Predict is 16px 600).
- **Pill** (500-600, 12-13px): pills, tags, axis text.

### Named Rules
**The Tabular Rule.** `font-variant-numeric: tabular-nums` is set app-wide; every count and percentage aligns.

**The Medium Weight Rule.** Large type is weight 500 with negative tracking, never 700. Bold (700) is reserved for small class pills, tags and chart callouts.

## Layout

A single centred column, max 1480px, padded 20px (12px under 560px). Below the top bar and hero, an input panel (4 parts) sits beside the prediction column (8 parts) with Streamlit's small gap. Prediction rows split 7:5: observed history or chance-by-class on the left, forecast tile or last quarter on the right; cards in a row stretch to share a height.

Reference sections (Feature guidance, Model and limits, Test evidence) are large panels that open in place, reached by top-nav anchors. The footer closes with a warning line and the name returned large.

Responsive: at 1100px the panel stacks above the prediction; at 860px nav hides, card rows stack and the forecast tile moves first; at 560px the hero becomes copy over a 180px image strip, the scope pill hides and padding tightens. The segmented control reflows by container query (380px, 320px).

## Elevation & Depth

Soft and ambient. One shared shadow, tinted toward class-high, lifts cards, panels and the pipeline off the field. Coloured tiles carry no extra lift; the idle tile and error tile drop the shadow for an outline.

### Shadow Vocabulary
- **Rest** (`0 1px 2px rgba(15,58,68,.05), 0 24px 32px -28px rgba(15,58,68,.16)`): cards, panels, pipeline, reference sections.
- **Pool** (rest plus `0 16px 22px -16px <card colour>`): hover on cards and forecast tiles; the shadow takes the card's own colour (teal at 32% for white cards, the tile's teal at 75% for forecast tiles).
- **Segment lift** (`0 1px 3px rgba(15,58,68,.1)`): the selected segment only.

### Named Rules
**The Pool Rule.** Cards do not move on hover; a small shadow in their own colour pools beneath them.

## Shapes

Generous, soft corners in three tiers: panels and hero 32px, cards, tiles and the pipeline 24px, fields and dropzone 16px. Every control, pill, nav link, segment, tag, chart callout and probability track is a full pill (999px); arrow and pipeline step marks are circles. Borders are 1px line; the dropzone is 1.5px dashed, the idle tile a 2px dashed inset outline. The brand mark is three stacked slips (a folded-corner document) in the three class teals; a single ink slip prefixes "Prediction".

## Components

### Buttons
- **Shape:** full pill (999px).
- **Primary (Predict):** ink, white 16px 600 label, 56px tall, full width, with a 40px white circle holding an ink arrow on the right. Hover rotates the circle -45deg on the back-ease (.45s); press scales to .97.
- **Quiet (downloads, browse):** paper with line border, ink 14px 500 label, 40px tall. Hover darkens the border to ink and lifts 2px on the back-ease.

### Chips
- **Pill:** field fill, muted 13px text; on teal or error tiles it becomes an 18% wash of the tile's text colour.
- **Trust pill:** tint with class-high text and a stroked tick; error variant uses error wash and ink; quiet variant is paper and muted. When a prediction lands, Streamlit's success alert is restyled as this pill.
- **Class pills (hero):** each class word on a 16% wash of its teal; a white-text copy clipped over it sweeps while predicting and fills for the predicted class, so the word never changes colour.

### Cards / Containers
- **Corner Style:** 24px cards, 32px panels.
- **Background:** paper.
- **Shadow Strategy:** Rest, with Pool on hover.
- **Internal Padding:** cards 22px 24px 24px (20px on small screens); panel 28px (22px 18px).
- **Top row:** 15px 600 title left, pill right.

### Inputs / Fields
- **Style:** paper, 1px line border, 16px radius, 52px select height, 16px 500 value.
- **Hover / Focus:** border to muted on hover, to class-medium on focus-within.
- **Segmented control:** Streamlit's radio restyled as a field-coloured pill track; the selected segment is paper with Segment lift and 600 ink text; press scales .95.

### Navigation
- **Top bar:** slip-mark brand (18px 600), pill nav links (muted, paper on hover, ink with white text when current), and a line-bordered scope pill pushed right. Nav hides under 860px, scope under 560px.

### Forecast tile (signature)
Filled with the predicted class's teal, white text. Reads top to bottom: probability at hero-figure size counting up from zero (700ms), "chance of" then the class name rising word by word, a per-month range line, and pills for "Forecast" and the window. Idle: paper with a dashed line outline and "No forecast yet". Error: error wash, 1px error-line outline, "No forecast" and the validation message set at 24px 600.

### Pipeline loader (signature)
A class-high card titled "Data processing" with a hairline track and three 82px white step circles (Validate inputs, Preprocess, Random Forest) that pop in on the back-ease as the white fill line draws. On invalid input the fill stops at Validate, that step turns error wash with a cross, and the later steps dim to 14% white.

### Charts
Inline SVG in Urbanist. Monthly bars (bar-rest, Aug-Oct in ink, negatives in error ink) grow from the baseline, with an ink bracket and ink pill callout over Aug-Oct. Last quarter lays the count against three pill threshold bands (track; the predicted band at 30% of its teal) with an ink marker. Chance by class uses pill tracks filled in each class's teal.

## Do's and Don'ts

### Do:
- **Do** show each class in its own teal everywhere (Low #5E98A5, Medium #2C6F7B, High #0F3A44).
- **Do** keep the primary action an ink pill with the white arrow circle.
- **Do** use back-ease `cubic-bezier(.175,.885,.32,1.275)` for pops, floats and button presses, and out-expo `cubic-bezier(.16,1,.3,1)` for reveals, rises and fills.
- **Do** put every animation inside `@media (prefers-reduced-motion: no-preference)`; content is visible by default. First-load motion (word-rise headline, panel float) keys off a session flag so reruns do not replay it.
- **Do** ship SVG through `ui.svgx` (escaped in `data-svg`, restored by the HYDRATE observer); `st.html` strips raw `<svg>`.
- **Do** style Streamlit widgets through `st-key-<key>` classes and Streamlit `data-testid`s.
- **Do** keep test-asserted widget keys, labels, metric order and error texts unchanged (see PRODUCT.md); reorder visually with CSS `order` instead, as the forecast tile does.

### Don't:
- **Don't** introduce a dark theme; the system is light only.
- **Don't** give UI elements a hue outside the teal ramp, ink and greys, except error red for invalid input. (The hero photograph keeps its own colour, desaturated to 80% under a 10% class-medium multiply.)
- **Don't** colour the Predict button teal; teal is reserved for classes, focus and links.
- **Don't** set display or figure type at 700; large type is 500 with negative tracking.
- **Don't** use square or small-radius controls; controls are pills (the segmented control alone relaxes to 16-20px when its container drops below 380px), containers use the 16/24/32px tiers.
