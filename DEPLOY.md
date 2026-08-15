# Kent Tools — Deploy to GitHub Pages

## 仓库与部署现状（务必先看）

- 本目录 `Kent Tools/` **就是**站点的 git 仓库，远程为
  `https://github.com/Andrew-Dufresne/kent-tools-website.git`，分支 `main`。
- GitHub Pages 已配置为 **Deploy from a branch → main → /(root)**，推送后自动构建上线。
- 根目录的 `CNAME` 已绑定自定义域名 **`kent-tools.com`**，线上地址即 https://kent-tools.com （无需再配 DNS）。
- ⚠️ **不要再去推 `power-tools-site/`**：那是另一份 2026-06 的谷歌翻译旧副本，与线上站点无关。真正的部署源只有本目录 `Kent Tools/`。

## 日常部署流程（仓库已初始化，无需 git init）

```bash
cd "Kent Tools"
python _build.py     # 用 _translations.json 重新生成 15 语 × 4 页（60 个 HTML）
python _verify.py    # 审计：0 结构问题 / 0 漏译 才算通过
git add -A
git commit -m "描述本次改动"
git push origin main # 触发 GitHub Pages 自动部署，约 1–3 分钟上线
```

## 翻译工作文件（已被 .gitignore 排除，请勿手动 add）

以下为翻译流程的中间产物，**不会进入仓库**：
`_batch_*.json`、`_merge_*.py`、`_fix_original.py`、`_proofread_*.py`、
`_keys_dump.txt`、`_keys_readable.txt`、`_ordered_keys.json`、`_proof_sample.txt`。

源文件（需提交）：`_build.py`、`_translations.json`、`_verify.py`。

## 新增 / 修改语言

1. 编辑 `_translations.json`（每个键需含 `en` + 14 个非英语译文，缺一不可）。
2. 在 `_build.py` 的 `NON_EN` / `LANG_NAMES` / `ARIA_LABELS` 登记新语言；RTL 语言（如 ar、fa）须加入 `RTL` 集合。
3. 同步更新 `_verify.py` 的 `NON_EN`、下拉选项期望值、RTL 检查、借词白名单。
4. 跑 `_build.py` → `_verify.py` → 提交推送。

> 语言下拉顺序：English 默认置顶，其余按**英文名称首字母**排列（非 ISO 代码）。马来语显示名为 `Melayu`。

## Site Structure（实际）

```
Kent Tools/
├── index.html          # 英文首页（hero / 分类 / 精选产品）
├── products.html       # 9 款钢筋工具，含完整参数表
├── about.html          # 公司故事 / 价值观 / 认证
├── contact.html        # 询盘表单 + WhatsApp + FAQ
├── ar/ de/ es/ fr/ ja/ pt/ ru/   # 原有 7 语子目录（各 4 页）
├── ko/ th/ ms/ tr/                # 韩语 / 泰语 / 马来语 / 土耳其语
├── fa/ hi/ vi/                    # 波斯语(RTL) / 印地语 / 越南语
├── css/style.css       # 工业蓝+橙主题样式
├── js/main.js          # 导航 / 表单 / 动画
├── images/             # 产品图（来自 aytotech.com）
├── CNAME               # 自定义域名 kent-tools.com
├── _build.py           # 构建脚本（英文模板 + 字典 → 各语言静态页）
├── _translations.json  # 翻译字典（355 键 × 15 语）
├── _verify.py          # 构建后审计脚本
└── DEPLOY.md           # 本文件
```

## Product Catalog (9 Items)

| # | Product | Models |
|---|---------|--------|
| 1 | Rebar Tying Tool | RT460, RT660 |
| 2 | Rebar Tying Machine | RT528, RT545, RT558 |
| 3 | Rebar Bender | C16-C36 |
| 4 | Brushless Rebar Bender | WSC16-WSC28 |
| 5 | Rebar Cutter | S18, C20 |
| 6 | Rebar Flush Cutter | F20, F30 |
| 7 | Hydraulic Rebar Cutter | A16-A32 |
| 8 | Rebar Sleeve Threading Machine | — |
| 9 | 0.8mm Tie Wire Roll | — |

## Customizing

### Contact Info (already set)
- Email: kent@gezhi.group
- WhatsApp: +995 593 583 830

### Activate the Contact Form
1. Sign up at https://formspree.io (free plan)
2. Create a new form
3. In `js/main.js`, replace `your-form-id` with your Formspree ID

### Factory Image
Replace the SVG placeholder in `about.html` (`.about-image-placeholder`) with a real factory photo.
