import React, {Component} from 'react';
import {Layout} from 'antd';

const {Content} = Layout;


class MessageList extends Component {
    render() {
        return (
            <Content style={styles}>
                <p>hello</p>
            </Content>
        )
    }
}


const styles = {
    height: '352px',
};

export default MessageList;