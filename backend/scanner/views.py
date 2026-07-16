from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ScanSerializer
from .services.website_scanner import WebsiteScanner

from analysis.services.header_analysis import HeaderAnalysis
from analysis.services.cookie_analysis import CookieAnalysis
from analysis.services.session_analysis import SessionAnalysis
from analysis.services.score_engine import ScoreEngine
from analysis.services.recommendations import RecommendationEngine


class ScanWebsiteView(APIView):

    def post(self, request):

        serializer = ScanSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        url = serializer.validated_data["url"]

        scan = WebsiteScanner.scan(url)

        if not scan["success"]:
            return Response(scan,
                            status=status.HTTP_400_BAD_REQUEST)

        # Analysis

        header_analysis = HeaderAnalysis.analyze(scan["headers"])

        cookie_analysis = CookieAnalysis.analyze(scan["cookies"])

        session_analysis = SessionAnalysis.analyze(scan["session"])

        # Overall Score

        score = ScoreEngine.calculate(
            header_analysis,
            cookie_analysis,
            scan["https"],
            session_analysis
        )

        # Recommendations

        recommendations = RecommendationEngine.generate(
            header_analysis,
            cookie_analysis,
            scan["https"],
            session_analysis
        )

        # Grade

        if score >= 90:
            grade = "A+"

        elif score >= 80:
            grade = "A"

        elif score >= 70:
            grade = "B"

        elif score >= 60:
            grade = "C"

        else:
            grade = "D"

        return Response({

            "website": scan["website"],

            "overall_score": score,

            "grade": grade,

            "https": scan["https"],

            "headers": header_analysis,

            "cookies": cookie_analysis,

            "session": session_analysis,

            "trackers": scan["trackers"],

            "recommendations": recommendations

        })