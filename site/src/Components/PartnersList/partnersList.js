import React from 'react';
import './partnersList.css';
import Partner from '../partner/partner';


class PartnersList extends React.Component{

    render (){
        return (
            <div className="row conteneur">   
                <div id ="conteneurLogos" className="container mt-2 ">
                       {
                           this.props.list.map(partner=>{
                               return <Partner key={partner.id} partner={partner}/>
                           })
                       } 
                </div>
              
            </div>
            
        )
    }
}

export default PartnersList;