from django.conf.urls import url, include
from . import models
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'about', views.AboutView.as_view(), name='about'),
    url(r'chat', views.ChatView.as_view(), name='chat'),
    url(r'^cryptocurrency$', views.CryptoListView.as_view(model=models.CryptoModel), name='cryptocurrency'),
    url(r'^cryptocurrency/(?P<pk>.*)/$', views.CryptoDetailView.as_view(model=models.CryptoModel), name='cryptocurrency_detail'),

    url(r'^hello/', views.hello, name='hello'),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^header/', views.display_header),
    url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contract/$', views.contract),
    url(r'publishers/$', views.PublisherList.as_view()),

    #example blog/revies/2018/01/01
    url(r'reviews/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.review_detail)
]