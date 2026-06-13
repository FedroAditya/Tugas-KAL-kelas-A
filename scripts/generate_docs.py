#!/usr/bin/env python3
from pathlib import Path
import re
import shutil
import sys

try:
    import markdown
except ImportError:
    print("Please install markdown with: pip install markdown")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / '_sources'
DOCS_DIR = ROOT / 'docs'
TEMPLATE_FILE = DOCS_DIR / 'Materi3.html'

if not TEMPLATE_FILE.exists():
    raise FileNotFoundError(f"Template file not found: {TEMPLATE_FILE}")

if not SRC_DIR.exists():
    raise FileNotFoundError(f"Source folder not found: {SRC_DIR}")

# Build navigation from markdown source files.

def title_from_markdown(md_path: Path) -> str:
    for line in md_path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line.startswith('#'):
            return line.lstrip('#').strip()
    return md_path.stem


def build_nav_html(md_files):
    lines = []
    for md in md_files:
        if md.name == 'intro.md':
            continue
        title = title_from_markdown(md)
        href = f"{md.stem}.html"
        lines.append(f'    <li class="toctree-l1"><a class="reference internal" href="{href}">{title}</a></li>')
    return '<ul class="current nav bd-sidenav">\n' + '\n'.join(lines) + '\n</ul>'


def normalize_template(html: str) -> str:
    # Remove any active/current classes from the template so the generated pages remain clean.
    html = re.sub(r' class="toctree-l1 current active"', ' class="toctree-l1"', html)
    html = re.sub(r' class="current reference internal"', ' class="reference internal"', html)
    return html


def replace_nav(html: str, nav_html: str) -> str:
    return re.sub(r'<ul class="current nav bd-sidenav">.*?</ul>', nav_html, html, flags=re.S)


def split_template(html: str):
    marker = '<article class="bd-article">'
    if marker not in html:
        raise ValueError('Template does not contain <article class="bd-article"> marker')
    prefix, remainder = html.split(marker, 1)
    if '</article>' not in remainder:
        raise ValueError('Template does not contain closing </article> marker')
    article_body, suffix = remainder.split('</article>', 1)
    return prefix + marker, article_body, '</article>' + suffix


def generate_page(template_prefix: str, template_suffix: str, article_html: str) -> str:
    return template_prefix + '\n' + article_html + '\n' + template_suffix


def copy_sources():
    target = DOCS_DIR / '_sources'
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(SRC_DIR, target)


def ensure_index_redirect():
    index_file = DOCS_DIR / 'index.html'
    redirect_html = '<meta http-equiv="Refresh" content="0; url=intro.html" />\n'
    index_file.write_text(redirect_html, encoding='utf-8')


def main():
    md_files = sorted(SRC_DIR.glob('*.md'))
    if not md_files:
        raise RuntimeError('No markdown source files found in _sources')

    template_html = TEMPLATE_FILE.read_text(encoding='utf-8')
    template_html = normalize_template(template_html)
    nav_html = build_nav_html(md_files)
    template_html = replace_nav(template_html, nav_html)
    prefix, _, suffix = split_template(template_html)

    generated = []
    for md in md_files:
        html_fragment = markdown.markdown(md.read_text(encoding='utf-8'), extensions=['fenced_code', 'tables', 'codehilite'])
        out_name = f"{md.stem}.html"
        out_path = DOCS_DIR / out_name
        page_html = generate_page(prefix, suffix, html_fragment)
        out_path.write_text(page_html, encoding='utf-8')
        generated.append(out_name)

    copy_sources()
    ensure_index_redirect()

    print('Generated pages:')
    for name in generated:
        print('-', name)
    print('Copied _sources to docs/_sources')


if __name__ == '__main__':
    main()
