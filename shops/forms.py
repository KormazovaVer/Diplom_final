from allauth.account.forms import BaseSignupForm
from allauth.socialaccount.forms import SignupForm


class UserSignupForm(SignupForm):
    def save(self, request):
        user = super(BaseSignupForm, self).save(request)
        user.is_active = True
        user.save()
        return user

