from django import template

register=template.Library()
    
    
@register.simple_tag
def is_favorite(question, user):
    favorites_by_user = question.favorites.filter(owner=user)
    if question in [favorite.question for favorite in favorites_by_user.all()]:
        return True
    else:
        return False