import React from 'react';
import './result.css';
import EventBis from '../allEvents/EventBis';
import ProjectBis from './projectBis';
import PublicationBis from '../allPublications/PublicationBis';
import GeoZoneBis from './geozoneBis'

class Result extends React.Component{
    render (){
        if (this.props.results.model === 'Event'){
            return ( <EventBis events={this.props.results}  /> )
        }else if (this.props.results.model === 'Project') {
            return(<ProjectBis projects={this.props.results}/>)
        }else if (this.props.results.model === 'Geo' && this.props.results.type === "COMMUNE") {
            return( <GeoZoneBis geo={this.props.results}  />)
        }else{
            return null
        }
    }
}

export default Result;