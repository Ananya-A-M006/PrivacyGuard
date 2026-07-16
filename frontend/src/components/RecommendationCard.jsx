import "./Card.css";

function RecommendationCard({ result }) {

    return (

        <div className="card">

            <h2>Recommendations</h2>

            <ul>

                {result.recommendations.length===0 ?

                    <li>No recommendations 🎉</li>

                    :

                    result.recommendations.map((rec,index)=>

                        <li key={index}>{rec}</li>

                    )

                }

            </ul>

        </div>

    );

}

export default RecommendationCard;