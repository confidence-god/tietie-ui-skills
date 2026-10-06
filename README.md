# Tietie UI Skills

[中文](#中文说明) | [English](#english-guide)

Five independent AI skills for visual theme, page design, asset generation,
front-end reconstruction and GSAP core motion. The stages are not an automatic
pipeline. The repository is ready to upload to GitHub; it is **not yet a
published GitHub URL**.

## 中文说明

### 技能与产物

| 阶段 | 技能 | 所需输入 | 交付与确认 |
| --- | --- | --- | --- |
| 1 主题 | [`ui-theme`](skills/ui-theme/SKILL.md) | 产品用途、用户、审美偏好、可选参考图 | 一张真实生图主题板；用户批准后交付 `theme-brief.md`、`theme-prompt.md` |
| 2 页面 | [`ui-design`](skills/ui-design/SKILL.md) | 完整 MVP、页面清单、获批主题和参考图 | 页面队列；逐页生成 PNG/JPEG，逐页等待用户批准 |
| 3 素材 | [`ui-assets`](skills/ui-assets/SKILL.md) | 获批页面图、可用的生图能力 | 盘点、批次记录、原生透明 PNG 素材库 |
| 4 复刻 | [`ui-build`](skills/ui-build/SKILL.md) | 技术栈、设计图、本地素材库 | 待批准设计板、页面代码、一次截图对照报告 |
| 5 动效 | [`ui-motion`](skills/ui-motion/SKILL.md) | 已实现页面、触发条件和状态 | GSAP 核心补间及响应式/减少动态效果处理 |

`ui-plan` **不在仓库中**。`ui-motion` 是 GSAP 核心 API 参考，**不是**
完整的动效策划/生产流程；复杂时间线、滚动触发与框架专用集成需要额外工具或指导。

### 目录结构

```text
tietie-ui-skills/
  README.md
  .gitignore
  THIRD_PARTY_LICENSES/
    README.md
    greensock-gsap-skills-LICENSE
  skills/
    ui-theme/
      SKILL.md
      agents/openai.yaml
      references/
    ui-design/
      SKILL.md
      agents/openai.yaml
    ui-assets/
      SKILL.md
      agents/openai.yaml
      scripts/create_asset_library.py
    ui-build/
      SKILL.md
      agents/openai.yaml
      references/output-contract.md
    ui-motion/
      SKILL.md
      agents/openai.yaml
```

一个 `skills/<名称>/` 目录是一个独立技能；必须保留整个目录和相对路径，
不能仅复制 `SKILL.md`。根目录 README 和第三方声明不是技能。

### 手动导入

1. 上传本目录到自己的 GitHub 仓库后，使用 **Code → Download ZIP**
   并解压，或 `git clone <你的仓库 URL>`。发布前这个 URL 只是占位符。
2. 找到解压目录下的 `skills/`，确认五个子目录均包含 `SKILL.md`。
3. 将所需的**整个技能子目录**复制到 AI 客户端指定的技能发现路径。
   Codex 的个人技能位置可用 `~/.agents/skills/`；如你的环境使用
   `~/.codex/skills/`，请以实际配置为准。项目共享可使用仓库内
   `.agents/skills/`。不要嵌套成
   `~/.agents/skills/tietie-ui-skills/skills/ui-theme/`。
4. 已有同名技能时，先检查本地改动，不要直接覆盖。刷新或重启客户端，
   输入 `$ui-theme` 等名称测试是否识别。
5. 其他 AI 客户端若支持类似技能目录，放到其指定位置；若不支持自动发现，
   明确提供所需 `SKILL.md` 的文件路径，要求它一并读取文件里的相对引用。
   `agents/openai.yaml` 是 Codex 的展示配置，其他产品可能忽略它。
   **从 GitHub 下载不等于自动安装到所有 AI 产品。**

在解压目录根路径运行以下 **Windows PowerShell** 示例（遇到重名即停止）：

```powershell
$dest = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
foreach ($name in "ui-theme","ui-design","ui-assets","ui-build","ui-motion") {
    $target = Join-Path $dest $name
    if (Test-Path -LiteralPath $target) { throw "Already exists: $target" }
    Copy-Item -LiteralPath (Join-Path (Get-Location) "skills\$name") -Destination $target -Recurse
}
```

在解压目录根路径运行以下 **macOS / Linux** 示例：

```bash
mkdir -p ~/.agents/skills
for name in ui-theme ui-design ui-assets ui-build ui-motion; do
  test ! -e "$HOME/.agents/skills/$name" || { echo "Already exists: $name" >&2; exit 1; }
  cp -R "skills/$name" "$HOME/.agents/skills/$name"
done
```

### 完整使用流程

1. **准备材料。** 整理产品目标、用户、完整 MVP、页面/导航清单、
   可选参考图、可用图像生成渠道及可写的项目目录。输出写入项目，
   不要写进已安装的技能目录。
2. **主题：`$ui-theme`。** 示例：「使用 `$ui-theme`，先了解这个产品的
   用户与氛围，再生一张主题板供我确认。」实际看图、修订、明确批准
   特定版本后，带着设计板、`theme-brief.md`、`theme-prompt.md` 进入
   下一阶段。文字偏好或尚未获批的图，不等于锁定主题。
3. **页面：`$ui-design`。** 示例：「使用 `$ui-design`，先审核完整
   MVP，列出页面队列；每次只生一页，待我批准后继续。」逐页检查
   功能模块、文字与跨页视觉一致性。主题板上的界面小样只是风格证据，
   不应成为页面模板。
4. **素材：`$ui-assets`。** 示例：「使用 `$ui-assets` 盘点获批
   设计图；仅为前端难以复现的对象制作透明 PNG。」CSS/SVG 可复现项
   交给前端；需真实生图、每批 **2–5 个**资产及原生透明 Alpha。
   可在项目目录运行下面的命令建立素材库骨架；这只创建目录和清单，
   **不会**生成图像。

   ```bash
   python <安装目录>/ui-assets/scripts/create_asset_library.py --root outputs --topic my-project
   ```
5. **复刻：`$ui-build`。** 示例：「使用 `$ui-build`，技术栈 React，
   参考获批首页图，素材在 `<素材库绝对路径>`；先展示设计板，等我
   批准后再实现。」它先产出预览并等待批准，然后实现并做一次截图对比。
   注意 `ui-assets` 将 PNG 放在 `04_final_assets/`，而 `ui-build`
   描述了按类型整理的素材目录；需明确提供真实路径和素材清单，或先在
   项目中进行映射/归类，**不能假定目录天然兼容**。
6. **动效：`$ui-motion`。** 示例：「使用 `$ui-motion` 给这个页面
   加卡片入场与按钮反馈，用 GSAP 核心补间；适配移动端与
   `prefers-reduced-motion`，卸载时清理动画。」提前说明触发条件、
   起止状态和静态兜底。复杂动画需额外方案，不应假定本技能全包。

### 环境要求、故障排查与发布前检查

- 主题、页面与 PNG 素材需要**真正可用**的生图/编辑能力。本仓库
  不含模型、API 密钥、参考图、字体或生成结果。`ui-design` 所提
  `scripts/image_gen.py` 是可选外部回退脚本，**本仓库不提供**。
  工具缺失时只能先做文字规划，不得假称已生成图片。
- 素材库骨架脚本只需 Python 3 标准库。页面复刻还需项目运行环境及
  浏览器截图能力。动效需在目标前端项目安装 GSAP，并单独核对软件许可。
- 无法调用 `$名称` 时，检查是否复制了完整子目录、技能扫描位置、
  是否需要刷新索引，或直接把 `SKILL.md` 路径提供给 AI。
- 发布前请为四项 Tietie 原创技能选择并加入项目级 `LICENSE`；
  当前**未授予统一的开源许可**。`ui-motion` 的上游 MIT 许可与
  GreenSock 版权声明在 [第三方声明](THIRD_PARTY_LICENSES/README.md)
  中。展示名里的 `(tietie)` 不是版权或许可声明。

## English Guide

### Skills and deliverables

| Stage | Skill | Required input | Deliverable and approval |
| --- | --- | --- | --- |
| 1 Theme | [`ui-theme`](skills/ui-theme/SKILL.md) | Product, audience, visual preferences, optional references | Generated board, then approved `theme-brief.md` and `theme-prompt.md` |
| 2 Pages | [`ui-design`](skills/ui-design/SKILL.md) | Complete MVP, page list, approved theme | One reviewed PNG/JPEG page design at a time |
| 3 Assets | [`ui-assets`](skills/ui-assets/SKILL.md) | Approved pages and working image generation | Inventory, batch records, transparent PNG library |
| 4 Build | [`ui-build`](skills/ui-build/SKILL.md) | Stack, canonical image, local assets | Approval board, code, one screenshot report |
| 5 Motion | [`ui-motion`](skills/ui-motion/SKILL.md) | Implemented UI and triggers/states | GSAP core animation and reduced-motion handling |

`ui-plan` is intentionally excluded. `ui-motion` covers **GSAP core API**;
it does not by itself plan and produce a complete advanced motion workflow.

### Manual installation

Each `skills/<name>/` folder is independently installable. Keep `SKILL.md`,
`agents/`, `references/`, and `scripts/` together.

1. Download the GitHub repository ZIP via **Code → Download ZIP** and extract
   it, or clone the repository.
2. Copy the five child folders from `skills/` into your client's skill
   discovery folder. For Codex, use `~/.agents/skills/` for personal skills;
   some environments use `~/.codex/skills/`. Repository-scoped installation
   may use `.agents/skills/`. Confirm the path in your own client.
3. Do not add an extra repository nesting level. Check for existing
   same-named skills before copying. Refresh/restart skill discovery and
   invoke `$ui-theme`, `$ui-design`, `$ui-assets`, `$ui-build`, or `$ui-motion`.

The PowerShell and macOS/Linux examples above copy without overwriting
existing skills. Other AI products have their own import conventions. If
automatic discovery is unavailable, point the AI at the desired `SKILL.md`
and have it follow relative references. `agents/openai.yaml` may be ignored
outside Codex. Downloading alone does not install a skill into every client.

### End-to-end use

1. **Prepare.** Gather the product goal, audience, full MVP, page/navigation
   inventory, reference images, available image-generation route and writable
   project directory. Never save project output inside an installed skill.
2. **Theme (`$ui-theme`).** Ask it to interview you and generate one visual
   theme board. Review and explicitly approve a specific image version before
   handing off the board, `theme-brief.md` and `theme-prompt.md`.
3. **Pages (`$ui-design`).** Supply the full MVP and approved theme. Review
   its page queue, then generate and approve each page one at a time. Check
   all required functionality and visual/character continuity.
4. **Assets (`$ui-assets`).** Give it approved pages. Route simple CSS/SVG
   elements to implementation; generate raster assets in **2–5 item batches**
   with genuine transparent alpha. Python 3's
   `skills/ui-assets/scripts/create_asset_library.py` creates the folder
   scaffold and inventory, not image assets.
5. **Build (`$ui-build`).** Provide the stack, page reference and local asset
   path. Approve the design board before implementation, then inspect the
   single screenshot comparison. `ui-assets` outputs to `04_final_assets/`,
   while `ui-build` illustrates categorized asset folders: provide a mapping
   or organize the files first. This handoff is **not automatic**.
6. **Motion (`$ui-motion`).** Point to implemented components and specify
   triggers, before/after states and static fallback. Use GSAP core tweens
   and responsive/reduced-motion handling; add separate guidance for
   advanced timelines, scrolling or framework integration.

Example requests:

```text
Use $ui-theme to generate a visual theme board for approval.
Use $ui-design with this complete MVP and approved theme; generate only the first page.
Use $ui-assets to build a transparent PNG library from these approved screens.
Use $ui-build with React, this home-page image and my asset-library path; show the approval board first.
Use $ui-motion to add GSAP card entrances with reduced-motion support.
```

### Requirements, troubleshooting and publication

- Theme, design and raster assets need a **real, configured** image-generation
  or editing capability. No model, credentials, source images, fonts or
  generated artifacts are included. `ui-design` mentions an optional
  external `scripts/image_gen.py` fallback; it is **not included**.
- The asset scaffold needs only Python 3 standard library. Front-end work
  needs a running project and browser screenshot capability. Motion needs
  GSAP installed and its software license reviewed separately.
- If `$skill-name` is not recognized, inspect the folder depth/discovery
  path, refresh the client or provide the full `SKILL.md` path. Stop at the
  affected stage if approval, input assets or generation access is missing.
- There is **no repository-wide open-source license yet** for the four
  original Tietie skills. Select one before claiming redistribution rights.
  Check the separate [third-party notice](THIRD_PARTY_LICENSES/README.md)
  and upstream obligations for the GSAP-derived skill. `(tietie)` is a
  display label, not a copyright claim.
