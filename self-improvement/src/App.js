import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {useEffect, useState} from 'react';
import {usePlaidLink} from 'react-plaid-link';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './home/index';
import { Dashboard } from './fulll-dashboard';
import { Provider } from './Providers/Provider';
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
    <span>{public_token}</span>
  )
}

function App() {
  
  return(
    <Provider>
    <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
    </Router>
    </Provider>
  )

}

export default App;
