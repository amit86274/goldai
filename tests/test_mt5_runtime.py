from mt5.connector import ConnectionConfig, MT5Connector


def test_connection_config_accepts_runtime_values():
    config = ConnectionConfig(login=123456, password="secret", server="MetaQuotes-Demo", path="C:/Program Files/MetaTrader 5/terminal64.exe")
    assert config.login == 123456
    assert config.server == "MetaQuotes-Demo"


def test_connector_tracks_state_after_disconnect():
    connector = MT5Connector(ConnectionConfig())
    connector.disconnect()
    assert connector.is_connected() is False


def test_connector_is_usable_without_the_optional_mt5_dependency(monkeypatch):
    import mt5.connector as connector_module

    monkeypatch.setattr(connector_module, "mt5", None)
    connector = MT5Connector(ConnectionConfig())

    assert connector.connect() is False
    assert connector.version() is None
    assert connector.last_error() is None
