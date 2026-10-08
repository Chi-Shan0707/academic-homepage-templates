# Academic Homepage Templates

A small Jekyll kit for a personal academic homepage, with **19 interchangeable designs**.
All designs share the same content files, so you write your information once and switch the look with one line.

- Works on **GitHub Pages** as-is (plain Jekyll, no plugins).
- Pages: **About** (entry page, with your photo), **Writing** (blog), individual posts, and **CV**.
- Posts support code highlighting, LaTeX math (MathJax), Mermaid diagrams, tables and footnotes.
- Everything shipped here is **sample data** (the fictional "Avery Lin"); replace it with your own.

---

## Quick start

1. **Copy this folder** into a new GitHub repository named `<your-handle>.github.io`
   (or any repo; see [Project sites](#project-sites) for `baseurl`).
2. **Fill in your details**
   | What | File |
   |---|---|
   | Name, affiliation, links, publications, experience, projects, talks, honors | `_data/profile.yml` |
   | About-page text (Markdown) | `_includes/about.md` |
   | CV page (Markdown) and optional PDF | `_includes/cv.md`, `files/cv.pdf` |
   | Portrait (rectangular, 3:4 recommended) | `assets/img/portrait.jpg` |
   | Site title, URL, description | `_config.yml` |
3. **Pick a design**: preview them (below), then set `design: <id>` in `_config.yml`.
4. **Write posts** in `_posts/` (the three included posts are samples; delete them).
5. **Publish**: push to GitHub → *Settings → Pages → Build and deployment → Deploy from a branch → `main` / root*.

## Previewing and choosing a design

With `previews: true` (the default) the site also builds every design:

| URL | What |
|---|---|
| `/` | your site in the design set by `design:` |
| `/gallery/` | all designs with colour swatches and links |
| `/<id>/`, `/<id>/writing/`, `/<id>/cv/` | the same pages in design `<id>` |

Every page shows a small **‹ n/19 · Name ›** switcher at the bottom that jumps to the *same page* in the previous/next design.

After adding or renaming posts, run `python3 scripts/make_previews.py` so each design gets a copy of the new post.

**When you have decided:**

```bash
# 1. in _config.yml
design: oxford        # your choice
previews: false

# 2. remove the preview pages
python3 scripts/make_previews.py --clean
rm gallery.html       # optional
```

Optionally delete the designs you don't use from `_data/styles.yml`, `_includes/styles/` and `assets/css/`
(keep `base.css`).

## Design catalogue

| id | Name | Look |
|----|------|------|
| `classic` | Classic | The familiar researcher page — name and bio beside a photo, a tidy publication list, Lato and calm blue links. |
| `article` | Article | Typeset like a LaTeX paper — Latin Modern, centered title block, an abstract, numbered sections. |
| `tufte` | Tufte | Edward Tufte's handout style — ET Book on cream, a wide margin for the photo, dates and notes. |
| `faculty` | Faculty | A university profile page — a deep teal header band, a contact card beside the bio, Noto Sans and Serif. |
| `oxford` | Oxford | Formal and collegiate — Oxford blue on parchment, Caslon type, double rules and small capitals. |
| `claret` | Claret | Burgundy and warm white; a sticky profile column with contact details and Crimson Pro text. |
| `ivy` | Ivy | Deep ivy green, Libre Baskerville text and Cormorant small-caps headings; quietly traditional. |
| `monograph` | Monograph | Book-like — running head, centered small-caps section titles, ornaments and a drop cap, set in Spectral. |
| `distill` | Distill | A research-journal look in the spirit of Distill — sans headings, serif text, a byline grid on posts. |
| `paper` | Paper | A single quiet column of serif text on warm ivory, like a well-set essay. |
| `sage` | Sage | A calm sidebar layout in pale sage and soft green, sans-serif with serif reading pages. |
| `mist` | Mist | Cool grey-blue, centered header, IBM Plex; clean lists separated by hairlines. |
| `linen` | Linen | Sand and terracotta with an elegant Garamond display face. |
| `forest` | Forest | A soft dark theme — deep green-charcoal, cream text and moss accents. |
| `ledger` | Ledger | A structured index with section labels in the margin, monospace details and an ochre accent. |
| `washi` | Washi | Japanese-inspired restraint — rice-paper tones, indigo ink, Mincho type. |
| `clay` | Clay | Warm and friendly — soft cards with a muted clay accent, Figtree and Lora. |
| `dusk` | Dusk | Muted lavender-grey with a large serif name; modern and editorial. |
| `stone` | Stone | Swiss-style grid on warm grey — big typographic name, strict alignment, one olive accent. |

## Run it locally (optional)

```bash
gem install bundler
bundle install                    # uses the Gemfile (github-pages gem = same versions as GitHub)
bundle exec jekyll serve          # → http://localhost:4000
```

Or with Docker: `docker run --rm -p 4000:4000 -v "$PWD":/srv/jekyll jekyll/jekyll:3.8 jekyll serve`.

## Writing posts

Create `_posts/YYYY-MM-DD-slug.md`; the URL becomes `/writing/slug/`.

```markdown
---
title: "Post title"
description: "One sentence shown in post lists and under the title."
category: "notes"          # shown as a small label (e.g. notes, essays, tech)
tags: ["topic", "another"]
math: true                 # load MathJax: $inline$, $$display$$, \( \), \[ \]
---
```

- Code blocks get syntax highlighting; a ` ```mermaid ` block is rendered as a diagram.
- `<details markdown="1"><summary>…</summary> … </details>` makes a collapsible section.
- A project link can point at a post: `{ name: Write-up, post: <slug> }` in `profile.yml`.

## Customising

**Colours & type** — each design's look lives in `assets/css/<id>.css`. The top of the file sets CSS variables:

```css
:root {
  --bg: …;  --text: …;  --muted: …;  --line: …;  --accent: …;   /* palette */
  --font-body: …;  --font-head: …;                                /* fonts */
  --fs: …;  --page: …;  --measure: …;  --photo-w: …;              /* size, page width, reading width, photo width */
}
```

If you change a font, also update that design's `fonts:` entry (a Google Fonts `css2` query) in `_data/styles.yml`.

**Shared behaviour** (spacing, publication list, CV, reading typography, mobile layout) is in `assets/css/base.css`.

**Sections of the About page** (order, titles, which ones appear) are in `_includes/k/about.html`.
**Navigation links** are in `_includes/nav.html`.

### Adding a new design

1. Copy a similar design: `_includes/styles/paper.html` → `mine.html`, `assets/css/paper.css` → `mine.css`
   (in the HTML, change `s-paper` to `s-mine`).
2. Add an entry with `id: mine` to `_data/styles.yml`.
3. Run `python3 scripts/make_previews.py` and open `/mine/`.

## Project sites

If the repository is not `<your-handle>.github.io`, the site lives under `/<repo-name>/`.
Set `baseurl: "/<repo-name>"` and `url: "https://<your-handle>.github.io"` in `_config.yml`.

## File map

```
_config.yml                 site settings: design, previews, url/baseurl
_data/profile.yml           all structured information about you
_data/styles.yml            the list of designs
_includes/about.md          About text          _includes/cv.md    CV text
_includes/k/                page templates shared by all designs (about, writing, post, cv)
_includes/parts/            publication / experience / project / post lists
_includes/styles/<id>.html  each design's page shell (header, nav, footer)
_includes/switcher.html     the preview switcher (only when previews: true)
_layouts/default.html       the single layout every page uses
assets/css/base.css         shared styles     assets/css/<id>.css   one per design
assets/img/portrait.jpg     your photo        files/cv.pdf          your CV (optional)
_posts/                     your posts
about.md, writing.md, cv.md the site's root pages (/, /writing/, /cv/)
gallery.html                the design gallery (/gallery/)
previews/                   generated preview pages (scripts/make_previews.py)
```

## Notes

- The photo appears **only on the About page**, always as a rectangle.
- Web fonts load asynchronously from Google Fonts (Article and Tufte load Latin Modern / ET Book from jsDelivr);
  if a font cannot load, a similar system font is used.
- MathJax and Mermaid are loaded only on posts that need them.
