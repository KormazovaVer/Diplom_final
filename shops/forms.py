from allauth.socialaccount.forms import SignupForm


class UserSignupForm(SignupForm):
    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        user.is_active = True
        user.save()
        return user

