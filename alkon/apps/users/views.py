from django.shortcuts import render, redirect

from . import forms
# Create your views here.
def edit_profile_view(request):
  template = 'users/edit-user-profile.html'
  form = forms.UserForm(
        request.POST or None,
        request.FILES or None,
        initial={
          'user': request.user
          },
        instance=request.user.userprofile_set.all()[0],
        )

  if request.method == 'POST':
      if form.is_valid():
          form.save()

      return redirect('users:profile-detail')

  user_photo = None
  if request.user.userprofile_set.all():
    user_photo = request.user.userprofile_set.all()[0].user_photo.url

  context = {
    'form': form,
    'user': request.user,
    'user_photo': user_photo
  }

  return render(request, template, context)

def user_profile_view(request):
  template = 'users/user-profile.html'
  media_form = forms.MediaUploadForm(
        request.POST or None,
        request.FILES or None,
        initial={
          'user': request.user
          },
        )
  if request.method == 'POST':
      if media_form.is_valid():
          media_form.save()

  user_photo = None
  skills = []
  if request.user.userprofile_set.all():
      user_photo = request.user.userprofile_set.all()[0].user_photo.url
      skills = request.user.userprofile_set.all()[0].skills.all()
  
  media = request.user.usermedia_set.all()
  
  context = {
    'user': request.user,
    'user_photo': user_photo,
    'skills': skills,
    'media': media,
    'media_form': media_form,
  }
  return render(request, template, context)