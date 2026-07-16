import { useState } from "react";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import UrlForm from "../components/UrlForm";
import Footer from "../components/Footer";

import ScoreCard from "../components/ScoreCard";
import HttpsCard from "../components/HttpsCard";
import HeaderCard from "../components/HeaderCard";
import CookieCard from "../components/CookieCard";
import SessionCard from "../components/SessionCard";
import TrackerCard from "../components/TrackerCard";
import RecommendationCard from "../components/RecommendationCard";

import "./Home.css";

function Home() {

    const [result, setResult] = useState(null);

    return (
        <>
            <Navbar />

            <Hero />

            <UrlForm setResult={setResult} />

            {result && (
                <>
                    <ScoreCard result={result} />

                    <div className="container dashboard-grid">

                        <HttpsCard result={result} />

                        <HeaderCard result={result} />

                        <CookieCard result={result} />

                        <SessionCard result={result} />

                        <TrackerCard result={result} />

                        <RecommendationCard result={result} />

                    </div>
                </>
            )}

            <Footer />
        </>
    );
}

export default Home;