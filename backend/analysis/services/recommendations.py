"""
Recommendation Engine
"""


class RecommendationEngine:

    @staticmethod
    def generate(header_result,
                 cookie_result,
                 https_result,
                 session_result):

        recommendations = []

        # Header recommendations

        for finding in header_result["findings"]:

            if finding["status"] == "FAIL":
                recommendations.append(finding["message"])

        # Cookie recommendations

        for finding in cookie_result["findings"]:

            if finding["status"] == "FAIL":
                recommendations.append(finding["message"])

        # HTTPS

        if not https_result["https_enabled"]:

            recommendations.append(
                "Enable HTTPS and redirect HTTP traffic."
            )

        # Session

        if "findings" in session_result:

            for finding in session_result["findings"]:

                if finding["status"] == "FAIL":
                    recommendations.append(finding["message"])

        return recommendations