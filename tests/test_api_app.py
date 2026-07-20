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
