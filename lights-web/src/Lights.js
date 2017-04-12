import React from 'react';
import reactCSS from 'reactcss';
import { Card, CardHeader, CardTitle, CardText } from 'material-ui/Card';
import { HuePicker, SliderPicker, SketchPicker } from 'react-color';
import './Lights.css';
var config = require('./config.json')[process.env.NODE_ENV];

class Lights extends React.Component {
    constructor(props) {
        super(props);
        this.state = { colour: [0, 0, 0], displayColorPicker: false, color:{r:'0',g:'0',b:'0',a:'0'} };
    }

	componentDidMount()	{
		this.timerID = setInterval(
      		() => this.fetchRGB(),
      		100
    		);
	}

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    fetchRGB() {
        fetch('http://' + config.lightsIP + ':3010/')
            .then((response) => response.json())
            .then((responseJson) => {
                this.setState({
                    colour: responseJson,
                    color: {
                        r: this.state.colour[0],
                        g: this.state.colour[1],
                        b: this.state.colour[2],
                        a: '1'
                      }
                })
            })
            .catch((error) => {
                console.error(error);
            });
    }

    setRGB(newColour) {
      console.log(newColour);
      fetch('http://' + config.lightsIP + ':3010/setColour/'+newColour.r+'-'+newColour.g+'-'+newColour.b)
          .then((response) => response.json())
          .catch((error) => {
              console.error(error);
          });
    }



      handleClick = () => {
        this.setState({ displayColorPicker: !this.state.displayColorPicker })
      };

      handleClose = () => {
        this.setState({ displayColorPicker: false })
      };

      handleChange = (color) => {
        this.setRGB(color.rgb);
      };


    render() {
        let rgbColour = { backgroundColor: "rgb(" + this.state.colour.join(',') + ")" }


        const styles = reactCSS({
          'default': {
            color: {
              width: '36px',
              height: '14px',
              borderRadius: '2px',
              background: `rgba(${ this.state.color.r }, ${ this.state.color.g }, ${ this.state.color.b }, ${ this.state.color.a })`,
            },
            swatch: {
              padding: '5px',
              background: '#fff',
              borderRadius: '1px',
              boxShadow: '0 0 0 1px rgba(0,0,0,.1)',
              display: 'inline-block',
              cursor: 'pointer',
            },
            popover: {
              position: 'absolute',
              zIndex: '2',
            },
            cover: {
              position: 'fixed',
              top: '0px',
              right: '0px',
              bottom: '0px',
              left: '0px',
            },
          },
        });

        return (
            <div style={{ display: 'flex' }} >
              <Card style={{ marginTop: 30, marginLeft: 30, marginRight: 30, flex: 1 }} >
                <CardHeader title="Jasmine's Lights" subtitle="Status of Lights" />
                <CardTitle title="Current live colour" subtitle="RGB Values" />
                <CardText>
                  <div style={ rgbColour } className="lightsBox">
                  { this.state.colour.join(',') }
                  </div>
                </CardText>
              </Card>
              <Card style={{ marginRight: 30, marginTop: 30, flex: 1 }}>
                <CardHeader title="Set Colour" subtitle="Change the colour of lights" />
                <CardText>
                  <div>
                      <div style={ styles.swatch } onClick={ this.handleClick }>
                        <div style={ styles.color } />
                      </div>
                      { this.state.displayColorPicker ? <div style={ styles.popover }>
                        <div style={ styles.cover } onClick={ this.handleClose }/>
                        <SketchPicker color={ this.state.color } onChange={ this.handleChange } />
                      </div> : null }

                    </div>
                </CardText>
              </Card>
            </div>
        )
    }
}

export default Lights;
