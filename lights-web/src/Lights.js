import React from 'react';
import {Card, CardHeader, CardTitle, CardText} from 'material-ui/Card';
import './Lights.css';

class Lights extends React.Component    {
        constructor(props)      {
                super(props);
                this.state = {colour: [0,0,0]};
        }

	componentDidMount()	{
		this.timerID = setInterval(
      		() => this.fetchRGB(),
      		1000
    		);
	}

	componentWillUnmount() {
    		clearInterval(this.timerID);
  	}

	fetchRGB() {
		fetch('http://192.168.42.152:3010/')
      			.then((response) => response.json())
      			.then((responseJson) => {
             			this.setState({
                        		colour: responseJson
                		});
			})
      			.catch((error) => {
        			console.error(error);
      			});
 	 }

        render()  {
		let rgbColour = {backgroundColor:"rgb(" + this.state.colour.join(',') + ")"}
                return (
		<div style={{display: 'flex'}}>
                  <Card style={{ marginTop: 30, marginLeft: 30, marginRight: 30, flex:1}}>
                        <CardHeader 
				title="Jasmine's Lights" 
				subtitle="status of current Lights" 
			/>
			<CardTitle title="Current live colour" subtitle="RGB Values" />
                        <CardText>
                		<div style={rgbColour} className="lightsBox">
                                	{this.state.colour.join(',')}
                         	</div>
			</CardText>  
		</Card>
		<Card style={{ marginRight: 30, marginTop: 30, flex:1}}>
			<CardHeader title="Set Colour" subtitle="Change the colour of lights" />
			<CardText>
				Colour Picker
			</CardText>
		</Card>
		</div>
                )
        }
}

export default Lights;