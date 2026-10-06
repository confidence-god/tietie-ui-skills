---
name: ui-design
description: Generate high-quality multi-page app design images with a real image-generation model from an MVP brief and one or more visual references. Use when the user wants the entire MVP project audited first, a page-by-page image-generation queue, and one-page-at-a-time generation with user review between pages. Analyze references such as screens, mascots, characters, scenes, backgrounds, components, icons, or mixed assets; preserve visual and character continuity across pages. Do not implement frontend code, HTML, a website, a complete design system, component cutouts, or programmatic substitute drawings.
---

# UI Design

## Overview

Translate two inputs into a coherent set of app design images:

- The MVP determines what the product must contain.
- The references determine how that product should look and feel.

Produce final visual design images only. Use a real image-generation model for every design image. Do not create intermediate HTML, frontend code, a live webpage, a component library, a design-system document, a manifest, or a large collection of intermediate assets.

## Image Generation Policy

Use this routing order for every generated image:

1. Use the built-in `image_gen` capability when available. Prefer `gpt-image-2`.
2. If `image_gen` is unavailable, inspect the current environment for other available image-generation skills or tools. Prefer the `image2` skill when available, using its configured `gpt-image-2` relay workflow.
3. If no image-generation skill is available, use `scripts/image_gen.py` only when that CLI fallback exists and its credentials are configured. The fallback must still call a real image-generation model.
4. If all real image-generation routes are unavailable, stop and clearly tell the user that image generation cannot be completed in the current environment.

Never silently substitute Python drawing, PIL, Matplotlib, Canvas, SVG construction, HTML/CSS screenshots, manually assembled raster primitives, or other programmatic artwork for a real image-generation model. Do not report success unless the requested final PNG/JPEG file was actually generated.

Before generation, verify the selected route and its configuration. For the `image2` route, respect its documented environment variables, including `GPT_IMAGE2_API_KEY` or `OPENAI_API_KEY`, `GPT_IMAGE2_BASE_URL` or `OPENAI_BASE_URL`, and `GPT_IMAGE2_MODEL`. Prefer `gpt-image-2` unless the user explicitly requests another available model.

If a route fails, record the failure briefly, try the next permitted route, and do not fall back to programmatic drawing. If no permitted route succeeds, return the failure clearly.

## Workflow

### 1. Audit the entire MVP project

Before generating any image, inspect the complete available project context:

- MVP brief and product goal
- Complete page list and navigation
- User flows and page relationships
- Required content, states, and functional modules
- Existing screenshots, wireframes, brand assets, and visual references
- Target platform, device, orientation, and viewport requirements

Treat the MVP as the only source of truth for product structure:

- Do not omit, delete, merge, or silently simplify any MVP-defined functional module.
- Do not add functional modules that are not present in the MVP.
- Keep page relationships, navigation, labels, states, and content requirements faithful to the MVP.
- If the MVP is ambiguous or internally inconsistent, ask a focused clarification before generating the affected page.

### 2. Build and confirm the image-generation queue

Determine which MVP pages need final image-generation output. Include pages that require visual design exploration or approval. Exclude purely technical routes, duplicate states that can be represented within another page, and pages the user explicitly does not want visualized. Do not merge distinct MVP pages merely to reduce the image count.

Present a compact queue before starting image generation. For each page, include:

- Page name and sequence position
- MVP purpose
- Required functional modules and important states
- Relevant references or recurring visual elements
- Whether it is the visual anchor page or a dependent page

Use the homepage as the default first page unless the MVP or user specifies another order. Ask the user to confirm or adjust the queue when page scope or order is uncertain. Do not generate a page before the queue is clear.

The queue is a lightweight conversation checklist, not a design document, manifest, design system, or large intermediate asset set.

### 3. Classify and analyze references

Inspect every supplied reference independently before combining them. Classify each as one or more of:

- Complete app page or screen
- Mascot or character
- Character illustration
- Environment or scene illustration
- Background or texture
- Component or UI pattern
- Icon, symbol, logo, or ornament
- Mixed reference

Extract only transferable visual information:

- Overall art direction and emotional tone
- Color relationships and accent hierarchy
- Material, texture, grain, paper, glass, metal, fabric, or surface treatment
- Line quality, contour language, edge softness, and rendering style
- Light direction, contrast, shadow softness, and atmospheric depth
- Composition language, density, rhythm, framing, and negative space
- Character identity, silhouette, pose language, costume, and signature accessories
- Reusable decorative motifs, symbols, patterns, or environmental cues
- Typography mood when typography is visibly part of the reference

Do not treat the literal layout of a reference screen as a requirement. A reference may provide visual DNA without providing page structure.

When references conflict, prioritize them in this order:

1. Explicit user direction
2. References that define the overall art direction
3. References that define recurring characters, objects, or motifs
4. References that define local details such as icons or textures

### 4. Lock continuity and confirm a compact visual direction

Before the first image, establish a compact continuity lock for the whole project. Keep it in the active conversation context and reuse it for every page:

- Global visual anchors: palette relationships, materials, linework, rendering, lighting, composition density, typography mood, and decorative vocabulary
- Mascot or character anchors: identity, silhouette, body proportions, face and eyes, colors and markings, costume, signature accessories, expression range, and pose language
- Recurring object anchors: shape language, scale relationships, surface treatment, and identifying details
- Forbidden drift: details that must not be redesigned, removed, recolored, aged, simplified, or replaced

When a mascot or recurring character exists, treat the original character reference as a persistent identity reference. Reuse the same continuity description and the original reference image whenever the generation tool supports image references or editing. Use approved page images as additional style and continuity references, but do not copy their layouts.

Before generating the first page, decide whether a short style confirmation is useful:

- Ask for confirmation when references have materially different visual directions, the intended fidelity is unclear, or a major interpretation could change the result.
- Proceed directly when the direction is coherent and the user has clearly asked for generation.

If presenting a confirmation, output only a short visual direction summary. Do not create a design document, manifest, design system, visual specification, or large intermediate asset set.

Example:

```text
Visual direction:
- Warm paper texture
- Hand-drawn dark brown linework
- Muted blue accent color
- Soft shadows
- Magical fairytale mood
- Black cat as the core character
- Medium decorative density
```

### 5. Generate exactly one queued page

Work through the confirmed queue in order. Generate exactly one page per interaction cycle. Never generate the remaining pages automatically as a batch.

For the first page, establish the project's visual anchor. For later pages, use the locked continuity anchors, the original relevant references, and previously approved page images as consistency references when the selected tool supports them.

Every generated page must:

- Represent the MVP-defined page structure and required modules
- Use reference-derived visual DNA without reproducing a reference layout
- Make required content and primary actions legible
- Match the requested device, orientation, and viewport
- Preserve the mascot's locked identity and recurring visual details

For each page cycle:

1. State which queued page is being generated and briefly restate its MVP modules.
2. Build the prompt from the continuity lock plus that page's MVP requirements.
3. Generate one final PNG or JPEG using a real image-generation model.
4. Stop and show the result for user review.
5. Wait for explicit approval, revision feedback, or a request to regenerate.
6. Only after approval mark the page complete and proceed to the next queued page.

If the user requests changes, revise only the current page until approved. Do not advance the queue while the current page is pending review.

### 6. Maintain cross-page consistency

Use these rules throughout the queue:

- Repeat the same global visual anchors in every generation prompt.
- Repeat the same mascot and recurring-character identity block, changing only page-specific pose or context.
- Prefer reference-conditioned generation or image editing when supported, using the original character reference plus an approved page image.
- Treat approved pages as visual evidence, not layout templates.
- Preserve character anatomy, facial features, colors, markings, accessories, material language, and rendering treatment.
- If a requested page conflicts with an approved continuity anchor, flag the conflict before generating it.
- If a result drifts, regenerate the current page with stronger continuity constraints; do not compensate by changing later pages.

When a page introduces a new functional context, adapt the composition while keeping the visual system coherent. Do not force irrelevant reference elements into a page merely for consistency.

### 7. Deliver and report

After each page, show only that page's final design image and a short review prompt. After the queue is complete, deliver the final images clearly labeled by page.

Keep accompanying text minimal:

- List the generated page names
- Mention the approved visual direction
- Note unresolved MVP ambiguity or image-generation limitations
- State whether any page required regeneration for continuity or fidelity

Do not deliver HTML, code, a design-system package, component slices, or unused intermediate assets.

## Quality Checks

Before reporting completion, verify:

- The entire MVP project was audited before generation.
- The image-generation queue was presented and confirmed when needed.
- Pages were generated in queue order, one at a time.
- Each page was reviewed and explicitly approved before the next page began.
- Every MVP-required page and functional module is represented.
- No MVP module was omitted, deleted, merged, or replaced by an invented module.
- The visual language is traceable to the references but is not a mechanical layout copy.
- Recurring characters, especially mascots, preserve their identity and signature details across pages.
- Recurring motifs, materials, and accents remain consistent where relevant.
- Text, controls, cards, navigation, and key states are visually legible.
- The output consists of final app design images rather than an implementation artifact.
