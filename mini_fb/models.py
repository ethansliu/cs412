from django.db import models
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data for a blog Article by some author.'''

    # data attributes:
    firstName = models.TextField(blank=False)
    lastName = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this Article.'''
        return f"{self.firstName} {self.lastName}"
    
    def get_status_messages(self):
        '''Retrieve all comments for this Article.'''

        # use the ORM to filter Comments where this 
        # instance of Article is the FK
        statusmessages = StatusMessage.objects.filter(profile=self)
        return statusmessages
    
    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after sucessful create'''
 
        return reverse('profile_page', kwargs={'pk': self.pk})
    


class StatusMessage(models.Model):
    '''Encapsulate a comment on an article.'''

    # create a 1 to many relationship between Articles and Comments
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE) ### IMPORTANT
    message = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this object.'''
        return f'{self.message}'