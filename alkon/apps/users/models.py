'''
User app models
'''
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.utils.translation import ugettext_lazy as __
from django.core.exceptions import ValidationError
from django.contrib.auth.backends import ModelBackend
from django_countries.fields import CountryField
from django.utils import timezone

@python_2_unicode_compatible
class User(AbstractUser):
    '''
    User model - django default plus additional fields
    '''
    site = models.ForeignKey(Site, null=True)
    last_activity = models.DateTimeField(default=timezone.now)

    # for backward compatibility for existing users default subscription
    # is false and default plan_type is null.
    # we will still need to manually make these users inactive
    is_subscriber = models.BooleanField(default=False)
    cell_phone = models.BigIntegerField()
    # Moved these two fields to the user model and included in sign up forms.
    # Moving them to this model does not require us to create a student profile
    # record at sign up and therefore we won't need to add more logic to show
    # the student profile form at the user's first sign in.

    objects = UserManager()
    on_site = CurrentSiteManager()
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Skills(models.Model):
    """
    List of skills
    """
    INSTRUMENT = 0
    PERORMANCE_ART = 1
    GRAPHIC_DESIGN = 2
    SOUND_EDITING = 3
    PRODUCTION = 4

    SKILL_TYPES = (
        (INSTRUMENT, __('Musical Instrument')),
        (PERORMANCE_ART, __('Performance Art')),
        (GRAPHIC_DESIGN, __('Graphic Design')),
        (SOUND_EDITING, __('Sound Editing')),
        (PRODUCTION, __('Production'))
    )
    name = models.CharField(max_length=100)
    skill_type = models.PositiveSmallIntegerField(choices=SKILL_TYPES)
    image = models.ImageField(upload_to='skills')

    def __str__(self):
        return self.name
class UserProfile(models.Model):
    """
    Other data than login information
    """
    user = models.ForeignKey(User)
    user_photo = models.ImageField(upload_to='users')
    skills = models.ManyToManyField(Skills)

class UserMedia(models.Model):
    """
    User uploaded files (images, audio, video)
    """
    AUDIO = 0
    IMAGE = 1
    VIDEO = 2
    FILE_TYPES = (
      (AUDIO, __('Audio')),
      (IMAGE, __('Image')),
      (VIDEO, __('Video')),
    )
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    media_type = models.PositiveSmallIntegerField(choices=FILE_TYPES)
    media_url = models.FileField(upload_to='uploads')

class CaseInsensitiveModelBackend(ModelBackend):
    """
    Override ModelBackend's default case sensitive authentication, and
    allow login via email or username.

    It's not clear that we're disallowing one student from having the same
    username as another user's email address.  So for now, just try
    logging in to either account.
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email__iexact=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        # can happen if a [legacy] user has multiple accounts tied to one email address:
        except User.MultipleObjectsReturned:
            raise ValidationError(
                "There are multiple accounts associated with this email \
                address. Please log in with your username instead."
            )
        try:
            user = User.objects.get(username__iexact=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None
