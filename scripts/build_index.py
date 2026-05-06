#!/usr/bin/env python3
"""Reads all meta.json files and injects presentation cards into index.html."""
import json, os, re
from pathlib import Path

root = Path('.')
presentations_dir = root / 'presentations'
cards = []

if presentations_dir.exists():
    for folder in sorted(presentations_dir.iterdir(), reverse=True):
        meta_file = folder / 'meta.json'
        if meta_file.exists():
            meta = json.loads(meta_file.read_text())
            cover = f"presentations/{folder.name}/{meta.get('cover', '')}" if meta.get('cover') else None
            cards.append({
                'title': meta.get('title', folder.name),
                'description': meta.get('description', ''),
                'date': meta.get('date', ''),
                'tags': meta.get('tags', []),
                'event': meta.get('event', ''),
                'slides_count': meta.get('slides_count', 0),
                'url': f"presentations/{folder.name}/index.html",
                'cover': cover
            })

index_html = root / 'index.html'
content = index_html.read_text()

# Generate cards HTML
if cards:
    cards_html = '\n'.join([
        f'''<article class="pres-card" onclick="window.open('{c['url']}','_blank')">
  <div class="pres-card-img" style="background-image:url('{c['cover']}')" aria-label="{c['title']}">
    {'<img src="' + c['cover'] + '" alt="" loading="lazy">' if c['cover'] else ''}
    <span class="slides-badge">{c['slides_count']} slides</span>
  </div>
  <div class="pres-card-body">
    <div class="pres-card-meta">
      <span class="pres-date">{c['date']}</span>
      {f'<span class="pres-event">{c["event"]}</span>' if c['event'] else ''}
    </div>
    <h3 class="pres-title">{c['title']}</h3>
    <p class="pres-desc">{c['description']}</p>
    <div class="pres-tags">{' '.join([f'<span class="tag">{t}</span>' for t in c['tags']])}</div>
  </div>
</article>''' for c in cards
    ])
else:
    cards_html = '''<div class="empty-state">
  <p>Презентаций пока нет.<br>Попроси Perplexity создать первую — просто дай ссылку на этот репо и описание.</p>
</div>'''

new_content = re.sub(
    r'<!-- PRESENTATIONS_START -->.*?<!-- PRESENTATIONS_END -->',
    f'<!-- PRESENTATIONS_START -->\n{cards_html}\n<!-- PRESENTATIONS_END -->',
    content,
    flags=re.DOTALL
)

index_html.write_text(new_content)
print(f'Built index with {len(cards)} presentations.')
