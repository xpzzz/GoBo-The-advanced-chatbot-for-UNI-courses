import React, {Component} from 'react';
import Title from './components/title';
import {Layout} from 'antd';
import MessageList from './components/messageList';
import InputForm from './components/inputForm';
import axios from "axios";
import Cookies from 'universal-cookie';
import {v4 as uuid} from 'uuid';

const cookies = new Cookies();

class ChatBot extends Component {

    constructor(props) {
        super(props);
        // These bindings are necessary to make `this` work in the callback
        this._handleInputKeyPress = this._handleInputKeyPress.bind(this);
        this.state = {
            messages: [
                {
                    speaks: 'bot',
                    msg: {
                        text: {
                            text: "Hello~ I'm GoBo"
                        }
                    }
                },
                {
                    speaks: 'user',
                    msg: {
                        text: {
                            text: "Hello~ I'm Eric!"
                        }
                    }
                }],
            showWelcomeSent: false,
            clientToken: false,
            // clientToken:"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjI2NjYxNGY3NzJlMGRhNTAzYmUzMmIxNjJkNGJiNjg1NjZjZWY1ZGQifQ.eyJpc3MiOiJkaWFsb2dmbG93LW5uaGppZUBnb2JvLTk3ZTVlLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwic3ViIjoiZGlhbG9nZmxvdy1ubmhqaWVAZ29iby05N2U1ZS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImF1ZCI6Imh0dHBzOi8vZGlhbG9nZmxvdy5nb29nbGVhcGlzLmNvbS9nb29nbGUuY2xvdWQuZGlhbG9nZmxvdy52MmJldGExLlNlc3Npb25zIiwiZXhwIjoxNTUyNzUwODkyLjYwMDg5LCJpYXQiOjE1NTI3NDcyOTIuNjAwODl9.dEz200K7SD80A6vUq8HrHpBOlN783W0SKRrtKPYSjtiJCGyRME2ScurGyGZHIVtgKX3In_VDUTy6_skTcnTUki3qAN99ro_D0EQvCYi6vX647ZSb7HDqfSoeqpXtX5-tXEYUJahI0YmWwk-sxUTleG49xUSGQuz6U9HXxU8H69RjdhlrZpktINfccZxI48dOYZMQCCwiaZuEKV4PdwvwAzKW6GPG2MkJvnm4ZZjlkv8ADM3qPtc-KVvSjtKt6SVktGqeCR7NTfKqf9N-ZUaiKHs0gFEp9Z5zyw9o42UGz_NB8a4OWGgKN-3mVYo87xVAYUb4ue-lXDpCNU6TcGNumQ",
            regenerateToken: 0,
        };
        if (cookies.get('userID') === undefined) {
            cookies.set('userID', uuid(), {path: '/'});
        }
    }

    async dfTextQuery(text) {
        let says = {
            speaks: 'user',
            msg: {
                text: {
                    text: text
                }
            }
        };
        console.log(says);
        setTimeout(() => {
            this.setState({messages: [...this.state.messages, says]});
            console.log((this.state.messages));
        });
        const request = {
            queryInput: {
                text: {
                    text: text,
                    languageCode: 'en-AU',
                },
            }
        };

        await this.dfClientCall(request);
    };


    async dfClientCall(request) {
        let says = await {
            speaks: 'bot',
            msg: "One more time!"
        };

        console.log('ClientCall!');

        try {
            if (this.state.clientToken === false) {
                // TODO: backend implementation needed!
                console.log('Calling backend to get token');
                const res = await axios.get('https://gobo-api.cfapps.io/v1/auth',
                    {
                        headers: {
                            'Access-Control-Allow-Origin': '*',
                        }
                    });
                // axios.get('https://gobo-api.cfapps.io/v1/auth')
                //     .then(function (response) {
                //         alert(response.token);
                //     });
                console.log('Getting auth from backend: ' + res);
                console.log(res);

                this.setState({clientToken: res.data.token});
            }

            var config = {
                headers: {
                    'Authorization': 'Bearer ' + this.state.clientToken,
                    'Content-Type': 'application/json; charset=utf-8'
                }
            };

            const res = await axios.post(
                'https://dialogflow.googleapis.com/v2beta1/projects/' +
                'gobo-97e5e' +
                '/agent/sessions/' +
                "1" +
                cookies.get('userID') +
                ':detectIntent',
                request,
                config
            );

            let says = {};

            if (res.data.queryResult.fulfillmentMessages) {
                for (let msg of res.data.queryResult.fulfillmentMessages) {
                    says = {
                        speaks: 'bot',
                        msg: msg
                    };
                    this.setState({messages: [...this.state.messages, says]});
                }
            }
        } catch (e) {
            if (e.response.status === 401 && this.state.regenerateToken < 1) {
                this.setState({clientToken: false, regenerateToken: 1});
                this.dfClientCall(request);
            } else {
                let says = {
                    speaks: 'bot',
                    msg: {
                        text: {
                            text: 'I\'m having issues. Will be back later'
                        }
                    }
                };
                this.setState({messages: [...this.state.message, says]});
                console.log(this.state.message);
            }
        }
    };


    _handleInputKeyPress(e) {
        if (e.key === 'Enter') {
            this.dfTextQuery(e.target.value);
            e.target.value = '';

        }
    }

    render() {
        return (
            <div>
                <Layout className="layout" style={styles}>
                    <Title/>
                    <MessageList data={this.state.messages}/>
                    <InputForm onKeyPress={this._handleInputKeyPress}/>
                </Layout>
            </div>


        );
    }

}


const styles = {
    width: '320px',
    height: '480px',


};
export default ChatBot;
