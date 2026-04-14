# HarnessFlow

**驾驭工程** — 人机协同内容生成的标准化工作流 SOP。

通过将人类意图（心力）与 AI 运算（算力）严格分离与协同，实现从需求到多模态交付物的完全工程化流程。

---

## 目录结构

```
HarnessFlow/
├── workflow/
│   ├── Harness-WorkFlow.html   # SOP 全景图（静态）
│   ├── workflow-panel.html     # 交互式流程面板（Chart.js Dashboard）
│   └── Harness-WorkFlow.md     # 工作流说明文档
├── websites/                   # 网站自动生成工具
│   ├── index.template.html     # 项目首页模板
│   └── generate_site.py        # 一键生成并推送网站的脚本
└── README.md
```

---

## 快速开始

### 方式一：从头创建新项目

**第一步：复制本仓库为新项目**

在 GitHub 上点击 **Use this template**，创建新的仓库（如 `my-course-project`）。

**第二步：配置项目信息**

编辑 `websites/generate_site.py`，更新顶部的配置：

```python
OWNER = "your-github-username"
REPO = "my-course-project"
```

**第三步：一键生成并推送网站**

```bash
export GITHUB_TOKEN=ghp_your_token_here

python websites/generate_site.py \
    --project "AI教学实战工作坊" \
    --title "AI时代教师能力提升计划" \
    --tagline "从信息化到智能化的教师转型之路" \
    --phase "2.x 阶段" \
    --description "通过驾驭工程方法论，实现教学内容的工业化生产" \
    --deploy-url "https://yourname.github.io/my-course-project/"
```

**第四步：访问部署的网站**

GitHub Actions 会自动构建并部署到 GitHub Pages，约 1-2 分钟后生效。

---

### 方式二：修改现有模板

直接编辑 `workflow/` 下的文件（`Harness-WorkFlow.html`、`workflow-panel.html`），
然后推送即可自动触发 GitHub Pages 更新。

---

## 工作流核心概念

| 阶段 | 名称 | 人类心力 | Agent 算力 | 核心产出 |
|------|------|---------|-----------|---------|
| 1.x  | 意图定调 | 95% | 5% | 1.1-Requirement, 1.2-Ideation |
| 2.x  | 框架分析 + 专项研究 | 15-20% | 80-85% | 2.1-framework, 2.2-brainstorm-fold |
| 3.x  | 收敛叙事 | 75% | 25% | 3.2-script-final |
| 3.x  | 自动化交付 | 10% | 90% | PPT / Website / Cards |

---

## 网站部署说明

本仓库的 **GitHub Pages** 已启用，访问：

```
https://jeekeagle.github.io/harnessFlow/
```

每次推送到 `main` 分支都会自动触发重新部署。

如需为新项目启用 Pages：在仓库 Settings → Pages → Source 选择 `main` 分支即可。

---

## Workflow 文件说明

### workflow-panel.html（推荐）

交互式 Dashboard，包含：
- 左侧步骤导航（5 步流程）
- 右侧动态详情面板（人类/Agent 动作、Skill 调用、数据流转）
- Chart.js 人力 vs 算力投入比堆叠柱状图

### Harness-WorkFlow.html

纯静态 SOP 全景图，适合截图分享和文档引用。
