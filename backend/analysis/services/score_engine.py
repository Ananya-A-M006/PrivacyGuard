"""
Score Engine

Calculates the final PrivacyGuard score.
"""


class ScoreEngine:

    @staticmethod
    def calculate(header_result,
                  cookie_result,
                  https_result,
                  session_result):

        score = 0

        max_score = 100

        # Headers = 40%

        score += header_result["percentage"] * 0.40

        # Cookies = 25%

        score += cookie_result["percentage"] * 0.25

        # HTTPS = 20%

        if https_result["https_enabled"]:
            score += 20

        # Session = 15%

        if session_result.get("count", 0) == 0:

            score += 15

        else:

            secure = 0

            for item in session_result["findings"]:

                if item["status"] == "PASS":
                    secure += 1

            score += (secure / session_result["count"]) * 15

        return round(score)