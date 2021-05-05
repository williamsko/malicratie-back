import React from 'react';
import {Form,Button} from 'react-bootstrap';
import "./addComment.css";
import Loader from 'react-loader-spinner';

class AddComment extends React.Component{
    constructor (props){
        super(props);
        this.state = {status:'nothing',
         newComment:{name:null, content:"", content_type:'TEXT' },
         file_audio:null,
         file_image:null,
         file_video:null,
         etat:'normal',
         buttonDisable:true,
         project_id:0,
         query:""
        }
    }

    handleInputChange = event => {
        const query = event.target.value;
        this.setState({query});
        
}


    renderForm(){
        return (
        
            <div id='textAreaContainer'>
            <Form>    
                <Form.Group id="inputComment" placeholder controlId="exampleForm.ControlTextarea1">
                    <Form.Control as="textarea" placeholder="Ecrivez votre commentaire" rows="5" 
                    value={this.state.query}
                    onChange={this.handleInputChange}
                    />
                </Form.Group>   
            </Form>
            <div id="btn_Container">
                <Button id="btn_valider" className="btn btn-success" onClick={()=>{this.sendingData()}}>  Valider  </Button>
            </div>
        </div>
        )
    }

    sendingData(){
        this.setState({status:'sending'});

        let formdata = new FormData();
        formdata.append('content',"testons")
        formdata.append('content_type','TEXT')
        formdata.append('content_img', this.state.file_image != null ? {uri: this.state.file_image.uri, name: 'image.jpg', type: this.state.file_image.type}:{ })
        formdata.append('content_video', this.state.file_video != null ? {uri: this.state.file_video.uri, name: 'video.mov', type:this.state.file_video.type}: { })
        formdata.append('name',this.state.newComment.name != null ? this.state.newComment.name : 'Anonyme')
        formdata.append('project_id', this.props.newCommentProps)

        
        
        fetch('https://core.malicratie.com/endpoints/v1/comment/new/', {
            method: 'POST',
            headers: {
              Accept: "application/json",
              'Content-Type': 'multipart/form-data',
          },
          body: formdata,
        }).then((response) => response.json())
            .then((responseJson) => {
              this.setState({status:'finished', query:null})
              return responseJson;
              
            })
            .catch((error) => {
              console.error("le commentaire n'est pas envoyé " + error);
              console.log('le commentaire na pas ete envoyé')
            });
        
    }

    sendingComment(){
        return (
            <div id='textAreaContainer'>
                  <Loader
                        type="Oval"
                        color="Green"
                        height={80}
                        width={80}
                        timeout={5000}/>
            <p> Envoi de votre commentaire en cours... </p>
          
        </div>
        )
    }

    commentAgain(){
        return (
            <div id='textAreaContainer'>
            <p> Votre commentaire à été bien envoyé. <span id="commentAgain"><a  onClick={()=> {this.setState({status:'nothing'})}}>Commenter à nouveau</a></span> </p>
            
        </div>
        )
    }

    rendering(){
        var status = this.state.status;
    switch(status){
        default:
            return this.renderForm();
        case 'sending':
            return this.sendingComment();
        case 'finished':
            return this.commentAgain();
        }
    }


    render(){
        
        console.log('informations dans le props ===>' + JSON.stringify(this.props.newCommentProps))
        console.log('informations dans le query ===>' + JSON.stringify(this.state.query))
        return (<div>
                    {this.rendering()}
                </div> 

        )
}
}

export default AddComment