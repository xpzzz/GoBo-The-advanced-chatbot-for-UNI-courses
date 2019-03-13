import React, { Component } from 'react';

class WebDemo extends Component {
    render() {
        return (
            <div>
                <iframe
                    title="gobo"
                    height="430"
                    width="350"
                    src="https://console.dialogflow.com/api-client/demo/embedded/f86df0e3-b597-47a7-bb8b-ed861e4a6227">
                </iframe>
            </div>
        )
    }
}

export default WebDemo;