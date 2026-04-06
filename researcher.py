from features.web_scraper import search
from core.llm import generate

def research(query):
    raw = search(query)

    if not raw.strip():
        return "No useful data found."
    

    prompt = f"""
You are a smart tutor.

Topic: {query}

Content:
{raw}

Your job:
- Extract REAL useful knowledge (ignore junk)
- Give 1 clear insight
- Give 1 practical action

DO NOT mention websites or sources.
DO NOT output garbage or unrelated text.
Keep it simple and useful.
"""

    return generate(prompt)