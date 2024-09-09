from django.contrib import admin
from .models import Contact,Team,Project,About



admin.site.register((Contact,About,Team,Project))

