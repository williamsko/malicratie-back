import React from 'react';
import './geozoneBis.css';
import Moment from 'react-moment';


export default class GeoZoneBis extends React.Component{

    render (){
        
        return(
            <a id="fill-div_project" href={`/zone/${this.props.geo.id}`}>
                <div id="resultContainer" className="row ml-1 row-sm-12">
                        <div id="GeoImageContainer" className="col-xs-4">
                        <p id="textGeoImage">Commune</p>
                        </div>
                        <div id="Detail_container_5" className="col-xs-8">
                            <h5 id="resultTitle_2" className="text-left">{this.props.geo.name}</h5>
                            <p id="textDetail" className="text-left"></p>
                            <p id="lieuEvent" className="text-left">{this.props.geo.type} </p>
                            <p id="lieuEvent" className="text-left">Nombre d'habitant : {this.props.geo.nb_hbts} </p>
                            <p id="lieuEvent" className="text-left">Manager : {this.props.geo.manager} </p>
                            <p id="lieuEvent" className="text-left">Coordonnées geographiqued : {this.props.geo.lon} / {this.props.geo.lat} </p>

                        </div>
                        <hr id="hr"/>
                </div>
             </a>
        )
    }
}
