from django.contrib import admin
from MockTrial.models import *

class AboutAdmin(admin.ModelAdmin):
	pass

class TeamMembersAdmin(admin.ModelAdmin):
	"""docstring for TeamMemberAdmin"""
	field = ('name')
		
class ContactAdmin(admin.ModelAdmin):
	pass
admin.site.register(About, AboutAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(Contact, ContactAdmin)
# Register your models here.
