import React from 'react';
import './projectZone.css';
import { Table } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faDownload } from '@fortawesome/free-solid-svg-icons';
import ProjectItem from './projectItem';

class ProjectZone extends React.Component{
    constructor(props){
        super (props);
        this.state={projects:[]}

    }

    componentDidMount(){
        const ProjectData = async ()=>{
    
            const urlToFetch = 'http://107.191.63.80/endpoints/v1/projects/?limit=10'
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                    this.setState({projects: data.objects})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }
    ProjectData();
    }


    render (){
        return (
            <div id="Container_budget"> 
            <p id="intro">Liste des projects initié dans cette zone : </p>
            {
                  this.state.projects.map(project => {
                        return  <ProjectItem project={project} />
                    })
            }
         
                      
            </div>
            
        )
    }
    
}


export default ProjectZone;