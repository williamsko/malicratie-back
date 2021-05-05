import React from 'react';
import {Carousel} from 'react-bootstrap';
import './slider.css';




class Slider extends React.Component{
    render (){
        
        return (
            <div id="slider_container" className="container-fluid">

                   <Carousel id="container_slide_all">
                       {
                        this.props.slides.map(slide => { 
                           return  <Carousel.Item  id="container_slide"> 
                           <a href={`/publication/${slide.id}`}>
                                <img id="image_slide"
                                className="d-block"
                                src={slide.content_img}
                                alt={slide.name}
                                />
                                
                                    <Carousel.Caption id="caption_part">
                                    <div id="caption_background">
                                    </div>
                                    <div id="captionContainer">
                                        <h1 id="titreSlide" >{slide.name}</h1>
                                        <p id="slideCaption"> {slide.summary} </p>
                                    </div>
                                   
                                    </Carousel.Caption>
                            </a>    
                            </Carousel.Item> 
                        })
                        
                         }
                   </Carousel>

            </div>
        )
    }
}

export default Slider;