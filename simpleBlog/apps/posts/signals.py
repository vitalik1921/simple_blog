from .utils import *


def post_save_handler(sender, **kwargs):
    create_thumbnail(kwargs['instance'].Image.path)


def pre_delete_handler(sender, **kwargs):
    delete_thumbnail(kwargs['instance'].Image.path)
