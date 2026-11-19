"""Wrap the artifact-style source page in a full HTML document for GitHub Pages and the vault copy.
Usage: python build.py   (reads ../Psychology Degree/index.html, writes ./index.html)"""
import re, pathlib
here = pathlib.Path(__file__).parent
src = (here.parent / "Psychology Degree" / "index.html").read_text(encoding="utf-8")
cut = src.index("</style>") + len("</style>")
head, body = src[:cut], src[cut:]
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta name="description" content="A free, self-directed psychology degree as a roadmap of open lectures and textbooks. Progress saves in your browser.">\n'
       + head + '\n</head>\n<body>' + body + '\n</body>\n</html>\n')
(here / "index.html").write_text(doc, encoding="utf-8")
print("wrote", here / "index.html", len(doc), "bytes")
