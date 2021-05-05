import React from 'react';
import t from 'typy';
import "./projectItem.css";
import Moment from 'react-moment';
import trackaBtn from './trackaBtn.png';

class ProjectItem extends React.Component{
render (){
  
    return ( 
        <div id='containerProjectItem'>
            <div id="imgContainer_pi">
                <img id="imgProject" alt=" " src={this.props.project.illustration}/>
            </div>

            <div id="detailContainer_pi">
                <div id="title">
                    <p id ="titre_project_pi">{this.props.project.name}</p>
                </div>
                <div id="otherDetail">
                    <div id="firstPart">
                        <p> Responsable(s) direct : <span id="data">{this.props.project.manager}</span></p>
                        <p> Entreprise(s) Contraté(s) :<span id="data"> {this.props.project.contracted_entreprise}</span></p>
                        <p> Début du projet : <span id="data"> <Moment  format="D MMM YYYY">{this.props.project.start_date}</Moment></span></p>
                        <p> Delai d'exécution : <span id="data">{this.props.project.duration}</span></p>
                    </div>
                    <div id="secondPart">
                        <p>Budget du Projet : <span id="data">{this.props.project.budget} F CFA </span> </p>
                        <p>Type de financement : <span id="data">{t(this.props.project, 'investment_type.name').safeObject} </span> </p>
                        <p>Financé par : <span id="data">{this.props.project.investor} </span> </p>
                        <p>Avancement du projet : <span id="data">{this.props.project.evolution}% </span> </p>
                    </div>
                </div>
            </div>
            <div id='trackaBtnContainer'>
                <img id="imgLogoTrack" alt=" " src={trackaBtn}/>
            </div>

        </div>
    )
}
}


export default ProjectItem
