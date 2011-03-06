from django.core.urlresolvers import reverse

class Page(object):
    def __init__(self, title, url, parent=None, permission=None):
        self._parent = parent
        self._title = title
        self._url = url
        self._permission = permission

    def get_url(self, context=None):
        return reverse(self._url)

    def get_title(self, context=None):
        return self._title

    def get_parent(self, context=None):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    parent = property(get_parent, set_parent)
        
    def in_path(self, current_page):
        while current_page is not None:
            if current_page is self:
                return True
            else:
                current_page = current_page.parent

        return False

class PageProxy(object):
    def __init__(self, page, context, current_page, overwrite_title=None):
        self._page = page
        self._context = context
        self._current_page = current_page
        self._overwrite_title = overwrite_title

    @property
    def title(self):
        if self._overwrite_title is not None:            
            return self._overwrite_title
        else:
            return self._page.get_title(self._context)

    @property
    def url(self):
        return self._page.get_url(self._context)

    @property
    def in_path(self):
        return self._page.in_path(self._current_page)

    @property
    def current_page(self):
        return self._page is self._current_page

class Navigation(object):
    def __init__(self):
        self._pages = []

    def register(self, page, title=None):
        self._pages.append((page, title))

    def bind_to_context(self, context, current_page):
        return [PageProxy(page, context, current_page, overwrite_title=title) 
                for page, title in self._pages]