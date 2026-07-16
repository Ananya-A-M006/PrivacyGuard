import "./ScoreCard.css";

function ScoreCard({ result }) {

    return (

        <section className="container">

            <div className="score-card">

                <h2>Overall Security Score</h2>

                <h1>{result.overall_score}/100</h1>

                <h3>Grade : {result.grade}</h3>

            </div>

        </section>

    );

}

export default ScoreCard;