from mt5.connector import ConnectionConfig, MT5Connector


def test_connector_configuration_defaults():
    config = ConnectionConfig()
    assert config.timeout == 60000
    assert config.portable is False


def test_connector_reports_connection_state():
    connector = MT5Connector(ConnectionConfig())
    assert connector.is_connected() is False
