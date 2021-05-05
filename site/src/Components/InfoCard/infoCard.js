import React from 'react';
import {Card, Button} from 'react-bootstrap';
import './infoCard.css';


class InfoCard extends React.Component{

    render (){
        return(
            <Card id="card1"className='card text-right shadow border-0 min-vw-20 row-sm-12'>
                <Card.Img className='card-img-top w-100 h-10 img' variant="top" src={this.props.article.content_img}/>
                <Card.Body>
                    <Card.Title id='titreArticle'className="text-left">{this.props.article.name}</Card.Title>
                    <Card.Text id="content" className="text-left font-weight-light small">
                    {this.props.article.summary}
                    </Card.Text>
                             <Button  variant="outline-dark float-left btn-sm" href={`/publication/${this.props.article.id}`}> Lire l'article </Button>
                </Card.Body>
              
            </Card>
        )
    }
}
export default InfoCard;