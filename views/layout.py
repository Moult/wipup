import pystache

class Layout(pystache.TemplateSpec):

    def render(self, path):
        self.path = path
        self.template_name = 'layout'
        renderer = pystache.Renderer(search_dirs = 'wipup/templates/')
        return renderer.render(self)

    def content(self):
        template_dir, separator, template_name = self.path.rpartition('/')
        self.template_name = template_name
        renderer = pystache.Renderer(search_dirs = 'wipup/templates/' + template_dir + separator)
        return renderer.render(self)
