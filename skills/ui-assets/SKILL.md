---
name: ui-assets
description: Rebuild dense ChatGPT image-generation sheets into consistent libraries of reusable transparent PNG UI stickers, icons, badges, panels, and decorative assets. Exclude assets reproducible with HTML/CSS/SVG, partition raster assets into mandatory 2-5 item generation batches by size and complexity, and require native transparent Alpha output through image2.5 or another supported image-generation capability.
---

# UI Assets

Build a reusable UI sticker asset library from crowded source sheets. The source image is the visual reference, while the final assets are always produced through image generation or image-to-image reconstruction. Preserve the source design language, visual identity, palette, proportions, and level of finish across the complete asset set.

## Hard Requirements

1. **Image generation is mandatory for selected raster assets.** Use the `image2.5` capability when available, or another available skill/tool that can generate or edit images.
2. **Stop when generation is unavailable.** Do not silently fall back to direct crops, manual redraws, text-only instructions, or background-removal-only output. Tell the user that this skill requires image-generation support and cannot complete the asset library in the current environment.
3. **Every selected final raster asset must be generated.** Source crops are references and inputs only. Never accept a direct source crop as a final asset.
4. **Use source-faithful reconstruction.** Generate all assets from their source crops or source-sheet regions. Do not redesign, reinterpret, simplify, or replace the visual language.
5. **Maintain set-level consistency.** Keep the same style summary, palette, lighting, edge treatment, texture, rendering quality, and background strategy across all batches. Reuse a shared prompt foundation and visual reference wherever possible.
6. **Every generated canvas must contain 2-5 selected raster assets.** This is a hard production constraint, not a preference. Partition assets into batches according to size, visual complexity, and separation risk. Never generate a one-asset canvas.
7. **Direct transparent output is mandatory.** Request and verify a valid transparent Alpha channel from the image-generation capability, preferably through `image2.5`. Do not use a pure-color background, background removal, or a cutout pass as a production substitute.
8. **Exclude frontend-reproducible assets from image generation.** Do not generate assets that can be recreated with high fidelity using ordinary HTML/CSS/SVG or other frontend primitives, such as simple geometric icons, flat shapes, borders, lines, basic arrows, plain badges, and simple panels. Keep them in the inventory as `frontend_reproducible` and mark them for implementation rather than generation.
9. **Do not use redraw as a fallback mode.** In this workflow, all selected raster reconstruction is the required production path. The old distinction between enhancement and fallback redraw does not apply.
10. **Do not free-style prompts.** Only add prompt content that comes directly from the source sheet, the shared style brief, or negative constraints needed to preserve fidelity. Do not inject new art direction, decorative ideas, or stylistic inventions.

## Operating Principle

Use this source-reference generation path:

1. Inspect the complete source sheet.
2. Create an inventory and a shared visual-style brief.
3. Crop each valuable source region with generous padding for use as a generation reference.
4. Rebuild every selected raster asset with image generation or image-to-image generation in grouped canvases containing exactly 2-5 assets. Choose the group size from the asset-size and complexity rules below.
5. Use a shared prompt foundation and reference strategy to keep the asset set visually coherent.
6. Require direct transparent output with a valid Alpha channel.
7. If transparency is invalid or missing, reject the batch and regenerate it with an explicit transparent-background requirement.
8. Validate each generated asset and queue failures for another generation pass.

The source crop is never the deliverable. It exists to preserve content, silhouette, composition, and design intent for generation.

## Generation Capability Gate

Before inspecting or processing assets, verify that an image-generation capability is available.

Acceptable capabilities include:

- the `image2.5` capability;
- the `imagegen` skill;
- an image-to-image generation tool;
- another installed skill that can generate or edit raster images while accepting a source reference.

If no such capability is available:

- stop the workflow immediately;
- do not create final assets;
- do not use direct cropping as a substitute;
- tell the user that image generation is required for this skill;
- explain that the current environment lacks a supported generation capability;
- ask the user to enable or provide an image-generation-capable skill/tool before continuing.

## Workflow

### 1. Inspect and inventory

Inspect every attached source image and create an inventory before generation. Identify valuable candidates, classify their implementation path, and rank raster candidates by:

1. visual completeness;
2. clarity;
3. theme fit;
4. style fit;
5. usefulness as a reusable UI asset.

For each candidate, record:

- `asset_id`: stable page-aware id such as `p001_a001` (page 1, asset 1);
- `page_id`: stable page id such as `page_001`;
- `page_number`: one-based page number matching the source image or sheet;
- `source_file`: exact original source filename;
- `source_dimensions`: original width x height in pixels;
- `source_position`: human-readable location such as `top-left`, `row 2 column 3`, or `center-right`;
- `bbox_px`: exact pixel bounding box as `x,y,width,height`;
- `bbox_norm`: normalized bounding box as `x,y,width,height` in the 0-1 range;
- `row`: visual row number, starting at 1;
- `column`: visual column number, starting at 1;
- `reading_order`: stable top-to-bottom, left-to-right order;
- `location_label`: concise nearby-anchor label to disambiguate similar assets;
- `crop_path`: exact path to the padded source reference crop;
- `name`: concise descriptive name;
- `type`: `icon`, `sticker`, `badge`, `panel`, `decoration`, `texture`, `ui_component`, or `uncertain`;
- `visual_complete`: high / medium / low;
- `clarity`: high / medium / low;
- `relative_size`: large / medium / small / tiny;
- `cutout_risk`: low / medium / high;
- `theme_fit`: high / medium / low;
- `style_fit`: high / medium / low;
- `implementation_path`: `generate_raster` / `frontend_reproducible` / `uncertain`;
- `text_handling`: normally `remove text`; use `preserve text` only when explicitly requested;
- `generation_group`: batch identifier;
- `decision`: normally `generate`, `frontend_implement`, `uncertain`, or `skip`.

Do not blindly generate every detected object. First exclude assets that frontend code can reproduce accurately. Select valuable raster assets for generation, and ensure every selected raster asset belongs to a 2-5 asset batch.

Use the same page-aware `asset_id` in the inventory, page map, crop folder, generation prompt, generated output notes, final filename, and rework queue. A later agent must be able to locate an asset from any one of these records without relying on visual guesswork.

### Frontend Reproducibility Gate

Before assigning an asset to a generation batch, ask whether a frontend developer can reproduce it with high visual fidelity using HTML/CSS/SVG, icon primitives, borders, gradients, pseudo-elements, or simple layout. If yes, do not generate it. Record it as `frontend_reproducible` and route it to frontend implementation.

Normally exclude:

- simple geometric icons, arrows, chevrons, dots, circles, stars, and line marks;
- flat-color shapes, borders, separators, underlines, corner brackets, and basic frames;
- plain pills, tags, badges, buttons, cards, panels, and simple progress or status indicators;
- simple gradients, shadows, glows, or repeated patterns that CSS/SVG can reproduce without raster texture;
- readable text labels that should remain live HTML text.

Keep an asset in the raster-generation path when fidelity depends on source-specific texture, painterly or organic contours, hand-rendered highlights, complex material response, irregular particles, expressive characters, detailed illustrations, or other visual information that CSS/SVG would reproduce poorly.

When uncertain, preserve the source crop and mark the candidate `uncertain`; do not silently generate it until the implementation path is decided.

### 2. Define the shared visual system

Before the first generation pass, write a shared style brief that is reused for every batch. Include:

- silhouette and proportion language;
- palette, gradients, contrast, and accent colors;
- line weight and edge treatment;
- shadows, highlights, glows, reflections, and material texture;
- UI iconography and component language;
- visual density and level of detail;
- treatment of readable text;
- transparent-background requirements;
- any recurring character, object, or motif details.

The shared brief is the source of truth for consistency. Batch-specific prompts may identify the assets, but should not introduce a conflicting art direction.

### 3. Create source references

Split every selected asset from the source sheet with generous padding. Preserve the complete silhouette, including:

- shadows;
- glows;
- outlines;
- rounded edges;
- semi-transparent effects;
- reflections;
- nearby context needed to understand the design.

Save these crops as generation references in `02_references/page_<page_number>/<asset_id>/crop.png`. They are not final assets and must not be copied directly into `04_final_assets/`.

### 4. Generate every selected asset

Use image-to-image generation when a source crop is available. Use the full source sheet as an additional reference when it helps preserve the shared visual system.

The default generation request must:

- use the source crop as the exact content reference;
- preserve silhouette, proportions, composition, palette, texture, shadows, glows, and UI styling;
- improve resolution, sharpness, and edge definition;
- generate a clean, complete, reusable asset;
- produce a valid transparent Alpha channel directly;
- keep the generated result tightly tied to the source crop and sibling assets;
- remove or convert readable text into non-text symbols unless preservation is explicitly requested;
- avoid extra labels, captions, watermarks, mockup screens, repeated icons, or unrelated decoration.

When expanding the prompt, only add details that are directly observable from the source or needed to preserve fidelity. Do not invent new aesthetic descriptors, mood words, era labels, or redesign instructions.

Do not accept a generated result merely because it looks attractive. Reject it when it changes the source identity, silhouette, proportions, palette, or style.

Suggested shared prompt foundation:

```text
Use the attached source image and source crop as the exact content, design, and style reference.
Reconstruct each selected UI asset as a clean, sharp, reusable production asset.
Preserve the original silhouette, proportions, composition, palette, gradients, texture, shadows,
highlights, glows, reflections, edge treatment, icon language, and overall rendering style.
Keep this asset visually consistent with the other assets generated from the same source sheet.
Only improve resolution, clarity, and edge definition. Do not redesign, reinterpret, simplify,
modernize, or change the art direction.
Remove or convert readable text into non-text symbols, simple marks, decorative lines, or abstract
UI glyphs unless text preservation is explicitly requested.
Generate a complete, uncropped asset with a transparent background and valid Alpha channel.
No extra labels, captions, typography, watermarks, mockup screens, repeated tiny icons, clutter,
merged assets, tight cropping, partial bodies, or cut-off silhouettes.
```

### 5. Partition assets into mandatory 2-5 asset batches

Partition selected raster assets before generation. Every generation canvas must contain at least 2 and at most 5 assets:

- 5 assets: very small, simple raster decorations with low separation risk;
- 4 assets: small simple-to-medium stickers with clear silhouettes;
- 3 assets: medium-detail stickers with distinct silhouettes and moderate spacing needs;
- 2 assets: large, complex, character-like, glow-heavy, or high-risk stickers.

Use the largest batch allowed by the source material, but let the largest or most complex asset determine the batch size. Pair a complex asset with one compatible asset from the same visual system; do not place it in a one-asset batch. Keep assets separated with sufficient transparent space and avoid mixing incompatible silhouettes or visual scales.

If a grouped result causes blur, overlap, inconsistent rendering, or weaker source fidelity, regenerate the affected assets in a smaller valid 2-5 asset batch. Never reduce the batch to one asset. If only one eligible raster asset remains, pause that generation, re-evaluate the inventory for another compatible raster asset, and record the unresolved grouping issue instead of violating the minimum.

### 6. Enforce direct transparent backgrounds

Request a valid transparent Alpha channel in every generation prompt. When the generation result contains valid transparency:

- preserve the alpha channel;
- inspect the edge for halos, missing pixels, and unwanted opaque regions;
- save the result directly after quality validation.

If the output has a visible solid background, grid, box, matte, or invalid Alpha channel, reject it. Regenerate the complete 2-5 asset batch with an explicit direct-transparency instruction. Do not use `scripts/remove_flat_background.py`, chroma-key extraction, border-connected removal, or any other post-generation cutout as a substitute for native transparency.

### 7. Validate and queue rework

Accept a generated asset only when:

- it is visually complete and not cropped;
- the silhouette and proportions remain faithful to the source;
- it has enough resolution for reuse;
- edges, shadows, glows, and transparency are clean;
- the asset is sharp at intended size;
- the palette and rendering style match the source sheet and sibling assets;
- unwanted readable text has been removed or converted unless preservation was requested;
- transparency has not erased real asset pixels;
- it does not contain unrelated generated elements.

When a result fails, record the reason and regenerate. Use the following rework labels:

- `generation_unavailable`: stop and inform the user;
- `generation_blurry`: regenerate with a smaller valid 2-5 asset group and stronger clarity requirements;
- `generation_cut_subject`: regenerate with a larger composition area and complete-silhouette constraints;
- `generation_style_drift`: reuse the shared style brief and source references, and reduce batch size;
- `generation_inconsistent`: regenerate the affected asset with sibling outputs as consistency references;
- `transparent_output_invalid`: reject the batch and regenerate with explicit direct-Alpha requirements;
- `canvas_too_crowded`: reduce the group size;
- `text_not_handled`: regenerate with explicit text-conversion constraints.
- `frontend_reproducible`: remove from the generation queue and route to CSS/SVG/HTML implementation;
- `batch_below_minimum`: regroup with another compatible raster asset before generation.

Never convert a failed generated asset into a direct crop just to fill the library.

## Asset Library Setup

Create the library with `scripts/create_asset_library.py` when starting a project:

```bash
python scripts/create_asset_library.py --root outputs --topic <short-topic>
```

Use this structure:

```text
asset-library-YYYYMMDD-topic/
  00_source/
  01_inventory/
    asset_inventory.md
    page_map.md
    batch_plan.md
    style_brief.md
  02_references/
    page_001/
      p001_a001/
        crop.png
        notes.md
  02_generated_batches/
    batch_01/
      prompt.md
      generated.png
      notes.md
  04_final_assets/
    p001_a001__asset-name.png
  05_rework_queue/
    rework_queue.md
```

Keep source images and source-image notes in `00_source/`. Save the complete page map and inventory in `01_inventory/`. Save padded source references under `02_references/page_<page_number>/<asset_id>/`. Save grouped generated canvases in `02_generated_batches/`. Save final transparent PNGs directly in `04_final_assets/` using `<asset_id>__<slug>.png`. Keep frontend-reproducible candidates in the inventory, but do not place them in the raster generation folders.

Every generated canvas in `02_generated_batches/` must contain 2-5 raster assets. Do not create a single-asset generation canvas.

## Prompt And Record Requirements

For every generation request, save:

- the source asset IDs;
- the page-aware asset IDs and page/position references;
- the source filename and source dimensions;
- the pixel and normalized bounding boxes;
- the row, column, reading order, and location label;
- the exact crop path;
- the shared style brief or a reference to it;
- the batch size;
- the complete prompt;
- the direct-transparency strategy and Alpha validation result;
- the generation result and quality notes;
- any rework reason.

For grouped generation canvases, write `prompt.md` before generation:

```text
Use the attached source sheet and source crops as the content, style, and theme references.
Reconstruct these <2-5> valuable raster UI assets as clean, sharp, reusable assets: <asset list>.
Apply this shared visual system consistently: <style brief summary>.
Preserve each source asset's silhouette, proportions, palette, composition, texture, shadows,
highlights, glows, and UI design language.
Generate each asset separately with wide spacing and no overlap.
Generate the entire canvas with a valid transparent Alpha channel directly. Do not use a solid
background, matte, grid, box, chroma key, or post-generation background removal.
Remove or convert readable text into non-text symbols unless text preservation is explicitly requested.
No extra labels, captions, typography, watermarks, mockup screens, merged assets, clutter, tight
cropping, partial bodies, or cut-off silhouettes.
```

## Output Rules

Save:

- original images and notes in `00_source/`;
- inventory, batch planning, and the shared visual brief in `01_inventory/`;
- page-aware source reference crops in `02_references/page_<page_number>/<asset_id>/`;
- all grouped generated canvases in `02_generated_batches/`;
- final transparent assets in `04_final_assets/` using page-aware filenames;
- low-confidence or damaged generated assets in `04_final_assets/` with an `uncertain__` filename prefix;
- failure notes and next actions in `05_rework_queue/rework_queue.md`.

Do not save direct source crops as final assets. Do not report success when image generation was unavailable. Do not silently omit an asset that was selected for generation; mark it as generated, uncertain, or queued for rework. Do not identify assets only by type folders or display names; use the page-aware ID and recorded coordinates.
