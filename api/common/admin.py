from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

from common.models import * 


admin.site.register(Profile)
admin.site.register(Bookmark)
