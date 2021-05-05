import React from 'react';
import Event from '../Event/event';
import './eventList.css';
import {Button} from 'react-bootstrap';

class EventList extends React.Component{
    constructor(props){
        super (props);
        this.setState={ }
    }
    render (){
        return (
            <div id="conteneur" className="container-fluid">
                <div id="header_container" className="row">
                    <div className="col-6">
                           <p id="section_name" className="h2 text-left ml-4"> CALENDRIER DU CITOYEN </p>
                    </div>
                    <div className="col-6">
                            <Button  variant="outline-light float-right mr-4" href="/allEvents"> Voir tous le calendrier </Button>
                    </div>     
                </div>

                <div id="events_container" className="row" >
                   {
                       this.props.events.map(event=>{
                            return <Event key={event.id} event={event}/>
                       })
                   }
                </div>      
            </div>
        )
    }
}

export default EventList;