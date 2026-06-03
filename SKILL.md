---
name: mockup-builder
description: Generate Balsamiq-style wireframe HTML demos compliant with the in-house mockup-kit design system. Use when the user provides a screenshot, sketch, or text prompt and asks to "用规范生成 HTML"、"按这套规范画一版"、"做个 demo / wireframe / 低保真"、"基于 mockup-kit 出页面" or similar. Produces a single self-contained HTML file (or a multi-variant scroll-spy file) using only design tokens, iconoir icons, and the regulation component classes — never custom hex colors, emoji icons, or invented component classes.
---

# Mockup Builder

## Overview

This skill turns screenshots / sketches / text prompts into a single self-contained HTML file that strictly follows the in-house **mockup-kit** wireframe spec (see `docs/mockup-kit.html` for the full living spec; or rely on `references/components-cheatsheet.md` here for the distilled cheatsheet).

**Spirit of the skill:** It produces *structural wireframes*, not visual designs.
The agent's job is to lay out information correctly — never to make it "prettier".
Polish is Figma's job; structure is this skill's job.

## Quick Start (90% case)

For a typical request — "用这个规范帮我把这张图做成 HTML" / "做个 dashboard demo" — follow this order:

```
1. read references/red-lines.md          ← the must-not-do list
2. read references/components-cheatsheet.md ← the lego catalog
3. (if screenshot involved) read references/theme-mapping.md ← pick theme
4. python3 scripts/new_demo.py <out>.html --theme <X> --title "<T>"
   # ↑ this also opens the file in the default browser by default
   # add --no-open if the user asked for "just generate, don't open"
5. open <out>.html, replace the <!-- SLOT:body --> placeholder block with real structure
6. python3 scripts/lint_demo.py <out>.html --open   ← pre-flight + re-open final
7. report path + theme + chosen accent + 1-line rationale
```

If the user wants **multiple variants on one page** ("再给我画两版 / 三种方案对比") add `--multi`:

```bash
python3 scripts/new_demo.py options.html --multi --title "Three options"
```

This swaps in `assets/template-multi.html` which has a sticky left TOC + ScrollSpy + multiple `.variant` sections.

## Workflow Decision Tree

```
User input?
│
├─ Screenshot
│   └─ Read theme-mapping.md → pick theme by accent color
│      └─ Identify regions top-down → map each to a regulation component
│         └─ Generate single-page (template-base) directly. Skip outline confirm.
│
├─ Text prompt (vague)
│   └─ Ask 1 question only: "单页 or 多版对比？" + "有偏好的主题色吗？(default/yellow/green/purple/pink)"
│      └─ Optionally produce a 5-line outline; confirm; then generate.
│
├─ Sketch / lo-fi mock
│   └─ Same as screenshot, but inference is looser.
│
└─ "改一下/加一块/换个主题"
    └─ Edit only the relevant slot. Never reflow unrelated structure.
```

## Hard Rules (Red Lines)

These four are non-negotiable. The lint script enforces them.

1. **Colors → tokens only.** Use `var(--color-*)`. Never `#xxx` or `rgb()` outside `:root` / `body[data-theme]`.
2. **Icons → iconoir only.** Always `<i class="iconoir-XXX"></i>`. Emoji is forbidden.
3. **Classes → regulation only.** Use `.btn` / `.card` / `.list` / `.accordion` / etc. Never invent `.my-foo` / `.special-bar`.
4. **Sizes → scale only.** Use `var(--sp*)` and `var(--fs-*)`. No raw `padding:13px` / `font-size:17px`.
5. **Mobile frame → 375px width, 8px radius (mandatory).** Use `width:375px` on `.phone-frame`. Never use other widths (300 / 360 / 390px). Do NOT include `.phone-notch` or `.phone-home` — both are hidden by the spec.
6. **Desktop frame → 1440px width (mandatory).** Use `.browser-frame` with `width:1440px` for any PC / desktop page. Never shrink it arbitrarily.

Full list with anti-patterns: `references/red-lines.md`.

## Theme Selection

Five themes are available: `default` (blue), `yellow`, `green`, `purple`, `pink`.

- If the user names a color, map directly.
- If a screenshot has an accent color, use the decision tree in `references/theme-mapping.md`.
- If unsure → `default`.
- Black/gold premium brands → still `default`, with **localized** ink-black hero card (see theme-mapping for the exact pattern).
- **Never invent a new theme.** If the user wants one, tell them: "新主题色属于规范级修改，建议在 mockup-kit 里加一个新 `body[data-theme=...]` 变体后再使用。"

## Component Coverage

The cheatsheet (`references/components-cheatsheet.md`) covers everything that should ever be needed:

- Layout: page wrapper, two-column, navbar, breadcrumb
- Forms: input variants, select, textarea, checkbox, radio, toggle, slider
- Actions: button matrix (primary/danger/success/ghost/outline/sm/lg/icon/block)
- Data display: card, list (+ section header), table, accordion (line / card; mutex by default), tabs (boxed/underlined), pagination, stepper (horizontal desktop), stepper-mobile-vertical (`.m-stepper` — current+next shown by default, expandable, no collapse)
- Status: avatar (4 sizes + sq), badge, tag, alert (4 semantics), toast, progress, spinner, skeleton, empty-state
- Overlays: modal, dropdown, popover, tooltip, bottom-sheet
- Frames: phone-frame, browser-frame
- Icons: 80+ common iconoir names listed by category

If a user asks for something **not** in the cheatsheet, the answer is: "这个组件 mockup-kit 还没收录。要么用现有组件拼，要么先把它加到规范里再用。" Do not invent CSS for it on the fly.

## Generation Protocol

When writing the body:

1. **Top-down structure first.** Identify regions (navbar / breadcrumb / hero / content grid / footer / floating actions) before any styling thoughts.
2. **One regulation class per region.** Pick the closest cheatsheet match.
3. **Page-specific tweaks go in `<!-- SLOT:page-styles -->`.** And those tweaks must still use tokens.
4. **Keep copy concise.** Use placeholder-y but plausible English/Chinese mix; this is a wireframe.
5. **Never animate.** The template's built-in micro-interactions (hover lift, chevron rotate) are sufficient.

## Validation Before Delivering

Always run the lint script before reporting back:

```bash
python3 scripts/lint_demo.py <out>.html
```

It catches: hardcoded hex outside `:root`/theme blocks, emoji used as icons, suspicious custom class names. If it warns, fix in place — do not ship.

## When the User Pushes Back

Common pushback and the right response:

| User says | Answer |
|---|---|
| "再做精致一点" | "Mockup-kit 是 wireframe 风格，再精致需要进 Figma；这边只能调整结构 / 信息层级。要不要我重新组织一下区块？" |
| "换个真实的图 / logo" | "用 `.img-ph` 占位是规范要求；真图请到 Figma 阶段再贴。" |
| "加个渐变 / 玻璃拟态" | "这是规范级修改，建议先加到 mockup-kit 里。当前 demo 不能加。" |
| "颜色我自己挑一个 #abcdef" | "5 个主题之外的颜色不能直接写。要新色请加到 mockup-kit 的 `body[data-theme]` 里。" |
| "字体换一下" | 同上：font 是 token，规范级。 |

## Reference Files

- `references/red-lines.md` — the must-not-do list with anti-pattern code examples
- `references/components-cheatsheet.md` — the lego catalog (always read this first)
- `references/theme-mapping.md` — how to pick a theme from a screenshot or description

## Asset Files

- `assets/template-base.html` — single-page template (default starting point)
- `assets/template-multi.html` — multi-variant page with sticky TOC + ScrollSpy

## Scripts

- `scripts/new_demo.py [out] [--theme X] [--title T] [--multi] [--no-open]` — bootstrap a fresh file from a template; auto-opens in browser unless `--no-open`
- `scripts/lint_demo.py <file> [--open]` — enforce the four red lines; optionally re-open in browser when lint passes
