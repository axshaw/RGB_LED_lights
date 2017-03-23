import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';
import './App.css';
import Lights from './Lights';
import DataSets from './DataSets';

class App extends Component {
  render() {
    return (
	<div>
		<AppBar title="Jasmine's Lights" />
		<Lights />
		<DataSets />
    	</div>
    );
  }
}

export default App;
