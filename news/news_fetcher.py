"""Basic news fetcher interface."""
from __future__ import annotations
from typing import List, Dict

class NewsFetcher:
    def fetch(self) -> List[Dict]:
        """Override this with a provider implementation."""
        return []
