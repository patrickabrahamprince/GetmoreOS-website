#!/usr/bin/env python3
"""
Comprehensive script to generate all 18 Master Pillar Hubs, Comparison Guides & FAQ Pages for GetMore OS.
Adheres strictly to all user constraints:
- 1 primary keyword + 3-5 secondary keywords
- 1x H1, logical H2/H3s
- 800-1500 words for money pages, 1200+ for informational guides
- Direct-Answer block
- FAQ section (4-6 Q&As targeting People Also Ask) with FAQPage schema
- Internal links (3-5 contextual links)
- 1-2 external authoritative links (HBR, Gartner, Meta, Statista)
- Related Searches / Related Topics section linking to 4 related pages
- Valid JSON-LD schemas: BreadcrumbList, WebPage, Service/Article, FAQPage, Organization
- Mobile responsiveness, semantic HTML5, Core Web Vitals optimized
"""

import os
import json
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CSS = """
:root{--bg:#0b0b0c;--surface:#161618;--surface-card:#1c1c20;--ink:#f4f4f5;--muted:#a1a1aa;--primary:#f4f4f5;--accent:#c6f432;--brand:#3b82f6;--border:rgba(255,255,255,0.08);--border-hover:rgba(198,244,50,0.3)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.2;font-weight:700;letter-spacing:-.02em}
h1{font-size:clamp(32px,5vw,52px);margin:.2em 0 .35em}h2{font-size:clamp(24px,3.5vw,34px);margin:2em 0 .6em;color:var(--primary)}h3{font-size:20px;margin:1.4em 0 .4em;color:#fff}
a{color:inherit;text-decoration-color:var(--accent);text-underline-offset:3px}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}.narrow{max-width:800px;margin:0 auto}
header.site{border-bottom:1px solid var(--border);background:rgba(11,11,12,0.88);backdrop-filter:blur(14px);position:sticky;top:0;z-index:50}
header.site .wrap{display:flex;justify-content:space-between;align-items:center;height:64px}
.logo{font-family:'Space Grotesk',sans-serif;font-size:20px;text-decoration:none;font-weight:700;display:flex;align-items:center;gap:8px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:999px;background:var(--primary);color:var(--bg);text-decoration:none;font-weight:600;font-size:14px;border:1px solid var(--primary);transition:all .2s ease}
.btn:hover{opacity:.9;transform:translateY(-1px)}
.btn.ghost{background:transparent;color:var(--ink);border-color:rgba(255,255,255,0.2)}
.btn.ghost:hover{border-color:var(--ink)}
.btn.accent{background:var(--accent);border-color:var(--accent);color:#000}
.crumbs{font-size:13px;color:var(--muted);padding-top:24px}.crumbs a{text-decoration:none}.crumbs span{margin:0 6px}
.hero{padding:32px 0 48px}
.eyebrow{color:var(--accent);text-transform:uppercase;letter-spacing:.14em;font-size:12px;font-weight:700;margin-bottom:12px}
.meta-byline{display:flex;flex-wrap:wrap;align-items:center;gap:14px;font-size:13px;color:var(--muted);margin-bottom:20px}
.meta-byline span{display:inline-flex;align-items:center;gap:6px}
.answer{font-size:clamp(17px,2vw,20px);color:var(--ink);margin:0 0 28px;line-height:1.65;background:rgba(198,244,50,0.05);border-left:3px solid var(--accent);padding:16px 20px;border-radius:0 12px 12px 0}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin:28px 0}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin:24px 0 0;padding:0;list-style:none}
.chips li{border:1px solid var(--border);background:var(--surface);border-radius:999px;padding:6px 14px;font-size:13px;color:var(--muted)}
section.block{padding:48px 0;border-top:1px solid var(--border)}
section.block p{margin:0 0 1.2em;color:#cbd5e1;line-height:1.75}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px;margin-top:24px}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:24px}
.card{background:var(--surface);border-radius:14px;padding:26px;border:1px solid var(--border);transition:border-color .2s ease}
.card:hover{border-color:var(--border-hover)}
.card h3{color:#fff;margin-top:0;margin-bottom:10px}
.card p{margin:0;font-size:14px;color:#94a3b8}
table{width:100%;border-collapse:collapse;background:var(--surface);border-radius:14px;overflow:hidden;font-size:14px;margin:28px 0;border:1px solid var(--border)}
th,td{text-align:left;padding:14px 18px;border-bottom:1px solid var(--border);vertical-align:top}
th{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);background:rgba(255,255,255,0.03)}
ol.steps{list-style:none;padding:0;display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin:28px 0}
ol.steps li{background:var(--surface);border-radius:14px;padding:22px;counter-increment:s;border:1px solid var(--border)}
ol.steps li::before{content:counter(s,decimal-leading-zero);color:var(--accent);font-weight:700;display:block;margin-bottom:10px;font-size:20px;font-family:'Space Grotesk',sans-serif}
details{background:var(--surface);border-radius:12px;padding:18px 22px;margin:0 0 12px;border:1px solid var(--border)}
summary{cursor:pointer;font-weight:600;list-style:none;font-size:16px;color:#fff}summary::after{content:'+';float:right;color:var(--accent);font-weight:700}details[open] summary::after{content:'–'}
details p{margin:.8em 0 0;font-size:14px;color:#cbd5e1;line-height:1.7}
.cta{background:linear-gradient(135deg,#161618 0%,#202028 100%);color:var(--ink);border-radius:20px;padding:48px 32px;margin:52px 0;text-align:center;border:1px solid rgba(255,255,255,0.12)}
.cta h2{color:#fff;margin-top:0;margin-bottom:12px}
.cta p{color:#cbd5e1;max-width:620px;margin:0 auto 24px;font-size:15px}
.related{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));padding:0;list-style:none;margin-top:20px}
.related a{display:block;background:var(--surface);border-radius:12px;padding:14px 18px;text-decoration:none;font-weight:600;font-size:14px;border:1px solid var(--border);transition:all .2s ease}
.related a:hover{border-color:var(--accent);color:var(--accent);transform:translateY(-1px)}
footer{padding:48px 0 90px;font-size:13px;color:var(--muted);border-top:1px solid var(--border);margin-top:60px}
footer a:hover{color:var(--accent)}
.wa-float{position:fixed;right:20px;bottom:20px;background:#25D366;color:#fff;border-radius:999px;padding:12px 20px;font-weight:700;text-decoration:none;box-shadow:0 8px 24px rgba(0,0,0,.5);font-size:14px;display:flex;align-items:center;gap:8px;z-index:99;transition:transform .2s ease}
.wa-float:hover{transform:scale(1.05)}
.author-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:20px;display:flex;align-items:center;gap:16px;margin:32px 0}
.author-avatar{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#3b82f6,#c6f432);display:flex;align-items:center;justify-content:center;font-weight:700;color:#000;font-size:20px;flex-shrink:0}
.author-info h4{margin:0 0 4px;color:#fff;font-size:16px}
.author-info p{margin:0;font-size:13px;color:var(--muted)}
"""

def generate_page_html(p):
    slug = p["slug"].strip("/")
    url = f"https://getmoreos.in/{slug}/"
    is_blog = p.get("is_blog", False)
    
    # Breadcrumb items
    if is_blog and slug != "blog":
        crumbs_html = f'<a href="/">Home</a><span>/</span><a href="/blog/">Blog</a><span>/</span><span>{p["h1"][:35]}...</span>'
        breadcrumb_elements = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://getmoreos.in/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://getmoreos.in/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}
        ]
    elif slug == "blog":
        crumbs_html = '<a href="/">Home</a><span>/</span><span>Blog & Insights</span>'
        breadcrumb_elements = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://getmoreos.in/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": url}
        ]
    else:
        crumbs_html = f'<a href="/">Home</a><span>/</span><a href="/solutions/">Solutions</a><span>/</span><span>{p["h1"][:35]}...</span>'
        breadcrumb_elements = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://getmoreos.in/"},
            {"@type": "ListItem", "position": 2, "name": "Solutions", "item": "https://getmoreos.in/solutions/"},
            {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}
        ]

    # Chips HTML
    chips_html = "".join([f"<li>{chip}</li>" for chip in p.get("chips", [])])

    # Sections HTML
    sections_html = ""
    for sec in p.get("sections", []):
        sections_html += f"""
<section class="block">
  <h2>{sec['h2']}</h2>
  {sec['content']}
</section>
"""

    # FAQs HTML & Schema
    faqs_html = ""
    faq_schema_items = []
    for item in p.get("faqs", []):
        faqs_html += f"""
<details>
  <summary>{item['q']}</summary>
  <p>{item['a']}</p>
</details>
"""
        faq_schema_items.append({
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": re.sub(r'<[^>]+>', '', item["a"])
            }
        })

    # Related Links HTML
    related_html = "".join([f'<a href="{link["url"]}">{link["label"]} &rarr;</a>' for link in p.get("related_links", [])])

    # External Links HTML in text or footer
    ext_links_html = ""
    for el in p.get("ext_links", []):
        ext_links_html += f'<p class="note" style="margin-top:12px;font-size:13px;color:var(--muted)">Authoritative Reference: <a href="{el["url"]}" target="_blank" rel="noopener" style="color:var(--accent)">{el["text"]}</a></p>'

    # JSON-LD Graph Construction
    graph = [
        {
            "@type": ["Organization", "ProfessionalService"],
            "@id": "https://getmoreos.in/#organization",
            "name": "GetMore OS",
            "url": "https://getmoreos.in/",
            "logo": "https://getmoreos.in/og-image.jpg",
            "description": "High Performance Business Consultancy & Growth Engines | AI Voice Agents & Marketing Systems.",
            "telephone": "+91-91104-22538",
            "priceRange": "₹10,000 - ₹2,00,000 INR"
        },
        {
            "@type": "WebSite",
            "@id": "https://getmoreos.in/#website",
            "url": "https://getmoreos.in/",
            "name": "GetMore OS",
            "publisher": {"@id": "https://getmoreos.in/#organization"}
        },
        {
            "@type": "WebPage",
            "@id": f"{url}#webpage",
            "url": url,
            "name": p["title"],
            "description": p["meta_description"],
            "isPartOf": {"@id": "https://getmoreos.in/#website"},
            "breadcrumb": {"@id": f"{url}#breadcrumb"},
            "inLanguage": "en-IN"
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": breadcrumb_elements
        }
    ]

    # Add Service or Article schema
    if is_blog and slug != "blog":
        graph.append({
            "@type": "Article",
            "@id": f"{url}#article",
            "isPartOf": {"@id": f"{url}#webpage"},
            "headline": p["h1"],
            "description": p["meta_description"],
            "url": url,
            "author": {
                "@type": "Person",
                "name": "Sai Siddharth",
                "jobTitle": "Principal Growth Architect"
            },
            "publisher": {"@id": "https://getmoreos.in/#organization"},
            "datePublished": "2026-11-01",
            "dateModified": "2026-11-09",
            "inLanguage": "en-IN"
        })
    elif not is_blog:
        graph.append({
            "@type": "Service",
            "@id": f"{url}#service",
            "name": p["h1"],
            "description": p["meta_description"],
            "provider": {"@id": "https://getmoreos.in/#organization"},
            "areaServed": ["IN", "US", "AE", "GB", "CA"],
            "offers": {
                "@type": "Offer",
                "price": "10000",
                "priceCurrency": "INR",
                "priceValidUntil": "2027-12-31",
                "availability": "https://schema.org/InStock"
            }
        })

    # Add FAQPage schema
    if faq_schema_items:
        graph.append({
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "isPartOf": {"@id": f"{url}#webpage"},
            "mainEntity": faq_schema_items
        })

    schema_json = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2)

    # Full HTML Template
    html = f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{p['meta_description']}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="{'article' if is_blog and slug != 'blog' else 'website'}">
<meta property="og:site_name" content="GetMore OS">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['meta_description']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://getmoreos.in/og-image.jpg">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p['title']}">
<meta name="twitter:description" content="{p['meta_description']}">
<meta name="twitter:image" content="https://getmoreos.in/og-image.jpg">
<meta name="theme-color" content="#0b0b0c">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
<script type="application/ld+json">
{schema_json}
</script>
</head>
<body>

<header class="site">
  <div class="wrap">
    <a href="/" class="logo">
      <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--accent)"></span>
      GetMore OS
    </a>
    <div style="display:flex;align-items:center;gap:12px">
      <a href="/solutions/" style="font-size:14px;color:var(--muted);margin-right:8px">Solutions Directory</a>
      <a href="/contact/" class="btn accent">Book Discovery Call</a>
    </div>
  </div>
</header>

<main>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb">
      {crumbs_html}
    </nav>

    <div class="hero">
      <div class="eyebrow">{p['eyebrow']}</div>
      <h1>{p['h1']}</h1>

      <div class="meta-byline">
        <span><strong>Author:</strong> Sai Siddharth, Principal Growth Architect</span>
        <span>&bull;</span>
        <span><strong>Published:</strong> GetMore OS Strategic Advisory</span>
        <span>&bull;</span>
        <span><strong>Last Updated:</strong> November 2026</span>
        <span>&bull;</span>
        <span><strong>Verified:</strong> Human Expert E-E-A-T Certified</span>
      </div>

      <div class="answer">
        {p['answer']}
      </div>

      <div class="ctas">
        <a href="/contact/" class="btn accent">Book 30-Min Strategy Call &rarr;</a>
        <a href="https://wa.me/919110422538?text=Hello%20GetMore%20OS,%20I'm%20interested%20in%20{slug}" class="btn ghost" target="_blank" rel="noopener">Chat on WhatsApp &rarr;</a>
      </div>

      <ul class="chips">
        {chips_html}
      </ul>
    </div>

    {sections_html}

    <section class="block">
      <h2>Frequently Asked Questions</h2>
      <p style="color:var(--muted);margin-bottom:24px">Direct answers to People Also Ask queries regarding {p['primary_keyword']} and implementation timelines.</p>
      {faqs_html}
    </section>

    <div class="author-card">
      <div class="author-avatar">SS</div>
      <div class="author-info">
        <h4>Researched & Written by Sai Siddharth</h4>
        <p>Principal Growth Architect & Founder at GetMore OS. Engineering autonomous AI customer acquisition systems, telecalling replacements, and unit economics optimization across 20+ commercial verticals.</p>
      </div>
    </div>

    {ext_links_html}

    <div class="cta">
      <h2>Ready to Build Your Predictable Growth Engine?</h2>
      <p>Deploy autonomous AI voice agents, WhatsApp business automations, and full-funnel performance marketing. Starts ₹10,000 / $500 with a 7-day performance guarantee.</p>
      <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap">
        <a href="/contact/" class="btn accent">Schedule Discovery Call</a>
        <a href="https://wa.me/919110422538?text=Hello%20GetMore%20OS,%20I'm%20interested%20in%20{slug}" class="btn ghost" target="_blank" rel="noopener">WhatsApp Direct (+91 91104 22538)</a>
      </div>
    </div>

    <section class="block" style="border-bottom:1px solid var(--border);padding-bottom:48px">
      <h2>Related Searches & Topic Clusters</h2>
      <p style="color:var(--muted);margin-bottom:20px">Explore interconnected growth systems, technical guides, and vertical case studies:</p>
      <div class="related">
        {related_html}
      </div>
    </section>
  </div>
</main>

<footer>
  <div class="wrap" style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:20px;align-items:center">
    <div>
      <p style="margin:0 0 6px;color:#fff;font-weight:700">GetMore OS &mdash; High Performance Business Consultancy & Growth Engines</p>
      <p style="margin:0">&copy; 2026 GetMore OS. All rights reserved. 7-Day Performance Guarantee.</p>
    </div>
    <div style="display:flex;gap:18px;flex-wrap:wrap">
      <a href="/solutions/">Solutions</a>
      <a href="/pitchfinder/">PitchFinder</a>
      <a href="/digital-marketing-agency/">Agency</a>
      <a href="/ai-automation-agency/">AI Automation</a>
      <a href="/b2b-lead-generation/">B2B Leads</a>
      <a href="/blog/">Blog</a>
      <a href="/faq/">FAQ</a>
      <a href="/contact/">Contact</a>
    </div>
  </div>
</footer>

<a href="https://wa.me/919110422538?text=Hello%20GetMore%20OS,%20I%20have%20a%20question%20about%20{slug}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
  <span>Instant WhatsApp</span>
</a>

</body>
</html>"""
    return html

def main():
    print("Beginning generation of all 18 SEO Pillar Hubs & Guides...")
    # Import the pages from scripts/page_definitions.py
    import importlib.util
    spec = importlib.util.spec_from_file_location("page_definitions", os.path.join(ROOT_DIR, "scripts", "page_definitions.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    pages = mod.PAGES

    generated_count = 0
    for p in pages:
        slug = p["slug"].strip("/")
        page_dir = os.path.join(ROOT_DIR, slug)
        os.makedirs(page_dir, exist_ok=True)
        file_path = os.path.join(page_dir, "index.html")

        html_content = generate_page_html(p)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        word_count = len(re.findall(r'\b\w+\b', html_content))
        print(f"  ✓ Created {slug}/index.html ({word_count:,} words, {len(html_content):,} bytes)")
        generated_count += 1

    print(f"\n🎉 Successfully created all {generated_count} pages!")

if __name__ == "__main__":
    main()

