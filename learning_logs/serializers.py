from rest_framework import serializers
from .models import Topic, Entry, TopicMark

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
 
        
class TopicMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicMark
        fields = "__all__"
        
        
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"        