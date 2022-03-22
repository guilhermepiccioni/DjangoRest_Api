from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers, models, permissions
from .serializers import UserProfileSerializer


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle updating a partial oa the object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """"""
        a_viewset = ['uses actions to create, update, partially update']
        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return {'message': message}
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Retrieves a request by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    """"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('id', 'name')
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    """Handle """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
