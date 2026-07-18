from datetime import datetime

def build_report(results):
    return {'generated_at': datetime.utcnow().isoformat(), 'results': results}
