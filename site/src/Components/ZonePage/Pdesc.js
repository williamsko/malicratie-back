import React from 'react';
import "./Pdesc.css";
import { Table } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faDownload } from '@fortawesome/free-solid-svg-icons';

class Pdesc extends React.Component {
    render (){
        return (
            <div id="Container_pdesc"> 
            <div id="infos">
                <p>Titre : <span id="infoResponses">PDESC Commune 2</span></p>
                <p>Période : <span id="infoResponses">2017-2021</span></p>
                <p> Document PDESC : <a id="linkPDF" href="#">Telecharger le fichier PDESC  <FontAwesomeIcon id="iconDownload" icon={faDownload}/></a></p>
                <p>Budget Total :<span id="infoResponses">307 000 000 F CFA</span> </p>
            </div>

            <div id ="DetailBudgetContainer">
                <p id="titreTable">Répartition du budget selon les secteurs :</p>
                    <Table striped bordered hover size="sm">
                                <thead>
                                    <tr>
                                    <th width="2%">#</th>
                                    <th width="21%">Sous-Secteur</th>
                                    <th width="22%">Objectifs</th>
                                    <th width="35%">Actions</th>
                                    <th width="5%"> Années</th>
                                    <th width="15%">Coûts</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                    <td className="align-middle">1</td>
                                    <td className="align-middle">  Emploi / travail  </td>
                                    <td className="align-middle">  Insertion des jeunes  </td>
                                    <td className="align-middle">Faciliter l’accès des jeunes (Former les jeunes sur le montage des projets et recherche de financement)</td>
                                    <td className="align-middle"> 4 </td>
                                    <td className="align-middle"> 40 000 000 F CFA </td>
                                    </tr>

                                    <tr>
                                    <td className="align-middle">2</td>
                                    <td className="align-middle">  Education/Formation  </td>
                                    <td className="align-middle">  </td>
                                    <td className="align-middle">Construire et équiper trois centres de formation pour les artisans</td>
                                    <td className="align-middle"> 4 </td>
                                    <td className="align-middle"> 35 000 000 F CFA </td>
                                    </tr>

                                    <tr>
                                    <td className="align-middle">3</td>
                                    <td className="align-middle">  Culture  </td>
                                    <td className="align-middle"> Promouvoir les valeurs culturelles positives </td>
                                    <td className="align-middle">Cultiver la cohésion sociale à travers des concertations locales sur la paix et cohésion sociale</td>
                                    <td className="align-middle"> 4 </td>
                                    <td className="align-middle"> 8 000 000 F CFA </td>
                                    </tr>

                                    <tr>
                                    <td>4</td>
                                    <td>  Communication / Information  </td>
                                    <td>  Communication/ Dialogue inclusif </td>
                                    <td>Elaborer d’un plan de communication </td>
                                    <td> 4 </td>
                                    <td> 20 000 000 F CFA </td>
                                    </tr>

                                    <tr>
                                    <td>5</td>
                                    <td>  Gouvernance  </td>
                                    <td>  Renforcement des capacités des acteurs régionaux </td>
                                    <td>Equiper et former les assemblées consulaires <td> Elaborer et mettre en œuvre le plan de formation des élus et agents du conseil Régional </td> </td>
                                    <td> 4 </td>
                                    <td> 50 000 000 F CFA </td>
                                    </tr>

                                    <tr>
                                    <td>6</td>
                                    <td>  Genre et promotions de la femme  </td>
                                    <td>  Renforcement des capacités des femmes_ Genre et développement </td>
                                    <td>Favoriser l’accès des femmes dans les instances de prise de décision (sensibilisation) <td> Renforcer les capacités des femmes en entreprenariat </td> </td>
                                    <td> 4 </td>
                                    <td> 2 000 000 F CFA </td>
                                    </tr>

                                </tbody>
                    </Table>
                </div>        
            </div>
            
        )
    }
    
}

export default Pdesc;  