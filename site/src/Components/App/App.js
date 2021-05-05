import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from '../home/home';
import Quizz from '../quizz/quizz';
import Login from '../login/login';
import ProjectPage from '../ProjectPage/projectPage';
import ZonePage from '../ZonePage/ZonePage';
import PagePublication from '../pagePublication/pagePublication'
import AllEvents from '../allEvents/allEvents';
import SearchPage from '../SearchPage/searchPage';
import AllPublications from '../allPublications/allPublications';
import AllProjectsPage from '../allProjectsPage/allProjectsPage';
import Apropos from '../ProjectPage/apropos';
import Pdesc from '../ZonePage/Pdesc';
import Tracka from '../ZonePage/tracka';
import ProjectZone from '../ZonePage/projectZone';
import CommentPart from '../ProjectPage/commentPart';
import TrackaPart from '../ProjectPage/trackaPart';
import Navbar from '../Navbar/Navbar';
import { Layout } from '../Layout/layout';
import {Route, Link, BrowserRouter as  Router, Switch} from 'react-router-dom'; 
import {Helmet} from 'react-helmet';


class App extends React.Component {
  constructor(props){
    super (props);
    this.state={query:"cin"};
    this.getDataToSearch=this.getDataToSearch.bind(this)
  }

  getDataToSearch =(data)=>{
    this.setState({query: data})

  }


  render (){
      console.log('dans query liiii mofi nek ===>'+ this.state.query)
    return (
      <React.Fragment>
       
        <Navbar recherche = {this.getDataToSearch}/>
        <Layout>
            <Router>

                <Switch>
                  <div className="App">
                     <Helmet>
                        <title>Malicratie | Le portail des jeunes patriotes</title>
                    </Helmet>
                    <Route exact path="/" component={Home}/>
                    <Route path="/projects" component={AllProjectsPage}/>
                    <Route path="/allEvents" component={AllEvents}/>
                    <Route path="/allpublications" component={AllPublications}/>
                    <Route path="/publication/:id" component={PagePublication}/>
                    <Route path="/project/:id" component={ProjectPage} />
                    <Route path="/project/:id/apropos" component={Apropos} />
                    <Route path="/project/:id/commentaires" component={CommentPart} />
                    <Route path="/project/:id/tracka" component={TrackaPart} />
                    <Route path="/search/:id" component={SearchPage}/>
                    <Route path="/zone/:id" component={ZonePage}/>
                    <Route path="/zone/:id/tracka" component={Tracka}/>
                    <Route path="/zone/:id/projects" component={ProjectZone}/>
                    <Route path="/zone/:id/pdesc" component={Pdesc}/>
                  
                  </div>
                  </Switch>  
              </Router>
        </Layout>
      </React.Fragment>
    );
  }
  
}

export default App;
