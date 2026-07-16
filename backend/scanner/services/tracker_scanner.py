"""
Tracker Scanner

Detects common third-party analytics
and tracking scripts.
"""

import re


class TrackerScanner:

    TRACKERS = {
        "Google Analytics": [
            r"googletagmanager\.com",
            r"google-analytics\.com",
            r"gtag\("
        ],

        "Google Ads": [
            r"googleadservices\.com",
            r"doubleclick\.net"
        ],

        "Meta Pixel": [
            r"connect\.facebook\.net",
            r"fbq\("
        ],

        "Hotjar": [
            r"static\.hotjar\.com",
            r"hotjar"
        ],

        "Microsoft Clarity": [
            r"clarity\.ms"
        ],

        "LinkedIn Insight": [
            r"snap\.licdn\.com"
        ]
    }

    @staticmethod
    def scan(html):

        detected = []

        for tracker, patterns in TrackerScanner.TRACKERS.items():

            found = False

            for pattern in patterns:

                if re.search(pattern, html, re.IGNORECASE):
                    found = True
                    break

            if found:
                detected.append(tracker)

        return {
            "tracker_count": len(detected),
            "detected_trackers": detected
        }