from rest_framework.views import APIView
from rest_framework.response import Response
from guruskull_utils.models import UserMaster
from guruskull_utils.serializers import UserMasterSerializer
from django.contrib.auth import authenticate
# Create your views here.

class Welcome(APIView):
    def get(self, request):
        return Response({'message': 'Hello, world!'})

class Login(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        try:
            if username:
                username = username.lower()
                kwargs = {'username__iexact': username}
            else:
                return Response({'message': 'Login Failed. Username must required'}, status=401)
            user = UserMaster.objects.get(**kwargs)
            user_data = UserMasterSerializer(user)
            user_data = user_data.data
            if user is None:
                try:
                    active_user = UserMaster.objects.get(email=username).is_active
                except Exception as e:
                    print("error", str(e))
                    return Response({'message': 'Login Failed. Username or password incorrect'},status=401)
                if not active_user:
                    return Response({'message': 'Login Failed. User needs to Activate'},status=401)
                else:
                    return Response({'message': 'Login Failed. Username or password incorrect'},status=401)

            return Response({'message': 'Login Success', 'data': user_data}, status=200)
        except Exception as e:
            print("error in login", str(e))
            return Response({'error': str(e)}, status=400)
