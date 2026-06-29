# Dedupe Rules

Use these rules to avoid repeating a topic.

## Inputs To Compare

- Current topic title.
- Source title.
- Product or company name.
- Keywords.
- User-provided historical topic list.
- Previously generated carousel titles in the current conversation or workspace, if available.

## Title Dedupe

Treat as duplicate when:

- The normalized title is the same.
- The only difference is punctuation or wording order.
- The new title uses a different hook for the same exact update.

## Keyword Dedupe

Compare core keywords:

- Company: OpenAI, Anthropic, Google, Meta, Microsoft, etc.
- Product: ChatGPT, Claude, Gemini, Copilot, Perplexity, etc.
- Capability: voice, multimodal, agent, memory, search, coding, image, video.
- Event type: launch, update, pricing, policy, acquisition, benchmark, outage.

If two topics share the same company, product, capability, and event type, they are likely duplicates.

## Semantic Dedupe

Treat as repeated when the reader takeaway is the same, even if the news source is different.

Example:

- "AI search is becoming the new information entrance."
- "Search products are turning answer pages into operating systems."

These can be merged unless there is a genuinely new fact.

## Historical Topic Records

When history is available, compare against:

- Final published title.
- Draft cover titles.
- Main keywords.
- Date published.
- Core viewpoint.

When history is not available, say the duplicate check is limited.

## Similar Hotspot Merge

If several updates point to the same trend, merge them into one trend carousel only when all sources are reliable and the page structure remains simple.
