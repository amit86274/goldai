
class AlertTemplate:
    def render(self, template, **kwargs):
        return template.format(**kwargs)
