from django import template

from common.utils import get_post

register = template.Library()

@register.simple_tag
def get_all_posts():
    return get_post()