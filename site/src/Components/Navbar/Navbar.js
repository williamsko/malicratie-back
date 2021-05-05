import React, { Fragment } from 'react';
import {Navbar, Nav, Form, Button} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faSearch } from '@fortawesome/free-solid-svg-icons';
import './Navbar.css';
import SearchPage from '../SearchPage/searchPage';
import Home from '../home/home';
import logoMalicratie from './logoMalicratie.svg';
import AllProjectsPage from '../allProjectsPage/allProjectsPage';
import AllPublications from '../allPublications/allPublications';
import {Link,Route,BrowserRouter} from 'react-router-dom'; 
class NavBar extends React.Component{
    
    constructor(props){
        super (props)
            this.state={query:""}
        
    }
   handleInputChange = event => {
            const query = event.target.value;
            this.setState({query});
            
    }



    render (){
        var querySansEspace = this.state.query;
            querySansEspace = querySansEspace.replace(/\s/g,'');
        const url =`/search/${querySansEspace}`;
        console.log("Dans props recherche il y a  ca ===> " + this.props.recherche)
        return (
       
            <Navbar  className="shadow" bg="light" expand="lg">
           
                <Navbar.Brand href="/" className="ml-2 mr-4" >
                    <img id="logo" src={logoMalicratie} alt="Logo Malicratie"/>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Form action={url} id="barContainer" className=" input-group w-45 mr-4">
                    <div class="input-group w-100 ">
                        <input 
                        value={this.state.query}
                        onChange={this.handleInputChange} 
                        type="search"
                        placeholder="Project, lieu, publication..." 
                        aria-describedby="button-addon5" 
                        class="form-control"
                        href={url}
                        
                        />
                        <div class="input-group-append">
                        <Button id="buttonSearch" type="submit"><FontAwesomeIcon id="icon" icon={faSearch}/> </Button>
                        </div>
                    </div>
                    </Form>
                  
                    <Nav className="mr-auto">
                        
                           
                            <Nav.Link id="menuItem" className="text-dark" href='/projects'>Politiques Actuelles</Nav.Link>
                            <Nav.Link  id="menuItem"  className="text-dark" href='/AllPublications'>Infos du citoyen</Nav.Link>
                        
                                <a href="/"><p id="sign" > Connexion </p> </a>
                                <p id="sign_2" > |</p>
                                <a href="/" > <p id="sign_2"  > S'inscrire </p> </a>
                            
                        
                    </Nav>
                    
                </Navbar.Collapse>
            </Navbar>
            
              
        )
    }
}

export default NavBar;