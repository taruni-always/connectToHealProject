from django.contrib import admin
from .models import Blog, DiscussionModel, Session, Therapist

admin.site.register(Blog)
admin.site.register(Session)
admin.site.register(Therapist)
admin.site.register(DiscussionModel)