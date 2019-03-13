import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import WebDemo from './service/WebDemo';
import { Button } from 'antd';

class App extends Component {
  render() {
    return (
      <div className="App">
        <WebDemo/>
        <Button type="primary" >TEST</Button>
      </div>
    );
  }
}

export default App;
