# Gold-AI v1.0

AI-assisted trading framework for XAUUSD.

## Structure
- app/
- mt5/
- features/
- news/
- models/
- strategy/
- backtesting/
- dashboard/
- alerts/
- api/
- database/
- utils/

## Run

```bash
pip install -r requirements.txt
python app/main.py
```

## Trade decisions

`POST /decision` returns a signal with its confidence and, for actionable
signals, a risk-controlled trade plan. Provide `entry_price`, `atr`, and
`value_per_price_unit` to receive automatic entry, stop-loss, take-profit,
and broker-step-normalized volume. Optional controls include
`stop_atr_multiplier`, `reward_to_risk`, and volume bounds.

Live broker connectivity is disabled by default. Set `LIVE_TRADING_ENABLED=true`
only after validating terminal credentials, symbol specifications, and the
execution workflow in a demo environment.

## Docker

```bash
docker compose up --build
```
