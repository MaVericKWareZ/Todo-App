from rest_framework import serializers

from ..models.account import Account


class AccountWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('account_number', 'display_image', 'display_name')
        read_only_fields = ('account_number',)

    def create(self, validated_data):
        request = self.context.get('request')
        account = super().create({
            **validated_data,
            'creator': request.user,
        })
        return account

    def validate(self, attrs):
        attrs = super().validate(attrs)
        return attrs


class AccountReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('account_number', 'display_image', 'display_name')
