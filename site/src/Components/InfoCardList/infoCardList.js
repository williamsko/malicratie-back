import React from 'react';
import InfoCard from '../InfoCard/infoCard';
import './infoCardList.css';
import {Button} from 'react-bootstrap';

class CardList extends React.Component{
    render (){
        return (
                <div className="col-sm-12 mb-5 mt-4">
                    <div id="headerContainer" className="row ml-4 mr-4">
                            <div id="container_name"className="col-6">
                                    <p id='section_Name'className="h2 text-left"> INFOS DU CITOYEN </p>
                            </div>
                            <div id="container_button" className="col-6 button container" >
                                    <Button  variant="outline-dark float-right" href="/Allpublications"> Voir tous les Article(s) </Button>
                            </div>

                    </div>

            

                    <div className="container-fluid">
                            {
                                this.props.articles.map(article => {
                                    return <InfoCard article ={article}/>
                                })
                            }
                    </div>
                </div>
        )
    }
}

export default CardList; 