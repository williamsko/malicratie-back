import React from 'react';
import TrackaItem from './trackaItem';
import {Form} from 'react-bootstrap';
import './tracka.css';



class Tracka extends React.Component{
    
    render (){
        return (
            <div id="Container_tracka"> 
            
               <div id="trackaItemContainer">
                <p id="intoText">Liste des dénonciations faites dans cette zone :  </p>
                    <TrackaItem/>
                    
                     
                    <div id="containerButtonDenoncer">
                        <div id="wannaComment_tracka">
                            <p id="#text_comment_tracka" > Pour faire une dénonciation il faudra se <a id="text_connect"href="#">Connecter</a>  </p>
                        </div>
                    </div>
                    <div id='addTrackaContainer'>
                            <Form>
                                <Form.Control type="textarea" placeholder="Sujet de la dénonciation" />    
                                <Form.Group id="inputCommentTracka" placeholder controlId="exampleForm.ControlTextarea1">     
                                <Form.Control as="textarea" placeholder="Ecrivez votre dénonciation" rows="5" />
                                </Form.Group>
                            </Form>
                    </div>
                </div>
                <div id="filtresContainer">
                   
                </div>       

             
                
            </div>
            
        )
    }
    
}


export default Tracka;