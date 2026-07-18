
import re
def extract_symbols(text):
    return re.findall(r'\b[A-Z]{3,6}\b', text)
