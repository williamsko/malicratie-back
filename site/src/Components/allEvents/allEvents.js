import React from 'react';
import EventBis from './EventBis';
import './allEvents.css';

class AllEvents extends React.Component{
    constructor (props){
        super(props);
        this.state={ events:[ ],nbreEvents:0}
    }
    componentDidMount(){
        const EventData = async ()=>{
    
            const urlToFetch = 'https://core.malicratie.com/endpoints/v1/events/'
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();    
                this.setState({ events: data.objects, nbreEvents: data.meta.total_count })
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }
    EventData();
    }

    render(){
        return(
            <div id="master_Container_5" className="container  mb-5 mt-2 ">
              
                <div id="headerContainer_5" >
                        <p id='section_Name'className="h2 text-left ml-5 mt-4">  Toutes le calendrier citoyen: {this.state.nbreEvents} </p>
                </div> 

                <div id="bodyContainer_5" className=" row container-fluid">
                        <div  id='publicationContainer_5'className="container col-md-9 col-sm-12 ">
                                {
                                    this.state.events.map(event => {
                                        return <EventBis events={event} key={event.id}/> 
                                    })
                                }
                        </div>

                        <div id="FitresContainer_5" className="col-md-3">
                                <h2 id="titreFiltre" className="h2 text-center mb-2" >Filter par Lieu </h2>
                                <hr id="divider_5"/>
                                <input id ="filterLocation_2"className="form-control" type="text" placeholder="Région, cercle, Commune..." aria-label="Search"/>

                                <h2 id="titreFiltre_2" className="h2 text-center mb-2" >Filter par Mois </h2>
                                <hr id="divider_5"/>
                                <div id="ListeMois">
                                      <p>Janvier</p>
                                      <p>Fevrier</p>
                                      <p>Mars</p>
                                      <p>Avril</p>
                                      <p>Mai</p>
                                      <p>Juin</p>
                                      <p>Juillet</p>
                                      <p>Aout</p>
                                      <p>Séptembre</p>
                                      <p>Octobre</p>
                                      <p>Novembre</p>
                                      <p>Décembre</p>
                                      
                                </div>
                                
                        </div> 
                </div> 

            

           </div>    
        )
    }
}

export default AllEvents;