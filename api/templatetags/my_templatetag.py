from django import template
register = template.Library()

@register.filter(name="multiply")
def multiply(qty, arg=2):
    return int(qty) * int(arg)
