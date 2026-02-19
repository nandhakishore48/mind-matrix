"""
Mock AI response generators for BrandCraft.
These simulate AI model outputs for demo/hackathon purposes.
Replace with real API calls (Gemini, Stable Diffusion, HuggingFace) in production.
"""
import random
import hashlib
import time


def generate_brand_names(industry: str, keywords: str, target_audience: str, tone: str) -> list:
    """Generate 10 mock brand names based on inputs."""
    prefixes = {
        "professional": ["Apex", "Prime", "Nova", "Vertex", "Elevate", "Pinnacle", "Summit", "Zenith", "Crest", "Vanguard"],
        "playful": ["Zippy", "Sparky", "Breezy", "Fizz", "Poppy", "Quirky", "Jolly", "Wink", "Doodle", "Bubbles"],
        "modern": ["Nexus", "Flux", "Pulse", "Aura", "Grid", "Sync", "Loop", "Wave", "Core", "Edge"],
        "bold": ["Thunder", "Blaze", "Titan", "Storm", "Force", "Strike", "Fury", "Iron", "Volt", "Rogue"],
    }
    suffixes = ["Labs", "Co", "Hub", "Studio", "Works", "Forge", "Stack", "Craft", "ify", "ly", "io", "AI"]

    keyword_list = [k.strip().capitalize() for k in keywords.split(",") if k.strip()]
    base_words = prefixes.get(tone, prefixes["modern"])
    names = []

    for i in range(10):
        if i < 3 and keyword_list:
            kw = random.choice(keyword_list)
            suf = random.choice(suffixes)
            names.append(f"{kw}{suf}")
        elif i < 6:
            pre = base_words[i % len(base_words)]
            suf = random.choice(suffixes)
            names.append(f"{pre}{suf}")
        else:
            pre = random.choice(base_words)
            kw = random.choice(keyword_list) if keyword_list else industry.capitalize()[:4]
            names.append(f"{pre}{kw}")

    return names


def generate_logo_urls(brand_name: str, style: str, primary_color: str, secondary_color: str) -> list:
    """Generate mock logo placeholder URLs."""
    logos = []
    clean_primary = primary_color.lstrip('#')
    clean_secondary = secondary_color.lstrip('#')
    styles_text = {"minimal": "Minimal", "modern": "Modern", "vintage": "Vintage", "tech": "Tech"}
    style_label = styles_text.get(style, "Modern")

    for i in range(4):
        seed = hashlib.md5(f"{brand_name}{style}{i}".encode()).hexdigest()[:8]
        # Using placeholder image services
        logos.append({
            "id": i + 1,
            "url": f"https://via.placeholder.com/400x400/{clean_primary}/{clean_secondary}?text={brand_name}+{style_label}+{i+1}",
            "style": style_label,
            "label": f"{style_label} Logo Variation {i + 1}"
        })
    return logos


def generate_brand_identity(brand_name: str, industry: str, target_audience: str) -> dict:
    """Generate mock brand identity."""
    return {
        "mission": f"{brand_name} is committed to revolutionizing the {industry} industry by delivering innovative, customer-centric solutions that empower {target_audience} to achieve their full potential. We bridge the gap between cutting-edge technology and everyday accessibility.",
        "vision": f"To become the world's most trusted {industry} platform, setting new standards for excellence, sustainability, and social impact. We envision a future where {target_audience} everywhere have instant access to transformative {industry} solutions.",
        "core_values": [
            "Innovation — Pushing boundaries with creative, AI-driven solutions",
            "Integrity — Building trust through transparent and ethical practices",
            "Impact — Creating measurable, positive change for every customer",
            "Inclusivity — Designing for diverse audiences and global accessibility",
            "Excellence — Pursuing the highest standard in every interaction"
        ],
        "tagline": f"{brand_name} — Empowering Your {industry.capitalize()} Journey with AI",
        "brand_story": f"{brand_name} was born from a simple yet powerful idea: that every {target_audience.lower()} deserves access to world-class {industry} tools. Our founders, a diverse team of industry experts and technologists, recognized that traditional {industry} processes were holding people back. By combining artificial intelligence with deep human insight, {brand_name} was created to democratize {industry} and make professional-grade solutions available to everyone. Today, we serve thousands of satisfied customers and continue to innovate at the intersection of technology and {industry}."
    }


def generate_content(brand_name: str, content_type: str, tone: str, keywords: str, length: str) -> dict:
    """Generate mock marketing content."""
    content_map = {
        "social_post": {
            "title": "Social Media Post",
            "content": f"🚀 Introducing {brand_name} — the future of branding is here!\n\nTired of spending weeks on brand identity? Our AI-powered platform generates stunning logos, compelling taglines, and complete brand kits in minutes.\n\n✨ Smart. Fast. Beautiful.\n\n{'🔑 ' + keywords if keywords else ''}\n\n👉 Start your free trial today and see the difference AI can make!\n\n#Branding #AI #Innovation #{brand_name.replace(' ', '')} #StartupLife #Design",
            "seo_keywords": [brand_name, "AI branding", "brand identity", "logo design", "startup branding"]
        },
        "ad_copy": {
            "title": "Advertisement Copy",
            "content": f"BUILD YOUR BRAND IN MINUTES, NOT MONTHS.\n\n{brand_name} uses cutting-edge AI to craft your complete brand identity — from logo to tagline to marketing content.\n\n⚡ AI-Powered Logo Generation\n⚡ Smart Brand Name Suggestions\n⚡ Auto-Generated Marketing Copy\n⚡ Real-Time Sentiment Analysis\n\nJoin 10,000+ entrepreneurs who transformed their brands with {brand_name}.\n\n[Try Free for 14 Days →]",
            "seo_keywords": [brand_name, "automated branding", "AI design", "brand builder"]
        },
        "blog": {
            "title": f"How {brand_name} is Revolutionizing Brand Building with AI",
            "content": f"# How {brand_name} is Revolutionizing Brand Building with AI\n\nIn today's fast-paced digital landscape, building a memorable brand is more crucial — and challenging — than ever. Enter {brand_name}, an AI-powered branding automation platform that's changing the game.\n\n## The Old Way vs. The {brand_name} Way\n\nTraditional branding takes weeks of agency consultations, design iterations, and strategy sessions. With {brand_name}, entrepreneurs and startups can generate professional brand identities in minutes.\n\n## Key Features\n\n### 1. AI Brand Name Generator\nInput your industry, keywords, and target audience — get 10 creative, market-ready brand names instantly.\n\n### 2. Logo Generation\nOur AI creates multiple logo variations in styles ranging from minimal to modern, all customizable to your brand palette.\n\n### 3. Content Automation\nFrom social media posts to full blog articles, {brand_name} generates on-brand marketing content tailored to your audience.\n\n### 4. Sentiment Analysis\nUnderstand how your audience perceives your brand with real-time sentiment analysis and actionable AI suggestions.\n\n## The Bottom Line\n\n{brand_name} isn't just a tool — it's your AI branding partner. Whether you're launching a startup or refreshing an established brand, our platform delivers professional results at a fraction of the traditional cost.\n\n*Ready to transform your brand? Get started with {brand_name} today.*",
            "seo_keywords": [brand_name, "AI branding", "brand building", "startup tools", "design automation"]
        },
        "email": {
            "title": "Email Marketing Template",
            "content": f"Subject: Your Brand Deserves Better — Meet {brand_name} 🎨\n\nHi [First Name],\n\nWe know building a brand from scratch is overwhelming. That's why we created {brand_name} — your AI-powered branding companion.\n\nHere's what you get:\n\n✅ Instant brand name generation\n✅ AI-designed logos in 4 unique styles\n✅ Complete brand identity kit (mission, vision, values)\n✅ Marketing content generation\n✅ Real-time sentiment analysis\n\n🎁 Special Offer: Start your free 14-day trial and get your first brand kit free.\n\n[Start Building Your Brand →]\n\nBest,\nThe {brand_name} Team\n\nP.S. Over 10,000 brands were created with {brand_name} last month alone. Don't miss out!",
            "seo_keywords": [brand_name, "email marketing", "branding", "free trial"]
        }
    }

    result = content_map.get(content_type, content_map["social_post"])
    return result


def analyze_sentiment(text: str) -> dict:
    """Mock sentiment analysis."""
    words = text.lower().split()
    positive_words = {"great", "love", "excellent", "amazing", "wonderful", "fantastic", "good", "best",
                      "happy", "awesome", "beautiful", "outstanding", "brilliant", "perfect", "superb"}
    negative_words = {"bad", "terrible", "awful", "worst", "hate", "poor", "horrible", "disgusting",
                      "disappointing", "frustrated", "angry", "ugly", "broken", "useless", "pathetic"}

    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    total = max(pos_count + neg_count, 1)

    if pos_count > neg_count:
        positive = round(random.uniform(55, 80), 1)
        negative = round(random.uniform(5, 15), 1)
    elif neg_count > pos_count:
        positive = round(random.uniform(10, 25), 1)
        negative = round(random.uniform(50, 75), 1)
    else:
        positive = round(random.uniform(30, 45), 1)
        negative = round(random.uniform(20, 35), 1)

    neutral = round(100 - positive - negative, 1)
    perception = round((positive * 1.0 + neutral * 0.5 + negative * 0.0) / 100 * 10, 1)

    suggestions = []
    if negative > 30:
        suggestions = [
            "Consider addressing customer complaints more proactively",
            "Improve response time to negative feedback",
            "Launch a customer satisfaction survey to identify pain points",
            "Develop a PR campaign to rebuild trust",
            "Create positive content to shift brand perception"
        ]
    elif positive > 60:
        suggestions = [
            "Leverage positive sentiment with testimonial campaigns",
            "Create a brand ambassador program",
            "Share user success stories on social media",
            "Consider expanding to new market segments",
            "Double down on what customers love about your brand"
        ]
    else:
        suggestions = [
            "Increase brand visibility through targeted content marketing",
            "Engage with customers more actively on social platforms",
            "Develop a consistent brand voice across all channels",
            "Run A/B tests on messaging to optimize engagement",
            "Consider influencer partnerships to boost awareness"
        ]

    return {
        "positive": positive,
        "neutral": neutral,
        "negative": negative,
        "brand_perception_score": perception,
        "suggestions": suggestions
    }


def chat_response(message: str, context: str = "") -> dict:
    """Mock AI branding consultant chatbot."""
    message_lower = message.lower()

    if any(w in message_lower for w in ["swot", "strength", "weakness", "opportunity", "threat"]):
        return {
            "response": """**SWOT Analysis for Your Brand:**

**Strengths:**
• Innovative AI-powered approach sets you apart from competitors
• Strong digital presence with modern, user-friendly design
• Cost-effective solution for startups and small businesses

**Weaknesses:**
• Limited brand recognition in the initial launch phase
• Dependence on AI may concern traditional customers
• Requires continuous model updates and maintenance

**Opportunities:**
• Growing demand for automated branding solutions
• Expansion into emerging markets and new industries
• Partnership potential with marketing agencies and design platforms

**Threats:**
• Established competitors with larger budgets and market share
• Rapid changes in AI technology landscape
• Economic downturns affecting startup funding and spending

I recommend focusing on your strengths while addressing weaknesses through targeted content marketing and customer education campaigns.""",
            "suggestions": [
                "Run a competitive analysis",
                "Define your unique value proposition",
                "Create a customer feedback loop"
            ]
        }

    elif any(w in message_lower for w in ["position", "market", "compete", "competitor"]):
        return {
            "response": """**Market Positioning Strategy:**

To effectively position your brand, I recommend the **"Innovative Disruptor"** positioning strategy:

1. **Identify Your Niche:** Focus on startups and small businesses who need affordable, fast branding solutions
2. **Unique Value Proposition:** "Professional branding in minutes, not months — powered by AI"
3. **Price Positioning:** Position as premium-quality at mid-market pricing
4. **Channel Strategy:** Focus on digital channels — content marketing, social media, and partnerships
5. **Differentiation:** Emphasize the AI advantage, speed, and cost savings vs. traditional agencies

**Key Message Framework:**
- For investors: "We're automating a $50B branding industry"
- For customers: "Your brand, perfected by AI, in under 10 minutes"
- For partners: "The future of branding workflow automation" """,
            "suggestions": [
                "Analyze top 5 competitors",
                "Create a positioning map",
                "Define target customer personas"
            ]
        }

    elif any(w in message_lower for w in ["campaign", "marketing", "promote", "advertise"]):
        return {
            "response": """**Marketing Campaign Ideas:**

🎯 **Campaign 1: "Brand in a Minute" Challenge**
- Social media campaign showing real-time brand creation
- User-generated content from beta testers
- Viral potential with time-lapse brand building videos

📱 **Campaign 2: "Before & After" Series**
- Showcase brand transformations
- Side-by-side comparisons of DIY vs AI-generated branding
- Testimonials from early adopters

🤝 **Campaign 3: "Startup Launch Kit" Partnership**
- Partner with accelerators and incubators
- Offer free brand kits for accepted startups
- Build word-of-mouth in the entrepreneur community

📧 **Campaign 4: "AI Brand Audit" Lead Magnet**
- Free brand health check tool
- Email capture for lead nurturing
- Segmented follow-up sequences based on score

**Recommended Budget Split:**
- Social Media: 35%
- Content Marketing: 25%
- Partnerships: 20%
- Paid Ads: 15%
- PR: 5%""",
            "suggestions": [
                "Start with Campaign 1 for viral potential",
                "Set up tracking for each campaign",
                "A/B test ad creatives"
            ]
        }

    else:
        return {
            "response": f"""Thanks for your question! As your AI Branding Consultant, here's my advice:

**Brand Strategy Insights:**

1. **Consistency is Key:** Ensure your brand voice, colors, and messaging align across all platforms
2. **Know Your Audience:** Deep understanding of your target market drives every branding decision
3. **Tell a Story:** Brands that tell compelling stories create emotional connections
4. **Be Authentic:** Modern consumers value transparency and authenticity
5. **Measure & Iterate:** Use sentiment analysis and engagement metrics to continuously improve

**Quick Action Items:**
- ✅ Generate your brand name and logo first — they're the foundation
- ✅ Build your brand identity (mission, vision, values) to guide all decisions
- ✅ Create a content calendar with AI-generated posts
- ✅ Run sentiment analysis monthly to track brand health
- ✅ Use this consultant for ongoing strategic advice

*What specific aspect of branding would you like to dive deeper into?*""",
            "suggestions": [
                "Tell me about your brand's target audience",
                "Generate a SWOT analysis",
                "Get marketing campaign ideas",
                "Discuss brand positioning"
            ]
        }
