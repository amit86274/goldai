
class WidgetManager:
    def __init__(self):
        self.widgets = {}

    def register(self, name, widget):
        self.widgets[name] = widget

    def get(self, name):
        return self.widgets.get(name)
