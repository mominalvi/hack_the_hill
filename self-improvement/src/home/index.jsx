import axios from 'axios';
import {useEffect, useState} from 'react';
import {usePlaidLink} from 'react-plaid-link';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useContext } from 'react';
import { PlaidContext } from '../context/PlaidContext';
import { Dashboard } from '../fulll-dashboard';

axios.defaults.baseURL = 'http://localhost:8000';

function PlaidAuth({public_token, access_token}){
  
  useEffect(() => {
    async function fetchTransactions(){
      const response = await axios.get('/api/transactions/sync');
      if(response.status === 200){
        console.log('Transactions: ', response.data);
      }else{
        console.log('Error fetching transactions');
        throw new Error('Error fetching transactions');
      }
    }
    fetchTransactions();
  }, [])

  useEffect(() => {
    async function fetchRecurringTransactions(){
      const response = await axios.get('/api/transactions/recurring/get');
      if(response.status === 200){
        console.log('Recurring Transactions: ', response.data);
      }else{
        console.log('Error fetching recurring transactions');
        throw new Error('Error fetching recurring transactions');
      }
    }
    
    fetchRecurringTransactions();
  }, [])
  return(

    // <span>{public_token}
    // <a href="/dashboard">go dashboard</a>
    // </span>

    <Dashboard />
  )
}

function Home() {

  const { linkToken, setLinkToken, accessToken, setAccessToken, accounts, setAccounts, public_token, setPublicToken, metadata, setMetadata } = useContext(PlaidContext);
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

  useEffect(() => {
    async function ExchangePublicToken() {
      const response = await axios.post('/api/item/public_token/exchange', {public_token});
      
      if (response.status === 200) {
        console.log(response.data);
        console.log('Access token: ', response.data.access_token);
        setAccessToken(response.data.access_token);

        //authenticating the user
        const auth_response = await axios.get('/api/auth/get');

        if(auth_response.status === 200){
          console.log('User authenticated');
          console.log(auth_response.data);
          setAccounts(auth_response.data.accounts.eft);
        }else{
          console.log('Error authenticating user');
          throw new Error('Error authenticating user');
        }
      }else{
        console.log('Error fetching access token');
        throw new Error('Error fetching access token');
      }
    }
    if(public_token){
      ExchangePublicToken();
    }
  }, [public_token])

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
  return public_token ? <PlaidAuth access_token={accessToken} public_token={public_token} /> : (
    <div className="">
        <button onClick={() => open()} disabled={!ready}>
        Connect a bank account
        </button>

        <a href="/dashboard">go dashboard</a>
    </div>
  );
}

export default Home;