from django.contrib import admin
from .models import *

admin.site.register([User, Subscription, Guides, Feedback, Feeds])
# Register your models here.
