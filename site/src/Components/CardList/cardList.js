/* eslint-disable import/first */
import React,{ Suspense } from 'react';
const ProjectCard = React.lazy(()=>import('../ProjectCard/projectCard'));
import './cardList.css';
import {Button} from 'react-bootstrap';


const Loading = ()=> <div id="loader"> <p>TESTTESTTEST</p></div>

class CardList extends React.Component{
    constructor(props){
        super (props)
        this.state={}
    }
    render (){
        return (
                <div className="col-sm-12 mb-5 mt-4 ">
                        <div id="headerContainer" className="row ml-4 mr-4">
                                <div id="container_name"className="col-6 ">
                                        <p id='section_Name'className="h2 text-left"> PROJECT(S) POPULAIRE(S) </p>
                                </div>
                                <div id="container_button" className="col-6 button" >
                                        <Button href="#" variant="outline-dark float-right" href="/projects"> Voir tous les projet(s) </Button>
                                </div>

                        </div>

                    <div id="scrolling-wrapper" className="container-fluid ">
                            
                        {
                            this.props.projects.map(project =>{
                                return <Suspense fallback={<Loading/>}>
                                            <ProjectCard key={project.id} project={project}/>
                                       </Suspense>
                            })
                        }
                        
                    </div>
                </div>
        )
    }
}

export default CardList; 