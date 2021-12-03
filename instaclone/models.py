from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    caption= models.TextField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,caption):
        self.caption = caption
        self.save()