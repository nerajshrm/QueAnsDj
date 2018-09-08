from django.conf.urls import  url
from django.urls import path,include
from QueAns.views import QuesView,ScoreView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',QuesView,name='index'),
    path('score/',ScoreView,name='score')
    # path('ques',QuesView.as_view(),name='que'),
    # path('ques/list',QuesListView.as_view(),name='quelist'),
    # url(r'^(<?P<pk>[-\w]+)/$',QuesDetView.as_view(),name='detail'),
]
