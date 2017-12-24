from django.shortcuts import render, HttpResponse
from blog import pagintator

from blog import models


def home(request):
    """  网站主界面视图函数 """

    site = models.Site.objects.all().first()
    response = render(request, 'home.html', {"site": site})
    response.set_cookie(
        key='has_counted',
        value='OK',
        max_age=300,
    )
    return response


def blog(request):
    """ 博客主界面视图函数 """
    search_key = request.GET.dict()
    if search_key.get('page'):              # 检索数据库内容时，不能包括page分页
        del search_key['page']
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
    """ 文章类型页面的视图函数
    Args:
        site_category: 文章类型
    """

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
    """ 文章页面视图函数
    Args:
        article_id: 文章id
    """
    article = models.Article.objects.filter(id=article_id).first()
    site_category = article.article_category.site_category
    article_category_list = article.article_category._meta.model.objects.filter(site_category=site_category)
    return render(request, 'blog_article.html', {"article_category_list": article_category_list, "article": article})
