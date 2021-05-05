import React from 'react';
import './slide.css';
import {Carousel} from 'react-bootstrap';


const caption = this.props.slides.slideCaption;
const caption_2 = caption.replace("\\n", "\n");

class Slide extends React.Component{
    constructor (props){
        super(props);
        this.state={slides: this.props.slide}
        console.log("team slide " + this.props.slides)
    }

    render(){
        
        return(     
        
            <Carousel.Item id="container_slide_all"> 
                <img
                className="d-block w-100 "
                src={this.props.slides.slideImgSrc}
                alt={this.props.slides.slideName}
                />
                <Carousel.Caption>
                <h3>{this.props.slides.slideName}</h3>
                <p></p>
                </Carousel.Caption>
            </Carousel.Item> 
       
        )
    }
}

export default Slide;