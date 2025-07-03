from django.contrib import admin
from .models import Post, Topic, Comment

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

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('name','email', 'text', 'approved')
    readonly_fields = ('name', 'email', 'text')
    extra = 0

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'approved')
    list_filter = ('approved', 'created')
    search_fields = ('name', 'email', 'text')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'status', 'author')
    list_filter = ('status', 'topics')
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('created',)
    filter_horizontal = ('topics',)
    inlines = [CommentInline]
