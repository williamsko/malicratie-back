import React from 'react';
import {Button,Dropdown} from 'react-bootstrap';
import Result from '../Result/result';
import './searchPage.css';
import {Helmet} from 'react-helmet';

class SearchPage extends React.Component{
    constructor(props){
        super (props)
            this.state={results:[ ],querymot:""}
    }


    componentDidMount(){
            
        const resultData = async ()=>{
            const {params} = this.props.match;
            const paramsId =  params.id
            const urlToFetch = `https://core.malicratie.com/endpoints/v1/search/?query=${paramsId}`
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                this.setState({results: data.data, querymot:paramsId})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }
    resultData();  

    }
    render (){
        return (
            
            <div className="col-sm-12 mb-5 mt-4">
                  <Helmet>
                        <title>{`Malicratie | Resultat(s) de la recherche sur : "${this.state.querymot}"`}</title>
                  </Helmet>
                    <div id="headerContainer" className="row ml-4 mr-4">
                            <div id="container_name"className="col-6">
                                    <p id='section_Name'className="h2 text-left"> "Les resultats de cette recherches pour " {this.state.querymot} " </p>
                            </div>
                            

                    </div>

                    <div  id="container_body" className="container-fluid">
                            <div id="container_results" className="col-9">
                            {
                                this.state.results.map(result =>{
                                    return <Result results={result}/>
                                })
                            }
                            </div>
                            <div  id="FitresContainer" className="col-3">
                            
                            <p className="h2 text-left" > Filtrer par Lieu </p>
                                <input id ="filterLocation"className="form-control" type="text" placeholder="Région, cercle, Commune..." aria-label="Search"/>
                                <p className="h2 text-left mt-3" > Type(s) de resultat</p>

                                <Dropdown>
                                    <Dropdown.Toggle className="btn-lg mt-2" variant="secondary" id="dropdown-basic">
                                       Tous types de Resultat
                                    </Dropdown.Toggle>

                                    <Dropdown.Menu>
                                        <Dropdown.Item href="#/action-2">Evenements</Dropdown.Item>
                                        <Dropdown.Item href="#/action-3">Politique(s)</Dropdown.Item>
                                        <Dropdown.Item href="#/action-3">Publication(s)</Dropdown.Item>
                                    </Dropdown.Menu>
                                </Dropdown>
                            
                            </div>
                     </div>
                
            </div>
                    
                
        )
    }
}

export default SearchPage;