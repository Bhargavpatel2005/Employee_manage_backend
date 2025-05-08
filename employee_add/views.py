from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import *
from rest_framework.views import APIView
from .Serializer import *
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
        
class hr_depatment(viewsets.ModelViewSet):
    queryset = HR_department.objects.all()
    serializer_class = hr_department_Serializer

    def list(self, request, *args, **kwargs):
        # Override to customize the response for listing HR jobs
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Structure the response for the list
        response_data = []
        for item in serializer.data:
            response_data.append({
                "department": item['department'],
                "data": item
            })
        
        return Response(response_data)

    def retrieve(self, request, *args, **kwargs):
        # Override to customize the response for a single HR job
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Structure the response for a single job
        response_data = {
            "department": instance.department,
            "data": serializer.data
        }

        return Response(response_data)