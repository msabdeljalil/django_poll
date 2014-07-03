from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		("Ony field to fill...", { 'fields': ['question'] } ),
		('Date information', { 'fields': ['pub_date'], 'classes': ['collapse'] } ),
	]
	
	# fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)