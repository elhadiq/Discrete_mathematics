# Discrete Mathematics — Project Memory

Static HTML course site for the "Discrete Mathematics" course.
Deployed via GitHub Pages.

Instructors:**Pr. Zouhair El Hadiq** & **Pr. Ismail Bouishak**.
The site is signed *"Notes By Pr. El Hadiq Zouhair"* on lessons authored here.

---

## Author / signing convention

Every lesson and exercise file authored in this project carries the italic orange line:

```html
<p style="font-size:1rem;color:#e67e22;margin-top:0.8rem;font-style:italic;
          font-weight:600;letter-spacing:.02em;">Notes By Pr. El Hadiq Zouhair</p>
```

The énoncés/exercises pages may use the shorter form `By Pr. El Hadiq Zouhair`.
**Never** remove the signature.

---

## Folder layout

```
Discrete_mathematics/
├── index.html                       ← landing page (collapsible session cards)
├── CLAUDE.md                        ← this memory file
└── Content/                         ← all course content lives here
    ├── course_overview.html
    ├── assignment_lessons2_3.html
    ├── Presentation/                ← shared slide / static assets
    ├── logic/                       ← Session 1 — Foundations of Logic
    │   ├── Lesson1/  presentation.html         exercises_lesson0.html
    │   ├── Lesson2/  proposition_logic.html    exercises_lesson2.html
    │   ├── Lesson3/  lesson3_moodle.html       exercises_lesson3.html
    │   ├── Lesson4/  lesson4_predicates.html   exercises_lesson4.html
    │   └── Lesson5/  lesson5_inference.html    exercises_lesson5.html
    └── Discrete Structures/         ← Session 2 — Discrete Structures (Python)
        ├── Sets/                       slides → Lesson/sets.html
        │   └── Lesson/    sets.html
        │                  exercises_sets.html              (with solutions)
        │                  exercises_sets_enonces.html      (no solutions)
        ├── Operations on Sets/
        │   └── Lesson/    operations_on_sets.html
        │                  exercises_operations_on_sets.html
        │                  exercises_operations_on_sets_enonces.html
        ├── Relations and Functions/
        │   └── Lesson/    relations_and_functions.html
        │                  exercises_relations_and_functions.html
        │                  exercises_relations_and_functions_enonces.html
        └── Sequences and Series/
            └── Lesson/    sequences_and_series.html
                           exercises_sequences_and_series.html
                           exercises_sequences_and_series_enonces.html
```

Each topic folder in `Content/Discrete Structures/<topic>/` also contains the
source `slide_XXXX.png` images that the lesson was built from.

**All href paths in `index.html` are relative to the repo root and start
with `Content/`** (e.g. `Content/logic/Lesson2/proposition_logic.html`,
`Content/Discrete%20Structures/Sets/Lesson/sets.html`).

---

## Visual / theme conventions

Reference file: **`logic/Lesson2/proposition_logic.html`** — every new lesson page
must reuse this look exactly.

CSS variables used on every lesson page:

```css
--orange:    #e67e22;
--darkblue:  #2c3e50;
--lightbg:   #f4f9fc;
--border:    #dce3ea;
/* Python blue (replaces Wolfram teal in this project) */
--py-fg: #1f4e7a;  --py-bg: #eaf3fb;  --py-border: #2a6fb3;  --py-head: #2a6fb3;
/* SymPy green */
--sp-fg: #1e824c;  --sp-bg: #e8f5ec;  --sp-border: #27ae60;  --sp-head: #27ae60;
/* Setup indigo */
--su-fg: #4a4aaa;  --su-bg: #eeeeff;  --su-border: #6060cc;  --su-head: #6060cc;
/* Output amber */
--out-fg: #6e4b0a; --out-bg: #fff7e0; --out-border: #e0b341; --out-head: #c89324;
```

Standard building blocks (class names — keep them stable across pages):

- `.slide` — white rounded card, max-width 940px
- `.slide.title-slide` — gradient cover with `h1` + subtitle + signature
- `h2.frame-title` — orange section title with bottom border
- `h3.sub-title` — smaller orange sub-heading
- `.code-pair` / `.code-pane` (`.python-pane`, `.sympy-pane`) — side-by-side code blocks
- `.python-block` / `.sympy-block` / `.setup-block` / `.output-block` — single-pane code blocks
- `.pane-label`, `.pane-code` — label header + code content
- `.truth-table` — bordered tables with `tr.row-t` (red tint) and `tr.row-f` (blue tint)
- `.note-box` — orange-left italic callout
- `.venn-wrap` — centered inline SVG container

Each lesson ends with a fixed slideshow navigation:

```html
<div id="nav">
  <button id="btn-prev">←</button>
  <button id="btn-scroll">Slideshow</button>
  <button id="btn-next">→</button>
</div>
```

with JS that toggles `body.slideshow` and uses arrow keys / buttons.

MathJax is loaded on every page from
`https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js` with
`inlineMath: [['$','$']]`.

---

## Content conventions

- **Python first, no Wolfram Language.** The original Wolfram course was
  translated: built-in `set`, `itertools`, `math`, `functools`, `fractions`
  for plain Python; **SymPy** for symbolic work (`FiniteSet`, `Interval`,
  `Union`, `Intersection`, `Complement`, `ProductSet`, `Sum`, `Product`,
  `Lambda`, `solve`, `rsolve`, `simplify`, `continuous_domain`,
  `function_range`, `catalan`, `prime`, etc.).
- Every lesson ends with a **"Wolfram → Python Quick Reference"** table so
  the equivalence to the original course is explicit.
- Every exercises file has a **paired `_enonces` version** that is
  byte-for-byte the same content but with solution blocks replaced by a
  dashed `.answer-space` placeholder.

### Exercises page structure

- 12 graded exercises per topic, tagged with `.difficulty` chips:
  `.easy` (green), `.medium` (amber), `.hard` (red).
- TOC slide at the top with anchor links to each `#exN`.
- Each exercise wraps its solution in:

  ```html
  <details class="solution"><summary>Solution</summary>
    <div class="python-block">…</div>
  </details>
  ```

- Énoncés version replaces the `<details>` block with:

  ```html
  <div class="answer-space">Your answer…</div>
  ```

---

## `index.html` behavior

- Top of page: hero + **Quick Access** (Course Overview, Assignment 1).
- Then a single **Sessions** grid of 6 cards — collapsed by default.
- Sessions 1 and 2 are clickable; clicking a session opens a `.course-panel`
  below the grid with the lesson cards. Only one panel open at a time.
- Sessions 3–6 are styled `.session.coming` with a "Coming soon" tag and are
  non-interactive.
- All href paths to `Discrete Structures/` use `%20` for spaces so GitHub
  Pages resolves them.
- The JS toggle lives at the bottom of the file (vanilla JS, no framework).

---

## When extending the site

1. New session content → drop files under `Content/<appropriate folder>/`, then
   add a new `.lesson-card` inside the matching `.course-panel` in `index.html`.
   Hrefs **must** start with `Content/…`.
2. New session → add a `.session` card to the `Sessions` grid with
   `data-target="panel-XYZ"` and a `<div class="course-panel" id="panel-XYZ">`.
3. Slide images for a new topic live under
   `Content/Discrete Structures/<Topic>/slide_XXXX.png`; build the HTML lesson
   from them inside `Content/Discrete Structures/<Topic>/Lesson/`.
4. Always produce the *énoncés* twin alongside any new exercises file.
5. Keep the signature, the orange/darkblue palette, and the
   `proposition_logic.html` layout — it is the canonical template.
