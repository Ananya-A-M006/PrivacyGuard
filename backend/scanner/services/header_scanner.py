"""
Header Scanner

Scans HTTP response headers and checks whether important
security headers are present.
"""


class HeaderScanner:

    SECURITY_HEADERS = {
        "Content-Security-Policy": {
            "risk": "High",
            "description": "Protects against Cross-Site Scripting (XSS).",
            "recommendation": "Implement a strong Content-Security-Policy."
        },

        "Strict-Transport-Security": {
            "risk": "High",
            "description": "Forces browsers to always use HTTPS.",
            "recommendation": "Enable HSTS with a suitable max-age."
        },

        "X-Frame-Options": {
            "risk": "Medium",
            "description": "Prevents Clickjacking attacks.",
            "recommendation": "Set X-Frame-Options to DENY or SAMEORIGIN."
        },

        "X-Content-Type-Options": {
            "risk": "Medium",
            "description": "Prevents MIME-type sniffing.",
            "recommendation": "Set X-Content-Type-Options to nosniff."
        },

        "Referrer-Policy": {
            "risk": "Low",
            "description": "Controls information shared in the Referer header.",
            "recommendation": "Use a strict Referrer-Policy."
        },

        "Permissions-Policy": {
            "risk": "Low",
            "description": "Restricts browser features like camera, microphone and geolocation.",
            "recommendation": "Define a Permissions-Policy."
        }
    }

    @staticmethod
    def scan(headers):

        results = []

        score = 0

        max_score = len(HeaderScanner.SECURITY_HEADERS)

        for header, info in HeaderScanner.SECURITY_HEADERS.items():

            if header in headers:

                results.append({
                    "header": header,
                    "status": "PASS",
                    "present": True,
                    "value": headers[header],
                    "risk": "None",
                    "description": info["description"],
                    "recommendation": None
                })

                score += 1

            else:

                results.append({
                    "header": header,
                    "status": "FAIL",
                    "present": False,
                    "value": None,
                    "risk": info["risk"],
                    "description": info["description"],
                    "recommendation": info["recommendation"]
                })

        return {

            "score": score,

            "max_score": max_score,

            "passed": score,

            "failed": max_score - score,

            "details": results
        }