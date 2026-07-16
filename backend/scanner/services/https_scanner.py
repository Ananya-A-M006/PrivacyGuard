"""
HTTPS Scanner

Checks whether the website uses HTTPS
and whether HTTP requests are redirected
to HTTPS.
"""

import requests


class HTTPSScanner:

    @staticmethod
    def scan(response):

        final_url = response.url

        is_https = final_url.startswith("https://")

        redirected = len(response.history) > 0

        redirect_chain = []

        for redirect in response.history:

            redirect_chain.append({
                "status_code": redirect.status_code,
                "url": redirect.url
            })

        return {
            "https_enabled": is_https,
            "redirected": redirected,
            "final_url": final_url,
            "redirect_chain": redirect_chain,
            "status": "PASS" if is_https else "FAIL",
            "risk": "Low" if is_https else "High",
            "recommendation": (
                None if is_https
                else "Enable HTTPS and redirect all HTTP traffic to HTTPS."
            )
        }