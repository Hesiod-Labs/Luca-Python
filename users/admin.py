from django.contrib import admin
from .models import Profile

# Allow the Profile section to be accessible through the admin page
admin.site.register(Profile)
