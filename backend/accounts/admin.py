from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser, MyUserProfile
from django import forms

"""
UserAdmin uses UserChangeForm as the form to be used when modifying the object, 
which in its turn uses User as its model.

UserAdmin defines a formsets-property, later used by UserChangeForm, 
which does not include your special fields.
"""


class MyUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges from the given email, username 
    password1 and password2.
    """
    # Overriding first_name field
    first_name = forms.CharField(
        max_length=50, required=True, label='First Name')

    class Meta(UserCreationForm.Meta):
        model = MyUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Defining our own label for password2 field
        self.fields['password2'].label = 'Confirm Password'


class MyUserChangeForm(UserChangeForm):
    """
    A form used in the admin interface to change a user’s information and permissions.
    """
    class Meta:
        model = MyUser
        fields = '__all__'


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    model = MyUser
    list_display = ['email', 'username', 'first_name']

class MyUserProfileAdmin(admin.ModelAdmin):
    model = MyUserProfile
    list_display = ['user', 'github_link', 'linkedin_link']

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyUserProfile, MyUserProfileAdmin)

# admin.site.unregister(Group)
