
class DynamicModelSelector:
    def select(self,models,regime):
        return models.get(regime, models.get("default"))
