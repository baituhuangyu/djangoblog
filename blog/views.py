#-*-:coding:utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from blog.models import *

logger = logging.getLogger('blog.views')

def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
        'WEIBO_SINA': settings.WEIBO_SINA,
        'WEIBO_TENCENT': settings.WEIBO_TENCENT,
        'PRO_RESS' : settings.PRO_RESS,
        'PRO_EMAIL' : settings.PRO_RESS,
    }
# Create your views here.
def index(request):
    try:
        #分类信息获取（导航数据）
        category_list = Category.objects.all()
        #广告数据（）
        #最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 10)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())













