import "./Card.css";

function HeaderCard({ result }) {

    const header = result.headers;

    return (

        <div className="card">

            <h2>Security Headers</h2>

            <p>Passed : {header.score}</p>

            <p>Failed : {header.max_score-header.score}</p>

            <p>Coverage : {header.percentage}%</p>

        </div>

    );

}

export default HeaderCard;