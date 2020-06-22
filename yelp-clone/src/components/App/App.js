import React from 'react';
// import logo from './logo.svg';
import BusinessList from '../BusinessList/BusinessList';
import SearchBar from '../SearchBar/SearchBar';
// import './App.css';
import './App.css';

class App extends React.Component{
    render(){
        return(
            <div className="App">
  <h1>Yelp Clone</h1>
  <SearchBar />
 <BusinessList /> 
</div>
        )
    }
}

export default App;
