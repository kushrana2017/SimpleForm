from django.contrib import admin
from .models import Account
from .models import Admin
from .models import LogInInfo
# Register your models here.

admin.site.register(Account)
admin.site.register(Admin)
admin.site.register(LogInInfo)