import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
seo_dir = os.path.join(ROOT_DIR, "SEO")
linking_map_path = os.path.join(seo_dir, "INTERNAL_LINKING_MAP.md")

content = """# GetMore OS — Master Internal Linking & Topic Cluster Architecture

> **Architecture Overview**: A high-performance internal linking mesh based on the **Hub & Spoke (Topic Cluster)** model. Every master pillar hub links contextually to its satellite industry cluster pages, and each satellite page links back to the central pillar using keyword-rich anchor text. 

---

## 1. Visual Topology & Linking Flow

```
                      +-----------------------------+
                      |     Homepage (Root Node)    |
                      |    https://getmoreos.in/    |
                      +--------------+--------------+
                                     |
             +-----------------------+-----------------------+
             |                                               |
+------------v------------+                     +------------v------------+
|  Solutions Directory    |                     |  PitchFinder Tool       |
|  /solutions/            |                     |  /pitchfinder/          |
+------------+------------+                     +-------------------------+
             |
             +-----------------------+-----------------------+-----------------------+
             |                       |                       |                       |
+------------v------------+ +--------v-------------+ +-------v--------------+ +------v---------------+
| Digital Marketing       | | AI Automation Agency | | B2B Lead Generation  | | Business Consultancy |
| /digital-marketing-     | | /ai-automation-      | | /b2b-lead-           | | /business-           |
| agency/                 | | agency/              | | generation/          | | consultancy/         |
+------------+------------+ +--------+-------------+ +-------+--------------+ +------+---------------+
             |                       |                       |                       |
   (20 Growth Engine Pages) (Voice & Chatbot Hubs) (PitchFinder & Email)  (Top Consulting Firms)
```

---

## 2. Topic Cluster Mesh & Internal Link Directory

### Cluster 1: Digital Marketing & Paid Acquisition Pillar
- **Central Pillar Hub**: [`/digital-marketing-agency/`](https://getmoreos.in/digital-marketing-agency/)
- **Primary Anchor Text**: `digital marketing agency`, `full-funnel marketing agency`, `performance marketing engine`
- **Outbound Contextual Links from Pillar**:
  - [`/ai-automation-agency/`](https://getmoreos.in/ai-automation-agency/) &mdash; Anchor: *AI Automation Agency Solutions*
  - [`/b2b-lead-generation/`](https://getmoreos.in/b2b-lead-generation/) &mdash; Anchor: *B2B Lead Generation Services*
  - [`/seo-services/`](https://getmoreos.in/seo-services/) &mdash; Anchor: *Full-Scale SEO Marketing Services*
  - [`/real-estate-lead-generation/`](https://getmoreos.in/real-estate-lead-generation/) &mdash; Anchor: *Luxury Real Estate Growth Engine*
  - [`/solutions/`](https://getmoreos.in/solutions/) &mdash; Anchor: *Directory of 100 Industry Solutions*
- **Spoke / Satellite Pages Linking Back to Pillar**:
  - All 20 `marketing-growth-engine-[industry]/` pages link back to `/digital-marketing-agency/`
  - [`/blog/social-media-marketing-agency-guide/`](https://getmoreos.in/blog/social-media-marketing-agency-guide/)
  - [`/solutions/index.html`](https://getmoreos.in/solutions/)

---

### Cluster 2: AI Automation & Intelligent Workflows Pillar
- **Central Pillar Hub**: [`/ai-automation-agency/`](https://getmoreos.in/ai-automation-agency/)
- **Primary Anchor Text**: `ai automation agency`, `ai workflow automation`, `enterprise ai automation`
- **Outbound Contextual Links from Pillar**:
  - [`/ai-voice-agents/`](https://getmoreos.in/ai-voice-agents/) &mdash; Anchor: *Autonomous AI Voice Agents*
  - [`/conversational-ai-platform/`](https://getmoreos.in/conversational-ai-platform/) &mdash; Anchor: *Enterprise Conversational AI Platform*
  - [`/whatsapp-marketing-software/`](https://getmoreos.in/whatsapp-marketing-software/) &mdash; Anchor: *Official WhatsApp Marketing Software*
  - [`/b2b-lead-generation/`](https://getmoreos.in/b2b-lead-generation/) &mdash; Anchor: *B2B Lead Generation Pipeline*
  - [`/blog/enterprise-ai-platforms-comparison/`](https://getmoreos.in/blog/enterprise-ai-platforms-comparison/) &mdash; Anchor: *Enterprise AI Platforms Comparison*
- **Spoke / Satellite Pages Linking Back to Pillar**:
  - [`/ai-voice-agents/`](https://getmoreos.in/ai-voice-agents/)
  - [`/conversational-ai-platform/`](https://getmoreos.in/conversational-ai-platform/)
  - [`/whatsapp-marketing-software/`](https://getmoreos.in/whatsapp-marketing-software/)
  - [`/faq/`](https://getmoreos.in/faq/)

---

### Cluster 3: B2B Lead Generation & Sales Prospecting Pillar
- **Central Pillar Hub**: [`/b2b-lead-generation/`](https://getmoreos.in/b2b-lead-generation/)
- **Primary Anchor Text**: `b2b lead generation`, `lead generation company`, `b2b sales pipeline`
- **Outbound Contextual Links from Pillar**:
  - [`/pitchfinder/`](https://getmoreos.in/pitchfinder/) &mdash; Anchor: *Search PitchFinder B2B Leads Database*
  - [`/blog/b2b-lead-generation-strategies/`](https://getmoreos.in/blog/b2b-lead-generation-strategies/) &mdash; Anchor: *LinkedIn Sales Navigator & Prospecting Playbook*
  - [`/email-marketing-software/`](https://getmoreos.in/email-marketing-software/) &mdash; Anchor: *Enterprise Email Marketing Software*
  - [`/digital-marketing-agency/`](https://getmoreos.in/digital-marketing-agency/) &mdash; Anchor: *Full-Funnel Digital Marketing Agency*
- **Spoke / Satellite Pages Linking Back to Pillar**:
  - [`/pitchfinder/`](https://getmoreos.in/pitchfinder/) & `pitchfinder.html`
  - [`/blog/b2b-lead-generation-strategies/`](https://getmoreos.in/blog/b2b-lead-generation-strategies/)
  - [`/contractor-lead-generation/`](https://getmoreos.in/contractor-lead-generation/)
  - [`/real-estate-lead-generation/`](https://getmoreos.in/real-estate-lead-generation/)

---

### Cluster 4: Business Consultancy & Advisory Pillar
- **Central Pillar Hub**: [`/business-consultancy/`](https://getmoreos.in/business-consultancy/)
- **Primary Anchor Text**: `business consultancy`, `management consulting firm`, `growth advisory`
- **Outbound Contextual Links from Pillar**:
  - [`/blog/top-consulting-firms-comparison/`](https://getmoreos.in/blog/top-consulting-firms-comparison/) &mdash; Anchor: *Top Consulting Firms Comparison*
  - [`/digital-marketing-agency/`](https://getmoreos.in/digital-marketing-agency/) &mdash; Anchor: *Full-Funnel Digital Marketing Agency*
  - [`/ai-automation-agency/`](https://getmoreos.in/ai-automation-agency/) &mdash; Anchor: *Enterprise AI Automation Agency*
  - [`/b2b-lead-generation/`](https://getmoreos.in/b2b-lead-generation/) &mdash; Anchor: *B2B Lead Generation Pipeline*
- **Spoke / Satellite Pages Linking Back to Pillar**:
  - [`/index.html`](https://getmoreos.in/)
  - [`/blog/top-consulting-firms-comparison/`](https://getmoreos.in/blog/top-consulting-firms-comparison/)
  - [`/faq/`](https://getmoreos.in/faq/)

---

### Cluster 5: SEO & Answer Engine Optimization (AEO) Pillar
- **Central Pillar Hub**: [`/seo-services/`](https://getmoreos.in/seo-services/)
- **Primary Anchor Text**: `seo marketing`, `search engine optimization seo services`, `best seo company`
- **Outbound Contextual Links from Pillar**:
  - [`/local-seo-bangalore/`](https://getmoreos.in/local-seo-bangalore/) &mdash; Anchor: *Local SEO Services in Bangalore*
  - [`/digital-marketing-agency/`](https://getmoreos.in/digital-marketing-agency/) &mdash; Anchor: *Full-Funnel Digital Marketing Agency*
  - [`/b2b-lead-generation/`](https://getmoreos.in/b2b-lead-generation/) &mdash; Anchor: *B2B Lead Generation Solutions*
  - [`/solutions/`](https://getmoreos.in/solutions/) &mdash; Anchor: *Explore 100 Industry Solutions*
- **Spoke / Satellite Pages Linking Back to Pillar**:
  - [`/local-seo-bangalore/`](https://getmoreos.in/local-seo-bangalore/)
  - [`/digital-marketing-agency/`](https://getmoreos.in/digital-marketing-agency/)

---

### Cluster 6: Software & Technology Platforms (Email & WhatsApp)
- **Email Hub**: [`/email-marketing-software/`](https://getmoreos.in/email-marketing-software/)
  - Links to: [`/blog/salesforce-marketing-cloud-pricing-alternatives/`](https://getmoreos.in/blog/salesforce-marketing-cloud-pricing-alternatives/), [`/whatsapp-marketing-software/`](https://getmoreos.in/whatsapp-marketing-software/), [`/b2b-lead-generation/`](https://getmoreos.in/b2b-lead-generation/)
- **WhatsApp Hub**: [`/whatsapp-marketing-software/`](https://getmoreos.in/whatsapp-marketing-software/)
  - Links to: [`/whatsapp-booking-automation/`](https://getmoreos.in/whatsapp-booking-automation/), all 20 `whatsapp-automation-for-[industry]/` pages, [`/ai-voice-agents/`](https://getmoreos.in/ai-voice-agents/)

---

### Cluster 7: Telephony & Autonomous Voice AI
- **Voice Agent Hub**: [`/ai-voice-agents/`](https://getmoreos.in/ai-voice-agents/)
  - Parent hub linking down to all 20 specialized industry voice agent landers:
    - [`/ai-voice-agent-for-dental-clinics/`](https://getmoreos.in/ai-voice-agent-for-dental-clinics/)
    - [`/ai-voice-agent-for-aesthetic-clinics/`](https://getmoreos.in/ai-voice-agent-for-aesthetic-clinics/)
    - [`/ai-voice-agent-for-luxury-real-estate/`](https://getmoreos.in/ai-voice-agent-for-luxury-real-estate/)
    - [`/ai-voice-agent-for-law-firms/`](https://getmoreos.in/ai-voice-agent-for-law-firms/)
    - [`/ai-voice-agent-for-luxury-car-dealerships/`](https://getmoreos.in/ai-voice-agent-for-luxury-car-dealerships/)
    - *(and 15 other vertical industry pages)*
  - Satellite pages link back to `/ai-voice-agents/` and `/solutions/`

---

### Cluster 8: Conversational AI & Chatbots
- **Conversational AI Hub**: [`/conversational-ai-platform/`](https://getmoreos.in/conversational-ai-platform/)
  - Parent hub linking down to all 20 specialized industry chatbot landers:
    - [`/ai-chatbot-lead-capture-dental-clinics/`](https://getmoreos.in/ai-chatbot-lead-capture-dental-clinics/)
    - [`/ai-chatbot-lead-capture-luxury-real-estate/`](https://getmoreos.in/ai-chatbot-lead-capture-luxury-real-estate/)
    - [`/ai-chatbot-lead-capture-law-firms/`](https://getmoreos.in/ai-chatbot-lead-capture-law-firms/)
    - *(and 17 other vertical chatbot pages)*

---

### Cluster 9: Industry Verticals (Real Estate & Contractors)
- **Real Estate Hub**: [`/real-estate-lead-generation/`](https://getmoreos.in/real-estate-lead-generation/)
  - Links to: [`/ai-voice-agent-for-luxury-real-estate/`](https://getmoreos.in/ai-voice-agent-for-luxury-real-estate/), [`/whatsapp-automation-for-luxury-real-estate/`](https://getmoreos.in/whatsapp-automation-for-luxury-real-estate/), [`/digital-marketing-agency/`](https://getmoreos.in/digital-marketing-agency/)
- **Contractor Hub**: [`/contractor-lead-generation/`](https://getmoreos.in/contractor-lead-generation/)
  - Links to: [`/b2b-lead-generation/`](https://getmoreos.in/b2b-lead-generation/), [`/digital-marketing-agency/`](https://getmoreos.in/digital-marketing-agency/), [`/ai-automation-agency/`](https://getmoreos.in/ai-automation-agency/)

---

### Cluster 10: Research, Comparison Guides & Knowledge Base
- **Blog & Insights Directory**: [`/blog/`](https://getmoreos.in/blog/)
  - Links to all research articles:
    - [`/blog/salesforce-marketing-cloud-pricing-alternatives/`](https://getmoreos.in/blog/salesforce-marketing-cloud-pricing-alternatives/)
    - [`/blog/enterprise-ai-platforms-comparison/`](https://getmoreos.in/blog/enterprise-ai-platforms-comparison/)
    - [`/blog/top-consulting-firms-comparison/`](https://getmoreos.in/blog/top-consulting-firms-comparison/)
    - [`/blog/b2b-lead-generation-strategies/`](https://getmoreos.in/blog/b2b-lead-generation-strategies/)
    - [`/blog/social-media-marketing-agency-guide/`](https://getmoreos.in/blog/social-media-marketing-agency-guide/)
- **Master FAQ Knowledge Hub**: [`/faq/`](https://getmoreos.in/faq/)
  - Contains 19 high-intent People Also Ask accordion Q&As, linking back to every core pillar hub.

---

## 3. Link Equity Distribution Rules

1. **Zero Orphan Pages**: Every page in the domain has at least 3 inbound contextual links from either the Homepage, Solutions directory, parent pillar, or related cluster articles.
2. **Descriptive Anchor Text**: No generic 'click here' or 'learn more' links. Anchors explicitly contain target keyword phrases (e.g. `b2b lead generation services`, `ai voice agents for dental clinics`).
3. **Canonical Self-References**: Every page explicitly defines its own canonical URL to prevent parameter-based duplication.
4. **Clean Slugs**: Strictly lowercase, hyphen-separated, trailing slash URLs (`/digital-marketing-agency/`, `/b2b-lead-generation/`).
"""

with open(linking_map_path, "w", encoding="utf-8") as f:
    f.write(content)

print("INTERNAL_LINKING_MAP.md generated successfully!")

