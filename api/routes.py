
def register(app):
    @app.get("/signal")
    def signal():
        return {"signal":"HOLD"}
