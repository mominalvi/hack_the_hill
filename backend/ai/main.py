import google.generativeai as genai

# Directly pass your API key as a string
# genai.configure(api_key="AIzaSyC8gBOzA3g17B2IzxEsrQBIwnApi0Apk48")

# Example request to generate text
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")


def spending_category(spending_by_category):
    categories = list(spending_by_category.keys())
    amounts = list(spending_by_category.values())

    total_spending = sum(amounts)    
    total_positive_spending = sum(amount for amount in amounts if amount > 0)
    average_spending = total_spending / len(categories)

    max_spending_category = max(spending_by_category, key=spending_by_category.get)
    min_spending_category = min(spending_by_category, key=spending_by_category.get)

    # Find negative spending categories (if any)
    negative_spending_categories = {category: amount for category, amount in spending_by_category.items() if amount < 0}

    summary = {
        "total_spending": total_spending,
        "total_positive_spending": total_positive_spending,
        "average_spending_per_category": average_spending,
        "highest_spending_category": max_spending_category,
        "highest_spending_amount": spending_by_category[max_spending_category],
        "lowest_spending_category": min_spending_category,
        "lowest_spending_amount": spending_by_category[min_spending_category],
        "negative_spending_categories": negative_spending_categories
    }

    return summary

# Example 
spending_by_category = {
    "Food and Drink": 26553.85,
    "Payment": 50509.0,
    "Recreation": 1962.5,
    "Shops": 12000.0,
    "Transfer": 171148.72,
    "Travel": -213.08000000000538
}
# summary = summarize_spending(spending_by_category)


def puruchase_freq_cat(spending_by_category):
    categories = list(spending_by_category.keys())
    amounts = list(spending_by_category.values())



def analyze_with_gbt(spending_by_category):

    genai.configure(api_key="AIzaSyC8gBOzA3g17B2IzxEsrQBIwnApi0Apk48")

    prompt = f"""
    Below is a summary of spending by category:
    {summary}
    
    Please provide an analysis of the data, pointing out significant trends or anomalies.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return print(response.text)

summary = "Food: $300, Travel: $200, Entertainment: $150"
analysis = analyze_with_gbt(summary)
print(analysis)