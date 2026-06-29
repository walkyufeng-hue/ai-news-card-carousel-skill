# AI News Card Carousel Skill

这是一个可发布到 GitHub 的 OpenAI Codex Skill 项目，用来把 AI 热点新闻、AI 工具更新、AI 产品变化和 AI 行业事件，整理成适合抖音图文和小红书图文发布的卡片式内容脚本。

它不直接生成图片，也不自动发布内容。它输出的是可以复制到 Figma、Canva、稿定设计、醒图等工具里继续排版的图文脚本。

## 适合谁用

- AI 产品经理
- UI/UX 设计师
- AI 工具体验博主
- AI 知识博主
- 想每日发布 AI 热点内容的人
- 想把 AI 新闻讲给普通人听的人

## 能解决什么问题

- 从多个 AI 热点里筛选一个适合做图文的选题。
- 把新闻事实翻译成普通人能理解的解释。
- 生成默认 6 页的知识卡片脚本。
- 给每页补充栏目标题、正文、重点词、版式说明和视觉提示。
- 输出封面标题、概述文案、发布文案、来源和检查清单。
- 提醒核查来源、避免重复、避免夸张表达。

## 怎么使用

把本仓库放到 Codex 可读取的 Skill 目录，或在使用 Codex 时显式引用这个目录中的 Skill。

示例请求：

```text
Use $ai-news-card-carousel-skill to turn this AI news into a 6-page Xiaohongshu carousel:

OpenAI announced a new model update that improves multimodal interaction.
Source: https://openai.com/
```

也可以直接说：

```text
用 $ai-news-card-carousel-skill 帮我整理今日 AI 热点，选 1 个适合做抖音图文的主题。
```

如果请求“今日”“最新”“最近”的 AI 热点，Codex 应该先核查可靠来源，再输出内容。

## 示例输入

```text
新闻：某 AI 写作工具上线团队知识库功能，可以把公司文档接入到写作流程里。
来源：官方博客
需求：做成 6 页小红书图文，给产品经理看。
历史选题：上周做过“AI 搜索改变信息入口”。
```

## 示例输出

完整示例见 `examples/` 目录。输出结构固定如下：

```markdown
# AI 热点图文卡片脚本

## 1. 热点标题
AI 写作工具开始接入团队知识库

## 5. 推荐封面标题
1. AI 写作真正变了
2. 它不只是帮你润色
3. 写作工具正在变成工作入口

## 6. 图文页内容

### 第 1 页｜封面
- 栏目小标题：AI PRODUCT NOTE
- 主标题：AI 写作真正变了
- 副标题：重点不是更会写，而是更懂你的上下文
- 重点词：团队知识库、上下文
- 版式说明：大标题居中偏上，副标题放在下方两行。
- 视觉提示：米白底、浅点阵、深绿色强调重点词。
```

## 脚本说明

`scripts/` 里的 Python 文件只是辅助示例，不依赖 API key，也不会真实联网抓取新闻。

- `fetch_news.py`：返回模拟 AI 热点数据。
- `dedupe_topics.py`：用本地 JSON 或内置示例历史做基础去重。
- `format_output.py`：把模拟新闻 JSON 格式化成 Markdown 图文脚本结构。

运行示例：

```bash
python3 scripts/fetch_news.py
python3 scripts/dedupe_topics.py --title "OpenAI 推出新的多模态模型" --keywords OpenAI 多模态 模型
python3 scripts/format_output.py
```

## 不会做什么

- 不直接生成图片。
- 不自动发布到抖音或小红书。
- 不保存平台草稿。
- 不生成虚假新闻。
- 不搬运新闻原文。
- 不做夸张标题党。
- 不模仿任何具体账号、头像、文案或视觉素材。

## License

MIT
