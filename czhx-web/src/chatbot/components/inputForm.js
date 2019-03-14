import React, { Component } from 'react';
import { Layout } from 'antd';
import {Input} from 'antd';
import {  Col,  Row,Button} from 'antd';
const {   Footer } = Layout;


class InputForm extends Component{
    render() {
        return(
                <Footer style={styles}>
                    <Row>
                        <Col span={20} >
                    <Input placeholder="Basic usage" />
                        </Col>
                        <Col span={4} push={1}>
                            <Button type="primary" style={{backgroundColor:'#a3cbfb',}}>Send</Button>
                        </Col>
                    </Row>
                </Footer>
        )
    }
}
const styles={
    height:'64px',
    borderStyle:'solid',
    borderWidth:'2px',
    display:'flex',
    justifyContent:'center',
    alignItems:'center',
    borderRadius:'0px 0px 10px 10px',
    backgroundColor:'#f4eaf5',


};

export default InputForm;