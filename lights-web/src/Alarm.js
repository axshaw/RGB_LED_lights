import React from 'react';
import { Card, CardHeader, CardTitle, CardText } from 'material-ui/Card';
import TimePicker from 'material-ui/TimePicker';  

class Alarm extends React.Component {

    render() {
        return (
          <Card style={{ marginRight: 30, marginTop: 30, flex: 1 }}>
            <CardHeader title="Timer" subtitle="Set the Alarm" />
            <CardText>
              <div>Time Picker
                  <TimePicker hintText="12hr Format" />
                </div>
            </CardText>
          </Card>
        )
    }
}

export default Alarm;
