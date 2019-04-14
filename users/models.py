from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Specifies the layout of the profile model
# Note the one-to-one correlation with the user model. The profile model uses user-model-inheritance to pull
# from the default user attributes of the model.
class Profile(models.Model):
    # The one-to-one correlation between profiles and users. on_delete ensures deleted users have their profiles deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The user's profile image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # The university the user attends
    university = models.CharField(max_length=50, default="No University")
    # The user's major
    major = models.CharField(max_length=20, default="Undecided")

    # Returns the path of the profile as a string
    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override of the save method for the purpose of scaling down images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        # Scaling down images if they are too large to reduce strain on system
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)