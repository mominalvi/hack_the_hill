from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS
from plaid.model.country_code import CountryCode
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products

# Import the functions from plaid_api.py
from plaid_api import create_plaid_client, exchange_public_token

app = Flask(__name__)
CORS(app)

load_dotenv()

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US').split(',')

# Set up Plaid client
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox if PLAID_ENV == 'sandbox' else plaid.Environment.Production,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
        'plaidVersion': '2020-09-14'
    }
)

# Create the Plaid client
client = create_plaid_client(configuration)
access_token = None
item_id = None

@app.route('/api/item/public_token/exchange', methods=['POST'])
def public_token_exchange():
    global access_token, item_id
    public_token = request.json['public_token']
    
    # Use the new exchange_public_token function from plaid_api.py
    access_token, item_id = exchange_public_token(client, public_token)
    
    if access_token:
        return jsonify({'access_token': access_token, 'item_id': item_id})
    else:
        return jsonify({'error': 'Token exchange failed'}), 400

if __name__ == '__main__':
    app.run(port=8000)
