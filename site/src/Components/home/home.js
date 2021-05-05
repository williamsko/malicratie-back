import React from 'react';
import CardList from '../CardList/cardList';
import AboutUs from '../AboutUs/aboutUs';
import Slider from '../Slider/slider';
import Eventlist from '../EventList/eventList';
import InfoCardList from '../InfoCardList/infoCardList';



class Home extends React.Component{
    constructor(props){
        super(props);
        this.state={projects:[], events:[], publications:[],slides:[]}
    }


    componentDidMount(){
            const ProjectData = async ()=>{
    
                const urlToFetch = 'https://core.malicratie.com/endpoints/v1/projects/?limit=4'
                try{
                    const response = await fetch(urlToFetch,{cache:'no-cache'});
                    const data = await response.json();
                        this.setState({projects: data.objects})
                } catch(error){
                    console.log("ça na pas marcher " + error);
                }
              
        }

        const PublicationsData = async ()=>{
    
            const urlToFetch = 'https://core.malicratie.com/endpoints/v1/publications/?limit=3'
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                    this.setState({publications: data.objects})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }


        const EventData = async ()=>{
    
            const urlToFetch = 'https://core.malicratie.com/endpoints/v1/events/?limit=4'
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                    this.setState({events: data.objects})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }

    const SliderData = async ()=>{
    
        const urlToFetch = 'https://core.malicratie.com/endpoints/v1/publications/?add_to_slider=1'
        try{
            const response = await fetch(urlToFetch,{cache:'no-cache'});
            const data = await response.json();
                this.setState({slides: data.objects})
                console.log('les slides sont la ===>'+ JSON.stringify(this.state.slides))
        } catch(error){
            console.log("ça na pas marcher " + error);
        }
      
    }  
        EventData();
        ProjectData();
        PublicationsData();
        SliderData();
      }
     
  
    render (){
        return (
            <>
                <Slider slides={this.state.slides}/>
                <CardList projects={this.state.projects}/>
                <Eventlist events={this.state.events}/>
                <InfoCardList articles={this.state.publications}/>
                <AboutUs/>
            </>
           
        )
    }
}

export default Home;