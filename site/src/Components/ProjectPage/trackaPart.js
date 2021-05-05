import React from 'react';
import Tracka from './tracka';
import AddTracka from './addTracka';
import "./trackaPart.css";




 class TrackaPart extends React.Component {
    constructor(props){
        super (props);
        this.state={ trackas:[],nbrTrackas:[] }
    }
    
    componentWillMount(){
        this.trackaData();
    }

     trackaData = async ()=>{
            
        const urlToFetch = `https://core.malicratie.com/endpoints/v1/trackas?project__id=${this.props.match.params.id}`
        try{
            const response =  await fetch(urlToFetch,{cache:'no-cache'});
            const data = await response.json();
                this.setState({trackas: data.objects, nbrTrackas: data.meta.total_count })
                await this.updateNbrTab();
        } catch(error){
            console.log("ça na pas marcher hein " + error);
        }
      
    }  

    render (){
        console.log('Contenu des props ===>' + JSON.stringify(this.props.match.params.id));
        console.log('Contenu dans Trackas ===>' + JSON.stringify(this.state.trackas));
        return (
            <div id="ContainerAllCommentsPart_2"> 
                <div id="containerComments">
                            <div id='subtitle'> 
                                <p>Toutes les dénonciations sur ce projet : </p> 
                            </div> 
                            <div>
                                { 
                                this.state.trackas.length>0 ?
                                            this.state.trackas.map(tracka => {
                                               return <Tracka tracka={tracka} />
                                            })   
                                           :   
                                            <p id='noComment'>Pas encore de dénonciations. Soyez le premier...</p> 
                                           
                                }
                               
                                
                            </div>
                        
                            {/* <div id="wannaComment">
                                <p id="#text_comment_2" > Pour commenter sur ce projet il faut se <a id="text_connect"href="#">Connecter</a>  </p>
                            </div>  */}
                        
                            <div>
                                <AddTracka newCommentProps={this.props.match.params.id} newComment={()=> this.AddComment()}/>
                            </div>
                          
                </div>
                
            </div>
            
        )
    }
    
}

export default TrackaPart;  