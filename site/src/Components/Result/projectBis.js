import React from 'react';
import './projectBis.css';
import {ProgressBar} from 'react-bootstrap';
import Moment from 'react-moment';


class ProjectBis extends React.Component{

    render (){
        return(
            <a id="fill-div_project" href={`/project/${this.props.projects.id}`}>
                <div id="resultContainer_2" className="row ml-1 row-sm-12">
                    
                            <div id="photo_container_2" className="col-xs-5">
                                <img id="img" src={this.props.projects.illustration} alt={this.props.projects.name}/>
                            </div>
                            <div id="Detail_container_2" className="col-xs-7">
                                <h5 id="resultTitle_2" className="text-left">{this.props.projects.name}</h5>
                                <p id="PublicationType_2">{this.props.projects.type}</p>
                                <p id="textDetail_2" className="text-left">{this.props.projects.summary}</p>
                                
                                <div id="container_avancement_pourcentage"  className="alignItems mb-2 mt-4">
                                        <span id="textAvencement" className='text-left small '>Avancement du projet :</span>
                                        <span id="textPourcentage" className=' text-right small ml-5'>{this.props.projects.evolution}% </span>
                                </div>
                                
                                <ProgressBar variant="success" className="barre" animated now={this.props.projects.evolution} />
                            </div>
                            <hr id="hr"/>
                    
                </div>
           </a>
        )
    }
}
export default ProjectBis;