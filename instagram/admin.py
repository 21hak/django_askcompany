from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post
from .models import Comment
# Register your models here.

# 1.
# admin.site.register(Post)

# 2.
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 3. wrapping


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # custom action, field 등을 설정 할 수 있음.
    list_display = ['pk', 'photo_tag', 'message',
                    'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']  # 원하는 필드에 링크 지정 가능
    list_filter = ['created_at', 'is_public']  # 오른쪽에 해당 필드에 대한 filter 추가
    search_fields = ['message']  # db에 Like 쿼리를 던져 검색하는 기능을 admin에 추가

    def photo_tag(self, post):
        if post.photo:
            # 없을 경우 None되는데 None.url로 참조할 경우 ValueError가 발생 
            return mark_safe(f'<img src="{post.photo.url}" style="width:75px;"/>')
        return None

    def message_length(self, post):
        return f"{len(post.message)}"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass