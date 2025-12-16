# Modern AI Chronicle

[Versión en español](README.md)

## What is this project?

**Modern AI Chronicle** is a chronicle created and maintained by the **Radient Institute** community to document—with historical and narrative perspective—how artificial intelligence moved from the lab to the mainstream in an extraordinarily short time.

The text covers the **post-ChatGPT** era, from December 2022 to the present: the moment when AI stopped being a niche technology and became a global cultural, economic, and political phenomenon.

It is not a blog or a news feed.  
It is a **chronicle**: self-contained but connected chapters, written with focus on what truly mattered, in what order it happened, and why it had consequences.

The project’s ambition is simple:

> If someone fell into a coma in January 2023 and woke up today, this book should let them understand what happened in AI while they were gone.

The project is a **living document**:
- new chapters are added as the story unfolds,
- facts are corrected when better information appears,
- community contributions are welcome.

The content is **free to modify and redistribute** under the **CC BY 4.0** license.

**Community and links**
- Web: https://cronicaia.com  
- Radient Web: https://radient.institute  
- YouTube: https://www.youtube.com/@RadientNews  
- X / Twitter: https://x.com/RadientAI  
- Discord: https://discord.gg/ducUQHQTeC  

---

## Writing and contribution

Contributions are welcome, both in content and in technical or editorial improvements. Before contributing, it is important to understand **how the project is structured and which editorial criteria it follows**.

### Overall project structure

The site is built with **Hugo (Extended)** using the base theme **hugo-book** plus customizations:  
https://github.com/alex-shpak/hugo-book

- **Main content (Spanish):** `content.es/docs/content/`
- **Optional translations (English):** `content.en/docs/content/`
- Chapters are ordered by:
  - filename (numbering)
  - `weight` in the front matter
- The final build is generated in `public/` (**do not edit**).

### Chapter format

Each chapter is a Markdown file in `content.es/docs/content/`. Minimal example:

```yaml
---
weight: 24
bookFlatSection: true
title: "24 - Chapter title"
image: style_1/banner_images/24_banner.webp
---
# Visible title

Chapter text...
```

Notes:
- `weight` controls ordering.
- `title` is used in the menu.
- `image` defines the chapter banner.
- Images are referenced from `static/`.
- If a translation exists, duplicate the file in `content.en/docs/content/`.

---

## Editorial guide

The stories told here are not automatically generated content.

- Chapters written exclusively by LLMs are not accepted.
- The chronicle must preserve a human viewpoint, with judgment, context, and temporal sequence.
- Narrative and informative tone: avoid headline lists and “noise.”
- The first version does not include references yet, but the goal is to add citations and sources to current and future chapters.
- Prefer small, frequent revisions over massive changes.

---

## Visual styles and assets

The project uses three visual styles: `style_1`, `style_2`, `style_3`.

- Static assets per style: `static/style_X/`
- Banners: `static/style_X/banner_images/`
- SCSS: `assets/style_X/`

Style selection happens in `layouts/partials/docs/html-head.html`: it picks a style at random and stores it in `localStorage` with the key `site-style`.  
To lock a style, change that value manually.

Images generated with Midjourney v7:
- `style_1`: `--sref 2661356114`
- `style_2`: `--sref 1625887214`
- `style_3`: `--sref 1782315770`

---

## Requirements and local development

- **Requirement:** Hugo Extended  
  https://gohugo.io/installation/

- **Local server (in `mydocs`):**
  ```bash
  hugo server --minify --theme hugo-book
  ```
- Default: http://localhost:1313/  
- Use `--disableFastRender` if you need full reloads.

---

## Contribution flow

- Open issues or pull requests at: https://github.com/RadientAI/Cronica-IA
- Keep changes focused.
- Include screenshots or previews if you modify styles.
- Ensure a clean build (`hugo server -D` or `hugo --minify`) before submitting.
- For questions or suggestions, join the community on Discord: https://discord.gg/ducUQHQTeC
