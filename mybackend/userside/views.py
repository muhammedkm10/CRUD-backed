from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Userserializer
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

class ListUser(APIView):
    def post(self , request):
        if request.data:
            print("innerjfak jdfkjaf fjadskfj alksdj fals")
            username = request.data['name']
            password = request.data['password']
            email  = request.data['email']
            phone = request.data['phone']
            if username is None:
                return Response("needed")
            try:
                already = User.objects.get(username = username)
            except:
                already  = None
            print(already)
            if already is not None:
                return Response('already')
            user = User.objects.create_user(username=username, password=password, email=email)
            user.phone = phone
            user.is_staff = True
            user.save()
            return Response("created")
        
        return Response("not saved")





class LoginByUser(APIView):
    def post(self , request):
        username = request.data['username']
        password  = request.data['password']
        print(password)
        try:
          user = User.objects.get(username=username)
        except:
            user  = None
        if user is not None:
             if check_password(password, user.password):
                return Response("authenticated")
             else:
                 return Response("incurrect")
        else:
            return Response("notfound")
        
    def put(self , request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]
            details = AccessToken(token)
            userid = details['user_id']
            print(request.data['username'])
            try:
                already = User.objects.get(username = request.data['username'])
            except:
                already = None
            if already is not None:
                if already.id  != userid:
                   print("already id ",already.id)
                   return Response("already")
            obj = User.objects.get(id = userid)
            obj.username = request.data['username']
            
            
            obj.email = request.data['email']
            obj.phone = request.data['phone']
            image = request.FILES.get('image')
            if image:
                obj.image = image
            obj.save()
            return Response("updated")
        return Response("someproblem")
        




class UserData(APIView):
    def get(self , request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:] # Extract the token part
            details = AccessToken(token)
            userId = details["user_id"]
            obj = User.objects.get(id = userId)
            serializer = Userserializer(obj) 
            return Response(serializer.data)
        else:
            return Response(status=401)
        
  
    
        

