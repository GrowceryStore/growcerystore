from django import template
register = template.Library()

@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return qty * unit_price
     

# @register.filter

# def running_total(fine_list):
#     sum=0
#     for d in fine_list:
#         sum+=d
#     return sum