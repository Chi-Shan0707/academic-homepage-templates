#!/usr/bin/env python3
"""Generate (or remove) the design-preview pages.

    python3 scripts/make_previews.py           # build previews/<id>/… for every design
    python3 scripts/make_previews.py --clean   # delete previews/ (use when you are done choosing)

For every design in _data/styles.yml this writes stub pages under previews/:
    previews/<id>/index.md            About (entry page)  →  /<id>/
    previews/<id>/writing.md          post archive        →  /<id>/writing/
    previews/<id>/cv.md               CV                  →  /<id>/cv/
    previews/<id>/writing/<slug>.md   one per post        →  /<id>/writing/<slug>/
Stubs contain front matter only; content comes from _includes/, _data/ and _posts/.
Re-run after adding, renaming or deleting posts or designs.
"""
import pathlib, re, shutil, sys, yaml

root = pathlib.Path(__file__).resolve().parent.parent
out = root / "previews"
if out.exists():
    shutil.rmtree(out)
if "--clean" in sys.argv:
    print("removed previews/ — remember to set `previews: false` in _config.yml")
    sys.exit()

styles = yaml.safe_load((root / "_data/styles.yml").read_text(encoding="utf-8"))
slugs = [m.group(1) for f in sorted((root / "_posts").glob("*.md"))
         if (m := re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.(md|markdown)$", f.name))]

def stub(path, **fm):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---", "layout: default"] + [f"{k}: {v}" for k, v in fm.items()] + ["---", ""]
    path.write_text("\n".join(lines), encoding="utf-8")

for st in styles:
    sid, d = st["id"], out / st["id"]
    stub(d / "index.md", style=sid, kind="about", permalink=f"/{sid}/")
    stub(d / "writing.md", style=sid, kind="writing", permalink=f"/{sid}/writing/")
    stub(d / "cv.md", style=sid, kind="cv", permalink=f"/{sid}/cv/")
    for slug in slugs:
        stub(d / "writing" / f"{slug}.md", style=sid, kind="post", post_slug=slug, permalink=f"/{sid}/writing/{slug}/")

print(f"{len(styles)} designs × {len(slugs)} posts → previews/")
