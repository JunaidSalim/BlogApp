from django.contrib import admin
from .models import User,Profile,Category,Comment,Post,Notification,Bookmark

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Notification)
admin.site.register(Comment)
admin.site.register(Bookmark)