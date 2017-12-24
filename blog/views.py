from django.shortcuts import render, HttpResponse
from blog import pagintator

from blog import models


def home(request):
    """ 网站主界面视图函数

    """

    site = models.Site.objects.all().first()
    return render(request, 'home.html', {"site": site})


def base(request):

    return render(request, 'base.html')


def blog(request):
    search_key = request.GET.dict()
    articles = models.Article.objects.filter(**search_key)
    page_obj = pagintator.Paingator(
        request=request,
        base_url=request.path_info,
        obj_count=articles.count(),
        params=request.GET,
        per_page_count=10,
        init_page_count=11,
    )
    return render(request, 'blog_home.html', {"articles": articles[page_obj.start:page_obj.end], "page_divider": page_obj})


def blog_category(request, site_category=None):
    articles = models.Article.objects.filter(article_category__site_category__site_category_title=site_category)
    article_category_list = models.ArticleCategory.objects.filter(site_category__site_category_title=site_category)
    page_obj = pagintator.Paingator(
        request=request,
        base_url=request.path_info,
        obj_count=articles.count(),
        params=request.GET,
        per_page_count=6,
        init_page_count=5,
    )
    return render(request, 'blog_category.html', {"articles": articles[page_obj.start:page_obj.end],
                                                  "page_obj": page_obj,
                                                  "article_category_list": article_category_list})


def blog_article(request, article_id=None):
    article = models.Article.objects.filter(id=article_id).first()
    site_category = article.article_category.site_category
    article_category_list = article.article_category._meta.model.objects.filter(site_category=site_category)
    return render(request, 'blog_article.html', {"article_category_list": article_category_list, "article": article})
