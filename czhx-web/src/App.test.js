import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { shallow } from 'enzyme';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});

describe('enzyme setup', () => {
  it('should run enzyme properly', () => {
    let wrapper = shallow(<App/>);
    expect(wrapper.find('a')).toExist();
  });
});