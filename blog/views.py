from django.shortcuts import render, HttpResponse

from blog import models


def home(request):
    """ 网站主界面视图函数

    """

    site = models.Site.objects.all().first()
    return render(request, 'home.html', {"site": site})


def base(request):

    return render(request, 'base.html')


def blog(request):
    articles = models.Article.objects.all()
    return render(request, 'blog_home.html', {"articles": articles})


def blog_category(request, site_category=None):
    articles = models.Article.objects.filter(article_category__site_category__site_category_title=site_category)
    article_category_list = models.ArticleCategory.objects.filter(site_category__site_category_title=site_category)
    return render(request, 'blog_category.html', {"articles": articles, "article_category_list": article_category_list})


def blog_article(request, article_id=None):
    article = models.Article.objects.filter(id=article_id).first()
    article_category_list = models.ArticleCategory.objects.filter(article__id=article_id)
    return render(request, 'blog_article.html', {"article_category_list": article_category_list, "article": article})