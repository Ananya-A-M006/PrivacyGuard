"""
Cookie Analysis

Analyzes cookies collected by CookieScanner.
"""


class CookieAnalysis:

    @staticmethod
    def analyze(cookie_scan):

        findings = []

        score = 0

        total = cookie_scan["total_cookies"]

        if total == 0:

            return {
                "score": 0,
                "percentage": 100,
                "findings": [
                    {
                        "status": "INFO",
                        "message": "No cookies detected."
                    }
                ]
            }

        for cookie in cookie_scan["details"]:

            if cookie["secure"]:

                findings.append({
                    "cookie": cookie["name"],
                    "status": "PASS",
                    "message": "Secure cookie."
                })

                score += 1

            else:

                findings.append({
                    "cookie": cookie["name"],
                    "status": "FAIL",
                    "severity": "High",
                    "message": "Cookie should use the Secure attribute."
                })

        percentage = round((score / total) * 100)

        return {
            "score": score,
            "percentage": percentage,
            "findings": findings
        }