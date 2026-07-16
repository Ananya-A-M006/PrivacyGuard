"""
Header Analysis

Analyzes the results from HeaderScanner
and assigns severity levels.
"""


class HeaderAnalysis:

    @staticmethod
    def analyze(header_scan):

        findings = []

        score = 0

        max_score = header_scan["max_score"]

        for item in header_scan["details"]:

            if item["present"]:

                findings.append({
                    "header": item["header"],
                    "status": "PASS",
                    "severity": "None",
                    "message": f"{item['header']} is configured correctly."
                })

                score += 1

            else:

                findings.append({
                    "header": item["header"],
                    "status": "FAIL",
                    "severity": item["risk"],
                    "message": item["recommendation"]
                })

        percentage = round((score / max_score) * 100)

        return {
            "score": score,
            "max_score": max_score,
            "percentage": percentage,
            "findings": findings
        }