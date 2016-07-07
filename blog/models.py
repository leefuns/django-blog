# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
#Article models
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=150, verbose_name='文章描述')
    psot_img = models.ImageField(upload_to='uploads/%Y-%m-%d', verbose_name='图片')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    # is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(verbose_name='发布时间')
    authors = models.CharField(default='admin', max_length=100,verbose_name='作者')
    # category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    # tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

class Contact(models.Model):
    subject = models.CharField(max_length=50, verbose_name='Subject')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = '联系信息'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    name = models.CharField(max_length=30,verbose_name='轮播名称',default='1')
    index = models.IntegerField(default=9, verbose_name='排列顺序(从小到大)')
    url = models.URLField(null=True, blank=True, verbose_name='回调url')
    img = models.ImageField(upload_to='banner/%Y-%m-%d', default='default.jpg', verbose_name='轮播图片')

    class Meta:
        verbose_name = '广告轮播'
        verbose_name_plural = verbose_name
