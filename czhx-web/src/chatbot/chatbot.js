import React, {Component} from 'react';
import Title from './components/title';
import {Col, Layout, Row} from 'antd';
import MessageList from './components/messageList';
import Form from './components/form';
import axios from "axios";
import Cookies from 'universal-cookie';
import {v4 as uuid} from 'uuid';
import { Typography, Divider } from 'antd';

const {  Paragraph, Text } = Typography;
const {
    Header, Footer
} = Layout;
const cookies = new Cookies();
const uuidv4 = require('uuid/v4');

const SUPPORTED_COURSES = ['comp9321', 'COMP9321', 'comp9311', 'COMP9311'];
const DEFAULT_REPLY = {
    speaks: 'bot',
    msg: {
        text: {
            text: "Could you give me the course code which you would like to view ? COMP9311 or COMP9321."
        }
    },
    flag:0,
};
const DEBUG_REPLY = {
    speaks: 'bot',
    msg: {
        text: {
            text: "Thanks! I am going to hack in this course~(You could also type a new course code to change the course~)"
            // text: "[DEBUG] Context updated!"
        }
    },
    flag:0,
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
                    },
                    flag:0,
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
                },
                flag:0,
            }
        } else if (res.status === 200) {
            // if get a good reply
            // console.log(res.data.flag);
            // console.log(res.data.text);
            var newUrl;
            var newflag;
            if (res.data.flag == 'forum'){
                var re=/(https:\/\/)?([A-Za-z0-9]+\.[A-Za-z0-9]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*)/g;
                newUrl=res.data.text.replace(re,function(a,b,c){return '<a href="http://'+c+'">thisLink</a>';}).replace(' before you post again.','').replace('and it has been replied, you can find it through ','');
                var textlist=newUrl.split("<a");
                var url=textlist[1].split('"');
                // console.log(newUrl);
                // console.log(textlist);
                console.log(url[1]);
                newflag=1;

                says = {
                    speaks: 'bot',
                    msg: {
                        text: {
                            text: textlist[0],
                            url:url[1],
                        }
                    },
                    flag: newflag,
                };
            }else {
                newflag=0;
                says = {
                    speaks: 'bot',
                    msg: {
                        text: {
                            text: res.data.text,
                        }
                    },
                    flag: newflag,
                };
            }

        } else {
            // else, something went wrong
            says = {
                speaks: 'bot',
                msg: {
                    text: {
                        text: 'I\'m having issues, please wait for a moment or contact my admin',
                    }
                },
                flag:0,
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
            },
            flag:0,
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
                <Layout style={layout_style}>
                    <Header style={header_style}>GoBoAI ChatBot</Header>
                    <Layout style={content_style}>
                        <Row>
                            <Col span={16}>
                                <Typography style={text_style}>
                                    <h1>Introduction</h1>
                                    <Paragraph>
                                        The GoBo AI is a functional chatbot, which provides a platform for UNSW CSE current or future students to have better understanding with the courses they would like to know, in both courses information and courses related knowledge. Users are free to ask anything related to the courses and the chatbot should return knowledge based on the relevant courses.
                                     </Paragraph>
                                    <h1>Team</h1>
                                    <Paragraph>
                                        <ul>
                                            <li><a href="#">Tianpeng Chen: DevOps Developer </a></li>
                                            <li><a href="#">Yifan Zhao: Frontend Developer & ML engineer</a></li>
                                            <li><a href="#">Wenxiao Xu: Backend Developer</a></li>
                                            <li><a href="#">Minjie Huang: Scrum Master & Backend Developer</a></li>
                                        </ul>
                                    </Paragraph>
                                    <Divider />
                                </Typography>,
                            </Col>
                            <Col span={8}>
                                <Layout className="layout" style={styles}>
                                    <Title/>
                                    <MessageList data={this.state.messages} />
                                    <Form passMessage={this.passMessage}/>
                                </Layout>
                            </Col>
                        </Row>
                    </Layout>
                    <Footer style={footer_style}>&copy;2019&nbsp;CZHX</Footer>
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
    margin:'40px',
    // border: '1px solid black'


};
const layout_style = {
    height: '100%',
    width: '100%',
    position: 'absolute',
    top: '0px',
    bottom: '0px',
    textAlign:'center',
};

const header_style={
    backgroundColor: '#f4eaf5',
};

const footer_style={
    backgroundColor: '#f4eaf5',
};

const text_style={
    margin:'40px',
    height: '480px',
    // border: '1px solid black',
    textAlign: 'left',
    fontSize:'23px',
};
const content_style={
    backgroundColor: '#fff',
};
export default ChatBot;
