"""Wrap the artifact-style source page in a full HTML document for GitHub Pages and the vault copy.
Usage: python build.py   (reads ../Psychology Degree/index.html, writes ./index.html)"""
import pathlib

here = pathlib.Path(__file__).parent
src = (here.parent / "Psychology Degree" / "index.html").read_text(encoding="utf-8")

URL = "https://annagibson645-prog.github.io/open-psychology-degree/"
TITLE = "The Open Psychology Degree"
DESC = ("A free, self-directed psychology degree built from open lectures and free textbooks. "
        "Pick your classes, see the hours, and track your progress in your browser.")
ALT = "Study Psychology, Tuition Free: The Open Psychology Degree"

META = f"""<meta name="description" content="{DESC}">
<meta name="theme-color" content="#18358A">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{TITLE}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{ALT}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{URL}og-image.png">
"""

cut = src.index("</style>") + len("</style>")
head, body = src[:cut], src[cut:]
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       + META + head + '\n</head>\n<body>' + body + '\n</body>\n</html>\n')
(here / "index.html").write_text(doc, encoding="utf-8")
print("wrote", here / "index.html", len(doc), "bytes")
