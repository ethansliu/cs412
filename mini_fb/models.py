from django.db import models
from django.urls import reverse
from django.db.models import Q



# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data for a blog Article by some author.'''

    # data attributes:
    firstName = models.TextField(blank=False)
    lastName = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    #image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)

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
    
    def get_friends(self):
        friends = Friend.objects.filter(Q(profile1=self) | Q(profile2=self))
        friends_profiles = [friend.profile2 if friend.profile1 == self else friend.profile1 for friend in friends]
        return friends_profiles
    
    def add_friend(self, other):
        # check if you are friending yourself
        if self == other:
            return
        
        # filters to find whether self and other are already friends 
        existing_friend = Friend.objects.filter((Q(profile1=self) & Q(profile2=other)) | (Q(profile1=other) & Q(profile2=self)))
        
        # if self is already friends with other, then do nothing, otherwise create the friendship
        if existing_friend:
            return
        else:
            Friend.objects.create(profile1 = self, profile2 = other)
    
    def get_friend_suggestions(self):
        friends = self.get_friends()
        friend_suggestions = Profile.objects.exclude(pk__in = [friend.pk for friend in friends]).exclude(pk=self.pk)
        return friend_suggestions

    def get_news_feed(self):
        friends = self.get_friends()
        my_messages = StatusMessage.objects.filter(profile=self.pk)
        friend_messages = StatusMessage.objects.filter(profile__in = [friend.pk for friend in friends])
        news_feed = my_messages | friend_messages
        return news_feed.order_by("-timestamp")
    


class StatusMessage(models.Model):
    '''Encapsulate a comment on an article.'''

    # create a 1 to many relationship between Articles and Comments
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE) ### IMPORTANT
    message = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this object.'''
        return f'{self.message}'
    
    def get_images(self):
        return Image.objects.filter(status_message=self)

    

class Image(models.Model):
    '''Encapsulate an image for a status message.'''
    image_file = models.ImageField(upload_to='images/', blank=True)
    status_message = models.ForeignKey(StatusMessage, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_file.name
    

class Friend(models.Model):
    '''encapsulates the idea of an edge connecting two nodes within the social network'''
    friendiversary = models.DateTimeField(auto_now=True)
    profile1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile1")
    profile2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile2")

    def __str__(self):
        return f"{self.profile1.firstName} {self.profile1.lastName} & {self.profile2.firstName} {self.profile2.lastName}"


