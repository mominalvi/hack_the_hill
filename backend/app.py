from flask import Flask, request, jsonify
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.item_get_request import ItemGetRequest
from dotenv import load_dotenv
import os
import time
import json
from flask_cors import CORS
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from utils import poll_with_retries, pretty_print_response, format_error
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

load_dotenv()

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions').split(',')
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US').split(',')

def empty_to_none(field):
    value = os.getenv(field)
    if value is None or len(value) == 0:
        return None
    return value

host = plaid.Environment.Sandbox

if PLAID_ENV == 'sandbox':
    host = plaid.Environment.Sandbox

if PLAID_ENV == 'production':
    host = plaid.Environment.Production

PLAID_REDIRECT_URI = empty_to_none('PLAID_REDIRECT_URI')

configuration = plaid.Configuration(
    host=host,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
        'plaidVersion': '2020-09-14'
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)
access_token = 'access-sandbox-a18083e0-53f7-4f22-98c1-28511e7aaf87' # testing access_token
item_id = None

products = []
for product in PLAID_PRODUCTS:
    products.append(Products(product))


@app.route('/api/transactions/sync', methods=['GET'])
def get_transactions():
    cursor = ''
    added = []
    has_more = True

    try:
        while has_more:
            request = TransactionsSyncRequest(
                access_token=access_token,
                cursor=cursor,
            )
            response = client.transactions_sync(request).to_dict()
            cursor = response['next_cursor']
            added.extend(response['added'])
            has_more = response['has_more']

        # Initialize data structures
        spending_by_category = defaultdict(float)  # Total spending by category
        spending_by_category_and_date = defaultdict(lambda: defaultdict(float))  # Spending by category AND date
        purchase_frequency_by_category = defaultdict(int)  # Count how often purchases are made per category

        # Loop through all transactions to gather data
        for transaction in added:
            if 'category' in transaction and len(transaction['category']) > 0:
                main_category = transaction['category'][0]  # Main category (e.g., Food and Drink)

                # Accumulate total spending in each category
                spending_by_category[main_category] += transaction['amount']

                # Convert the date string into a datetime object
                transaction_date = transaction['date']  # It's already a datetime.date object

                # Increment the purchase count for each category
                purchase_frequency_by_category[main_category] += 1

                # Add the transaction amount to the spending by category and date
                spending_by_category_and_date[main_category][transaction_date] += transaction['amount']

        # Prepare the dataset to be sent to the AI model
        structured_data = {
            'spending_by_category': dict(spending_by_category),  # Total spending by category
            'purchase_dates_by_category': {k: [d.strftime("%Y-%m-%d") for d in v] for k, v in purchase_dates_by_category.items()},  # Dates as strings
            'purchase_frequency_by_category': dict(purchase_frequency_by_category),  # Frequency by category
            'spending_by_category_and_date': {k: {d.strftime("%Y-%m-%d"): v for d, v in date_dict.items()} for k, date_dict in spending_by_category_and_date.items()}  # Spending by category and date
        }

        # Print the structured data for debugging
        print(f"Structured Data for AI Model: {structured_data}")

        return jsonify(structured_data)

    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)





if __name__ == '__main__':
    app.run(port=8000, debug=True)from flask import Flask, request, jsonify
import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.item_get_request import ItemGetRequest
from plaid.model.transactions_recurring_get_request import TransactionsRecurringGetRequest
from dotenv import load_dotenv
import os
import time
import json
from flask_cors import CORS
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from utils import poll_with_retries, pretty_print_response, format_error

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

load_dotenv()

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions').split(',')
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US').split(',')

def empty_to_none(field):
    value = os.getenv(field)
    if value is None or len(value) == 0:
        return None
    return value

host = plaid.Environment.Sandbox

if PLAID_ENV == 'sandbox':
    host = plaid.Environment.Sandbox

if PLAID_ENV == 'production':
    host = plaid.Environment.Production

PLAID_REDIRECT_URI = empty_to_none('PLAID_REDIRECT_URI')

configuration = plaid.Configuration(
    host=host,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
        'plaidVersion': '2020-09-14'
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)
access_token = None
item_id = None

products = []
for product in PLAID_PRODUCTS:
    products.append(Products(product))


@app.route("/api/create_link_token", methods=['POST'])
def create_link_token():
    # Get the client_user_id by searching for the current user
    # user = User.find(...)
    # client_user_id = user.id

    # Create a link_token for the given user
    try:
        link_token_request = LinkTokenCreateRequest(
                products=products,
                client_name="Hack The Hill Self-Improvement App",
                country_codes=[CountryCode(country) for country in PLAID_COUNTRY_CODES],
                redirect_uri='http://localhost:3000/', 
                language='en',
                webhook='https://webhook.example.com',
                user=LinkTokenCreateRequestUser(
                    client_user_id='user-id', #unique id for the user
                )
            )
        response = client.link_token_create(link_token_request)

        # Send the data to the client
        return jsonify(response.to_dict())
    except plaid.ApiException as e:
        print(e)
        return json.loads(e.body)

    
@app.route('/api/item/public_token/exchange', methods=['POST'])
def public_token_exchange():
    global access_token
    global item_id
    public_token = request.json['public_token']
    try:
        exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
        exchange_response = client.item_public_token_exchange(exchange_request)

        access_token = exchange_response['access_token']
        item_id = exchange_response['item_id']
        return jsonify(exchange_response.to_dict())
    except plaid.ApiException as e:
        print(e)
        return json.loads(e.body)


@app.route('/api/auth/get', methods=['GET'])
def get_auth():
    global access_token
    try:
        auth_request = AuthGetRequest(access_token=access_token)
        auth_response = client.auth_get(auth_request)
        numbers = auth_response['numbers']
        return jsonify(auth_response.to_dict())
    except plaid.ApiException as e:
        print(e)
        return json.loads(e.body)
    except Exception as e:
        print(e)
        return jsonify({'error': {'display_message': str(e)}})

@app.route('/api/transactions/sync', methods=['GET'])
def get_transactions():
    # Set cursor to empty to receive all historical updates
    cursor = ''

    # New transaction updates since "cursor"
    added = []
    modified = []
    removed = [] # Removed transaction ids
    has_more = True
    try:
        # Iterate through each page of new transaction updates for item
        while has_more:
            request = TransactionsSyncRequest(
                access_token=access_token,
                cursor=cursor,
            )
            response = client.transactions_sync(request).to_dict()
            cursor = response['next_cursor']
            # If no transactions are available yet, wait and poll the endpoint.
            # Normally, we would listen for a webhook, but the Quickstart doesn't 
            # support webhooks. For a webhook example, see 
            # https://github.com/plaid/tutorial-resources or
            # https://github.com/plaid/pattern
            if cursor == '':
                time.sleep(2)
                continue  
            # If cursor is not an empty string, we got results, 
            # so add this page of results
            added.extend(response['added'])
            modified.extend(response['modified'])
            removed.extend(response['removed'])
            has_more = response['has_more']
        # Return the 8 most recent transactions
        latest_transactions = sorted(added, key=lambda t: t['date'])[-8:]
        return jsonify({
            'latest_transactions': latest_transactions})

    except plaid.ApiException as e:
        print(e)
        error_response = format_error(e)
        return jsonify(error_response)


@app.route('/api/transactions/recurring/get', methods=['GET'])
def get_recurring_transactions():
    global access_token
    try:
        recur_trans_request = TransactionsRecurringGetRequest(
            access_token=access_token,
        )
        recur_trans_response = client.transactions_recurring_get(recur_trans_request)
        # inflow_streams = recur_trans_response.inflow_streams
        # outflow_streams = recur_trans_response.outflow_streams
        return jsonify(recur_trans_response.to_dict())
    except plaid.ApiException as e:
        print(e)
        return json.loads(e.body)

if __name__ == '__main__':
    app.run(port=8000, debug=True)