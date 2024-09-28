import { Pie, Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { useEffect, useState } from 'react';
import axios from 'axios';
import { useContext } from 'react';
import { PlaidContext } from '../context/PlaidContext';

// Register the required elements for the chart
ChartJS.register(ArcElement, Tooltip, Legend);

export function Dashboard() {
  const labels = ["Inflow", "Outflow"];
  const { linkToken, setLinkToken, accessToken, setAccessToken, accounts, setAccounts, public_token, setPublicToken, metadata, setMetadata } = useContext(PlaidContext);
  const [flowMoney, setFlowMoney] = useState(null);

  useEffect(() => {
    async function fetchRecurringTransactions(){
      const response = await axios.get('/api/transactions/recurring/get');
      if(response.status === 200){
        let inflow = 0;
        let outflow = 0;
        console.log('Recurring Transactions: ', response.data);

        response.data.inflow_streams.forEach((stream) => {
            inflow += Math.abs(stream.average_amount.amount);
        })

        response.data.outflow_streams.forEach((stream) => {
            outflow += Math.abs(stream.average_amount.amount);
        })

        setFlowMoney([inflow, outflow]);
        
      }else{
        console.log('Error fetching recurring transactions');
        throw new Error('Error fetching recurring transactions');
      }
    }
    
    if(accessToken){
      fetchRecurringTransactions();
    }
  }, [accessToken])


  useEffect(() => {
    async function fetchData() {
      const response = await axios.post('/api/create_link_token', {name:"divine"});
      console.log(response);
      if (response.status === 200) {
        setLinkToken(response.data.link_token);
      }else{
        console.log('Error fetching link token');
        throw new Error('Error fetching link token');
      }
    }
    if(!linkToken){
      fetchData();
    }
  }, [linkToken]);

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

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 2,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Doughnut Chart: Monthly Sales",
      },
    },
  };

  const data = {
    labels,
    datasets: [
        {
            data: flowMoney,
            backgroundColor: [
                "rgba(255, 99, 132)",
                "rgba(53, 162, 235)"
            ],
            borderColor: [
                "rgb(255, 99, 132)",
                "rgb(53, 162, 235)",
            ],
            borderWidth: 1,
        }
    ]
  }

  

  return flowMoney ? <Doughnut className='doughnut' data={data} options={options} /> : <span>Loading...</span>;
}
