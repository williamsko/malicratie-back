import React, { Component } from 'react';
import "./sharing.css";
import {
  FacebookShareCount,

  FacebookShareButton,
  LinkedinShareButton,
  TwitterShareButton,
  WhatsappShareButton,
  EmailShareButton,
  TumblrShareButton,

  FacebookIcon,
  TwitterIcon,
  LinkedinIcon,
  EmailIcon,
  WhatsappIcon,


} from 'react-share';


class Sharing extends Component {
  render() {
    
    const shareUrl = this.props.shareUrl;
    const title = this.props.title;
    const image = this.props.image;

    return (
      <div className="Demo__container">
         <p>Partager :  </p> 
        <div className="Demo__some-network">
          <FacebookShareButton
            url={shareUrl}
            quote={title}
            className="Demo__some-network__share-button">
            <FacebookIcon
              size={24}
              round />
          </FacebookShareButton>

  
        </div>

        <div className="Demo__some-network">
          <TwitterShareButton
            url={shareUrl}
            title={title}
            className="Demo__some-network__share-button">
            <TwitterIcon
               size={24}
              round />
          </TwitterShareButton>

          
        </div>


        <div className="Demo__some-network">
          <WhatsappShareButton
            url={shareUrl}
            title={title}
            separator=":: "
            className="Demo__some-network__share-button">
            <WhatsappIcon  size={24} round />
          </WhatsappShareButton>

          <div className="Demo__some-network__share-count">
            &nbsp;
          </div>
        </div>

        <div className="Demo__some-network">
          <LinkedinShareButton
            url={shareUrl}
            windowWidth={750}
            windowHeight={600}
            className="Demo__some-network__share-button">
            <LinkedinIcon
               size={24}
              round />
          </LinkedinShareButton>
        </div>

       
       

        <div className="Demo__some-network">
          <EmailShareButton
            url={shareUrl}
            subject={title}
            body="body"
            className="Demo__some-network__share-button">
            <EmailIcon
               size={24}
              round />
          </EmailShareButton>
        </div>
       
     

       
        

      
      </div>
    );
  }
}

export default Sharing;