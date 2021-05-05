import React from 'react';
import "./aboutUs.css";
import PartnersList from '../PartnersList/partnersList';

class AboutUs extends React.Component{
    constructor(props){
        super(props)
            this.state={ textAboutUs :'Rien pour le moment', partnersList: [{}],}
    }
    componentDidMount(){
        const textAboutUs = async ()=>{

            const urlToFetch = 'https://core.malicratie.com/endpoints/v1/aboutus'
            try{
                const response = await fetch(urlToFetch,{cache:'no-cache'});
                const data = await response.json();
                    this.setState({textAboutUs: data.objects[0].about})
            } catch(error){
                console.log("ça na pas marcher " + error);
            }
          
    }


    const partnerList = async ()=>{

        const urlToFetch = 'https://core.malicratie.com/endpoints/v1/partners/'
        try{
            const response = await fetch(urlToFetch,{cache:'no-cache'});
            const data = await response.json();
                this.setState({partnersList: data.objects})
        } catch(error){
            console.log("ça na pas marcher " + error);
        }
      
    }
    partnerList();
    textAboutUs();
  
}


    render(){
        return(
            <div id="conteneur"className="container-fluid">
                    <div className="row">
                        <div className="col-md-6 col-sm-12">
                                <p className="h2 text-left ml-4 mb-2 mt-3"> A PROPOS DE NOUS </p>
                                <p className="aboutUs font-weight-light text-left ml-4 mb-5">{this.state.textAboutUs}</p>
                        </div>
                        <div className="col-md-6 col-sm-12 button container" >
                                <p id="partner_title" className="h2 text-left ml-5 mb-4 mt-3"> NOS PARTENAIRES </p>
                                <div id="conteneurLogos">
                                <PartnersList list={this.state.partnersList}/>
                                </div>
                                
                        </div>

                    </div>

            </div>
        )
    }
}

export default AboutUs;