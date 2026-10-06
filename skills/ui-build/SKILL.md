---
name: ui-build
description: Build high-fidelity front-end UI code from image2-generated product UI references. Use when the user wants to reconstruct a UI from screenshots or product images into HTML/CSS, Vue, or React, with a mandatory style-approval stage, a local asset library, reusable design-system extraction, and a one-shot screenshot comparison.
---

# UI Build

Reconstruct product UI pages from reference images with a focus on visual fidelity, shared structure, and reusable front-end patterns.

## Core rules

- Always ask for the target stack before generating implementation code.
- Default to `HTML + CSS`, but support `Vue` and `React` when the user chooses them.
- Require a local asset library before high-fidelity reconstruction. If the user does not provide it, stop and request it.
- First produce a design-board preview for approval; do not build the page until the user confirms the style.
- Build a shared design system first, then page code.
- Keep bottom navigation structurally consistent across pages and treat the home page as the canonical reference.
- Use assets from the provided folder tree; prefer the visually closest match within the relevant folder category.
- Run only one automatic screenshot comparison after implementation, then output a short report. Do not loop repeatedly.

## Workflow

Read [the output contract](references/output-contract.md) when creating the design board, asset index, or screenshot report.

1. Inspect the reference image and local asset library.
2. Extract reusable UI rules: background, palette, typography, spacing, card shapes, borders, shadows, header treatment, bottom nav, icon sizing, and illustration usage.
3. Identify likely reusable components and list them before implementation.
4. Generate a design-board page in `outputs/` that previews the palette, typography, shared components, and bottom navigation.
5. Ask the user to approve the visual direction.
6. After approval, ask for or confirm the target stack.
7. Implement the target page or pages using the approved shared system.
8. Map assets from the library by folder:
   - `icons/`: small icons, status icons, function icons
   - `stickers/`: characters, decorative stickers, emoji-style assets
   - `badges/`: badges, labels, corner marks, signboards
   - `panels/`: cards, panels, overlays, base surfaces
   - `decorations/`: ornaments, patterns, borders, separators
   - `textures/`: paper grain, noise, material backgrounds
   - `ui_components/`: visual blocks that map directly to interface components
   - `uncertain_assets/`: ambiguous or low-confidence assets
9. Prefer the visually closest asset inside the right folder; use filename meaning only as a secondary tie-breaker.
10. Run one screenshot comparison, note the main deviations, and stop.

## Design-board expectations

- Present the palette as a front-end page, not just a text list.
- Include shared tokens for background, ink, accent colors, surface colors, border colors, and state colors.
- Include typography samples and size hierarchy.
- Include reusable component samples when useful, especially navigation and primary cards.
- Show the approval-ready direction clearly so the user can confirm or reject the style.

## Implementation expectations

- Prioritize overall texture, mood, layout hierarchy, and visual consistency.
- Allow approximate fonts when exact matches are unavailable.
- Approximate corner radii, shadows, and spacing when needed, but keep the result close to the reference.
- Prefer reconstruction over redesign.
- Keep logic simple and avoid introducing unnecessary UI behavior.

## Output expectations

- Put generated preview pages and implementation artifacts in `outputs/`.
- If useful, create a nearby asset index beside the local library so future pages do not rescan everything.
- Return a brief post-build report covering visual match, notable gaps, and the next recommended fix.
