import React, {Component} from 'react';
import {Layout, List} from 'antd';
import MessageItem from './messageItem';
import scrollIntoView from 'scroll-into-view-if-needed';

const {Content} = Layout;

// window.HTMLElement.prototype.scrollIntoView = function() {};

class MessageList extends Component {
    constructor(props) {
        super(props);
        this.messagesEnd = React.createRef();
    }


    scrollToBottom = () => {
        // this function is non-standard
        // this.messagesEnd.current.scrollIntoViewIfNeeded();
        scrollIntoView(this.messagesEnd.current, {
            scrollMode: 'if-needed',
            block: 'nearest',
            inline: 'nearest',
        });
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
                    <div ref={this.messagesEnd}>---</div>
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
    overflow: 'auto',
    display: 'block',
};

export default MessageList;