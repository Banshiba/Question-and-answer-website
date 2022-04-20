from django.contrib import admin
from django.urls import path
from . import views
from . views import questionsListView,questionsDetailView
urlpatterns=[
    
    path('',views.questionsListView.as_view(),name='qs-index'),
    path('questions/<int:pk>/',views.questionsDetailView.as_view(),name='qs-details'),
    path('questions/new/',views.questionsCreateView.as_view(),name='qs-create'),
    path('questions/<int:pk>/',views.CommentDetailView.as_view(),name='qs-details'),
    path('questions/<int:pk>/comment/',views.AddCommentView.as_view(),name='qs-answers'),
    
    

]