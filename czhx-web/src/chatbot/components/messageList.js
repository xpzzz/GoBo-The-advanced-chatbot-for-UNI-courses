import React, {Component} from 'react';
import {Layout} from 'antd';
import {
    List,
    // Avatar
} from 'antd';
import MessageItem from './messageItem';

const {Content} = Layout;


class MessageList extends Component {
    render() {
        return (
            <Content style={styles}>
                <List
                    itemLayout="horizontal"
                    dataSource={this.props.data}
                    renderItem={item => (
                        <MessageItem data={item}/>
                    )}
                />
            </Content>
        )
    }
}



const styles = {
    height: '352px',
    weight: '300px',
    backgroundColor: '#f4eaf5',
    padding: '10px'
};

export default MessageList;