import { useState } from "react";
import API from "../services/api";
import "./UrlForm.css";

function UrlForm({ setResult }) {

    const [url, setUrl] = useState("");
    const [loading, setLoading] = useState(false);

    const handleScan = async () => {

        if (!url.trim()) {
            alert("Please enter a website URL.");
            return;
        }

        try {

            setLoading(true);

            const response = await API.post("/scan/", {
                url,
            });

            setResult(response.data);

        } catch (error) {

            console.error(error);

            alert("Failed to scan website.");

        } finally {

            setLoading(false);

        }

    };

    return (
        <section className="scan-box">

            <div className="container">

                <div className="scan-card">

                    <h2>Scan Website</h2>

                    <input
                        type="text"
                        placeholder="https://github.com"
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                    />

                    <button onClick={handleScan}>
                        {loading ? "Scanning..." : "Scan Website"}
                    </button>

                </div>

            </div>

        </section>
    );
}

export default UrlForm;