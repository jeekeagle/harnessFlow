#!/usr/bin/env python3
"""
HarnessFlow Website Generator
将项目信息注入模板，自动生成并推送网站到 GitHub Pages

用法：
    python generate_site.py --project "我的课程项目" --title "AI时代教师能力提升" \
        --tagline "从信息化到智能化的教师转型之路" --phase "3.x 阶段" \
        --repo jeekeagle/my-course --deploy-url https://jeekeagle.github.io/my-course/

前置依赖：
    pip install requests
"""
import argparse
import urllib.request
import json
import base64
import os
import sys

TOKEN = os.environ.get("GITHUB_TOKEN", "")
OWNER = "jeekeagle"
REPO = "harnessFlow"

TEMPLATE_PATH = "websites/index.template.html"


def get_sha(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())["sha"]
    except:
        return None


def upsert(path, content, message):
    sha = get_sha(path)
    data = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "branch": "main"
    }
    if sha:
        data["sha"] = sha
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}",
        data=json.dumps(data).encode("utf-8"),
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read())


def generate_index(tpl, args):
    return (tpl
        .replace("{{PROJECT_NAME}}", args.project)
        .replace("{{TITLE}}", args.title)
        .replace("{{TAGLINE}}", args.tagline)
        .replace("{{PHASE}}", args.phase)
        .replace("{{DATE}}", args.date)
        .replace("{{DESCRIPTION}}", args.description or args.title)
        .replace("{{DEPLOY_URL}}", args.deploy_url or "")
        .replace("{{PANEL_PATH}}", args.panel_path or "workflow/workflow-panel.html")
        .replace("{{FLOW_PATH}}", args.flow_path or "workflow/Harness-WorkFlow.html")
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HarnessFlow 网站生成器")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--title", required=True, help="页面主标题")
    parser.add_argument("--tagline", required=True, help="项目标语")
    parser.add_argument("--phase", default="1.x 阶段", help="当前驾驭阶段")
    parser.add_argument("--description", default="", help="项目描述")
    parser.add_argument("--date", default="", help="创建日期")
    parser.add_argument("--deploy-url", default="", help="部署地址")
    parser.add_argument("--panel-path", default="workflow/workflow-panel.html", help="面板页路径")
    parser.add_argument("--flow-path", default="workflow/Harness-WorkFlow.html", help="SOP图路径")
    args = parser.parse_args()

    if not args.date:
        from datetime import date
        args.date = date.today().isoformat()

    if not TOKEN:
        print("Error: Set GITHUB_TOKEN environment variable", file=sys.stderr)
        sys.exit(1)

    # Read template
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r") as f:
            tpl = f.read()
    else:
        # Fetch from GitHub if local not found
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{TEMPLATE_PATH}"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
        with urllib.request.urlopen(req, timeout=10) as r:
            tpl = base64.b64decode(json.loads(r.read())["content"]).decode("utf-8")

    html = generate_index(tpl, args)
    result = upsert("index.html", html, f"Auto-generate site for project: {args.project}")
    print(f"Done: {result.get('content', {}).get('path', 'index.html')} generated")
