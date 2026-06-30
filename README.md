# AI News Card Carousel Skill

这是一个 OpenAI Codex Skill 项目，用来把 AI 热点新闻、AI 工具更新、AI 产品变化和 AI 行业事件，整理成适合抖音图文和小红书图文发布的中文卡片内容，并可选渲染成 `1080 × 1440 px` 的 3:4 PNG 卡片图。

默认视觉风格是暗色 AI prompt 卡片风：深黑背景、暗绿色重点色、半透明内容卡片、细线边框、科技感标签。每一页左上角固定显示 `YF拾光机`，右下角保留 `1/6` 这类页码。

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
- 给每页补充主标题、正文、重点词和图片说明。
- 输出封面标题、发布文案、来源信息。
- 可选把卡片内容渲染成 PNG 图片。

## 输出结构

默认只输出这些部分：

```markdown
# AI 热点图文卡片脚本

## 1. 热点标题

## 2. 新闻来源

## 3. 推荐封面标题

## 4. 图文页内容

## 5. 抖音 / 小红书发布文案
```

Skill 内部仍会做事实核查、选题判断和重复风险判断，但默认只展示上面的精简发布结构。

## 怎么使用

示例请求：

```text
用 $ai-news-card-carousel-skill 帮我整理今日 AI 热点，选 1 个适合做小红书图文的主题，并生成 6 张 3:4 卡片图。
```

如果请求“今日”“最新”“最近”的 AI 热点，Codex 应该先核查可靠来源，再输出内容。

## 生成图片

图片渲染脚本：

```bash
python3 scripts/render_cards.py examples/render-input-gpt56-sol.json --output output/gpt56-sol-cards
```

脚本需要 Pillow：

```bash
python3 -m pip install Pillow
```

输出文件：

```text
output/gpt56-sol-cards/card-01.png
output/gpt56-sol-cards/card-02.png
...
output/gpt56-sol-cards/preview-contact-sheet.png
```

## 示例输入

```text
新闻：某 AI 写作工具上线团队知识库功能，可以把公司文档接入到写作流程里。
来源：官方博客
需求：做成 6 页 3:4 小红书图文，风格参考暗色 prompt 卡片。
```

## 不会做什么

- 不自动发布到抖音或小红书。
- 不保存平台草稿。
- 不生成虚假新闻。
- 不搬运新闻原文。
- 不做夸张标题党。
- 不模仿任何具体账号、头像、文案或视觉素材。

## License

MIT
