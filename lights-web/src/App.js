import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';
import './App.css';
import Lights from './Lights';
import DataSets from './DataSets';
import Alarm from './Alarm';
import injectTapEventPlugin from 'react-tap-event-plugin';

// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941
injectTapEventPlugin();
class App extends Component {
  render() {
    return (
	<div>
		<AppBar title="Jasmine's Lights" />
    <div style={{ display: 'flex' }} >
		    <Lights />
        <Alarm />
    </div>
		<DataSets />
    	</div>
    );
  }
}

export default App;
