import React, {Component} from 'react';
import {Layout} from 'antd';
import {
    List,
    // Avatar
} from 'antd';
import MessageItem from './messageItem';

const {Content} = Layout;

window.HTMLElement.prototype.scrollIntoView = function() {};

class MessageList extends Component {
    scrollToBottom = () => {
        this.messagesEnd.scrollIntoView({ behavior: "auto" });
    };

    componentDidMount() {
        this.scrollToBottom();
    }

    componentDidUpdate() {
        this.scrollToBottom();
    }

    render() {
        return (
            <Content style={styles}>

                <List
                    style={styles}
                    itemLayout="horizontal"
                    dataSource={this.props.data}
                    renderItem={item => (
                        <MessageItem data={item}/>
                    )}
                >
                    <div ref={(el) => { this.messagesEnd = el; }}>---</div>
                </List>

            </Content>
        )
    }
}



const styles = {
    height: '352px',
    weight: '300px',
    backgroundColor: '#f4eaf5',
    padding: '10px',
    overflow:'auto',
    display: 'block',
};

export default MessageList;