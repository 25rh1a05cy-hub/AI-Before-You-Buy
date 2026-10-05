import ollama


def explain_product(best_product, budget, priorities):

    prompt = f"""
You are an AI product decision assistant.

Analyze the selected product using ONLY the information provided.

PRODUCT DATA:
Name: {best_product['name']}
Price: ₹{best_product['price']}
Performance Score: {best_product['performance']}/100
Battery Score: {best_product['battery']}/100
Portability Score: {best_product['portability']}/100
Gaming Score: {best_product['gaming']}/100
Display Score: {best_product['display']}/100
Storage: {best_product['storage']} GB
RAM: {best_product['ram']} GB

USER BUDGET: ₹{budget}

USER PRIORITY WEIGHTS:
Performance: {priorities['performance']}
Battery: {priorities['battery']}
Portability: {priorities['portability']}
Gaming: {priorities['gaming']}

IMPORTANT:
- Priority values are WEIGHTS, not required scores.
- A higher priority weight means that feature is more important to the user.
- Product feature values are scores out of 100.
- Never say that a product score "meets" or "does not meet" a priority weight.
- Never call feature scores percentages.
- Never convert the battery score into hours or battery life.
- Never invent weight, size, processor, screen size, battery hours,
  real-world performance, or other specifications.
- Only use the exact product data provided.
- Explain the recommendation using the user's priority weights.
- Keep the answer short and factual.

Use EXACTLY these headings:

BEST CHOICE:
One short sentence explaining why this product was selected.

WHY IT MATCHES:
Two short sentences explaining how its feature scores align
with the user's most important priority weights.

MAIN STRENGTHS:
- Strength based on actual product data.
- Strength based on actual product data.
- Strength based on actual product data.

POSSIBLE LIMITATION:
One short sentence about a comparatively weaker feature.

FINAL ADVICE:
One short sentence.

Do not invent information.
Do not make assumptions about real-world usage.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]