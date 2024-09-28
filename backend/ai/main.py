import google.generativeai as genai
from dotenv import load_dotenv
import os
from collections import defaultdict
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

lt = {
    "latest_transactions": [
        {
            "account_id": "zq4ABLlwW5t3zQlBKzaWFoLrb6JpZ8hlXJMEr",
            "account_owner": None,
            "amount": 6.33,
            "authorized_date": "Tue, 03 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Travel",
                "Taxi"
            ],
            "category_id": "22016000",
            "check_number": None,
            "counterparties": [
                {
                    "confidence_level": "VERY_HIGH",
                    "entity_id": "eyg8o776k0QmNgVpAmaQj4WgzW9Qzo6O51gdd",
                    "logo_url": "https://plaid-merchant-logos.plaid.com/uber_1060.png",
                    "name": "Uber",
                    "phone_number": None,
                    "type": "merchant",
                    "website": "uber.com"
                }
            ],
            "date": "Wed, 04 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": None
            },
            "logo_url": "https://plaid-merchant-logos.plaid.com/uber_1060.png",
            "merchant_entity_id": "eyg8o776k0QmNgVpAmaQj4WgzW9Qzo6O51gdd",
            "merchant_name": "Uber",
            "name": "Uber 072515 SF**POOL**",
            "payment_channel": "online",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "VERY_HIGH",
                "detailed": "TRANSPORTATION_TAXIS_AND_RIDE_SHARES",
                "primary": "TRANSPORTATION"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_TRANSPORTATION.png",
            "transaction_code": None,
            "transaction_id": "E4znRXVBdrcWJa4BrJlecVDJeNyJvkc45JQ3r",
            "transaction_type": "special",
            "unofficial_currency_code": None,
            "website": "uber.com"
        },
        {
            "account_id": "BxqvNXLKB5C3AD897AomFwmve5PRa4t4x6X7l",
            "account_owner": None,
            "amount": -4.22,
            "authorized_date": "Mon, 16 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Transfer",
                "Payroll"
            ],
            "category_id": "21009000",
            "check_number": None,
            "counterparties": [],
            "date": "Mon, 16 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": None
            },
            "logo_url": None,
            "merchant_entity_id": None,
            "merchant_name": None,
            "name": "INTRST PYMNT",
            "payment_channel": "other",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "LOW",
                "detailed": "INCOME_WAGES",
                "primary": "INCOME"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_INCOME.png",
            "transaction_code": None,
            "transaction_id": "A3l45Xwkz9uoElPxjEVWt43B6m8Bbrf9xEw3M",
            "transaction_type": "special",
            "unofficial_currency_code": None,
            "website": None
        },
        {
            "account_id": "zq4ABLlwW5t3zQlBKzaWFoLrb6JpZ8hlXJMEr",
            "account_owner": None,
            "amount": 89.4,
            "authorized_date": "Mon, 16 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Food and Drink",
                "Restaurants"
            ],
            "category_id": "13005000",
            "check_number": None,
            "counterparties": [
                {
                    "confidence_level": "LOW",
                    "entity_id": None,
                    "logo_url": None,
                    "name": "FUN",
                    "phone_number": None,
                    "type": "merchant",
                    "website": None
                }
            ],
            "date": "Tue, 17 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": None
            },
            "logo_url": None,
            "merchant_entity_id": None,
            "merchant_name": "FUN",
            "name": "SparkFun",
            "payment_channel": "in store",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "LOW",
                "detailed": "ENTERTAINMENT_SPORTING_EVENTS_AMUSEMENT_PARKS_AND_MUSEUMS",
                "primary": "ENTERTAINMENT"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_ENTERTAINMENT.png",
            "transaction_code": None,
            "transaction_id": "8Gxv4XJjbRSxZNP7zZp6hlPrWBdr5McWJjaez",
            "transaction_type": "place",
            "unofficial_currency_code": None,
            "website": None
        },
        {
            "account_id": "zq4ABLlwW5t3zQlBKzaWFoLrb6JpZ8hlXJMEr",
            "account_owner": None,
            "amount": 12,
            "authorized_date": "Wed, 18 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Food and Drink",
                "Restaurants",
                "Fast Food"
            ],
            "category_id": "13005032",
            "check_number": None,
            "counterparties": [
                {
                    "confidence_level": "VERY_HIGH",
                    "entity_id": "vzWXDWBjB06j5BJoD3Jo84OJZg7JJzmqOZA22",
                    "logo_url": "https://plaid-merchant-logos.plaid.com/mcdonalds_619.png",
                    "name": "McDonald's",
                    "phone_number": None,
                    "type": "merchant",
                    "website": "mcdonalds.com"
                }
            ],
            "date": "Wed, 18 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": "3322"
            },
            "logo_url": "https://plaid-merchant-logos.plaid.com/mcdonalds_619.png",
            "merchant_entity_id": "vzWXDWBjB06j5BJoD3Jo84OJZg7JJzmqOZA22",
            "merchant_name": "McDonald's",
            "name": "McDonald's",
            "payment_channel": "in store",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "VERY_HIGH",
                "detailed": "FOOD_AND_DRINK_FAST_FOOD",
                "primary": "FOOD_AND_DRINK"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_FOOD_AND_DRINK.png",
            "transaction_code": None,
            "transaction_id": "oVRWZa1meLcQL8ZpWLzvcJmX1EbXG3coV89Gk",
            "transaction_type": "place",
            "unofficial_currency_code": None,
            "website": "mcdonalds.com"
        },
        {
            "account_id": "zq4ABLlwW5t3zQlBKzaWFoLrb6JpZ8hlXJMEr",
            "account_owner": None,
            "amount": 4.33,
            "authorized_date": "Wed, 18 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Food and Drink",
                "Restaurants",
                "Coffee Shop"
            ],
            "category_id": "13005043",
            "check_number": None,
            "counterparties": [
                {
                    "confidence_level": "VERY_HIGH",
                    "entity_id": "NZAJQ5wYdo1W1p39X5q5gpb15OMe39pj4pJBb",
                    "logo_url": "https://plaid-merchant-logos.plaid.com/starbucks_956.png",
                    "name": "Starbucks",
                    "phone_number": None,
                    "type": "merchant",
                    "website": "starbucks.com"
                }
            ],
            "date": "Wed, 18 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": None
            },
            "logo_url": "https://plaid-merchant-logos.plaid.com/starbucks_956.png",
            "merchant_entity_id": "NZAJQ5wYdo1W1p39X5q5gpb15OMe39pj4pJBb",
            "merchant_name": "Starbucks",
            "name": "Starbucks",
            "payment_channel": "in store",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "VERY_HIGH",
                "detailed": "FOOD_AND_DRINK_COFFEE",
                "primary": "FOOD_AND_DRINK"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_FOOD_AND_DRINK.png",
            "transaction_code": None,
            "transaction_id": "gVrNwqMaxJcXGV8jJG3LfENA6pVA8WiE7qDdM",
            "transaction_type": "place",
            "unofficial_currency_code": None,
            "website": "starbucks.com"
        },
        {
            "account_id": "zq4ABLlwW5t3zQlBKzaWFoLrb6JpZ8hlXJMEr",
            "account_owner": None,
            "amount": -500,
            "authorized_date": "Thu, 19 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Travel",
                "Airlines and Aviation Services"
            ],
            "category_id": "22001000",
            "check_number": None,
            "counterparties": [
                {
                    "confidence_level": "VERY_HIGH",
                    "entity_id": "NKDjqyAdQQzpyeD8qpLnX0D6yvLe2KYKYYzQ4",
                    "logo_url": "https://plaid-merchant-logos.plaid.com/united_airlines_1065.png",
                    "name": "United Airlines",
                    "phone_number": None,
                    "type": "merchant",
                    "website": "united.com"
                }
            ],
            "date": "Thu, 19 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": None
            },
            "logo_url": "https://plaid-merchant-logos.plaid.com/united_airlines_1065.png",
            "merchant_entity_id": "NKDjqyAdQQzpyeD8qpLnX0D6yvLe2KYKYYzQ4",
            "merchant_name": "United Airlines",
            "name": "United Airlines",
            "payment_channel": "in store",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "VERY_HIGH",
                "detailed": "TRAVEL_FLIGHTS",
                "primary": "TRAVEL"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_TRAVEL.png",
            "transaction_code": None,
            "transaction_id": "pVJlb4MRQXcwb8Loab7yc9RpmWxpoGCpQ3g8J",
            "transaction_type": "special",
            "unofficial_currency_code": None,
            "website": "united.com"
        },
        {
            "account_id": "zq4ABLlwW5t3zQlBKzaWFoLrb6JpZ8hlXJMEr",
            "account_owner": None,
            "amount": 5.4,
            "authorized_date": "Fri, 20 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Travel",
                "Taxi"
            ],
            "category_id": "22016000",
            "check_number": None,
            "counterparties": [
                {
                    "confidence_level": "VERY_HIGH",
                    "entity_id": "eyg8o776k0QmNgVpAmaQj4WgzW9Qzo6O51gdd",
                    "logo_url": "https://plaid-merchant-logos.plaid.com/uber_1060.png",
                    "name": "Uber",
                    "phone_number": None,
                    "type": "merchant",
                    "website": "uber.com"
                }
            ],
            "date": "Sat, 21 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": None
            },
            "logo_url": "https://plaid-merchant-logos.plaid.com/uber_1060.png",
            "merchant_entity_id": "eyg8o776k0QmNgVpAmaQj4WgzW9Qzo6O51gdd",
            "merchant_name": "Uber",
            "name": "Uber 063015 SF**POOL**",
            "payment_channel": "online",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "VERY_HIGH",
                "detailed": "TRANSPORTATION_TAXIS_AND_RIDE_SHARES",
                "primary": "TRANSPORTATION"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_TRANSPORTATION.png",
            "transaction_code": None,
            "transaction_id": "LZRQGXpNebfrZGjxoZJWt9nrP5krW7CkWG8dk",
            "transaction_type": "special",
            "unofficial_currency_code": None,
            "website": "uber.com"
        },
        {
            "account_id": "BxqvNXLKB5C3AD897AomFwmve5PRa4t4x6X7l",
            "account_owner": None,
            "amount": 25,
            "authorized_date": "Fri, 20 Sep 2024 00:00:00 GMT",
            "authorized_datetime": None,
            "category": [
                "Payment",
                "Credit Card"
            ],
            "category_id": "16001000",
            "check_number": None,
            "counterparties": [],
            "date": "Sat, 21 Sep 2024 00:00:00 GMT",
            "datetime": None,
            "iso_currency_code": "CAD",
            "location": {
                "address": None,
                "city": None,
                "country": None,
                "lat": None,
                "lon": None,
                "postal_code": None,
                "region": None,
                "store_number": None
            },
            "logo_url": None,
            "merchant_entity_id": None,
            "merchant_name": None,
            "name": "CREDIT CARD 3333 PAYMENT *//",
            "payment_channel": "other",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "pending": False,
            "pending_transaction_id": None,
            "personal_finance_category": {
                "confidence_level": "LOW",
                "detailed": "LOAN_PAYMENTS_CREDIT_CARD_PAYMENT",
                "primary": "LOAN_PAYMENTS"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_LOAN_PAYMENTS.png",
            "transaction_code": None,
            "transaction_id": "WGopwnXyW4SjJXMZwJg4HDvE5ZBEznc6QKMqB",
            "transaction_type": "special",
            "unofficial_currency_code": None,
            "website": None
        }
    ]
}

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

def sum_spent_by_merchant(transactions):
    merchant_sums = defaultdict(float)

    for transaction in transactions['latest_transactions']:
        merchant_name = transaction.get('merchant_name', 'Unknown')
        amount = transaction.get('amount', 0)
        merchant_sums[merchant_name] += amount

    return dict(merchant_sums)



def ai_test_d():
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

    prompt = f"""
    Based on the user's transactions only in one week in the following:
    {sum_spent_by_merchant(lt)}
    
    Please recommend areas the user can cut back in order to save more, prioritizing non-essential categories first. Assume user has no priorities and is willing to cut anything to save more money. dont give any other context. just give only recommendation on what to cut back .
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return print(response.text)


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
    #test_analyze_with_gbt()
    ai_test_d()
    print(sum_spent_by_merchant(lt))