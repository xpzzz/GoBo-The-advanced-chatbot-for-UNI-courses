import React, {Component} from 'react';
import {Avatar, Button, Col, Layout, Row} from 'antd';

const {Header} = Layout;

class Title extends Component {
    render() {
        return (

                <Header style={styles}>
                    <Row>
                        <Col span={2} pull={2}>
                            <Avatar size={48}
                                    src='http://img.mp.itc.cn/upload/20170621/e9a96f4bd1f94c89b98b7a0d7a848b3f_th.jpg'/>
                        </Col>
                        <Col span={4} push={2}>
                            <h1 style={{color: '#afe3e8'}}>GoBoAI</h1>
                        </Col>
                        <Col span={18} push={10}>
                            <Button shape="circle" icon="setting"/>
                        </Col>

                    </Row>
                </Header>
        )
    }
}

const styles = {
    height: '64px',
    fontSize: '28px',
    borderRadius:'10px 10px 0px 0px',
    backgroundColor:'#f9f5fb',

};


export default Title;