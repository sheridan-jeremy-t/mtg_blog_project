from django.contrib import admin
from .models import Post, Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'status', 'author')
    list_filter = ('status', 'topics')
    search_fields = ('title', 'author__username', 'author__first_name', 'author__lastname')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('created',)
    filter_horizontal = ('topics',)