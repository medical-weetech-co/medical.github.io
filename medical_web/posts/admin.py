from django.contrib import admin

# Register your models here.
# . is relative import
from .models import Post

# referece https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#modeladmin-options

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]
	
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)