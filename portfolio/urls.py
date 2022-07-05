from django.urls import path
from portfolio.views import main_view, persian_view


urlpatterns = [
    path('', main_view),
    path('fa', persian_view),
]