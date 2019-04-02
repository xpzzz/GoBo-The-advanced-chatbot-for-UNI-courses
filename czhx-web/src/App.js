import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import ChatBot from './chatbot/chatbot';

class App extends Component {
  render() {
    return (
      <div className="App">
        <ChatBot/>
      </div>
    );
  }
}

export default App;
