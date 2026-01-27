from django.urls import path
from web.views import landing_page


urlpatterns = [
    path('', landing_page, name='landing_page'),
]