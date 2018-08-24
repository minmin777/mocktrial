from django.contrib import admin
from MockTrial.models import *

class AboutAdmin(admin.ModelAdmin):
	pass

class TeamMembersAdmin(admin.ModelAdmin):
	"""docstring for TeamMemberAdmin"""
	field = ('name')
		
class ContactAdmin(admin.ModelAdmin):
	pass

class InvitationalAdmin(admin.ModelAdmin):
	pass

class MainLineAdmin(admin.ModelAdmin):
	pass
admin.site.register(About, AboutAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Invitational, InvitationalAdmin)
admin.site.register(MainLine, MainLineAdmin)
# Register your models here.
