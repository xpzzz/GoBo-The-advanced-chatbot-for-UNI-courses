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
    weight:'300px',
    backgroundColor:'#EED2EE',
    padding:'10px'
};

export default MessageList;