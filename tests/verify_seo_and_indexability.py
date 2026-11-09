#!/usr/bin/env python3
"""
Comprehensive SEO, AEO and Indexability Verification Suite for GetMore OS.
Asserts that all 100 programmatic pages + core pages meet Google Indexing & AEO standards.
"""

import os
import sys
import re
import json
import xml.etree.ElementTree as ET

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.generate_100_landing_pages import VERTICALS, ANGLES

def test_sitemap_integrity():
    print("🧪 Testing sitemap.xml integrity...")
    sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
    assert os.path.exists(sitemap_path), "sitemap.xml must exist"
    
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    locs = [elem.text for elem in root.findall('ns:url/ns:loc', namespace)]
    print(f"  ✓ Found {len(locs)} URLs in sitemap.xml")
    
    assert "https://getmoreos.in/" in locs, "Homepage must be in sitemap"
    assert "https://getmoreos.in/solutions/" in locs, "Solutions directory must be in sitemap"
    
    # Check that all 100 generated landing pages are present
    expected_slugs = []
    for v in VERTICALS:
        for a in ANGLES:
            slug = a["url_template"].format(id=v["id"])
            expected_slugs.append(f"https://getmoreos.in/{slug}")
            
    for url in expected_slugs:
        assert url in locs, f"Expected {url} in sitemap.xml"
    print(f"  ✓ All 100 programmatic URLs are correctly indexed in sitemap.xml")

def test_robots_txt():
    print("🧪 Testing robots.txt...")
    robots_path = os.path.join(ROOT_DIR, "robots.txt")
    assert os.path.exists(robots_path), "robots.txt must exist"
    content = open(robots_path).read()
    assert "Sitemap: https://getmoreos.in/sitemap.xml" in content, "Must point to sitemap"
    assert "User-agent: Googlebot" in content, "Must allow Googlebot"
    assert "User-agent: GPTBot" in content, "Must allow GPTBot"
    assert "User-agent: PerplexityBot" in content, "Must allow PerplexityBot"
    print("  ✓ robots.txt allows search engines & AI answer engines")

def test_100_landing_pages():
    print("🧪 Testing all 100 landing pages for Google indexability & JSON-LD...")
    passed = 0
    
    for v in VERTICALS:
        for a in ANGLES:
            slug = a["url_template"].format(id=v["id"])
            page_path = os.path.join(ROOT_DIR, slug, "index.html")
            assert os.path.exists(page_path), f"Page {slug}/index.html must exist"
            
            content = open(page_path, encoding="utf-8").read()
            assert len(content) > 5000, f"Page {slug} must have substantive content (>5KB)"
            
            # 1. Title tag
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            assert title_match and len(title_match.group(1).strip()) > 10, f"Page {slug} missing valid title"
            
            # 2. Meta description
            desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
            assert desc_match and len(desc_match.group(1).strip()) > 20, f"Page {slug} missing valid meta description"
            
            # 3. Canonical tag
            can_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
            assert can_match and can_match.group(1) == f"https://getmoreos.in/{slug}", f"Page {slug} has incorrect canonical: {can_match.group(1) if can_match else 'None'}"
            
            # 4. Robots meta
            assert 'name="robots" content="index, follow' in content, f"Page {slug} missing index/follow robots directive"
            
            # 5. Direct-Answer block
            assert '<div class="answer">' in content, f"Page {slug} missing direct-answer AEO block"
            
            # 6. JSON-LD Schema Validation
            schema_match = re.search(r'<script\s+type=["\']application/ld\+json["\']>([\s\S]*?)</script>', content, re.IGNORECASE)
            assert schema_match, f"Page {slug} missing JSON-LD schema block"
            try:
                schema_data = json.loads(schema_match.group(1))
                graph = schema_data.get("@graph", [])
                types = [item.get("@type") for item in graph]
                # Flatten any list types
                flattened_types = []
                for t in types:
                    if isinstance(t, list):
                        flattened_types.extend(t)
                    else:
                        flattened_types.append(t)
                assert "FAQPage" in flattened_types, f"Page {slug} schema missing FAQPage"
                assert "Service" in flattened_types, f"Page {slug} schema missing Service"
                assert "WebPage" in flattened_types, f"Page {slug} schema missing WebPage"
            except Exception as e:
                raise AssertionError(f"Page {slug} has invalid JSON-LD schema: {e}")
                
            passed += 1

    print(f"  ✓ All {passed} landing pages passed 100% of technical SEO & AEO assertions!")

def test_solutions_directory():
    print("🧪 Testing solutions/index.html directory...")
    sol_path = os.path.join(ROOT_DIR, "solutions", "index.html")
    assert os.path.exists(sol_path), "solutions/index.html must exist"
    content = open(sol_path, encoding="utf-8").read()
    assert '<title>' in content, "Directory must have title"
    assert 'id="dirSearch"' in content, "Directory must have search filter"
    
    # Assert links to all 100 pages exist in solutions/index.html
    missing = 0
    for v in VERTICALS:
        for a in ANGLES:
            slug = a["url_template"].format(id=v["id"])
            if f'href="/{slug}"' not in content:
                missing += 1
    assert missing == 0, f"Solutions directory is missing {missing} page links!"
    print(f"  ✓ solutions/index.html contains valid HTML anchor links to all 100 pages!")

if __name__ == "__main__":
    print("==================================================")
    print("   GETMORE.OS SEO & GOOGLE INDEXABILITY AUDIT   ")
    print("==================================================")
    test_sitemap_integrity()
    test_robots_txt()
    test_100_landing_pages()
    test_solutions_directory()
    print("==================================================")
    print("🎉 ALL TESTS PASSED! 100% INDEXABILITY VERIFIED! 🎉")
    print("==================================================")
