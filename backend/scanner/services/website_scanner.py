import requests

from .header_scanner import HeaderScanner
from .cookie_scanner import CookieScanner
from .https_scanner import HTTPSScanner
from .session_scanner import SessionScanner
from .tracker_scanner import TrackerScanner


class WebsiteScanner:
    """
    Main Scanner Controller

    Responsibilities:
    - Send request to target website
    - Collect response
    - Delegate analysis to individual scanners
    - Return unified scan result
    """

    @staticmethod
    def scan(url: str):

        try:
            response = requests.get(
                url,
                timeout=10,
                allow_redirects=True,
                headers={
                    "User-Agent": "PrivacyGuard/1.0"
                }
            )

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e)
            }

        headers = dict(response.headers)

        result = {
            "success": True,

            "website": {
                "original_url": url,
                "final_url": response.url,
                "status_code": response.status_code
            },

            "https": HTTPSScanner.scan(response),

            "headers": HeaderScanner.scan(headers),

            "cookies": CookieScanner.scan(response.cookies),

            "session": SessionScanner.scan(response.cookies),

            "trackers": TrackerScanner.scan(response.text)
        }

        return result