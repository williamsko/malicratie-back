import React from 'react';
import './PublicationBis.css';
import Moment from 'react-moment';


class PublicationBis extends React.Component{

    render (){
        return(
       
            <div id="resultContainer" className="row ml-1 row-sm-12">
                <a id="fill-div_2" href={`/publication/${this.props.publications.id}`}>
                    <div id="photo_container" className="col-xs-4">
                        <img id="img" src={this.props.publications.content_img} alt={this.props.publications.name}/>
                    </div>
                    <div id="Detail_container" className="col-xs-8">
                        <h5 id="resultTitle" className="text-left">{this.props.publications.name}</h5>
                        <p id="PublicationType">{this.props.publications.category.name}</p>
                        <p id="textDetail" className="text-left">{this.props.publications.summary}</p>
                        <p id="textDatePublication_bis" className="text-left">Publié le : <Moment  format="D MMM YYYY">{this.props.publications.created_at}</Moment></p>

                    </div>
                </a>    
                    <hr id="hr"/>
               
            </div>
        )
    }
}
export default PublicationBis;