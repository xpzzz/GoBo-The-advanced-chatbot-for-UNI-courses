import React, { Component } from 'react';
import Title from './components/title';
import { Layout, Menu, Breadcrumb } from 'antd';
import MessageList from './components/messageList';
import InputForm from  './components/inputForm';

const {  Content, Footer } = Layout;

class ChatBot extends Component {
    render() {
        return (
            <div>
                <div>
                    <Layout className="layout" style={styles}>
                        <Title/>
                        <MessageList/>
                        <InputForm/>

                    </Layout>
                </div>
            </div>

        );
    }
}


const styles={
    width:'320px',
    height:'480px',

};
export default ChatBot;
