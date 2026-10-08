---
title: "Start here: using this template"
description: "A sample post that doubles as a checklist for setting up the site."
category: "guide"
tags: ["sample"]
---

This post is sample content. Replace it (and the other posts in `_posts/`) with your own writing.

## Five-minute setup

1. **Your details** — edit `_data/profile.yml` (name, affiliation, links, publications, experience…).
2. **About text** — edit `_includes/about.md`. It is the first thing visitors read.
3. **Photo** — replace `assets/img/portrait.jpg` with a rectangular portrait (3:4 works best).
4. **CV** — edit `_includes/cv.md`, and put a PDF at `files/cv.pdf` if you have one.
5. **Design** — open `/gallery/`, compare designs with the ‹ › switcher, then set `design:` in `_config.yml`.

## Writing a post

Create `_posts/YYYY-MM-DD-your-slug.md`:

```markdown
---
title: "Your title"
description: "One sentence shown in post lists."
category: "notes"
tags: ["topic"]
math: true    # only if the post uses LaTeX
---

Your text in Markdown. Inline math: $e^{i\pi} + 1 = 0$.
```

While `previews: true`, run `python3 scripts/make_previews.py` after adding a post so every design gets a copy of it.
