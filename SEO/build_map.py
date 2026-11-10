import os
import csv
import re
from collections import Counter, defaultdict

csv_path = '/Users/zhaviangrsaisiddharth/.gemini/antigravity/brain/99f9360f-e6d4-4aba-b73a-fec3f3039aa0/.user_uploaded/media_1794235560753_7d363e0e.csv'
seo_dir = '/Users/zhaviangrsaisiddharth/Documents/getmore.os-website/SEO'
os.makedirs(seo_dir, exist_ok=True)

with open(csv_path, 'r', encoding='utf-16') as f:
    lines = [l.rstrip('\r\n') for l in f]

header_idx = 2
raw_data = []
for line in lines[header_idx+1:]:
    if not line.strip(): continue
    parts = line.split('\t')
    kw = parts[0].strip()
    try: vol = int(parts[2].strip())
    except: vol = 0
    comp_text = parts[5].strip() if len(parts) > 5 and parts[5].strip() else 'Low'
    try: comp_idx = int(parts[6].strip())
    except: comp_idx = 0
    bid_low = parts[7].strip() if len(parts) > 7 else '0'
    bid_high = parts[8].strip() if len(parts) > 8 else '0'
    raw_data.append({
        'kw': kw,
        'vol': vol,
        'comp_text': comp_text,
        'comp_idx': comp_idx,
        'bid_low': bid_low,
        'bid_high': bid_high
    })

print(f"Loaded {len(raw_data)} keywords.")

def get_intent(kw):
    kw_l = kw.lower()
    nav_brands = ['salesforce', 'bain & company', 'bain and company', 'tcs', 'tata consultancy', 
                  'uipath', 'datorama', 'leadfeeder', 'cinc', 'boomtown', 'marketo', 'zapier', 
                  'make.com', 'hubspot', 'zoho', 'freshworks', 'activecampaign', 'mailchimp', 
                  'clickfunnels', 'semrush', 'ahrefs', 'moz', 'hootsuite', 'sprout social', 'arthur andersen', 'merkle']
    is_nav = any(b in kw_l for b in nav_brands)
    comm_modifiers = ['vs', 'alternative', 'alternatives', 'competitor', 'competitors', 'pricing', 'review', 'reviews', 'cost', 'comparison']
    if is_nav and any(m in kw_l for m in comm_modifiers):
        return 'Commercial'
    if is_nav and not any(w in kw_l for w in ['agency', 'services', 'how', 'what', 'guide', 'best']):
        return 'Navigational'

    trans_words = ['agency', 'agencies', 'services', 'service', 'company', 'companies', 'firm', 'firms', 
                   'hire', 'buy', 'pricing', 'quote', 'packages', 'near me', 'pay per lead', 'vendor', 
                   'contractor', 'consultancy', 'consultant', 'consultants', 'specialist', 'specialists',
                   'marketing agen', 'ad firm', 'ad agency', 'pr agency', 'ppc agency']
    if any(re.search(r'\b' + re.escape(w) + r'\b', kw_l) for w in trans_words):
        return 'Transactional'

    comm_words = ['best', 'top', 'software', 'tool', 'tools', 'platform', 'platforms', 'system', 'systems', 
                  'solution', 'solutions', 'provider', 'providers', 'comparison', 'compare', 'review', 
                  'reviews', 'pricing', 'cost', 'vs', 'alternative', 'alternatives', 'lead generation', 
                  'leads for', 'lead capture', 'growth engine', 'automation tool', 'lead finder']
    if any(re.search(r'\b' + re.escape(w) + r'\b', kw_l) for w in comm_words):
        return 'Commercial'

    return 'Informational'

def get_priority(vol, comp_idx, intent):
    if vol >= 5000 and comp_idx <= 60 and intent in ['Transactional', 'Commercial']:
        return 'P0'
    elif (vol >= 5000 and intent in ['Informational', 'Navigational']) or (vol == 500 and intent in ['Transactional', 'Commercial']):
        return 'P1'
    else:
        return 'P2'

def assign_page(kw, vol, intent):
    k = kw.lower()

    # 1. Competitor / Enterprise Platforms (Informational / Comparison Blogs)
    if any(b in k for b in ['salesforce', 'datorama', 'exacttarget', 'marketing cloud', 'pardot']):
        return ('/blog/salesforce-marketing-cloud-pricing-alternatives/', 'Comparison Guide', 'New')
    if any(b in k for b in ['google cloud ai', 'open source ai', 'gartner magic quadrant', 'uipath', 'machine learning platform', 'vertex ai', 'cloud platform machine learning', 'ai learning platform', 'artificial intelligence platform', 'ai platform', 'ml platform', 'aiops', 'data science platform', 'cloud platform ml', 'aws ml', 'computer vision', 'conversation intelligence', 'machine learning', 'cdp platforms gartner', 'competitive intelligence platforms', 'mobile attribution platforms', 'customer segmentation software', 'customer research platform', 'data labeling platform']):
        return ('/blog/enterprise-ai-platforms-comparison/', 'Informational Guide', 'New')
    if any(b in k for b in ['bain & company', 'bain and company', 'tcs', 'tata consultancy', 'mckinsey', 'boston consulting', 'big 4', 'accenture', 'deloitte', 'kpmg', 'pwc', 'ernst & young', 'ey consulting', 'strategy&', 'arthur andersen', 'protiviti', 'mbb company', 'segal group']):
        return ('/blog/top-consulting-firms-comparison/', 'Comparison Guide', 'New')
    if any(b in k for b in ['linkedin sales navigator', 'sales navigator', 'zoominfo', 'apollo.io', 'lusha', 'leadfeeder', 'merkle b2b', 'dentsu merkle']):
        return ('/blog/b2b-lead-generation-strategies/', 'Informational Guide', 'New')

    # 2. PitchFinder Specific (Lead databases, lead finders, B2B lists)
    if any(w in k for w in ['lead finder', 'b2b lead finder', 'lead list', 'business leads list', 'leads database', 'b2b contact database', 'pitchfinder', 'verified leads', 'leads in bangalore']):
        return ('/pitchfinder/', 'Lead Generation Tool', 'Existing')

    # 3. Industry Verticals
    # Real estate
    if any(w in k for w in ['real estate', 'realtor', 'realty', 'property agent', 'realestate', 'housing lead', 'property lead', 'estate agent', 'cinc', 'boomtown']):
        if any(w in k for w in ['voice', 'call', 'calling', 'phone', 'receptionist']):
            return ('/ai-voice-agent-for-luxury-real-estate/', 'Industry Voice Agent', 'Existing')
        elif any(w in k for w in ['whatsapp', 'message', 'messaging']):
            return ('/whatsapp-automation-for-luxury-real-estate/', 'Industry WhatsApp', 'Existing')
        elif any(w in k for w in ['chat', 'bot', 'capture']):
            return ('/ai-chatbot-lead-capture-luxury-real-estate/', 'Industry Chatbot', 'Existing')
        else:
            return ('/real-estate-lead-generation/', 'Industry Pillar Hub', 'New')

    # Healthcare / Dental / Aesthetic / Wellness
    if any(w in k for w in ['dental', 'dentist', 'orthodont']):
        if any(w in k for w in ['voice', 'calling', 'receptionist']):
            return ('/ai-voice-agent-for-dental-clinics/', 'Industry Voice Agent', 'Existing')
        elif any(w in k for w in ['whatsapp']):
            return ('/whatsapp-automation-for-dental-clinics/', 'Industry WhatsApp', 'Existing')
        elif any(w in k for w in ['chat', 'chatbot']):
            return ('/ai-chatbot-lead-capture-dental-clinics/', 'Industry Chatbot', 'Existing')
        else:
            return ('/marketing-growth-engine-dental-clinics/', 'Industry Growth Engine', 'Existing')

    if any(w in k for w in ['aesthetic', 'dermatolog', 'cosmetic clinic', 'skincare clinic', 'plastic surge']):
        return ('/marketing-growth-engine-aesthetic-clinics/', 'Industry Growth Engine', 'Existing')

    if any(w in k for w in ['physio', 'chiropract']):
        return ('/marketing-growth-engine-physiotherapy-centres/', 'Industry Growth Engine', 'Existing')

    if any(w in k for w in ['clinic', 'doctor', 'healthcare', 'medical', 'hospital', 'patient lead']):
        if 'bangalore' in k:
            return ('/clinic-website-bangalore/', 'Local Clinic Landing', 'Existing')
        return ('/marketing-growth-engine-dental-clinics/', 'Industry Growth Engine', 'Existing')

    # Legal / Law Firm
    if any(w in k for w in ['law', 'lawyer', 'attorney', 'legal']):
        if any(w in k for w in ['voice', 'calling']):
            return ('/ai-voice-agent-for-law-firms/', 'Industry Voice Agent', 'Existing')
        elif any(w in k for w in ['whatsapp']):
            return ('/whatsapp-automation-for-law-firms/', 'Industry WhatsApp', 'Existing')
        elif any(w in k for w in ['chat', 'bot']):
            return ('/ai-chatbot-lead-capture-law-firms/', 'Industry Chatbot', 'Existing')
        else:
            return ('/marketing-growth-engine-law-firms/', 'Industry Growth Engine', 'Existing')

    # Hospitality / Hotel
    if any(w in k for w in ['hotel', 'resort', 'hospitality', 'direct booking', 'guest booking']):
        if 'booking' in k or 'direct' in k:
            return ('/hotel-direct-booking-website/', 'Direct Booking Landing', 'Existing')
        return ('/ai-voice-agent-for-boutique-hotels/', 'Industry Voice Agent', 'Existing')

    # Restaurants / Food
    if any(w in k for w in ['restaurant', 'cafe', 'food ordering', 'dining', 'catering']):
        return ('/restaurant-website-zero-commission/', 'Zero-Commission Dining', 'Existing')

    # Salons / Spas
    if any(w in k for w in ['salon', 'spa', 'barber', 'beauty parlour', 'hair salon']):
        if 'bangalore' in k:
            return ('/salon-website-bangalore/', 'Local Salon Landing', 'Existing')
        return ('/ai-voice-agent-for-salons-spas/', 'Industry Voice Agent', 'Existing')

    # Automotive / Car
    if any(w in k for w in ['car detailing', 'auto detailing', 'detailing studio']):
        return ('/ai-voice-agent-for-car-detailing-studios/', 'Industry Voice Agent', 'Existing')
    if any(w in k for w in ['car dealer', 'auto dealer', 'luxury car', 'dealership', 'automotive lead']):
        return ('/ai-voice-agent-for-luxury-car-dealerships/', 'Industry Voice Agent', 'Existing')

    # Fitness / Gym
    if any(w in k for w in ['gym', 'fitness', 'crossfit', 'personal trainer']):
        return ('/ai-voice-agent-for-fitness-gyms/', 'Industry Voice Agent', 'Existing')

    # Interior Design / Home Improvement / Contractors
    if any(w in k for w in ['interior design', 'interior decor', 'architect']):
        return ('/marketing-growth-engine-interior-designers/', 'Industry Growth Engine', 'Existing')
    if any(w in k for w in ['roofing', 'hvac', 'plumbing', 'contractor', 'remodel', 'home improvement', 'handyman', 'solar lead']):
        return ('/contractor-lead-generation/', 'Contractor Leads Hub', 'New')

    # Finance / Advisory / Wealth / Insurance
    if any(w in k for w in ['financial advis', 'wealth management', 'financial plan', 'cpa', 'accounting firm', 'insurance lead', 'tax consultant']):
        return ('/marketing-growth-engine-financial-advisory/', 'Industry Growth Engine', 'Existing')

    # B2B SaaS
    if any(w in k for w in ['saas', 'software startup', 'b2b saas', 'enterprise software marketing']):
        return ('/marketing-growth-engine-b2b-saas-startups/', 'Industry Growth Engine', 'Existing')

    # Coaching / Institutes
    if any(w in k for w in ['coaching', 'institute', 'preschool', 'daycare', 'tutoring', 'edtech']):
        return ('/marketing-growth-engine-coaching-institutes/', 'Industry Growth Engine', 'Existing')

    # Coworking
    if any(w in k for w in ['coworking', 'shared office', 'workspace']):
        return ('/marketing-growth-engine-coworking-spaces/', 'Industry Growth Engine', 'Existing')

    # D2C / Fashion / E-commerce / Retail
    if any(w in k for w in ['d2c', 'fashion brand', 'ecommerce brand', 'clothing brand', 'retail ai', 'ai in retail']):
        return ('/marketing-growth-engine-d2c-fashion-brands/', 'Industry Growth Engine', 'Existing')

    # 4. Core Channels & Capabilities
    # WhatsApp Marketing & Automation & SMS
    if any(w in k for w in ['whatsapp', 'wa bot', 'whatsapp business', 'bulk whatsapp', 'omni channel', 'sms platform', 'text blast', 'sms marketing', 'bulk sms']):
        if 'booking' in k:
            return ('/whatsapp-booking-automation/', 'WhatsApp Booking Landing', 'Existing')
        return ('/whatsapp-marketing-software/', 'WhatsApp Software Pillar', 'New')

    # Email Marketing & CRM
    if any(w in k for w in ['email marketing', 'newsletter software', 'email software', 'crm email', 'email platform', 'drip email', 'email blast', 'bulk email', 'email campaign software', 'amazon ppc management software', 'newsletter platform', 'semrush crm', 'affiliate tracking', 'affiliate software']):
        return ('/email-marketing-software/', 'Email Software Pillar', 'New')

    # Voice Agents & Calling
    if any(w in k for w in ['voice agent', 'voice bot', 'ai calling', 'ai receptionist', 'phone bot', 'telecalling', 'cold call', 'call center ai', 'answering service']):
        return ('/ai-voice-agents/', 'Voice Agents Pillar Hub', 'New')

    # Chatbots & Conversational AI
    if any(w in k for w in ['chatbot', 'chat bot', 'conversational ai', 'live chat', 'virtual assistant', 'ai chat']):
        return ('/conversational-ai-platform/', 'Conversational AI Hub', 'New')

    # SEO Services & Local SEO
    if any(w in k for w in ['seo', 'search engine optimization', 'local seo', 'seo agency', 'seo company', 'seo services', 'seo consultant', 'seo firm', 'ecommerce seo', 'search optimization', 'search engine optimisation', 'search optimisation', 'sem company']):
        if 'bangalore' in k:
            return ('/local-seo-bangalore/', 'Local SEO Landing', 'Existing')
        return ('/seo-services/', 'SEO Services Pillar Hub', 'New')

    # Social Media / SMMA / Influencer
    if any(w in k for w in ['social media', 'smma', 'influencer', 'instagram marketing', 'facebook marketing', 'tiktok marketing', 'social media agency', 'social media company']):
        if 'how' in k or 'course' in k or 'start' in k or 'what is' in k:
            return ('/blog/social-media-marketing-agency-guide/', 'Informational Guide', 'New')
        return ('/digital-marketing-agency/', 'Agency Pillar Hub', 'New')

    # Lead Generation (B2B, Demand Gen, Sales Leads)
    if any(w in k for w in ['lead generation', 'lead gen', 'leads', 'demand generation', 'demand gen', 'prospecting', 'lead capture', 'sales leads', 'b2b leads', 'leads for', 'generate leads', 'buying leads', 'pipeline generation', 'sales automation', 'b2b in demand', 'generate facebook']):
        if 'how' in k or 'strategy' in k or 'tips' in k or 'guide' in k:
            return ('/blog/b2b-lead-generation-strategies/', 'Informational Guide', 'New')
        return ('/b2b-lead-generation/', 'Lead Generation Pillar Hub', 'New')

    # AI Automation & AI Agency Services
    if any(w in k for w in ['ai automation', 'ai workflow', 'process automation', 'intelligent automation', 'intelligence automation', 'ai agency', 'ai solutions', 'rpa', 'ai consulting', 'ai and automation', 'automation and ai', 'ai in automation', 'ai for automation', 'enterprise ai', 'ai business', 'ai integration', 'ai development company', 'ai firm', 'ai operations', 'artificial intelligence solutions', 'artificial intelligence', 'aws intelligent document', 'ibm it automation', 'creative automation']):
        return ('/ai-automation-agency/', 'AI Automation Pillar Hub', 'New')

    # Business Consultancy & Strategy Advisory
    if any(w in k for w in ['consultancy', 'consulting', 'management consult', 'business consult', 'advisory firm', 'consultant', 'business advisory', 'strategy consult', 'hr consult', 'management advisory', 'business advisor', 'project management companies', 'hr companies', 'hr firms', 'startup advisory', 'naming service', 'consumer research', 'b2b research', 'qualitative research', 'research firm', 'tiger analytics']):
        return ('/business-consultancy/', 'Business Consultancy Hub', 'New')

    # Digital Marketing, Advertising, Branding, PPC, PR Agencies
    if any(w in k for w in ['marketing', 'agency', 'agencies', 'advertising', 'branding', 'ppc', 'pr agency', 'digital pr', 'facebook ads', 'google ads', 'media agency', 'creative agency', 'content agency', 'dev agency', 'creatives agency', 'ad firm', 'ecommerce agency', 'reputation management', 'programmatic advertising', 'digital media company', 'digital marketers', 'brand design', 'ad solutions', 'media solution', 'langoor digital', 'omnicom', 'mrkt solutions', 'techwyse', 'content company', 'brand management', 'publicist company', 'digital website design', 'martech solutions', 'music promotion']):
        return ('/digital-marketing-agency/', 'Agency Pillar Hub', 'New')

    if any(w in k for w in ['ai', 'lead', 'consult']):
        if 'ai' in k: return ('/ai-automation-agency/', 'AI Automation Pillar Hub', 'New')
        if 'lead' in k: return ('/b2b-lead-generation/', 'Lead Generation Pillar Hub', 'New')
        if 'consult' in k: return ('/business-consultancy/', 'Business Consultancy Hub', 'New')

    # Remaining informational queries
    return ('/faq/', 'FAQ & Knowledge Base', 'New')

# Generate KEYWORD_MAP.md
map_path = os.path.join(seo_dir, 'KEYWORD_MAP.md')
print(f"Writing keyword map to {map_path}...")

total_count = len(raw_data)
vols_stat = Counter([d['vol'] for d in raw_data])
comp_stat = Counter([d['comp_text'] for d in raw_data])
intent_stat = Counter([get_intent(d['kw']) for d in raw_data])
prio_stat = Counter()
page_stat = Counter()

processed_rows = []
for d in raw_data:
    intent = get_intent(d['kw'])
    prio = get_priority(d['vol'], d['comp_idx'], intent)
    url, ptype, status = assign_page(d['kw'], d['vol'], intent)
    prio_stat[prio] += 1
    page_stat[(url, ptype, status)] += 1
    
    diff_str = f"{d['comp_text']} ({d['comp_idx']})"
    clean_kw = d['kw'].replace('|', '/')
    processed_rows.append({
        'kw': clean_kw,
        'vol': d['vol'],
        'diff': diff_str,
        'intent': intent,
        'url': url,
        'status': status,
        'ptype': ptype,
        'prio': prio
    })

prio_order = {'P0': 0, 'P1': 1, 'P2': 2}
processed_rows.sort(key=lambda x: (prio_order[x['prio']], -x['vol'], x['kw']))

with open(map_path, 'w', encoding='utf-8') as f:
    f.write('# GetMore OS — Master SEO Keyword Map\n\n')
    f.write('> **Dataset Overview**: 6,540 total keywords analyzed from Google Keyword Planner report (`Keyword_Stats_2026-11-09_at_20_03_59.csv`). Zero keywords omitted. Every single keyword is mapped to an assigned existing page or dedicated new pillar / cluster URL.\n\n')
    
    f.write('## 1. Executive Summary & Macro Metrics\n\n')
    f.write(f'- **Total Search Queries Mapped**: {total_count:,}\n')
    f.write(f'- **Total Monthly Search Volume Represented**: {sum([d["vol"] for d in raw_data]):,} searches/month\n')
    f.write(f'- **Unique Assigned URLs**: {len(page_stat)} URLs (Covering Core Pillars, Money Pages, Programmatic Industry Verticals & Comparison Hubs)\n\n')
    
    f.write('### Priority Breakdown\n\n')
    f.write('| Priority | Definition | Keyword Count | % of Total |\n')
    f.write('|---|---|---|---|\n')
    f.write(f'| **P0** | High Volume (>=5,000) + Low/Med KD (<=60) + Transactional / Commercial | {prio_stat["P0"]:,} | {prio_stat["P0"]/total_count*100:.1f}% |\n')
    f.write(f'| **P1** | High Volume Informational / Navigational + Mid-Volume (500) Transactional / Commercial | {prio_stat["P1"]:,} | {prio_stat["P1"]/total_count*100:.1f}% |\n')
    f.write(f'| **P2** | Long-tail / Low Volume (50 & 0 vol) Supporting Queries | {prio_stat["P2"]:,} | {prio_stat["P2"]/total_count*100:.1f}% |\n\n')
    
    f.write('### Search Intent Distribution\n\n')
    f.write('| Search Intent | Keyword Count | % of Total | Strategic Action |\n')
    f.write('|---|---|---|---|\n')
    f.write(f'| **Transactional** | {intent_stat["Transactional"]:,} | {intent_stat["Transactional"]/total_count*100:.1f}% | Direct money pages, agency landing pages, conversion funnels, transparent pricing CTA |\n')
    f.write(f'| **Commercial** | {intent_stat["Commercial"]:,} | {intent_stat["Commercial"]/total_count*100:.1f}% | Software/solution comparisons, platform feature grids, social proof, case studies |\n')
    f.write(f'| **Informational** | {intent_stat["Informational"]:,} | {intent_stat["Informational"]/total_count*100:.1f}% | Comprehensive pillar guides, FAQs, how-to tutorials, framework explanations |\n')
    f.write(f'| **Navigational** | {intent_stat["Navigational"]:,} | {intent_stat["Navigational"]/total_count*100:.1f}% | Competitor alternative guides (Salesforce, UiPath, MBB, Bain) redirecting interest to GetMore OS |\n\n')

    f.write('## 2. Topic Clusters & Target URL Architecture\n\n')
    f.write('| Assigned URL | Page Type | Status | Keyword Count | Total Volume | Primary Keyword Target |\n')
    f.write('|---|---|---|---|---|---|\n')
    
    cluster_metrics = defaultdict(lambda: {'count': 0, 'vol': 0, 'ptype': '', 'status': ''})
    for r in processed_rows:
        u = r['url']
        cluster_metrics[u]['count'] += 1
        cluster_metrics[u]['vol'] += r['vol']
        cluster_metrics[u]['ptype'] = r['ptype']
        cluster_metrics[u]['status'] = r['status']
    
    sorted_clusters = sorted(cluster_metrics.items(), key=lambda x: (x[1]['vol'], x[1]['count']), reverse=True)
    for u, m in sorted_clusters:
        top_kw = [r['kw'] for r in processed_rows if r['url'] == u][0]
        f.write(f'| `{u}` | {m["ptype"]} | **{m["status"]}** | {m["count"]:,} | {m["vol"]:,} | `{top_kw}` |\n')
    
    f.write('\n## 3. Site Architecture & Technical SEO Audit Findings\n\n')
    f.write('### Current Strengths:\n')
    f.write('- Robust programmatic matrix: 20 distinct industries x 5 service categories (100 landing pages) already established with clean semantic HTML.\n')
    f.write('- Modern, responsive UI with Tailwind CSS and dark high-conversion branding.\n')
    f.write('- Fully configured AI crawler allowances in `robots.txt` (GPTBot, ClaudeBot, PerplexityBot, Google-Extended).\n\n')
    
    f.write('### Critical Gaps & Cannibalization Risks Identified:\n')
    f.write('1. **Duplicate PitchFinder URLs**: `pitchfinder.html` and `pitchfinder/index.html` duplicate content and title tags. Fix: Set canonical of `pitchfinder.html` to `https://getmoreos.in/pitchfinder/`.\n')
    f.write('2. **Cannibalization in Calling vs Voice Agent Pages**: For each industry, `ai-voice-agent-for-[industry]` and `inbound-outbound-ai-calling-[industry]` target the same search intent. Fix: Cross-link with distinct semantic focus (Inbound Autonomous Reception vs Outbound Cold Reactivation/Lead Qualification) and establish clear parent-child topical links.\n')
    f.write('3. **Missing Master Pillar Hubs**: Massive high-volume terms (`digital marketing agency` - 50k, `ai automation agency` - 5k, `b2b lead generation` - 5k, `email marketing software` - 50k, `real estate leads` - 5k) currently have NO dedicated master hubs. Fix: Create dedicated pillar pages with internal links out to vertical industry landing pages.\n')
    f.write('4. **Zero Coverage for Competitor / Alternative Queries**: 700+ high-value keywords search for Salesforce Marketing Cloud, UiPath, Big 4 consulting, and enterprise AI platforms. Fix: Create high-intent comparison and alternative guides under `/blog/` to siphon this organic traffic into GetMore OS service inquiries.\n\n')
    
    f.write('## 4. Master Keyword Mapping Table (All 6,540 Keywords)\n\n')
    f.write('| Keyword | Volume | Difficulty | Intent | Assigned URL (existing or new) | Page Type | Priority (P0/P1/P2) |\n')
    f.write('|---|---|---|---|---|---|---|\n')
    for r in processed_rows:
        f.write(f"| {r['kw']} | {r['vol']} | {r['diff']} | {r['intent']} | `{r['url']}` ({r['status'].lower()}) | {r['ptype']} | {r['prio']} |\n")

print("Master Keyword Map generated successfully!")

