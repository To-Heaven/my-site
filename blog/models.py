from django.db import models


class Site(models.Model):
    """ 网站主要信息表

    """
    introduction = models.CharField(max_length=1024, verbose_name='网站介绍')
    access_count = models.IntegerField(verbose_name='访问数量')

    class Meta:
        verbose_name_plural = '网站信息表'


class Admin(models.Model):
    """ 站长信息表

    """
    name = models.CharField(max_length=32, verbose_name='站长姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')
    city = models.CharField(max_length=32, verbose_name='所在城市')
    introduction = models.CharField(max_length=2048)

    class Meta:
        verbose_name_plural = '站长信息表'


class ArticleCategory(models.Model):
    """ 文章分类表

    """
    article_category_title = models.CharField(max_length=32, verbose_name='所属文章分类')
    site_category = models.ForeignKey(to='SiteCategory', to_field='id', on_delete=True)

    def __str__(self):
        return self.article_category_title

    class Meta:
        verbose_name_plural = '文章分类表'


class SiteCategory(models.Model):
    """ 站点文章分类表

    """
    site_category_title = models.CharField(max_length=32, verbose_name='所属站点分类')

    def __str__(self):
        return self.site_category_title

    class Meta:
        verbose_name_plural = '站点文章分类表'


class Tag(models.Model):
    """ 文章标签表

    """

    tag_title = models.CharField(max_length=32, verbose_name='标签标题')

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name_plural = '文章标签表'


class Article(models.Model):
    """ 文章表

    """

    article_title = models.CharField(verbose_name='文章标题', max_length=32)
    read_count = models.IntegerField(verbose_name='阅读数')
    create_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=204800)

    article_category = models.ForeignKey(to='ArticleCategory', to_field='id', on_delete=True, verbose_name='文章分类')
    tags = models.ManyToManyField(to='Tag', verbose_name='文章标签')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name_plural = '文章表'
