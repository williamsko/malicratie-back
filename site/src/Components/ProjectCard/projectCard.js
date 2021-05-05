import React from 'react';
import {Card,ProgressBar} from 'react-bootstrap';
import './projectCard.css';


class ProjectCard extends React.Component{
   
    render (){
        return(
           
                <Card id="CardProject" className='card text-right shadow border-0 m-3 row-sm-12'>
                     
                        <span className="badge badge-pill badge-light m-2">{this.props.project.late_delay} Mois de retard</span>   
                        <a id="fill-div" href={`/project/${this.props.project.id}/apropos`}>
                        <Card.Img className='card-img-top w-100 h-10 img' variant="top" src={this.props.project.illustration}/>
                        <Card.Body>
                            <Card.Title id='titreProject'className="text-left">{this.props.project.name}</Card.Title>
                            <Card.Text id="resume" className="text-left font-weight-light small">
                            {this.props.project.summary}
                            </Card.Text>
                            <div id="container_avancement_pourcentage"  className="alignItems mb-2 mt-4">
                                    <span id="textAvencement" className='text-left small '>Avancement du projet :</span>
                                    <span id="textPourcentage" className=' text-right small ml-5'>{this.props.project.evolution}% </span>
                            </div>
                            
                            <ProgressBar variant="success" className="barre" animated now={this.props.project.evolution} />
                        </Card.Body>
                    </a>
                </Card>
            
        )
    }
}
export default ProjectCard;