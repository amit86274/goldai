
import importlib
class PluginManager:
    def load(self,module):
        return importlib.import_module(module)
