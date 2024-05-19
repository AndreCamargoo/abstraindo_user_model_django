from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsers


# Criação
class CustomUsersCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsers
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username: Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


# Alteração
class CustomUsersChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsers
        labels = {'username: Username/E-mail'}
        fields = ('first_name', 'last_name', 'fone')
