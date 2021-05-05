import React from 'react';
import './partner.css';


class Partner extends React.Component{
    render (){
        
        return (
            <div>
                <img  src={this.props.partner.logo} className="imageLogo" alt={this.props.partner.brand_name}/>
            </div>
        )
    }

}

export default Partner; 
