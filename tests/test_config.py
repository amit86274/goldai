from app.config import settings


def test_settings_expose_runtime_configuration():
    payload = settings.to_dict()
    assert payload["ai"]["model_directory"]
    assert payload["redis"]["host"]
    assert payload["database"]["host"]
