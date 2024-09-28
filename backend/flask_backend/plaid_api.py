import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

def create_plaid_client(configuration):
    """Create and return a Plaid API client using the configuration."""
    api_client = plaid.ApiClient(configuration)
    return plaid_api.PlaidApi(api_client)

def exchange_public_token(client, public_token):
    """Exchange a public token for an access token."""
    try:
        exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
        exchange_response = client.item_public_token_exchange(exchange_request)
        return exchange_response['access_token'], exchange_response['item_id']
    except plaid.ApiException as e:
        print(e)
        return None, None
