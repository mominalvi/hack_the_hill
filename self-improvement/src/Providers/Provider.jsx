import { useState } from 'react';
import { PlaidContext } from '../context/PlaidContext';

export const Provider = ({ children }) => {
    const [linkToken, setLinkToken] = useState(''); // plaid link token state gotten from the server
    const [public_token, setPublicToken] = useState(''); // plaid public token state gotten from the server
    const [metadata, setMetadata] = useState(''); // plaid metadata state gotten from the server
    const [accessToken, setAccessToken] = useState(''); // plaid access token state gotten from the server
    const [accounts, setAccounts] = useState([]); // plaid accounts state gotten from the server

  return (
    <PlaidContext.Provider value={{ linkToken, setLinkToken, accessToken, setAccessToken, accounts, setAccounts, public_token, setPublicToken, metadata, setMetadata }}>
      {children}
    </PlaidContext.Provider>
  );
};
