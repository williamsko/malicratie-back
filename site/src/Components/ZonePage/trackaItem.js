import React from 'react';
import "./trackaItem.css";
import {badge} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faCheckCircle } from '@fortawesome/free-solid-svg-icons';

const TrackaItem = () =>{
    return (
        <div id="trackaAllContainer"> 
            
            <div id="trackaContainer">
                <div id="trackaHeaderContainer">
                    <div id="ContainerAvatarUserInfo"> 
                        <div id="trackaAvatar"></div>
                        <div id ="userInfos">
                            <p id="userName">Abdoulaye Sanogo</p>
                            <p>Utilisateur Enregistré</p>
                        </div>
                    </div>
                    
                    <div id="creationDate">
                        <p> il y a 3 mois</p>
                        <span id="badgeVerifie"class="badge badge-pill badge-success"> <FontAwesomeIcon id="iconChecked" icon={faCheckCircle}/> Info Verifié</span>
                    </div>
                   
                </div>
                <p id="titre_tracka">
                    Gestion du budget de la commune
                </p>
                <p id="text_tracka">
                Ex turba vero imae sortis et paupertinae in tabernis aliqui pernoctant vinariis, non nulli velariis umbraculorum theatralium latent, quae Campanam imitatus lasciviam Catulus in aedilitate sua suspendit omnium primus; aut pugnaciter aleis certant turpi sono fragosis naribus introrsum reducto spiritu concrepantes; aut quod est studiorum omnium maximum ab ortu lucis ad vesperam sole fatiscunt vel pluviis, per minutias aurigarum equorumque praecipua vel delicta scrutantes.
                </p>
            </div>
            
            
        </div>
        
    )
}

export default TrackaItem;  