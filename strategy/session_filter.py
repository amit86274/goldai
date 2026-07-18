
ACTIVE_SESSIONS={"LONDON","NEW_YORK"}

def session_allowed(session):
    return session.upper() in ACTIVE_SESSIONS
