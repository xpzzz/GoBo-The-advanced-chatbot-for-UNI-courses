import React, {Component} from 'react';
import {Col, Row} from 'antd';


class MessageItem extends Component {
    // constructor(props) {
    //     super(props)
    // }

    render() {
        return (
            <Row>
                <Col span={2}>
                    {this.props.data.speaks === 'bot' &&
                    <div>
                        {this.props.data.speaks}
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
                        {this.props.data.speaks}
                    </div>
                    }
                </Col>

            </Row>

        )
    }
}


export default MessageItem;