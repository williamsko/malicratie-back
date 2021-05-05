import React,{button} from 'react';
import './categorie.css';

class Categorie extends React.Component{

        filterPublication(id){
                this.props.filter(id)
                console.log('lid de la categorie est ====> '+ id)
        }
        

        render (){

    return (
        <div>
            <div>
                  
                        <p id="PublicationType">Infos utiles</p>
                        <a href="#" onClick={()=> this.filterPublication(this.props.categorie.id)}>
                                <p id="resultTitle">{this.props.categorie.name}</p>
                                <div id="divider" ></div>
                        </a> 
            </div>
         
        </div>
        
        
    )
}

}

export default Categorie;