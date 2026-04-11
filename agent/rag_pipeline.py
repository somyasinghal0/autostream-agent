import json
from difflib import get_close_matches


def load_knowledge():
    with open("data/knowledge_base.json") as f:
        return json.load(f)


def get_answer(query):
    data = load_knowledge()
    q = query.lower()

    # ✅ STEP 1: Normalize vague queries
    if any(word in q for word in ["offer", "offers", "feature", "features", "plans", "service"]):
        q = "pricing"

    # ✅ STEP 2: Similarity matching
    options = ["basic plan", "pro plan", "pricing", "refund", "support"]
    match = get_close_matches(q, options, n=1, cutoff=0.3)

    if match:
        q = match[0]

    # ✅ STEP 3: Retrieval logic (ENSURE RETURNS)

    if "basic" in q:
        basic = data["pricing"]["basic"]
        return f"""
🔹 Basic Plan – {basic['price']}
- {basic['videos']}
- {basic['resolution']}
"""

    elif "pro" in q:
        pro = data["pricing"]["pro"]
        return f"""
🔹 Pro Plan – {pro['price']}
- {pro['videos']}
- {pro['resolution']}
- AI captions included
- 24/7 support
"""

    elif "pricing" in q:
        pricing = data["pricing"]
        return f"""
📦 Our Pricing Plans:

🔹 Basic Plan – {pricing['basic']['price']}
- {pricing['basic']['videos']}
- {pricing['basic']['resolution']}

🔹 Pro Plan – {pricing['pro']['price']}
- {pricing['pro']['videos']}
- {pricing['pro']['resolution']}
- AI captions included
- 24/7 support
"""

    elif "refund" in q:
        return f"🔁 Refund Policy: {data['policies']['refund']}"

    elif "support" in q:
        return f"📞 Support: {data['policies']['support']}"

    # ✅ FINAL FALLBACK (VERY IMPORTANT)
    return "🤖 Sorry, I couldn't find that information."