import React from 'react';
import './EventBis.css';
import Moment from 'react-moment';
import 'moment/locale/fr';


export default class EventBis extends React.Component{

    render (){
        console.log("date de l'evenement ===> " +  JSON.stringify(this.props.events));
        const Myobject = new Date(this.props.events.event_date) 
        console.log('dans my object ====>' + this.props.events.event_date);
        return(
       
            <div id="resultContainer" className="row ml-1 row-sm-12">
                    <div id="date_Container_5" className="col-xs-4">
                        <h2 id='date_5'> <Moment format="D MMMM YYYY" date={Myobject} locale="fr" /> </h2>
                    </div>
                    <div id="Detail_container_5" className="col-xs-8">
                        <h5 id="resultTitle_2" className="text-left">{this.props.events.title}</h5>
                        <p id="textDetail" className="text-left">{this.props.events.summary}</p>
                        <p id="lieuEvent" className="text-left">Lieu : {this.props.events.adress} </p>
                    </div>
                    <hr id="hr"/>
            </div>
        )
    }
}
