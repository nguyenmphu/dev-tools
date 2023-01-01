from django.contrib import admin

from .models import Language, Snippet, Tag


admin.site.register(Language)
admin.site.register(Tag)


class SnippetAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "code",
        "language",
        "tags",
    )

    list_display = (
        "title",
        "language",
        "get_tags",
        "updated_by",
    )

    @admin.display(description="tags")
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    def save_model(self, request, obj, form, change) -> None:
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Snippet, SnippetAdmin)
