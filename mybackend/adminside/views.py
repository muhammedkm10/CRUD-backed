from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from userside.models import User
from django.contrib.auth.hashers import make_password, check_password
from userside.serializers import Userserializer
from django.db.models import Q
# Create your views here.



# admin login
class AdminLogin(APIView):
    def post(self,requst):
        username = requst.data.get('username')
        password = requst.data.get('password')
        try:
            admin = User.objects.get(username = username)
        except:
            admin = None
        if admin is not None:
            if admin.is_superuser:
                if check_password(password,admin.password):
                    return Response("currect")
                return Response("incurrect")
            return Response("notadmin")
        return Response("nomatch")
    def get(self , request):
        qu = request.GET
        string = qu.get('string')
        if string != "":
            queryset = User.objects.filter(is_staff = True,is_superuser = False,username__startswith=string).order_by('-id')
        else:
            queryset = User.objects.filter(is_staff = True,is_superuser = False).order_by('-id')
        serializer = Userserializer(queryset ,many = True)
        return Response(serializer.data)
            

  
class UserManagement(APIView):
    def post(self, request):
        username = request.data.get('username')
        print(username)
        if username is None:
            return Response("enter")
        try:
          already = User.objects.get(username = username)
        except:
            already = None
        if already is not None:
            return Response("userisalreadythere")
        print(request.data.get('password'))
        user  = User.objects.create_user(username = request.data.get('username'),email = request.data.get('email'),password = request.data.get('password'))
        user.phone = request.data.get('phone')
        user.is_staff = True
        user.save()
        return Response("added")
    def delete(self , request,id):
        user = User.objects.get(id = id)
        user.delete()
        return Response('deleted')
    def get(self, request,id):
        try:
            user = User.objects.get(id = id)
            serializer = Userserializer(user)
            return Response(serializer.data)
        except:
            return Response("problem")
    def put(self , request):
        username = request.data.get('username')
        print(username)
        id = request.data.get('id')
        print(id)
        try:
                already = User.objects.exclude(id = id).get(username = request.data['username'])
        except:
                already = None
        print(id)
        if already is not None:
                if  already.id  != id:
                   return Response("already")
        user = User.objects.get(id = id)
        user.username = request.data.get('username')
        user.phone = request.data.get('phone')
        user.email = request.data.get('email')
        user.save()
        return Response("updated")
        
    
    







