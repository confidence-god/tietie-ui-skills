#!/usr/bin/env python3
"""Create a source-faithful, generation-first UI sticker asset library scaffold."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import re


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "ui-stickers"


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a source-faithful, generation-first UI sticker asset library scaffold."
    )
    parser.add_argument("--root", default="outputs", help="Root directory for libraries.")
    parser.add_argument("--topic", default="ui-stickers", help="Short project topic/name.")
    parser.add_argument("--date", default=datetime.now().strftime("%Y%m%d"), help="Date prefix, default today.")
    args = parser.parse_args()

    library = Path(args.root) / f"asset-library-{args.date}-{slugify(args.topic)}"
    directories = [
        "00_source",
        "01_inventory",
        "02_references/page_001/p001_a001",
        "02_generated_batches/batch_01",
        "04_final_assets",
        "05_rework_queue",
    ]
    for directory in directories:
        (library / directory).mkdir(parents=True, exist_ok=True)

    write_if_missing(
        library / "01_inventory" / "asset_inventory.md",
        "# Asset Inventory\n\n"
        "| asset_id | name | page_id | page_number | source_file | source_position | bbox_px | bbox_norm | row | column | reading_order | crop_path | type | visual_complete | clarity | relative_size | cutout_risk | theme_fit | style_fit | implementation_path | text_handling | generation_group | decision | notes |\n"
        "|---|---|---|---:|---|---|---|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
    )
    write_if_missing(
        library / "01_inventory" / "page_map.md",
        "# Page And Position Map\n\n"
        "Create one row for every detected candidate. Use stable page-aware IDs such as "
        "`p001_a001`. Record the original source filename, page number, pixel bounding box "
        "`x,y,width,height`, normalized bounding box `x,y,width,height` in the 0-1 range, "
        "row/column, reading order, and the exact crop path. Never identify an asset only by name.\n\n"
        "| asset_id | page_id | page_number | source_file | source_dimensions | bbox_px | bbox_norm | row | column | reading_order | location_label | crop_path |\n"
        "|---|---|---:|---|---|---|---|---:|---:|---:|---|---|\n",
    )
    write_if_missing(
        library / "01_inventory" / "batch_plan.md",
        "# Generation Batch Plan\n\n"
        "## Rules\n\n"
        "- Crop every valuable asset first with generous padding.\n"
        "- Image generation is mandatory for every selected final asset.\n"
        "- Use image2.5 or another available image-generation-capable skill/tool by default.\n"
        "- Never use direct source crops as final assets.\n"
        "- Exclude assets reproducible with HTML/CSS/SVG and record them as frontend_reproducible.\n"
        "- Native transparent Alpha output is mandatory; reject and regenerate any batch with a visible or invalid background.\n"
        "- Use a shared style brief and source references across all generation batches.\n"
        "- Every generated canvas must contain exactly 2-5 raster assets.\n"
        "- Choose the batch size by asset size, complexity, and separation risk: 5 simple, 4 simple-to-medium, 3 medium-detail, or 2 large/complex.\n"
        "- Never create a one-asset generation canvas; regroup with another compatible raster asset instead.\n\n"
        "## Batches\n\n"
        "| batch | asset ids | page/position references | method | alpha_validation | status | notes |\n"
        "|---|---|---|---|---|---|---|\n",
    )
    write_if_missing(
        library / "01_inventory" / "style_brief.md",
        "# Shared Visual Style Brief\n\n"
        "Record the source sheet's palette, silhouettes, proportions, line treatment, lighting, "
        "texture, UI language, recurring motifs, and negative constraints that prevent style drift. "
        "Reuse this brief for every generation batch.\n",
    )
    write_if_missing(
        library / "02_references" / "page_001" / "p001_a001" / "notes.md",
        "# p001_a001 Reference Notes\n\n"
        "Record page number, source filename, source dimensions, pixel and normalized bounding boxes, "
        "row/column, reading order, and nearby visual anchors.\n",
    )
    write_if_missing(library / "02_generated_batches" / "batch_01" / "prompt.md", "# Batch 01 Prompt\n\n")
    write_if_missing(library / "02_generated_batches" / "batch_01" / "notes.md", "# Batch 01 Notes\n\n")
    write_if_missing(
        library / "05_rework_queue" / "rework_queue.md",
        "# Rework Queue\n\n"
        "| asset id | reason | next action |\n"
        "|---|---|---|\n",
    )

    print(library.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
