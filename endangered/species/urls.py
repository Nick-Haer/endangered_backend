from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # # ex: /polls/5/
    path('<str:name>/getMatchingCharities',
         views.getMatchingCharities, name='getMatchingCharities'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('getAllAnimals', views.getAllAnimals, name='getAllAnimals')
]
