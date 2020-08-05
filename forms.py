from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    ''' Custom user creation form'''

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    '''Custom user change form'''

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username',)



