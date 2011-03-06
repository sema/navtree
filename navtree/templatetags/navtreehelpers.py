from django import template

from navtree.navigation import PageProxy

register = template.Library()

@register.tag
def get_navigation_pages(parser, token):
    """
    {% get_navigation_pages navigation current_page as pages %}
    """

    try:
        tag_name, navigation, current_page, _as_, target = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]

    return GetNavigationPage(navigation, current_page, target)

class GetNavigationPage(template.Node):
    def __init__(self, navigation, current_page, target):
        self.navigation = navigation
        self.current_page = current_page
        self.target = target

    def render(self, context):
        current_page = context.get(self.current_page, None)

        context[self.target] = context[self.navigation].bind_to_context(context, current_page)

        return ''

@register.tag
def get_breadcrumbs(parser, token):
    """
    {% get_breadcrumbs current_page as breadcrumbs %}
    """

    try:
        tag_name, current_page, _as_, target = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]

    return GetBreadcrumbs(current_page, target)

class GetBreadcrumbs(template.Node):
    def __init__(self, current_page, target):
        self.current_page = current_page
        self.target = target

    def render(self, context):
        self.current_page = context[self.current_page]

        pages = []
        page = self.current_page

        while page is not None:
            pages.append(PageProxy(page, context, self.current_page))
            page = page.parent

        pages.reverse()

        context[self.target] = pages

        return ''

