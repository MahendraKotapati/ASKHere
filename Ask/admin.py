from django.contrib import admin
from .models import *

# Register your models here.

class InterestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(UserLogin)
admin.site.register(Interest,InterestAdmin)
admin.site.register(UserInterest)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Upvote) 


