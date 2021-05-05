import React from 'react';
import Question from './question';
import './quizz.css';
import t from 'typy';

const scorereal = 0;

class Quizz extends React.Component{
    constructor(props){
        super (props)
        this.state={
            questions:[this.props.questions.questions],
            score:0,
            highestScore :(this.props.questions.questions).length*10,
        }

        this.incrementScore=this.incrementScore.bind(this)
    }


    incrementScore = () =>{
        this.setState({score: this.state.score + 10 })
    }

    render (){
           

        return (
                    
                    <div id="master_Container_6" className="container-fluid mb-5 mt-2 ">
                        
                    <div id="headerContainer_6" className="row">
                            <p id='section_Name'className="h2 text-left ml-5 mt-4">  Quizz : {this.props.questions.name } </p>
                    </div> 

                    <div id="bodyContainer_6" className="row">
                            <div  id='publicationContainer_6'className="col-md-9 col-sm-12 ">
                                    {
                                        this.props.questions.questions.map(question => {
                                            return <Question questions={question} score={()=> this.incrementScore()}/>
                                        })
                                    }
                            </div>

                            <div id="FitresContainer_6" className="col-md-3">
                                <h2 id="titreFiltre" className="h2 text-center mb-2" >Votre score est de : </h2>
                                <div id="ContainerScore">
                                        <p id="score">{this.state.score}<span id="HighScore">/ {this.state.highestScore}</span></p>
                                       
                                        
                                </div> 
                                </div>
                            
                    </div> 

                

            </div>   
            
            
        )
    }
}

export default Quizz;