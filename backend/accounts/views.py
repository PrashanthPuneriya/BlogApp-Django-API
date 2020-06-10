from rest_framework import views, response, permissions, status

from .models import (
    MyUser as User,
    MyUserProfile as UserProfile
)


class RegisterView(views.APIView):

    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):

        data = self.request.data

        email = data["email"]  # or email = self.request.data.get('email')
        username = data["username"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        password = data["password"]
        password2 = data["password2"]

        github_link = data["github_link"]
        linkedin_link = data["linkedin_link"]

        if email == "" or username == "" or first_name == "" or password == "":
            return response.Response({'error': 'Fill all the required fields'})
        else:
            if password == password2:
                if User.objects.filter(email=email).exists():
                    return response.Response({'error': 'Email already exists'})
                else:
                    if User.objects.filter(username=username).exists():
                        return response.Response({'error': 'username is already taken by someone'})
                    else:
                        user = User.objects.create_user(
                            email=email, username=username, password=password, first_name=first_name, last_name=last_name)
                        profile = UserProfile.objects.create(
                            user=user, github_link=github_link, linkedin_link=linkedin_link)

                        # user.save() -- No need of .save() because of create_user()
                        return response.Response({'success': 'User created successfully'})
            else:
                return response.Response(data={'error': 'Passwords do not match'}, status=status.HTTP_200_OK)


class ProfileView(views.APIView):

    def get(self, request):
        user = request.user
        user_profile = user.myuserprofile
        print(user_profile)
        data = {
            "user": {
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name
            },
            "user_profile": {
                "github_link": user_profile.github_link,
                "linkedin_link": user_profile.linkedin_link
            }
        }
        return response.Response(data=data, status=status.HTTP_200_OK)
