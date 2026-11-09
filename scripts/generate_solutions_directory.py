#!/usr/bin/env python3
"""
Generate a comprehensive HTML Solutions Directory (solutions/index.html)
linking to all 100 programmatic landing pages, organized by industry vertical.
This guarantees Googlebot and web crawlers can discover every page through standard HTML links.
"""

import os
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOLUTIONS_DIR = os.path.join(ROOT_DIR, "solutions")
os.makedirs(SOLUTIONS_DIR, exist_ok=True)

from generate_100_landing_pages import VERTICALS, ANGLES

def main():
    print("🏗️ Building solutions/index.html directory...")

    # Group verticals by broad sector
    sectors = {
        "Healthcare & Wellness": ["dental-clinics", "aesthetic-clinics", "physiotherapy-centres", "veterinary-pet-clinics", "salons-spas"],
        "Automotive & High-Ticket": ["luxury-car-dealerships", "car-detailing-studios"],
        "Real Estate, Spaces & Architecture": ["luxury-real-estate", "interior-designers", "coworking-spaces"],
        "Hospitality, Dining & Stays": ["restaurants-cafes", "boutique-hotels"],
        "Professional & Financial Services": ["law-firms", "financial-advisory", "b2b-saas-startups"],
        "Education, Academies & Childcare": ["coaching-institutes", "preschools-daycares"],
        "Luxury Events & D2C Brands": ["wedding-event-planners", "d2c-fashion-brands", "fitness-gyms"]
    }

    v_map = {v["id"]: v for v in VERTICALS}

    sections_html = ""

    total_links = 0
    for sector_name, v_ids in sectors.items():
        cards_html = ""
        for v_id in v_ids:
            if v_id not in v_map:
                continue
            v = v_map[v_id]
            
            links_list_html = ""
            for a in ANGLES:
                slug = a["url_template"].format(id=v["id"])
                # Extract clean anchor label
                if a["key"] == "ai-voice-agent-for":
                    label = "📞 24/7 AI Voice Agent"
                elif a["key"] == "whatsapp-automation-for":
                    label = "💬 WhatsApp Bot Automation"
                elif a["key"] == "inbound-outbound-calling":
                    label = "⚡ Inbound/Outbound AI Calling"
                elif a["key"] == "ai-chatbot-lead-capture":
                    label = "🤖 AI Website Chatbot"
                elif a["key"] == "marketing-growth-engine":
                    label = "🚀 Marketing & Growth Engine"
                else:
                    label = a["title_template"].format(name=v["name"], short_name=v["short_name"]).split("|")[0].strip()

                links_list_html += f'<li><a href="/{slug}">{label} →</a></li>\n'
                total_links += 1

            cards_html += f"""
            <div class="v-card">
              <div class="v-cat">{v['category']}</div>
              <h3>{v['name']}</h3>
              <p>{v['pain_points']}</p>
              <ul class="v-links">
                {links_list_html}
              </ul>
            </div>
            """

        sections_html += f"""
        <section class="sector-block">
          <h2>{sector_name}</h2>
          <div class="v-grid">
            {cards_html}
          </div>
        </section>
        """

    html = f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Voice Agents, WhatsApp Bot Automations & Growth Solutions Directory | GetMore OS</title>
<meta name="description" content="Explore 100 specialized AI automation, voice agent, WhatsApp bot, and performance marketing growth solutions tailored across 20+ industries. Starts at ₹10K.">
<link rel="canonical" href="https://getmoreos.in/solutions/">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GetMore OS">
<meta property="og:title" content="AI Voice Agents & WhatsApp Bot Automations Directory | GetMore OS">
<meta property="og:description" content="Explore 100 specialized AI automation, voice agent, WhatsApp bot, and performance marketing growth solutions tailored across 20+ industries.">
<meta property="og:url" content="https://getmoreos.in/solutions/">
<meta property="og:image" content="https://getmoreos.in/og-image.jpg">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0c">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0b0b0c;--surface:#161618;--ink:#f4f4f5;--muted:#a1a1aa;--primary:#f4f4f5;--accent:#c6f432;--brand:#3b82f6}}
*{{box-sizing:border-box}}html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
h1,h2,h3{{font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.2;font-weight:700;letter-spacing:-.02em}}
h1{{font-size:clamp(30px,4.5vw,48px);margin:.2em 0 .35em}}h2{{font-size:clamp(22px,3vw,30px);margin:2em 0 .8em;color:var(--accent)}}h3{{font-size:18px;margin:0 0 .4em;color:#fff}}
a{{color:inherit;text-decoration:none}}
.wrap{{max-width:1160px;margin:0 auto;padding:0 20px}}
header.site{{border-bottom:1px solid rgba(255,255,255,0.08);background:rgba(11,11,12,0.85);backdrop-filter:blur(12px);position:sticky;top:0;z-index:50}}
header.site .wrap{{display:flex;justify-content:space-between;align-items:center;height:64px}}
.logo{{font-family:'Space Grotesk',sans-serif;font-size:20px;font-weight:700;display:flex;align-items:center;gap:8px}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:999px;background:var(--primary);color:var(--bg);font-weight:600;font-size:13px;border:1px solid var(--primary);transition:all .2s ease}}
.btn:hover{{opacity:.9}}
.btn.accent{{background:var(--accent);border-color:var(--accent);color:#000}}
.hero{{padding:40px 0 20px;text-align:center}}
.eyebrow{{color:var(--accent);text-transform:uppercase;letter-spacing:.14em;font-size:12px;font-weight:700;margin-bottom:12px}}
.answer{{font-size:17px;color:#cbd5e1;max-width:760px;margin:0 auto 28px;line-height:1.6}}
.search-box{{max-width:480px;margin:0 auto 40px;position:relative}}
.search-box input{{width:100%;padding:14px 20px;border-radius:999px;border:1px solid rgba(255,255,255,0.15);background:var(--surface);color:#fff;font-size:15px;outline:none}}
.search-box input:focus{{border-color:var(--accent)}}
.sector-block{{margin-bottom:50px}}
.v-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px}}
.v-card{{background:var(--surface);border-radius:14px;padding:24px;border:1px solid rgba(255,255,255,0.06);display:flex;flex-direction:column}}
.v-cat{{font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-bottom:8px}}
.v-card p{{margin:0 0 16px;font-size:13px;color:#94a3b8;flex-grow:1}}
.v-links{{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px;border-top:1px solid rgba(255,255,255,0.06);padding-top:14px}}
.v-links a{{font-size:13px;font-weight:600;color:var(--primary);display:block;padding:4px 0;transition:color .2s}}
.v-links a:hover{{color:var(--accent)}}
footer{{padding:40px 0 80px;font-size:13px;color:var(--muted);border-top:1px solid rgba(255,255,255,0.08);margin-top:60px}}
</style>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": ["Organization", "ProfessionalService"],
      "@id": "https://getmoreos.in/#organization",
      "name": "GetMore OS",
      "url": "https://getmoreos.in/",
      "telephone": "+91-9738397933",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "#343, 9th Main, 22nd Cross, HSR Layout 7th Sector",
        "addressLocality": "Bengaluru",
        "addressRegion": "Karnataka",
        "postalCode": "560102",
        "addressCountry": "IN"
      }}
    }},
    {{
      "@type": "CollectionPage",
      "@id": "https://getmoreos.in/solutions/#webpage",
      "url": "https://getmoreos.in/solutions/",
      "name": "AI Voice Agents, WhatsApp Bot Automations & Growth Solutions Directory | GetMore OS",
      "description": "Comprehensive directory of 100 specialized AI automation, voice agent, WhatsApp bot, and marketing engines across 20 industries."
    }}
  ]
}}
</script>
</head>
<body>

<header class="site">
  <div class="wrap">
    <a href="/" class="logo">
      <span style="display:inline-block;width:10px;height:10px;background:#c6f432;border-radius:50%"></span>
      GetMore OS
    </a>
    <div>
      <a href="https://wa.me/919738397933?text=Hi%2C%20I%20would%20like%20to%20consult%20on%20AI%20automation%20for%20my%20business." target="_blank" class="btn accent">Consult on WhatsApp</a>
    </div>
  </div>
</header>

<main class="wrap">
  <div class="hero">
    <div class="eyebrow">Enterprise &amp; Local Business Directory</div>
    <h1>Industry Growth &amp; AI Automation Solutions</h1>
    <div class="answer">
      Explore 100 dedicated AI automation engines across 20 high-value sectors. Every solution integrates 24/7 Inbound &amp; Outbound AI Voice Agents, official WhatsApp Business bot flows, and performance marketing backed by a risk-free 7-day results guarantee starting at ₹10,000 INR.
    </div>

    <div class="search-box">
      <input type="text" id="dirSearch" placeholder="Filter by industry (e.g. dental, car, real estate)..." oninput="filterCards(this.value)">
    </div>
  </div>

  <div id="sectorsContainer">
    {sections_html}
  </div>
</main>

<footer>
  <div class="wrap" style="display:flex;flex-wrap:wrap;justify-content:space-between;gap:24px">
    <div>
      <strong style="color:#fff;font-size:15px;display:block;margin-bottom:8px">GetMore OS (getmoreos.in)</strong>
      <p style="margin:0;max-width:380px">High Performance Business Consultancy Firm &amp; Growth Engine. #343, 9th Main, 22nd Cross, HSR Layout 7th Sector, Bengaluru 560102.</p>
    </div>
    <div>
      <strong style="color:#fff;font-size:14px;display:block;margin-bottom:8px">Get In Touch</strong>
      <p style="margin:0">Direct Phone: +91-9738397933<br>WhatsApp: +91-9738397933<br>Strategic Marketing Partner: <a href="https://www.theaxiomgrid.com" target="_blank" rel="noopener">The Axiom Grid</a></p>
    </div>
  </div>
</footer>

<script>
function filterCards(query) {{
  const q = query.toLowerCase().trim();
  const cards = document.querySelectorAll('.v-card');
  cards.forEach(card => {{
    const text = card.textContent.toLowerCase();
    card.style.display = text.includes(q) ? 'flex' : 'none';
  }});
}}
</script>

</body>
</html>
"""

    out_file = os.path.join(SOLUTIONS_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ solutions/index.html generated with {total_links} indexed solution links!")

if __name__ == "__main__":
    main()

