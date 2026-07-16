import "./Card.css";

function CookieCard({ result }) {

    const cookie = result.cookies;

    return (

        <div className="card">

            <h2>Cookies</h2>

            <p>Secure Cookies : {cookie.score}</p>

            <p>Total Score : {cookie.percentage}%</p>

        </div>

    );

}

export default CookieCard;