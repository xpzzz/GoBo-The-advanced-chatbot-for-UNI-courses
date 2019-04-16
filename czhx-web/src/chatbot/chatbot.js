import React, {Component} from 'react';
import Title from './components/title';
import {Layout} from 'antd';
import MessageList from './components/messageList';
import Form from './components/form';
import axios from "axios";
import Cookies from 'universal-cookie';
import {v4 as uuid} from 'uuid';

const cookies = new Cookies();
const uuidv4 = require('uuid/v4');

const SUPPORTED_COURSES = ['comp9321', 'COMP9321', 'comp9311', 'COMP9311'];
const DEFAULT_REPLY = {
    speaks: 'bot',
    msg: {
        text: {
            text: "Could you give me the course code which you would like to view ? COMP9311 or COMP9321."
        }
    }
};
const DEBUG_REPLY = {
    speaks: 'bot',
    msg: {
        text: {
            text:"Thanks! I am going to hack in this course~(You could also type a new course code to change the course~)"
            // text: "[DEBUG] Context updated!"
        }
    }
};

class ChatBot extends Component {

    constructor(props) {
        super(props);
        // These bindings are necessary to make `this` work in the callback

        this.passMessage = this.passMessage.bind(this);
        ChatBot.newSessionId = ChatBot.newSessionId.bind(this);
        this.state = {
            messages: [
                {
                    speaks: 'bot',
                    msg: {
                        text: {
                            text: "Hello~ I'm GoBo~ I could help you find some information about COMP9311 and COMP9321. Dude~"
                        }
                    }
                }],
            showWelcomeSent: false,
            clientToken: false,
            regenerateToken: 0,
            currentContext: null,
        };
        if (cookies.get('userID') === undefined) {
            cookies.set('userID', uuid(), {path: '/'});
        }
    }

    static randomIcon() {
        return [Math.floor(Math.random() * 3)];
    }

    static newSessionId() {
        let value = uuidv4();
        sessionStorage.setItem('gobo', value);
        session_ID = value;
    }

    //cant replace this passMessage just as this.dftextquery

    async dfTextQuery(text) {
        // let says = {
        //     speaks: 'user',
        //     icon: iconIndex,
        //     msg: {
        //         text: {
        //             text: text
        //         }
        //     }
        // };
        // console.log(says);
        // setTimeout(() => {
        //     this.setState({messages: [...this.state.messages, says]});
        //     console.log((this.state.messages));
        // });
        // const request = {
        //     queryInput: {
        //         text: {
        //             text: text,
        //             languageCode: 'en-AU',
        //         },
        //     }
        // }
        const request = {
            text: text,
            sessionID: session_ID,
            context: this.state.currentContext,
        };

        await this.dfClientCall(request);
    };

    async dfClientCall(request) {


        console.log('ClientCall!');

        // try {
        //     if (this.state.clientToken === false) {
        //         console.log('Calling backend to get token');
        //         await axios.get('https://gobo-api.cfapps.io/v1/auth',
        //             // const res = await axios.get('http://0.0.0.0:5000/v1/auth',
        //         ).then((response) => {
        //             console.log(response);
        //             this.setState({clientToken: response.data.token});
        //         }).catch((response) => {
        //             console.log('rejected' + response);
        //         });
        //     }
        //
        //     var config = {
        //         headers: {
        //             'Authorization': 'Bearer ' + this.state.clientToken,
        //             'Content-Type': 'application/json; charset=utf-8'
        //         }
        //     };

        // const res = await axios.post(
        //     'https://dialogflow.googleapis.com/v2beta1/projects/' +
        //     'gobo-97e5e' +
        //     '/agent/sessions/' +
        //     "1" +
        //     cookies.get('userID') +
        //     ':detectIntent',
        //     request,
        //     config
        // );

        const config = {
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'Access-Control-Allow-Origin': '*'
            }
        };
        console.log('Posting request...', request);
        const res = await axios.post(
            'https://gobo-api.cfapps.io/v1/ask',
            // 'http://localhost:5000/v1/ask',
            request,
            config
        ).catch(err => console.log(err));

        let says = {};

        console.log('response from server: ', res);

        if (res.status === 400) {
            // if context not provided
            says = {
                speaks: 'bot',
                msg: {
                    text: {
                        text: "Could you give me the course code which you would like to view ? COMP9311 or COMP9321.(You could also type a new course code to change the course~)"
                    }
                }
            }
        } else if (res.status === 200) {
            // if get a good reply
            says = {
                speaks: 'bot',
                msg: {
                    text: {
                        text: res.data.text,
                    }
                }
            };
        } else {
            // else, something went wrong
            says = {
                speaks: 'bot',
                msg: {
                    text: {
                        text: 'I\'m having issues, please wait for a moment or contact my admin',
                    }
                }
            }
        }
        console.log('updating says: ', says);
        this.setState({messages: [...this.state.messages, says]});
        // this.passMessage(this.state.messages);
        // } catch (e) {
        //     if (e.response.status === 401 && this.state.regenerateToken < 1) {
        //         this.setState({clientToken: false, regenerateToken: 1});
        //         this.dfClientCall(request);
        //     } else {
        //         let says = {
        //             speaks: 'bot',
        //             msg: {
        //                 text: {
        //                     text: 'I\'m having issues. Will be back later'
        //                 }
        //             }
        //         };
        //         this.setState({messages: [...this.state.message, says]});
        //         console.log(this.state.message);
        //     }
    }

    // because value is not define
    passMessage(value) {
        let says = {
            speaks: 'user',
            icon: iconIndex,
            msg: {
                text: {
                    text: value
                }
            }
        };
        this.setState({messages: [...this.state.messages, says]});
        // try to update context
        if (value === 'comp9321' || value === 'COMP9321') {
            setTimeout(() => {
                this.setState({
                    currentContext: 'comp9321',
                    messages: [...this.state.messages, DEBUG_REPLY]
                });
            }, 2000);
            return;

        } else if (value === 'comp9311' || value === 'COMP9311') {
            setTimeout(() => {
                this.setState({
                    currentContext: 'comp9311',
                    messages: [...this.state.messages, DEBUG_REPLY]
                });
            }, 2000);
            return;
        }
        // check context
        if (this.state.currentContext === null && !SUPPORTED_COURSES.includes(value)) {
            this.setState({messages: [...this.state.messages, says]});
            setTimeout(() => {
                this.setState({
                    messages: [...this.state.messages, DEFAULT_REPLY]
                });
            }, 2000);
        } else {
            this.dfTextQuery(value);
        }
    };

    componentWillMount() {
        if (sessionStorage.getItem('gobo')) {
            session_ID = sessionStorage.getItem('gobo');
        } else {
            ChatBot.newSessionId();
        }

        iconIndex = ChatBot.randomIcon();
        console.log('session_ID' + session_ID);
    }

    render() {
        return (
            <div>
                <Layout className="layout" style={styles}>
                    <Title/>
                    <MessageList data={this.state.messages}/>
                    <Form passMessage={this.passMessage}/>
                </Layout>
            </div>


        );
    };

}

let iconIndex = 0;
let session_ID = 0;
const styles = {
    width: '320px',
    height: '480px',


};
export default ChatBot;
