
def generate_openapi(title="Gold AI API", version="1.0.0"):
    return {
        "openapi": "3.0.0",
        "info": {
            "title": title,
            "version": version
        }
    }
