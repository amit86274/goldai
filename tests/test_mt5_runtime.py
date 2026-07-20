from mt5.connector import ConnectionConfig, MT5Connector


def test_connection_config_accepts_runtime_values():
    config = ConnectionConfig(login=123456, password="secret", server="MetaQuotes-Demo", path="C:/Program Files/MetaTrader 5/terminal64.exe")
    assert config.login == 123456
    assert config.server == "MetaQuotes-Demo"


def test_connector_tracks_state_after_disconnect():
    connector = MT5Connector(ConnectionConfig())
    connector.disconnect()
    assert connector.is_connected() is False
