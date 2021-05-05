import React from 'react';
import {Button} from 'react-bootstrap';
import './pagePublication.css';
import Quizz from '../quizz/quizz';
import InfoCardCategory from "../InfoCardCategory/InfoCardCategory";
import t from 'typy';

class PagePublication extends React.Component{
    constructor(props){
        super(props)
        this.state={articles:{},quizzpart:false,sameCategorieArticles:[],categorie:[2]}
    }
    componentDidMount = async ()=>{

        //recuperer information de la publication 
        const publicationData = async ()=>{
            const {params} = this.props.match;
            const urlToFetch = `https://core.malicratie.com/endpoints/v1/publications/${params.id}`
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                await this.setState({articles: data})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
  
    }

    //recuperer les infos des publications d'une mm categorie
    const sameCategoryArticlesData = async ()=>{
        const {params} = this.props.match;
        const idCategorie = t(this.state.articles.category, 'id').safeObject;
        const urlToFetch = `https://core.malicratie.com/endpoints/v1/publications/?category__id=${idCategorie}&limit=3`
        try{
            const response = await fetch(urlToFetch,{cache:'no-cache'});
            const data = await response.json();
            this.setState({sameCategorieArticles: data.objects})
        } catch(error){
            console.log("ça na pas marcher " + error);
        }

}
    await publicationData();
    sameCategoryArticlesData();
    }
   

    displayQuizz=()=>{
        this.setState({quizzpart:true})
    }
    render (){
        return this.state.quizzpart ? (<Quizz questions={this.state.articles.quizz}/>) : (
            <div id="master_Container_2" className="container  mb-5 mt-4">
              
                 
                <div id="headerContainer_2" >
                        <p id='section_Name'className="h2 text-left ml-5 mt-4"> {this.state.articles.name}</p>
                </div> 

                <div id="bodyContainer_2" className=" row container-fluid">
                        <div id="ContentPubContent" className="col-8">
                            <div id="ContainerIllustration"> 
                            {
                                this.state.articles.content_video==="///" ?
                                <img id="imgProject" alt=" " src={this.state.articles.content_img}/> :
                                <iframe width="100%" height="100%" src={this.state.articles.content_video}
                                frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                                allowfullscreen></iframe>
                            }
                                
                            </div>
                            <div id="ContentDetail">    
                                <p className="h2 text-left">Résumé</p>
                                {this.state.articles.summary}
                                <div id="quizzButton">
                                          <Button onClick={this.displayQuizz} className="mt-3" variant="outline-success" block  >J'y compris, je veux faire un quizz</Button>
                                </div>
                            </div>
                        

                        </div> 

                        <div id="AutrePublication" className="col-4">
                            <p className="h2 text-center" > Autres Publications </p>
                            <div id="otherArticleContainer"> 
                                <div>
                                        {
                                            this.state.sameCategorieArticles.map(article => {
                                                return   <InfoCardCategory article={article}/>
                                            })
                                        }
                                </div>
                               
                              
                            </div>
                        </div> 
            
                </div>

           </div>    
        )
    }
}

export default PagePublication;