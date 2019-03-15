import React, {Component} from 'react';
import Title from './components/title';
import {Layout} from 'antd';
import MessageList from './components/messageList';
import InputForm from './components/inputForm';

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


const styles = {
    width: '320px',
    height: '480px',

};
export default ChatBot;
