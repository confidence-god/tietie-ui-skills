# Output contract

Use this contract when executing the `ui-build` workflow.

## Required intake questions

Ask these before implementation code:

1. What target stack should be used? Recommend `HTML + CSS` by default; allow `Vue` or `React`.
2. Which reference image is the canonical visual source?
3. What local asset library path should be used?
4. Which page should be built first?
5. Should multiple pages be generated now? If yes, warn that one-shot multi-page generation may reduce per-page fidelity.

Do not continue to high-fidelity page implementation without a local asset library.

## Design board file

Create an approval artifact in `outputs/`, usually named `design-board.html` or `<project>-design-board.html`.

Include:

- page background and texture sample
- neutral palette, accent palette, status palette
- typography hierarchy and font fallback stack
- card, panel, separator, button, tag, progress, and list item samples
- bottom navigation sample using the home page as the canonical structure
- selected or candidate assets from the local library
- CSS variables or design tokens
- notes about acceptable approximations

Stop after creating the board and ask the user to approve or request changes.

## Asset index

If repeated work is expected, create an index beside the asset library, for example:

- `asset-manifest.json`
- `asset-contact-sheet.html` or `asset-contact-sheet.png`
- `asset-mapping.md`

The manifest should capture path, category, dimensions when available, semantic tags when inferable, and selected UI usage.

## Screenshot report

After implementation, run one screenshot comparison and report:

- overall match judgment
- layout deviations
- color and texture deviations
- asset/icon mismatches
- typography mismatches
- recommended next manual or user-approved fix

Do not run repeated automatic correction loops unless the user explicitly asks.
