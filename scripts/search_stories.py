import urllib.request
import urllib.parse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

TEMPLATES = {
    "pawn_gold": [
        '"银包金" 剪开 故事',
        '变卖 前女友 剪开 金',
        '收金 典当 真实 故事',
        '旧金饰 剪开 秘密'
    ],
    "reddit_confession": [
        'site:reddit.com/r/TrueOffMyChest "never told anyone" "secret"',
        'site:reddit.com/r/TrueOffMyChest "years later" "realized" "regret"',
        'site:reddit.com/r/AskReddit "secret you will never tell"'
    ],
    "thrift_secrets": [
        'site:reddit.com "thrift store" "found inside" "letter" OR "note"',
        'thrift store found hidden money letter viral story',
        '旧货店 遗物 夹层 秘密 发现'
    ],
    "delayed_love": [
        '分手多年 整理遗物 发现 秘密',
        '前任留下的 抽屉 发现 哭了',
        'viral story engagement ring shamed'
    ]
}

def search_google(query, max_results=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    encoded = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded}&hl=zh-CN"
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            clean = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL)
            text = re.sub(r'<[^>]+>', '\n', clean)
            lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 15]
            return lines[:max_results * 4]
    except Exception as e:
        return [f"Error fetching {query}: {e}"]

def main():
    category = sys.argv[1] if len(sys.argv) > 1 else "pawn_gold"
    if category not in TEMPLATES and category != "all":
        print(f"Usage: python search_stories.py [{'/'.join(TEMPLATES.keys())}|all]")
        return

    queries = []
    if category == "all":
        for q_list in TEMPLATES.values():
            queries.extend(q_list)
    else:
        queries = TEMPLATES[category]

    print(f"[*] Starting story harvest for category: {category} ({len(queries)} queries)")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = Path(__file__).resolve().parent.parent / "stories" / "raw"
    out_file = out_dir / f"harvest_{category}_{timestamp}.md"

    content = [f"# 故事素材采集简报 - {category}", f"- 采集时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ""]

    for q in queries:
        print(f" -> Querying: {q}")
        snippets = search_google(q)
        content.append(f"## 检索词: {q}")
        for s in snippets[:8]:
            content.append(f"- {s}")
        content.append("")

    out_file.write_text("\n".join(content), encoding="utf-8")
    print(f"[+] Saved raw story findings to: {out_file}")

if __name__ == "__main__":
    main()
