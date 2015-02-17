
import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render

from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			Account.objects.create_user(**serializer.validated_data)

			return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

		return Response({
			'status': 'Bad request',
			'message': 'Account could not be created with received data.'
		}, status=status.HTTP_400_BAD_Request)

# APIView allows us to handle AJAX requests better than djnago views
class LoginView(views.APIView):
	#logging in should typically be a POST request, so we override self.post()
	def post(self, request, format=None):
		data = json.loads(request.body)

		email = data.get('email', None)
		password = data.get('password', None)

		#authenticate() is a django function that returns Account if verified
		account = authenticate(email=email, password=password)

		if account is not None:
			if account.is_active:
				# if authenticate() and user is active, create new session with login()
				login(request, account)
				#serialize the Account object found by authenticate()
				serialized = AccountSerializer(account)
				# return with resulting JSON as response
				return Respnse(serialized.data)
			else:
				return Response({
					'status': 'Unauthorized',
					'message': 'Username/password combination invalid.'
				}, status=status.HTTP_401_UNAUTHORIZED)