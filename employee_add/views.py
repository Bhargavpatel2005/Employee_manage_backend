from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import Employee_add,post_job,Login
from rest_framework.views import APIView
from .Serializer import EmployeeSerializer,post_jobSerializer,LoginSerializer
import jwt,datetime


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee_add.objects.all()
    serializer_class = EmployeeSerializer

class post_job(viewsets.ModelViewSet):
    queryset = post_job.objects.all().order_by('-id')
    serializer_class = post_jobSerializer
    
class RegisterView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = Login.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        playload ={
            'id':user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token =jwt.encode(playload,'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data={
            'jwt':token
        }        
        return response
    
class adminviews(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            playload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except AuthenticationFailed:
            return AuthenticationFailed('Unauthenticated')
        
        login=Login.objects.filter(id=playload['id']).first()
        serializer = LoginSerializer(login)
        return Response(serializer.data)
    
class logoutview(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success'
        }
        return response