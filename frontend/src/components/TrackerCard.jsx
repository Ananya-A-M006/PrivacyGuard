import "./Card.css";

function TrackerCard({ result }) {

    const tracker = result.trackers;

    return (

        <div className="card">

            <h2>Trackers</h2>

            <p>Total : {tracker.tracker_count}</p>

            <p>

                {tracker.tracker_count===0
                ?"No Trackers Found"
                :tracker.detected_trackers.join(", ")}

            </p>

        </div>

    );

}

export default TrackerCard;