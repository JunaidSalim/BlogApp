from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
import shortuuid

class User(AbstractUser):
    username = models.CharField(unique=True,max_length=20)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

    def save(self,*args, **kwargs):
        email_username,temp = self.email.split('@')
        if self.full_name=="" or self.full_name==None:
            self.full_name = email_username
        if self.username=="" or self.username==None:
            self.username = email_username

        super(User,self).save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    image = models.FileField(upload_to="image",default="default/default-user.jpg",null=True,blank=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)
    bio = models.CharField(max_length=200,null=True,blank=True)
    about = models.CharField(max_length=200,null=True,blank=True)
    author = models.BooleanField(default=False)
    country = models.CharField(max_length=100,null=True,blank=True)
    facebook = models.CharField(max_length=100,null=True,blank=True)
    twitter = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

    def save(self,*args, **kwargs):
        if self.full_name=="" or self.full_name==None:
            self.full_name = self.user.full_name

        super(Profile,self).save(*args, **kwargs)

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance,full_name = instance.full_name)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="image",null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if self.slug=="" or self.slug==None:
            self.slug = slugify(self.title)

        super(Category,self).save(*args, **kwargs)
    
    def post_count(self):
        return Post.objects.filter(category=self).count()

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    STATUS_CHOICES = (
    ("Active","Active"),
    ("Disabled","Disabled"),
    ("Draft","Draft")
    )

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    profile = models.ForeignKey(to=Profile,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(to=Category,blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to="image",null=True,blank=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=100,default="Active")
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(to=User,blank=True,related_name="likes_user")
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=True,blank=True,max_length=1000)


    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if self.slug=="" or self.slug==None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]

        super(Post,self).save(*args, **kwargs)

    def comments(self):
        return Comment.objects.filter(post=self)

class Comment(models.Model):
    post = models.ForeignKey(to=Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField(null=True,blank=True)
    reply = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.post.title
    
class Bookmark(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.post.title

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("Like","Like"),
        ("Comment","Comment"),
        ("Bookmark","Bookmark"),
    )

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=NOTIFICATION_TYPES, max_length=100)
    seen = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        if self.post:
            return f"{self.post.title} - {self.type}"
        else:
            return "Notification"