from django.contrib import admin

from blog import models


admin.site.register(models.Site)
admin.site.register(models.SiteCategory)
admin.site.register(models.ArticleCategory)
admin.site.register(models.Article)
admin.site.register(models.Admin)
admin.site.register(models.Tag)