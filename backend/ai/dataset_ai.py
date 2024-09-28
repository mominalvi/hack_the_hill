import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

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


def puruchase_freq_cat(purchase_frequency_by_category):
    categories = list(spending_by_category.keys())
    amounts = list(spending_by_category.values())

    # Step 1: Total the number of purchases
    total_purchases = sum(purchase_frequency_by_category.values())

    # Step 2: Find the category with the highest and lowest purchase frequencies
    most_frequent_category = max(purchase_frequency_by_category, key=purchase_frequency_by_category.get)
    least_frequent_category = min(purchase_frequency_by_category, key=purchase_frequency_by_category.get)

    # Step 3: Create the summary
    summary = (
        f"Total number of purchases: {total_purchases}\n"
        f"The category with the most purchases is '{most_frequent_category}' with {purchase_frequency_by_category[most_frequent_category]} purchases.\n"
        f"The category with the fewest purchases is '{least_frequent_category}' with {purchase_frequency_by_category[least_frequent_category]} purchases.\n"
    )

    # Return the summary
    return summary

# Example usage:
purchase_frequency_by_category = {
    "Food and Drink": 122,
    "Payment": 49,
    "Recreation": 25,
    "Shops": 24,
    "Transfer": 74,
    "Travel": 98
}

summary = puruchase_freq_cat(purchase_frequency_by_category)
# print(summary)

def summarize_spending_by_date(spending_by_category_and_date):
    summary = "Here is the spending summary:\n"
    
    # Loop through each category
    for category, date_spending in spending_by_category_and_date.items():
        summary += f"\nCategory: {category}\n"
        for date, amount in date_spending.items():
            summary += f"  On {date}, you spent: ${amount}\n"
    
    return summary

# Example
spending_by_category_and_date = {
    "Food and Drink": {
        "2024-09-18": 300.00,
        "2024-09-19": 300.00
    },
    "Travel": {
        "2024-09-20": 1200.00
    }
}
summary = summarize_spending_by_date(spending_by_category_and_date)

def test_analyze_with_gbt():
    analysis = analyze_with_gbt(spending_by_category_and_date)
    print(analysis)

def analyze_with_gbt(spending_by_category):

    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

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
#print(analysis)

if __name__ == "__main__":
    # Your test function or main logic here
    test_analyze_with_gbt()