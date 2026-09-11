 # Editing - 情绪故事与叙事视频工作室
 
 专注于挖掘真实人间世情、情感反转故事及高情绪短视频剧本（“银包金”以物喻人模型）的创作工作区。
 
 ## 目录结构
 
 - `scripts/`
   - `search_stories.py`：基于 Google 语法的情绪故事采集器（覆盖典当收金、Reddit 真实树洞、二手旧物遗存等分类）。
   - `adapt_story.py`：将原始真实事件重构为三幕式镜头分镜与配音旁白脚本。
 - `stories/`
   - `raw/`：抓取与收集到的一手真实自白与原始新闻素材。
   - `scripts/`：已完成视听化改编、可直接进剪辑软件（剪映/PR）制作的成片剧本卡片。
 
 ## 常用命令
 
 抓取高情绪故事素材：
 ```bash
 python scripts/search_stories.py pawn_gold
 python scripts/search_stories.py reddit_confession
 python scripts/search_stories.py thrift_secrets
 ```
 
 导出剧本卡片示例：
 ```bash
 python scripts/adapt_story.py
 ```
