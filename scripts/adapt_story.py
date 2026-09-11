import sys
import json
from pathlib import Path
from datetime import datetime

STORY_SAMPLE = {
    "title": "终点线前的幽灵车",
    "carrier_surface": "落满灰尘的二手旧 Xbox 游戏机与 2001 年的拉力赛车光盘",
    "carrier_truth": "亡父十年前创下的全赛道最快单圈纪录（幽灵车），以及儿子跨越生死的克制守护",
    "logline": "男孩在亡父留下的老旧赛车游戏里与父亲的“幽灵车”赛车十年，但在终于要超越父亲的那一刻，他猛踩刹车停在终点线前，只为了不抹掉父亲在世界上留下的最后痕迹。",
    "tone": "克制、深情、男人的沉默与终极温柔",
    "bgm": "低沉平缓的大提琴前奏，中段加入心跳般的鼓点，结尾留白",
    "shots": [
        {"timing": "00:00-00:15", "visual": "车库昏暗光线，特写落满灰尘的初代黑绿色游戏手柄，吹散积灰。", "narration": "有些东西表面上看是一堆电子垃圾，扔进废品回收站都换不来一碗面。但在某个人心里，那是通往另一个世界的唯一电话亭。"},
        {"timing": "00:15-00:45", "visual": "电视机显像管通电的微光，赛道画面启动，半透明的灰色赛车若隐若现。", "narration": "六岁那年，父亲猝然离世。之后整整十年，他都不敢碰那台旧机器。直到十六岁那年通上电，他在老拉力赛里，看到了一条幽灵。那是单圈最快纪录留下的半透明虚影——是他父亲十年前跑出来的。"},
        {"timing": "00:45-01:15", "visual": "快节奏剪辑：少年的手指在按键上磨出老茧，屏幕里两辆车在发卡弯疯狂贴身漂移。", "narration": "接下来的无数个放学黄昏，他都在和父亲的虚影赛跑。他拼命练习换挡、走线、漂移，就好像父亲一直坐在副驾，无声地看着他长成一个大人。"},
        {"timing": "01:15-01:45", "visual": "高潮特写：终点线黑白方格旗就在眼前，少年的赛车车头已经越过了幽灵车，特写刹车制动，车轮冒烟急停。", "narration": "终于在某一天，他在最后一个大直道超越了那辆车。但在距离终点线只剩最后三米的地方，他一脚把刹车焊死在了地板上。"},
        {"timing": "01:45-02:10", "visual": "慢镜头：父亲的半透明赛车呼啸着穿过终点，少年的车静静停在终点线前，字幕淡出。", "narration": "他看着父亲的车率先冲过终点。因为他知道，一旦打破纪录，系统就会自动覆盖存档。在这世上，有些人的爱是金包银，赢给全世界看；有些人的爱是银包金，宁可一辈子停在终点线前，也绝不覆盖你来过的痕迹。"}
    ]
}

def export_script(story_data, out_path):
    lines = []
    lines.append(f"# 剧本卡片：{story_data['title']}")
    lines.append(f"- **生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **表面载体（银）**：{story_data['carrier_surface']}")
    lines.append(f"- **隐秘真相（金）**：{story_data['carrier_truth']}")
    lines.append(f"- **情感基调**：{story_data['tone']}")
    lines.append(f"- **配乐参考**：{story_data['bgm']}")
    lines.append(f"- **一句话故事梗概**：{story_data['logline']}")
    lines.append("")
    lines.append("## 分镜与旁白台词表")
    lines.append("")
    lines.append("| 时间段 | 画面镜头指示 (Visual) | 配音旁白台词 (Voiceover) |")
    lines.append("|---|---|---|")
    for s in story_data["shots"]:
        visual = s["visual"].replace("|", "/")
        narration = s["narration"].replace("|", "/")
        lines.append(f"| {s['timing']} | {visual} | {narration} |")
    lines.append("")
    lines.append("## 核心金句提取")
    lines.append(f"> {story_data['shots'][-1]['narration'].split('。')[-2]}。")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Script exported successfully to: {out_path}")

def main():
    out_dir = Path(__file__).resolve().parent.parent / "stories" / "scripts"
    target_file = out_dir / "script_01_ghost_car.md"
    export_script(STORY_SAMPLE, target_file)

if __name__ == "__main__":
    main()
