import "./Card.css";

function SessionCard({ result }) {

    return (

        <div className="card">

            <h2>Session</h2>

            <p>{result.session.message}</p>

        </div>

    );

}

export default SessionCard;