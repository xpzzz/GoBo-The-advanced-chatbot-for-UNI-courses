import React, { Component } from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
const {   Footer } = Layout;


class InputForm extends Component{
    render() {
        return(
                <Footer style={styles}>
                    Ant Design ©2018 Created by Ant UED
                </Footer>
        )
    }
}
const styles={
    height:'64px',
};

export default InputForm;