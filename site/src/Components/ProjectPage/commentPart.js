import React from 'react';
import Comment from './comment';
import AddComment from './addComment';
import "./commentPart.css";




 class CommmentPart extends React.Component {
    constructor(props){
        super (props);
        this.state={comments:[]}
    }
    
    componentWillMount(){
        this.commentData();
    }

    addComment = async (CommentData)=>{
        const newComments = this.state.comments;
        await newComments.push(CommentData);
        this.setState({comments: newComments})
    }

    

    commentData = async ()=>{
            
        const urlToFetch = `https://core.malicratie.com/endpoints/v1/comments?project__id=${this.props.match.params.id}`
        try{
            const response =  await fetch(urlToFetch,{cache:'no-cache'});
            const data = await response.json();
                this.setState({comments: data.objects, nbrComments: data.meta.total_count })
                await this.updateNbrTab();
        } catch(error){
            console.log("ça na pas marcher hein " + error);
        }
      
    }  

    render (){
        console.log('Contenu des props ===>' + JSON.stringify(this.props.match.params.id));
        console.log('Contenu dans comments ===>' + JSON.stringify(this.state.comments));
        return (
            <div id="ContainerAllCommentsPart_2"> 
                <div id="containerComments">
                            <div id='subtitle'> 
                                <p>Tous les commentaires sur ce projet : </p> 
                            </div> 
                            <div>
                                { 
                                this.state.comments.length>0 ?
                                            this.state.comments.map(comment => {
                                               return <Comment comment={comment} />
                                            })   
                                           :   
                                            <p id='noComment'>Pas encore de commentaires. Soyez le premier...</p> 
                                           
                                }
                               
                                
                            </div>
                        
                            {/* <div id="wannaComment">
                                <p id="#text_comment_2" > Pour commenter sur ce projet il faut se <a id="text_connect"href="#">Connecter</a>  </p>
                            </div>  */}
                        
                            <div>
                                <AddComment newCommentProps={this.props.match.params.id} newComment={()=> this.AddComment()}/>
                            </div>
                          
                </div>
                
            </div>
            
        )
    }
    
}

export default CommmentPart;  