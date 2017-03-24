from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def deploy_buttons(
    context,
    deploy_button_template='deploy/deploy_buttons.html'
):
    user = context.get('user')
    can_deploy = user.groups.filter(name='deployers').exists()
    context.update({'can_deploy': can_deploy})
    tmpl = template.loader.get_template(deploy_button_template)
    return tmpl.render(context)