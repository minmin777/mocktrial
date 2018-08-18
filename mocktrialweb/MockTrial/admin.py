from django.contrib import admin
from MockTrial.models import *

class AboutAdmin(admin.ModelAdmin):
	pass

class TeamMembersAdmin(admin.ModelAdmin):
	"""docstring for TeamMemberAdmin"""
	pass
		
admin.site.register(About, AboutAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
# Register your models here.
