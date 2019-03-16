import React, {Component} from 'react';
import {Button, Col, Input, Layout, Row} from 'antd';

const {Footer} = Layout;


class InputForm extends Component {
    constructor(props){
        super(props);
    }

    render() {
        const onChange = (e) => {
            console.log(e);
        };
        return (
            <Footer style={styles}>
                <Row>
                    <Col span={20}>
                        <Input onPressEnter={this.props.onKeyPress}
                            placeholder="type a message:"
                               allowClear
                               onChange={onChange}
                        />
                    </Col>
                    <Col span={4} push={1}>
                        <Button type="primary"
                                onClick={this.props.onKeyPress}
                                style={{backgroundColor: '#a3cbfb',}
                                }>Send</Button>
                    </Col>
                </Row>
            </Footer>
        )
    }
}

const styles = {
    height: '64px',
    // borderStyle:'solid',
    // borderWidth:'2px',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: '0px 0px 10px 10px',
    backgroundColor: '#f9f5fb',


};

export default InputForm;