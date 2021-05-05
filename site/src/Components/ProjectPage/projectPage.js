import React from 'react';
import './projectPage.css';
import {ProgressBar,Nav} from 'react-bootstrap';
import { Route, Link } from 'react-router-dom';
import t from 'typy';
import Sharing from '../Sharing/sharing';
import {Helmet} from 'react-helmet';



class ProjectPage extends React.Component{
    
    constructor(props){
        super(props);
        this.state={project:{}}
    }
    
    componentDidMount(){
        const ProjectData2 = async ()=>{
            const {params} = this.props.match;
            const urlToFetch = `https://core.malicratie.com/endpoints/v1/projects/${params.id}`
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                this.setState({project: data})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
  
    }
    ProjectData2();
    }
    render (){

         
        return (

            <div id="master_Container_1" className="container  mb-5 mt-4">
              
              <Helmet>
                        <title>{`Malicratie | Projet : ${this.state.project.name}`}</title>
             </Helmet>
                <div id="bodyContainer_1" className=" row container-fluid">
                        <div id="ContainerImgProject" className="col-5">
                            <img id="imgProject" alt=" " src={this.state.project.illustration}/>
                        </div> 

                    <div id="projectDetail" className="col-7">
                       <Sharing shareUrl={`www.malicratie.com/project/${this.state.project.id}/apropos`} image={this.state.project.illustration} title={`Le projet: ${this.state.project.name}`}/>
                        <p id="project_type">{t(this.state.project, 'type.name').safeObject}</p>
                        <h4 id ="titre_project"className="mb-4">{this.state.project.name}</h4>
                       
                        <p>Budget du Projet : <span id="data">{this.state.project.budget}</span> </p>
                        <p>Type de financement : <span id="data">{t(this.state.project, 'investment_type.name').safeObject} </span> </p>
                        <p>Financé par : <span id="data">{this.state.project.investor} </span> </p>
                        <p> Responsable(s) direct : <span id="data">{this.state.project.manager}</span></p>
                        <p> Entreprise(s) Contraté(s) :<span id="data"> {this.state.project.contracted_entreprise}</span></p>
                        <p> Début du projet : <span id="data">{this.state.project.start_date}</span></p>
                        <p> Delai d'exécution : <span id="data">{this.state.project.duration}</span></p>
                    <ProgressBar variant="success" className="barre mt-4" animated now={this.state.project.evolution}/>
                    </div> 
           

            <div id="containerTab">

                <div id="dividerContainer"> 
                        <hr id="divider"/> 
                </div>

                 <Nav justify variant="tabs" defaultActiveKey={`/project/${this.state.project.id}/apropos`}>
                    <Nav.Item>
                        <Nav.Link href={`/project/${this.state.project.id}/apropos`}>
                             <Link id="link" to={`/project/${this.state.project.id}/apropos`}>À propos du project</Link>
                        </Nav.Link>
                    </Nav.Item>

                    <Nav.Item>
                        <Nav.Link href={`/project/${this.state.project.id}/commentaires`}>
                            <Link id="link" to={`/project/${this.state.project.id}/commentaires`}>Commentaires</Link>
                        </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link href={`/project/${this.state.project.id}/tracka`}>
                            <Link id="link" to={`/project/${this.state.project.id}/tracka`} >Dénonciation(s)</Link>
                        </Nav.Link>        
                    </Nav.Item>

                </Nav>
                      
                </div>

            </div>
                
            
            </div>
        )
    }
}

export default ProjectPage;