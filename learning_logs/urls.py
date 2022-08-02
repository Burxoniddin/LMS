"""Defines url patterns for learning_logs."""

from django.urls import path

from . import views
from .views import TopicViewSet, TopicMarkViewSet, EntryViewSet

app_name = 'learning_logs'
urlpatterns = [
    
    path('api/topic/create', TopicViewSet.as_view()),
    path('api/topicmark/create', TopicMarkViewSet.as_view()),
    path('api/entry/create', EntryViewSet.as_view()),
    
    # Home page.
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),
    
    # Show all schedule.
    path('schedule/', views.schedule, name='time_table'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for a user to add a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for a user to add an Entry to a topic.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for a user to edit an Entry.for
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Page for deleting an Entry.
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
]