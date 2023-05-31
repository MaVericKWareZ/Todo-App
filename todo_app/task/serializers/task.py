from rest_framework import serializers

from todo_app.accounts.serializers.account import AccountSerializer

from ..models.task import Task


class TaskReadSerializer(serializers.ModelSerializer):
    creator = AccountSerializer()

    class Meta:
        model = Task
        fields = '__all__'


class TaskWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = 'creator'

    def create(self, validated_data):
        request = self.context.get('request')
        recipe = super().create({
            **validated_data,
            'creator': request.user,
        })
        return recipe

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs
