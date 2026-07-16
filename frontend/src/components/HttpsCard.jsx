import "./Card.css";

function HttpsCard({ result }) {

    const https = result.https;

    return (

        <div className="card">

            <h2>HTTPS</h2>

            <p><strong>Status :</strong> {https.status}</p>

            <p><strong>Enabled :</strong> {https.https_enabled ? "Yes" : "No"}</p>

            <p><strong>Redirect :</strong> {https.redirected ? "Yes" : "No"}</p>

        </div>

    );

}

export default HttpsCard;