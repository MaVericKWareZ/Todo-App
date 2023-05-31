import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response

from todo_app.general.permissions import IsAccountOwner, IsObjectCreatorOrReadOnly
from todo_app.general.utils.cryptography import generate_key_pair

from ..models import Account
from ..serializers.account import AccountReadSerializer, AccountWriteSerializer

logger = logging.getLogger(__name__)


class AccountViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsObjectCreatorOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountWriteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        key_pair = generate_key_pair()
        name = request.data['display_name']
        account = Account.objects.create(account_number=key_pair.public, display_name=name)

        results = {
            'account': AccountReadSerializer(account).data,
            'signing_key': key_pair.private,
        }

        return Response(results, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes = [IsAccountOwner]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]
