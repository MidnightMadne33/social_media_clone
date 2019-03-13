from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('email', 'username', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'E-mail'
        self.fields['password1'].label = 'Enter password'
        self.fields['password2'].label = 'Confirm password'
