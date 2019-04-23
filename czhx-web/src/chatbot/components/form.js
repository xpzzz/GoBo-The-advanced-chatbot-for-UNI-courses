import React, {Component} from 'react';
import {Button, Col, Form, Input, Row,} from 'antd';

function hasErrors(fieldsError) {
    return Object.keys(fieldsError).some(field => fieldsError[field]);
}

class HorizontalLoginForm extends Component {
    componentDidMount() {
        // To disabled submit button at the beginning.
        this.props.form.validateFields();
    }

    handleSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            if (!err) {
                console.log('Received values of form: ', values);
                this.props.passMessage(values.query);
                this.props.form.resetFields();
            }
        });
    };

    render() {
        const {
            getFieldDecorator, getFieldsError, getFieldError, isFieldTouched,
        } = this.props.form;

        // Only show error after a field is touched.
        const messageError = isFieldTouched('query') && getFieldError('query');
        return (

            <Row>
                <Form layout="inline" onSubmit={this.handleSubmit}>
                    <Col span={18}>
                        <Form.Item
                            validateStatus={messageError ? 'error' : ''}
                            help={messageError || ''}
                        >
                            {getFieldDecorator('query', {
                                rules: [{required: true, message: 'Please input your question!'}],
                            })(
                                <Input placeholder="Send me message!"/>
                            )}
                        </Form.Item>
                    </Col>
                    <Col span={6} >
                        <Form.Item>
                            <Button
                                type="primary"
                                htmlType="submit"
                                disabled={hasErrors(getFieldsError())}
                            >
                                Send
                            </Button>
                        </Form.Item>
                    </Col>
                </Form>

            </Row>
        );
    }
}


const WrappedHorizontalLoginForm = Form.create({name: 'horizontal_login'})(HorizontalLoginForm);


export default WrappedHorizontalLoginForm;