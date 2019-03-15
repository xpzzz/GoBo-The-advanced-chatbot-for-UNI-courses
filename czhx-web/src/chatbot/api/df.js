import React, {Component} from 'react';

import Cookies from 'universal-cookie';
import {v4 as uuid} from 'uuid';
import axios from 'axios/index';

const cookies = new Cookies();

class DFChatbot extends Component {
    messagesEnd;
    talkInput;

    constructor(props) {
        super(props);
        // These bindings are necessary to make `this` work in the callback
        this._handleInputKeyPress = this._handleInputKeyPress.bind(this);
        this._handleQuickReplyPayload = this._handleQuickReplyPayload.bind(this);
        this.state = {
            messages: [],
            showBot: true,
            showWelcomeSent: false,
            clientToken: false,
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
        this.setState({messages: [...this.state.messages, says]});

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

    async dfEventQuery(event) {

        const request = {
            queryInput: {
                event: {
                    name: event,
                    languageCode: 'en-AU',
                },
            }
        };

        await this.dfClientCall(request);
    };

    async dfClientCall(request) {
        try {
            if (this.state.clientToken === false) {
                // TODO: backend implementation needed!
                const res = await axios.get('api/auth');
                this.setState({clientToken: res.data.token});
            }

            var config = {
                headers: {
                    'Authorization': 'Bearer ' + this.state.clientToken,
                    'Content-Type': 'application/json; charset=utf-8'
                }
            };

            const res = await axios.post(
                'https://dialogflow.googleapis.com/v2/projects/' +
                process.env.REACT_APP_GOOGLE_PROJECT_ID +
                '/agent/sessions/' +
                process.env.REACT_APP_DF_SESSION_ID +
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
                let that = this;
                setTimeout(() => {
                    that.setState({showBot: false})
                }, 2000);
            }
        }
    };

    resolveAfterXSeconds(x) {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve(x);
            }, x * 1000)
        })
    }


}