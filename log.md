# ksink log

## 2026-01-05 initial setup

Set up tools repo inspired by Simon Willison's approach:
- Created CLAUDE.md with custom instructions for Python and HTML tools
- Added index.html listing page with purple gradient header
- Created sample tools:
  - `tools/html/gravity-balls.html` - physics sim with bouncing balls
  - `tools/python/excuse.py` - random developer excuse generator
- Created GitHub repo and enabled Pages

Live at: https://odcoda.github.io/ksink/

## 2026-01-05 ai timeline estimator

Added `tools/html/ai-timeline.html`:
- Sliders for compute, algorithms, investment, regulation, coordination
- Real-time hockey-stick curve visualization
- Color scheme shifts ominous (red) to chill (blue) based on timeline
- Emojis reflect the mood from 😱 to 🌴

## 2026-01-06 wikiquote reels

Built a short-form literature feed:
- TikTok-style shell with quote cards instead of video
- Infinite scroll with auto-advance and progress bars
- Curated classic literature quotes linked to Wikiquote
Up next:
- Add a simple search/filter for authors

## 2026-01-06 live wikiquote feed

Switched the reels tool to live data:
- Fetch quotes from Wikiquote with a fixed classics list
- Auto-fit long excerpts into the quote card
- Added randomized typographic treatments and card palettes
Up next:
- Add an author search or filter
