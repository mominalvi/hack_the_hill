import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {useEffect, useState} from 'react';
import {usePlaidLink} from 'react-plaid-link';

axios.defaults.baseURL = 'http://localhost:8000';

function PlaidAuth({public_token}){
  return(
    <span>{public_token}</span>
  )
}

function App() {

  const [linkToken, setLinkToken] = useState(''); // plaid link token state gotten from the server
  const [public_token, setPublicToken] = useState(''); // plaid public token state gotten from the server
  const [metadata, setMetadata] = useState(''); // plaid metadata state gotten from the server

  useEffect(() => {
    async function fetchData() {
      const response = await axios.post('/api/create_link_token', {name:"divine"});
      
      if (response.status === 200) {
        setLinkToken(response.data.link_token);
      }else{
        console.log('Error fetching link token');
        throw new Error('Error fetching link token');
      }
    }
    fetchData();
  }, []);

  const { open, ready } = usePlaidLink({
    token: linkToken,
    onSuccess: (public_token, metadata) => {
      console.log('public_token: ', public_token);
      console.log('metadata: ', metadata);
      setPublicToken(public_token);
      setMetadata(metadata);
    },
  });
  
  //if public_token is available, render the PlaidAuth component else render the button to connect a bank account, because it means the user has not connected a bank account yet
  return public_token ? <PlaidAuth public_token={public_token} /> : (
    <button onClick={() => open()} disabled={!ready}>
      Connect a bank account
    </button>
  );
}

export default App;
