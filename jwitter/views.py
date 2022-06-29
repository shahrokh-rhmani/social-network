from django.shortcuts import render
from .models import Profile

def dashboard(request):
    return  render(request, 'jwitter/dashboard.html')


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles':profiles,

    }
    return render(request, 'jwitter/profile_list.html', context)


def profile(request, pk):
    # check user exists
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        present_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            present_user_profile.follows.add(profile)
        elif action == "unfollow":
            present_user_profile.follows.remove(profile)
        present_user_profile.save()
    context = {
        'profile':profile,
    }
    return render(request, 'jwitter/profile.html', context)
