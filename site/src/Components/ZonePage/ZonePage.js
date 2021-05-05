import React from 'react';
import './ZonePage.css';
import {Nav,Badge} from 'react-bootstrap';
import {Link } from 'react-router-dom';
import Mairie from './Mairie.jpg'



class ZonePage extends React.Component{
    
    constructor(props){
        super(props);
        this.state={zone:{id:5, illustration: Mairie, type:"Commune", name:"Commune 2",parent:"District de Bamako", population:"2 000 000", area:"2 992",coords:"1003993,3039494",manager:"‎Adama Sangaré‎"   }}
    }
    
   
    
    render (){

         
        return (
            <div id="master_Container_zonePage" className="container  mb-5 mt-4">
              

                <div id="bodyContainer_zonepage" className=" row container-fluid">
                        <div id="ContainerImgProject_zonepage" className="col-5">
                            <img id="imgProject_zonepage" alt=" " src={this.state.zone.illustration}/>
                        </div> 

                    <div id="projectDetail_zonepage" className="col-7">
                        <p id="project_type_zonepage">{this.state.zone.type}</p>
                        <h4 id ="titre_project_zonepage"className="mb-4">{this.state.zone.name}</h4>
                       
                        <p>Se Trouve dans : <span id="data">{this.state.zone.parent}</span> </p>
                        <p>Population : <span id="data">{this.state.zone.population} </span> </p>
                        <p>Superficie : <span id="data">{this.state.zone.area} Km2</span> </p>
                        <p>Coordonnées GPS: <span id="data">{this.state.zone.coords}</span></p>
                        <p>Maire :<span id="data"> {this.state.zone.manager}</span></p>
                    </div> 
           

            <div id="containerTab">

                <div id="dividerContainer"> 
                        <hr id="divider"/> 
                </div>

                 <Nav justify variant="tabs" defaultActiveKey={`/zone/${this.state.zone.id}/tracka`}>
                    <Nav.Item>
                        <Nav.Link href={`/zone/${this.state.zone.id}/tracka`}>
                             <Link id="link" to={`/zone/${this.state.zone.id}/tracka`}>Dénonciation(s) <Badge id="badge" variant="success">Tracka</Badge></Link>
                        </Nav.Link>
                    </Nav.Item >
                    
                    <Nav.Item>
                         <Nav.Link href={`/zone/${this.state.zone.id}/projects`}>
                             <Link id="link" to={`/zone/${this.state.zone.id}/projects`} >Projects</Link>
                         </Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                         <Nav.Link href={`/zone/${this.state.zone.id}/pdesc`}>
                             <Link id="link" to={`/zone/${this.state.zone.id}/pdesc`} >PDESC</Link>
                         </Nav.Link>     
                    </Nav.Item>
                  
                </Nav>
                      
                </div>

            </div>
                
            
            </div>
        )
    }
}

export default ZonePage;