import React,{button} from 'react';
import './question.css';
import t from 'typy';

const reponseStyle ={

        padding:'2px',
        fontSize:'12px',
        borderStyle: 'solid',
        borderColor: 'rgb(223, 223, 223)',
        backgroundColor: 'rgb(235, 235, 235)',
        borderRadius: '4px',
        borderWidth: '1px',
        width:'32%',
        height:'50px',
}

const reponseStyle2 ={

    padding:'2px',
    fontSize:'12px',
    color:'white',
    borderStyle: 'solid',
    borderColor: 'rgb(223, 223, 223)',
    backgroundColor: 'green',
    borderRadius: '4px',
    borderWidth: '1px',
    width:'32%',
    height:'50px',
}

const reponseStyle3 ={

    padding:'2px',
    fontSize:'12px',
    color:'white',
    borderStyle: 'solid',
    borderColor: 'rgb(223, 223, 223)',
    backgroundColor: 'red',
    borderRadius: '4px',
    borderWidth: '1px',
    width:'32%',
    height:'50px',
}

const buttonStyle1 ={
    width:"100%",
    height:'100%',
    background:'rgb(0,0,0,0.0)',
    borderWidth:0
}

const buttonStyle2 ={
    color:'white',
    width:"100%",
    height:'100%',
    background:'rgb(0,0,0,0.0)',
    borderWidth:0
}

const buttonStyle3 ={
    width:"100%",
    height:'100%',
    background:'rgb(0,0,0,0.0)',
    borderWidth:0
}



class Question extends React.Component{
    constructor(props){
        super (props)
        this.state={isTrueResponse:false,clickedResponse:'', question:'',responsesNormales:[this.props.questions.wrong_answer1,this.props.questions.wrong_answer2,this.props.questions.correct_answer], randomReponses:["test","rest2","best3"]}
        this.melange = this.melange.bind(this);
        this.sendResponses =this.sendResponses.bind(this);
        this.isgoodresponse=this.isgoodresponse.bind(this);
    }

    melange(reponses){
        let i = reponses.length - 1;
        for (; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          const temp = reponses[i];
          reponses[i] = reponses[j];
          reponses[j] = temp;    
        }
       return reponses
    }

    sendResponses = async (quest) =>{
        await this.setState({randomReponses: quest});
}

    isgoodresponse = async (responseClicked)=>{
        console.log('responseClicked==> ' + responseClicked + "  responseCorrect ===> " + this.props.questions.correct_answer)
         if (responseClicked===this.props.questions.correct_answer){
            await this.setState({isTrueResponse:true})
            await this.setState({clickedResponse:responseClicked})
            this.props.score();
        }
        else {
             return responseClicked
        }
    }
   

    styleToRender(clicked){
    switch(true){
        default:
            return reponseStyle;
        case (this.state.isTrueResponse):
            return reponseStyle2;
        case  (!this.state.isTrueResponse && this.state.clickedResponse===clicked):
            return reponseStyle3;
        }
    }

    componentDidMount(){
     this.sendResponses(this.melange(this.state.responsesNormales));
    }
   
    
    render (){
        return (
        <div id="ContainerQuestionsReponseAll">
            <div id="numberContainer"> 
                <div id="number_border">
                     <p id="number">{this.props.questions.id}</p> 
                </div>
                
            </div>
            
                <div id="ContainerQuestionsReponse">
                         <p id="question"> {this.props.questions.question}</p>
                    <div id="responsesContainer">
                    <div style={this.state.isTrueResponse && this.state.clickedResponse===this.state.randomReponses[0] ? reponseStyle2: this.state.clickedResponse===this.state.randomReponses[1] && this.state.isTrueResponse!==true ? reponseStyle3 : reponseStyle}>
                                
                                    <button onClick={()=> this.isgoodresponse(this.state.randomReponses[0])} style={this.state.isTrueResponse && this.state.clickedResponse===this.state.randomReponses[0] ? buttonStyle2 : buttonStyle1} >{this.state.randomReponses[0]} </button>
                               
                           </div> 

                           <div style={this.state.isTrueResponse && this.state.clickedResponse===this.state.randomReponses[1] ? reponseStyle2: this.state.clickedResponse===this.state.randomReponses[1] && this.state.isTrueResponse!==true ? reponseStyle3 : reponseStyle}>
                                
                                <button onClick={()=> this.isgoodresponse(this.state.randomReponses[1])} style={this.state.isTrueResponse && this.state.clickedResponse===this.state.randomReponses[1] ? buttonStyle2 : buttonStyle1}>{this.state.randomReponses[1]} </button>
                               
                           </div> 

                           <div style={this.state.isTrueResponse && this.state.clickedResponse===this.state.randomReponses[2] ? reponseStyle2:  this.state.clickedResponse===this.state.randomReponses[2] && this.state.isTrueResponse!==true ? reponseStyle3 : reponseStyle}>
                                
                                <button onClick={()=> this.isgoodresponse(this.state.randomReponses[2])} style={this.state.isTrueResponse && this.state.clickedResponse===this.state.randomReponses[2] ? buttonStyle2 : buttonStyle1} >{this.state.randomReponses[2]}</button>
                               
                           </div> 
                          
                    </div>
                <hr id="hr_2"/>     
                </div>
                
                  
        </div> 
                )
    }
}

export default Question;