import React from 'react';
import ProjectCard from '../ProjectCard/projectCard'
import './allProjectsPage.css';
import {Dropdown} from 'react-bootstrap';
import {Helmet} from 'react-helmet';

class AllProjectsPage extends React.Component{
    constructor (props){
        super(props);
        this.state={ projects:[ ],nbreProject:0}
    }
    componentDidMount(){
        const ProjectData = async ()=>{
    
            const urlToFetch = 'https://core.malicratie.com/endpoints/v1/projects/?limit=10'
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                    this.setState({projects: data.objects, nbreProject: data.meta.total_count })
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }
    ProjectData();
    }

    render(){
        return(
            <div id="master_Container_3" className="container  mb-5 mt-2">
              <Helmet>
                        <title>{`Malicratie | Toutes les projects`}</title>
              </Helmet>
                <div id="headerContainer_3" >
                        <p id='section_Name'className="h2 text-left ml-5 mt-4"> Tous les projects : {this.state.nbreProject} </p>
                </div> 

                <div id="bodyContainer_3" className=" row container-fluid">
                        <div  id='projectsContainer'className="container col-md-9 col-sm-12 col-9">
                                {
                                    this.state.projects.map(project => {
                                        return <ProjectCard project={project}/> 
                                    })
                                }
                        </div>

                        <div id="FitresContainer" className="col-3">
                                <p className="h2 text-left" > Filtre(s) </p>
                                <input id ="filterLocation"className="form-control" type="text" placeholder="Région, cercle, Commune..." aria-label="Search"/>
                                <p className="h2 text-left mt-3" > Type(s) de project</p>

                                <Dropdown>
                                    <Dropdown.Toggle className="btn-lg mt-2" variant="secondary" id="dropdown-basic">
                                        Tous type de project
                                    </Dropdown.Toggle>

                                    <Dropdown.Menu>
                                        <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                                        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                                        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                                    </Dropdown.Menu>
                                </Dropdown>
                        </div> 
                </div> 

            

           </div>    
        )
    }
}

export default AllProjectsPage;