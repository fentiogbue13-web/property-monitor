"""
Minimal in-memory "already seen" store.

This is deliberately the simplest thing that could work, standing in
for the Postgres-backed store from Phase 2 of the brief. The interface
(has_seen / remember) is what matters -- swap the body for a real DB
later without touching main.py's flow logic.
"""
from __future__ import annotations

from property_monitor.utils.models import Property


class ListingStore:
    def __init__(self):
        # Dict keeps the whole property object stored rather than just the ID
        self._seen_ids: dict[str, Property] = {}

    def has_seen(self, prop: Property) -> bool:
        return prop.listing_id in self._seen_ids

    def remember(self, prop: Property) -> None:
        self._seen_ids[prop.listing_id] = prop

    def __len__(self) -> int:
        return len(self._seen_ids)

    def __iter__(self):
        """allow for prop in store to iterate over stored properties"""
        return iter(self._seen_ids.values())
