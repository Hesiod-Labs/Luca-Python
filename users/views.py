from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


# Register is the view seen for new users registering for the site
def register(request):
    if request.method == 'POST':  # on submit
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.university = form.cleaned_data.get('university')  # update profile components as well
            user.profile.major = form.cleaned_data.get('major')
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')  # fstring for displaying a new profile
            return redirect('login')
    # If no post-request received
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# This view describes the detailView of each user's profile
# It inherits Django's prebuilt DetailView for easy management
class ProfileDetailView(LoginRequiredMixin, DetailView):
    # The profile model is referenced
    model = Profile
    # The template to be linked
    template_name = 'users/profile.html'

    # Filling the profile update with the contextual data of the profile to be updated
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = ProfileUpdateForm(instance=self.request.user.profile)
        # Adding contextual data for the user form and the profile form
        context['u_form'] = u_form
        context['p_form'] = p_form
        return context

    # If the ProfileDetailView receives a post request
    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=self.request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=self.request.user.profile)

        # If forms meet Django valid criteria
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect(request.user.profile.get_absolute_url())  # redirect to newly updated profile
