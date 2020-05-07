from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import Profile,Projects


STATUS_CHOICES = (("1","Student"),("2","Alumni"))
YEAR_CHOICES = (("1st year","1st year"),("2nrd year","2nd year"),("3rd year","3rd year"),("4th year","4th year"))



class PostSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label = '',
                    widget=forms.TextInput(attrs={'placeholder': 'search by username'})
                  )


class ProjectSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label = '',
                    widget=forms.TextInput(attrs={'placeholder': 'search by title'})
                  )



class UserRegisterForm(UserCreationForm):
    email_id = forms.EmailField()
    #status = forms.ChoiceField(choices=STATUS_CHOICES)
    #mobile_no = forms.IntegerField()
    #current_year = forms.CharField()  

    class Meta:
        model = User 
        fields = ['username','email_id','password1','password2']



class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Projects 
        fields = ['student1','student2','student3','title','description','tech_stack','working_ss']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image','email_id','status','mobile_no','current_year','short_note_about_yourself']
    
class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Projects 
        fields = ['title','description','tech_stack','working_ss'] 
