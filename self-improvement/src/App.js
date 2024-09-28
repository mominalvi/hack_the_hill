import logo from './logo.svg';
import './App.css';
import axios from 'axios';


axios.defaults.baseURL = 'http://localhost:8000';

function PlaidAuth({public_token}){
  return(
    <span>{public_token}</span>
  )
}

function App() {
  return(
    <h1>Self Improvement</h1>
  );
}

export default App;
