import React from 'react';
import {Card} from 'react-bootstrap';
import Moment from 'react-moment';
import "./event.css";

class Event extends React.Component{
    render(){
        const dateToFormat = new Date(this.props.event.event_date);
        return (
            <div>
                <Card id="event" >
                        <div id="date" className="col-4 ">
                            <div id="date_child">
                                <h2 id="jour"> <Moment  format="D MMMM">{dateToFormat}</Moment></h2>
                                <h1 id="year"><Moment  format="YYYY" date= {dateToFormat}/></h1>
                            </div>
                           
                        </div>

                        <div className="col-8">
                                <Card.Body>
                                    <Card.Title id="event_titre">{this.props.event.title}</Card.Title>
                                    <Card.Text id="event_detail">
                                    {this.props.event.summary}
                                    </Card.Text>
                                    <p id="event_place"> Lieu: {this.props.event.adress} </p>
                                </Card.Body>
                        </div>
                        
                </Card>
            </div>
        )
    }
}
export default Event ;