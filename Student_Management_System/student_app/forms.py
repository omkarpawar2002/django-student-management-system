from django import forms
from .models import Student

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

language_choices = [
    ('PYTHON','PYTHON'),
    ('C++','C++'),
    ('JAVASCRIPT','JAVASCRIPT'),
    ('JAVA','JAVA'),
    ('.NET','.NET'),
    ('SQL','SQL'),
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'roll':forms.NumberInput(attrs={
                'placeholder':'E.g.,101'
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name Here'
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name Here'
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'Enter City Name Here'
            }),
            'dob':forms.DateInput(attrs={
                'type':'date'
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'mobile_no':forms.TextInput(attrs={
                'placeholder':'+91 ***** *****'
            }),
            'fav_language':forms.Select(choices=language_choices),
            'address':forms.Textarea(attrs={
                'rows':'3',
                'placeholder':'E.g., Maharashtra , Mumbai'
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com'
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password'
            })
        }