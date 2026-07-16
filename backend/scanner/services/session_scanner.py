"""
Session Scanner

Analyzes session cookies returned by
the website.
"""


class SessionScanner:

    SESSION_COOKIE_NAMES = [
        "sessionid",
        "session",
        "jsessionid",
        "phpsessid",
        "asp.net_sessionid",
        "connect.sid"
    ]

    @staticmethod
    def scan(cookies):

        session_cookies = []

        for cookie in cookies:

            if cookie.name.lower() in [
                name.lower() for name in SessionScanner.SESSION_COOKIE_NAMES
            ]:

                session_cookies.append({
                    "name": cookie.name,
                    "secure": cookie.secure,
                    "session_cookie": cookie.expires is None,
                    "domain": cookie.domain,
                    "path": cookie.path
                })

        return {
            "session_cookie_found": len(session_cookies) > 0,
            "count": len(session_cookies),
            "details": session_cookies
        }