import React, {Component} from 'react';
import {Col, Row} from 'antd';


class MessageItem extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <Row>
                <Col span={2}>
                    {this.props.data.speaks === 'bot' &&
                    <div>
                        <a href="/">{this.props.data.speaks}</a>
                    </div>
                    }
                </Col>
                <Col span={20}>
                    <span className="black-text">
                        {this.props.data.msg.text.text}
                      </span>
                </Col>
                <Col span={2}>
                    {this.props.data.speaks === 'user' &&
                    <div className="col s2">
                        <a href="/">{this.props.data.speaks}</a>
                    </div>
                    }
                </Col>

            </Row>

        )
    }
}


export default MessageItem;