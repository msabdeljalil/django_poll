from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		("Ony field to fill...", { 'fields': ['question'] } ),
		('Date information', { 'fields': ['pub_date'], 'classes': ['collapse'] } ),
	]
	inlines = [ChoiceInLine]

admin.site.register(Poll, PollAdmin)