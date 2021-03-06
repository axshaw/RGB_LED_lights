import React from 'react';
import reactCSS from 'reactcss';
import { Card, CardHeader, CardTitle, CardText} from 'material-ui/Card';

import { SketchPicker } from 'react-color';
import RaisedButton from 'material-ui/RaisedButton';
import './Lights.css';

class Lights extends React.Component {
    constructor(props) {
        super(props);
        this.state = { colourJSON: [0, 0, 0], displayColorPicker: false, colour:{r:'0',g:'0',b:'0',a:'0'} };
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
        fetch('http://' + [process.env.REACT_APP_LIGHTS_IP] + ':3010/')
            .then((response) => response.json())
            .then((responseJson) => {
                this.setState({
                    colourJSON: responseJson,
                    colour: {
                        r: responseJson[0],
                        g: responseJson[1],
                        b: responseJson[2],
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
      fetch('http://' + [process.env.REACT_APP_LIGHTS_IP] + ':3010/setColour/'+newColour.r+'-'+newColour.g+'-'+newColour.b)
          .then()
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

      handleChange = (colour) => {
        this.setRGB(colour.rgb);
      };


    render() {

        const style = {
          margin: 12,
        };

        const styles = reactCSS({
          'default': {
            colour: {
              width: '100%',
              height: '25px',
              borderRadius: '2px',
              background: `rgba(${ this.state.colour.r }, ${ this.state.colour.g }, ${ this.state.colour.b }, 1)`,
            },
            swatch: {
              width: '100%',
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
              <Card style={{ marginTop: 30, marginLeft: 30, marginRight: 30, flex: 1 }} >
                <CardHeader title="Jasmine's Lights" subtitle="Status of Lights" />
                <RaisedButton label="Turn Off" primary={true} style={style} onClick={() => { this.setRGB({r:'0',g:'0',b:'0',a:'0'}) }}/>
                <CardTitle title="Current live colour" subtitle="RGB Values" />
                <CardText>
                    <div style={ styles.swatch } onClick={ this.handleClick }>
                      <div style={ styles.colour } />
                    </div>
                    { this.state.displayColorPicker ? <div style={ styles.popover }>
                      <div style={ styles.cover } onClick={ this.handleClose }/>
                      <SketchPicker color={ this.state.colour } onChange={ this.handleChange } />
                    </div> : null }

                </CardText>
              </Card>
        )
    }
}

export default Lights;
