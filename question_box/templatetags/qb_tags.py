from django import template

register=template.Library()
    
    
@register.simple_tag
def is_favorite(question, user):
    favorites_by_user = question.favorites.filter(owner=user)
    if question in [favorite.question for favorite in favorites_by_user.all()]:
        return True
    else:
        return False


# we will need this in the question_list template once we get the templatetags to work
#  {% if not is_favorite question user %} 

    # {% else %}
    # <p>is favorite</p>
    # {% endif %}

