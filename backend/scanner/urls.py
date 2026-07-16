from django.urls import path
from .views import ScanWebsiteView

urlpatterns = [

    path(
        "scan/",
        ScanWebsiteView.as_view(),
        name="scan"
    ),

]