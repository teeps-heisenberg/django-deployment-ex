from django import template

register = template.Library()

def cut(value,arg):
    """
    CUT ALL VALUES OF ARG FROM Value string
    """
    return value.replace(arg,'')

register.filter('cut1',cut)
