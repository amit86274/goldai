
LONDON=("07:00","10:00")
NEW_YORK=("13:00","16:00")
def in_killzone(session):
    return session.upper() in ("LONDON","NEW_YORK")
