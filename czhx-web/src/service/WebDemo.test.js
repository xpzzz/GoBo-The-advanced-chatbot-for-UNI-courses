import React from 'react';
import { shallow } from 'enzyme';
import WebDemo from './WebDemo';

describe('<WebDemo />', () => {
    let wrapper = shallow(<WebDemo />);
    it('should display a WebDemo component', () => {
        expect(wrapper.find('iframe')).toExist();
    });
});