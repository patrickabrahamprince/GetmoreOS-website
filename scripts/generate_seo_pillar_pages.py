#!/usr/bin/env python3
"""
Generate Core Master Pillar Pages & High-Intent Blog Comparison Guides for GetMore OS.
Covers 11 Pillar/Money Pages and 7 Informational/Comparison Guides.
All pages follow exact GetMore OS brand styling, E-E-A-T standards, JSON-LD schemas,
and internal linking requirements.
"""

import os
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Shared CSS styles aligned with GetMore OS brand
SHARED_CSS = """
:root{--bg:#0b0b0c;--surface:#161618;--surface-card:#1c1c20;--ink:#f4f4f5;--muted:#a1a1aa;--primary:#f4f4f5;--accent:#c6f432;--brand:#3b82f6;--border:rgba(255,255,255,0.08);--border-hover:rgba(198,244,50,0.3)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.2;font-weight:700;letter-spacing:-.02em}
h1{font-size:clamp(32px,5vw,54px);margin:.2em 0 .35em}h2{font-size:clamp(24px,3.5vw,36px);margin:2em 0 .6em;color:var(--primary)}h3{font-size:20px;margin:1.4em 0 .4em;color:#fff}
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

print("Shared CSS initialized.")

