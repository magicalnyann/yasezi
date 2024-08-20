# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    id = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'id': 'id'}))
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'id': 'password1'}))
    password2 = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput(attrs={'id': 'password2'}))
    name = forms.CharField(label='이름', widget=forms.TextInput(attrs={'id': 'name'}))
    email = forms.EmailField(label='이메일', widget=forms.EmailInput(attrs={'id': 'email'}))
    address = forms.CharField(label='주소', widget=forms.TextInput(attrs={'id': 'address'}))
    address_detail = forms.CharField(label='상세주소', widget=forms.TextInput(attrs={'id': 'address_detail'}))
    phone_number = forms.CharField(label='전화번호', widget=forms.TextInput(attrs={'id': 'phone_number'}))
    gender = forms.ChoiceField(label='성별', choices=[('M', '남자'), ('F', '여자')],
                               widget=forms.Select(attrs={'id': 'gender'}))
    birth_date = forms.DateField(label='생년월일', widget=forms.DateInput(attrs={'type': 'date', 'id': 'birth_date'}))
    breed = forms.CharField(label='야옹이 묘종', widget=forms.TextInput(attrs={'id': 'breed'}))
    cat_name = forms.CharField(label='야옹이 이름', widget=forms.TextInput(attrs={'id': 'cat_name'}))

    class Meta:
        model = User
        fields = ("id", "name", "password1", "password2", "email", "address", "address_detail", "phone_number", "gender", "birth_date", "breed", "cat_name")

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            profile, created = Profile.objects.get_or_create(user=user)
            profile.address = self.cleaned_data.get('address')
            profile.address_detail = self.cleaned_data.get('address_detail')
            profile.phone_number = self.cleaned_data.get('phone_number')
            profile.gender = self.cleaned_data.get('gender')
            profile.birth_date = self.cleaned_data.get('birth_date')
            profile.breed = self.cleaned_data.get('breed')
            profile.cat_name = self.cleaned_data.get('cat_name')
            profile.save()
        return user
