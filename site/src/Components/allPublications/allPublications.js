import React from 'react';
import PublicationBis from './PublicationBis';
import Categorie from './categorie';
import './allPublications.css';
import {Helmet} from 'react-helmet';
import Pagination from 'react-bootstrap/Pagination'


  
class allPublications extends React.Component{
    constructor (props){
        super(props);
        this.state={ publications:[ ],nbrePublications:0,categories:[],categorie_id:'',active:1}
    }
    componentDidMount(){
        const PublicationsData = async ()=>{
    
            const urlToFetch = `https://core.malicratie.com/endpoints/v1/publications/${this.state.categorie_id}`
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();    
                this.setState({publications: data.objects, nbrePublications: data.meta.total_count , items2:[]})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }
    const categorieData = async ()=>{
    
        const urlToFetch = 'https://core.malicratie.com/endpoints/v1/categories/'
        try{
            const response = await fetch(urlToFetch,{cache:'no-cache'});
            const data = await response.json();    
            this.setState({categories: data.objects})
        } catch(error){
            console.log("ça na pas marcher " + error);
        }
      
}
    categorieData();
    PublicationsData();
    }

    filterpublicationsByCategorie = async (id)=>{
        await this.setState({categorie_id:`?category__id=${id}` })
        console.log('héééé hooooo je suis cliquééééé===> '+ this.state.categorie_id)
        this.componentDidMount();
    }

    changeActive = async (num)=>{
        await this.setState({active:num, categorie_id:`?limit=20&offset=${num*20}`})
        this.componentDidMount();
     }

    render(){
        console.log('les categories sont la ===> '+ JSON.stringify(this.state.categories))
        console.log('contenu de items ===> ' + this.state.items2)


        let items = [];

       
        
        for (let number = 1; number <= (this.state.nbrePublications/20); number++) {
            items.push(
            <Pagination.Item key={number} active={number === this.state.active} onClick={()=>this.changeActive(number) } >
                {number}
            </Pagination.Item>)
            ;}
        

        return(
            <div id="master_Container_4" className="container  mb-5 mt-2 ">
                <Helmet>
                        <title>{`Malicratie | Toutes les infos du citoyens`}</title>
               </Helmet>
                <div id="headerContainer_4" >
                        <p id='section_Name'className="h2 text-left ml-5 mt-4">  Toutes les publications : {this.state.nbrePublications} </p>
                </div> 

                <div id="bodyContainer_4" className=" row container-fluid">
                        <div  id='publicationContainer'className="container col-md-9 col-sm-12 ">
                            <div>
                                {
                                    this.state.publications.map(publication => {
                                        return <PublicationBis publications={publication}/> 
                                    })
                                }
                            </div>
                                <div  id="paginationContainer">
                                            
                                        <Pagination className="pagination-success">{items}</Pagination>
              
                                </div>
                        </div>

                        <div id="FitresContainer" className="col-3">
                                <h2 id="titreFiltre" className="h2 text-center mb-2" >Catégorie(s) </h2>
                                <hr id="divider_2"/>
                                {
                                    this.state.categories.map(categorie => {
                                        return <Categorie categorie={categorie} filter={this.filterpublicationsByCategorie}/> 
                                    })
                                }
                               
                        </div> 
                </div> 

            

           </div>    
        )
    }
}

export default allPublications;