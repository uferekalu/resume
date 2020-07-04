from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'

class AddForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
        exclude = ['school','level','faculty']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
    
class AddCourses(ModelForm):
    class Meta:
        model = CoursesRegistered
        fields = '__all__'

class UpdateCourse(ModelForm):
    class Meta:
        model = CoursesRegistered
        fields = '__all__'
