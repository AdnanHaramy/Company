import React from 'react';
import '../News-card/news-card.css'
import { ReactComponent as FaceBook } from '../Svg/facebook.svg';
import { ReactComponent as Twitter } from '../Svg/twitter.svg';
import { ReactComponent as LinkedIn } from '../Svg/linkedin.svg';
const NewsCard = () => (
    <section className='newsCardSection'>
        <div className='newsCardContainer'>
            <div className="newsCard1">
                <div className="newsCardTextContainer">
                    <p>News</p>
                    <p>See all</p>
                </div>
                <hr />
                <div className="news">
                </div>
                <hr />
                <div className="news">
                </div>
                <hr />
                <div className="news">
                </div>
            </div>
            <div className="newsCard2">
                <div className='newsCardChild1' >
                    <h1>Blog</h1>
                    <p className='newsCardParagragh' >Visit Our SIEA Solar Blog</p>
                    <p className='newsCardParagragh'>SIEA Solar colleaguees from our various departments write about the photovoltaic market, our latest projects and company news</p>
                </div>
                <div className='newsCardChild2'>
                    <h1>Follow Us On</h1>
                    <div className="socialMediaContainer">
                        <FaceBook />
                        <Twitter />
                        <LinkedIn />
                    </div>

                </div>
            </div>
        </div>
    </section>

)
export default NewsCard;