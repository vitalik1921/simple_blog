from django.http import HttpResponse
from .models import Category


def categories(request):
    """
    Show all categories
    :param request:
    :return categories.html:
    """

    s = ''
    for cat in Category.objects.all():
        s = s + cat.get_absolute_url() + '<br>'

    return HttpResponse('categories <br>' + s)


def category(request, slug=None):
    """
    Show all posts in Category
    :param request:
    :return category.html:
    """
    return HttpResponse('category {}'.format(slug))


def post(request, slug=None):
    """
    Show single post
    :param request:
    :return post.html:
    """
    return HttpResponse('post {}'.format(slug))



