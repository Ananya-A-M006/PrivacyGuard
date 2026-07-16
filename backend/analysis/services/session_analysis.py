"""
Session Analysis
"""


class SessionAnalysis:

    @staticmethod
    def analyze(session_scan):

        if not session_scan["session_cookie_found"]:

            return {
                "status": "INFO",
                "message": "No session cookies detected."
            }

        findings = []

        for cookie in session_scan["details"]:

            if cookie["secure"]:

                findings.append({
                    "cookie": cookie["name"],
                    "status": "PASS",
                    "message": "Secure session cookie."
                })

            else:

                findings.append({
                    "cookie": cookie["name"],
                    "status": "FAIL",
                    "severity": "High",
                    "message": "Session cookie should be Secure."
                })

        return {
            "count": session_scan["count"],
            "findings": findings
        }