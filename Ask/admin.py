from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class InterestAdmin(admin.ModelAdmin):
    class Meta:
        model = Interest
    list_display = ('interest_title',)
    def interest_title(self,obj):
        return obj.topic

#class QuestionAdmin(admin.ModelAdmin):
#    form = QuestionForm
	
admin.site.register(UserLogin)
admin.site.register(Interest,InterestAdmin)
admin.site.register(UserInterest)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Upvote) 


