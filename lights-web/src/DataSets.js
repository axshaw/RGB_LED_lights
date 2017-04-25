import React from 'react';
import { Card, CardHeader, CardTitle, CardText } from 'material-ui/Card';

class DataSets extends React.Component {

    render() {
        return (
          <div>
            <Card style={{ marginLeft: 30, marginRight: 30, marginTop: 30 }} >
              <CardHeader title="Data URLs" subtitle="Source of Data Streams" />
              <CardTitle title="URLS" subtitle="Feeds used for app" />
              <CardText>
                <ul>
                  <li> 52.629316, -0.407777 </li>
                  <li> http://api.sunrise-sunset.org/json?lat=52.629316&lng=-0.407777&date=today </li>
                  <li> http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3462/?res=hourly&key=cee0b1ec-a751-458a-894e-6aec68a91beb</li>
                  <li> http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/3462/?res=3hourly&key=cee0b1ec-a751-458a-894e-6aec68a91beb</li>
                  <li>https://fnpyq47dr5.execute-api.eu-west-1.amazonaws.com/prod/met-barnack-obs</li>
		  <li>https://emoncms.org/feed/value.json?id=149796&apikey=2abd3073e21f9af1a566544f64ceb7b9</li>

              </ul>
              </CardText>
            </Card>
          </div>
        )
    }
}

export default DataSets;
