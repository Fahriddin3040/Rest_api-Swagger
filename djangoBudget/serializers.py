from rest_framework import serializers
from djangoBudget.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('user', 'category', 'reason', 'price', 'date_time')

