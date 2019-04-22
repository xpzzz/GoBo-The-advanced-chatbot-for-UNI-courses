import React, {Component} from 'react';
import {Avatar, Col, Row} from 'antd';


class MessageItem extends Component {
    // constructor(props) {
    //     super(props)
    // }

    componentDidMount() {
        console.log('MessageItem: ', this.props);
    };

    render() {
        console.log(this.props.data.flag);
        return (
            <Row>
                <Col span={2} pull={1}>
                    {this.props.data.speaks === 'bot' &&
                    <div>
                        <Avatar size={30}
                                src='http://img.mp.itc.cn/upload/20170621/e9a96f4bd1f94c89b98b7a0d7a848b3f_th.jpg'/>
                    </div>
                    }
                </Col>
                <Col span={20} style={messageStyle}>
                    <span className="black-text">
                        {this.props.data.msg.text.text}
                        {this.props.data.flag === 1 &&
                        <div><br/>
                            <p>It has been replied, you can find it through <a
                                href={this.props.data.msg.text.url}>thisLink</a></p>
                        </div>

                        }

                      </span>
                </Col>
                <Col span={2}>
                    {this.props.data.speaks === 'user' &&
                    <div className="col s2">
                        {/*{this.props.data.speaks}*/}
                        <Avatar size={30}
                                src={userIcon[this.props.data.icon]}/>
                    </div>
                    }
                </Col>

            </Row>

        )
    }
}

const userIcon = [
    'https://d24h4out7wreu3.cloudfront.net/product_images/p/697138.f56.61774S7ay1Cm2MjUAAA-650x650-b-p.jpg',
    'https://images-na.ssl-images-amazon.com/images/I/51O6wRTcBSL._SX425_.jpg',
    'https://as2.ftcdn.net/jpg/01/80/58/43/500_F_180584318_kcRpImU2nfJqasP8PrOZayGURuKMIbit.jpg'

];
const messageStyle = {
    position: 'relative',
    border: '1px solid #989898',
    borderRadius: '5px',
    background: '#fff',
    padding: '5px 8px',
    margin: '1px auto',
};

export default MessageItem;