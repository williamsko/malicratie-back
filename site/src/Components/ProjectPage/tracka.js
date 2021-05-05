import React from 'react';
import "./tracka.css";
import {badge} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faCheckCircle } from '@fortawesome/free-solid-svg-icons';

class  Tracka extends React.Component{
    
    
    renderImg=()=>{
        return (
            <div id="illustrationContainer">
                    <img id="com_img" alt=" " src={this.props.tracka.content_img}/>
            </div>
            
        )



    }

    render(){
        console.log('image dans les illustration :-===>' + this.props.tracka.illustration )

        return (
            <div id="CommentAllContainer"> 
                
                <div id="CommentContainer">
                    <div id="CommentHeaderContainer">
                        <div id="ContainerAvatarUserInfo"> 
                            <div id="CommentAvatar"></div>
                            <div id ="userInfos">
                                <p id="userName">{this.props.tracka.name}</p>
                                <p>Utilisateur Enregistré</p>
                            </div>
                        </div>
                        
                        <div id="creationDate">
                            <p>{this.props.tracka.sentDate}</p>
                           
                        </div>
                       
                    </div>
                    <p id="text_Comment">
                        {this.props.tracka.content_text} 
                     </p>
                     
                     {this.props.tracka.content_img != null ? this.renderImg(): null}
                </div>
                
                
            </div>
            
        )
    }
    
}

export default Tracka;  