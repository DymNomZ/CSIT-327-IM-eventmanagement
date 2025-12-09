from django import forms
from django.forms import ModelForm

from User.models import Student, Teacher


class StudentForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
    firstname = forms.CharField(widget=forms.TextInput())
    middlename = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    type = 'S'
    course = forms.CharField(widget=forms.TextInput())
    year = forms.CharField(widget=forms.NumberInput())
    department = forms.NumberInput()

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['middlename'].required = False

    def clean_year(self):
        year = self.cleaned_data['year']
        if int(year) > 5 or int(year) < 1:
            raise forms.ValidationError('Year must be between 1 and 5')
        else:
            return year

    class Meta:
        model = Student
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname', 'course', 'year', 'department']


class TeacherForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
    firstname = forms.CharField(widget=forms.TextInput())
    middlename = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    type = 'T'
    age = forms.IntegerField(widget=forms.NumberInput())

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['middlename'].required = False

    class Meta:
        model = Teacher
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname', 'age']