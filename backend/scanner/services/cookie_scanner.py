"""
Cookie Scanner

Analyzes cookies returned by the target website.
"""

from http.cookiejar import CookieJar


class CookieScanner:

    @staticmethod
    def scan(cookies: CookieJar):

        cookie_list = []

        secure_count = 0
        session_count = 0
        persistent_count = 0

        for cookie in cookies:

            is_secure = cookie.secure

            is_session = cookie.expires is None

            if is_secure:
                secure_count += 1

            if is_session:
                session_count += 1
            else:
                persistent_count += 1

            cookie_list.append({
                "name": cookie.name,
                "domain": cookie.domain,
                "path": cookie.path,
                "secure": is_secure,
                "session_cookie": is_session,
                "persistent_cookie": not is_session,
                "expires": cookie.expires
            })

        return {
            "total_cookies": len(cookie_list),
            "secure_cookies": secure_count,
            "session_cookies": session_count,
            "persistent_cookies": persistent_count,
            "details": cookie_list
        }