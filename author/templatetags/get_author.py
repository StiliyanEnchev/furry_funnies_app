from django import template

from common.utils import get_current_author

register = template.Library()

@register.simple_tag
def get_author():
    return get_current_author()