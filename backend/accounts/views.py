from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import views, permissions, status

from accounts.models import MyUser as User


class RegisterView(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):
        data = self.request.data

        email = data["email"]
        username = data["username"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        password = data["password"]
        password2 = data["password2"]
        if email == "" or username == "" or first_name == "" or password == "":
            return Response({'error': 'Fill all the required fields'})
        else:
            if password == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'error': 'Email already exists'})
                else:
                    if User.objects.filter(username=username).exists():
                        return Response({'error': 'username is already taken by someone'})
                    else:
                        user = User.objects.create_user(
                            email=email, username=username, password=password, first_name=first_name, last_name=last_name)
                        # user.save() -- No need of .save() because of create_user()
                        return Response({'success': 'User created successfully'})
            else:
                return Response(data={'error': 'Passwords do not match'}, status=status.HTTP_200_OK)