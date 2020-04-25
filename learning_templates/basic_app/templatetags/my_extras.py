from django import template

register=template.Library()

@register.filter
def cut(value,arg):
    """
    this cuts out all valuse of arg from the string
    """
    return value.replace(arg,"")

@register.filter
def jai(value,arg):
    return value.replace(arg,"@@@@@")

# register.filter('cutter',cut)
# register.filter('jai',jai)
