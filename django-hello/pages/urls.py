from django.urls import path
from .views import AboutPageView, HomePageView

urlpatterns = [ # maps a particular endpoint (str) to a view within the app
    # path('', homePageView, name='home'),
    path('', HomePageView.as_view(), name='home'), 
    path('about', AboutPageView.as_view(), name='about')
]