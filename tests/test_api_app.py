from api.app import create_app


def test_health_endpoint_reports_service_status():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["service"] == "gold-ai"
    assert payload["status"] in {"ok", "warning", "error"}


def test_decision_endpoint_returns_structured_signal():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/decision",
        json={
            "probability": 0.86,
            "trend_strength": 0.82,
            "volatility": 0.18,
            "balance": 10000.0,
            "risk_percent": 1.0,
            "max_position_size": 0.02,
            "market_session": "active",
        },
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["decision"]["action"] == "BUY"
    assert payload["decision"]["confidence"] >= 0.75


def test_decision_endpoint_returns_a_risk_controlled_trade_plan():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/decision",
        json={
            "probability": 0.86,
            "trend_strength": 0.82,
            "volatility": 0.18,
            "balance": 10_000.0,
            "risk_percent": 1.0,
            "max_position_size": 0.02,
            "market_session": "active",
            "entry_price": 2000.0,
            "atr": 10.0,
            "value_per_price_unit": 100.0,
        },
    )

    assert response.status_code == 200
    plan = response.get_json()["trade_plan"]
    assert plan["action"] == "BUY"
    assert plan["stop_loss"] < plan["entry_price"] < plan["take_profit"]
    assert plan["volume"] > 0
