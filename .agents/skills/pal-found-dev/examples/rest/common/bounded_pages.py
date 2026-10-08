"""Finite raw-page retrieval with explicit partial results.

The supplied callable is an SDK raw-response method, usually a partial with
resource identifiers and filters bound. Prepared SDK 1.101.0 is the baseline.
"""

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class PageResult:
    items: list[Any]
    remaining_on_page: list[Any]
    next_page_token: str | None
    pages: int
    complete: bool
    reason: str


def _accept(page, items, max_items):
    values = list(page.data or [])
    available = max_items - len(items)
    items.extend(values[:available])
    return values[available:]


def fetch_pages(fetch_page: Callable, *, max_pages=10, max_items=1000, page_token=None):
    """Fetch sync raw pages; empty intermediate pages still advance their cursor."""
    if max_pages <= 0 or max_items <= 0:
        raise ValueError("Page and item budgets must be positive")
    items, used_tokens, cursor = [], set(), page_token
    for number in range(1, max_pages + 1):
        if cursor is not None:
            if cursor in used_tokens:
                return PageResult(items, [], cursor, number - 1, False, "repeated-token")
            used_tokens.add(cursor)
        response = fetch_page(page_token=cursor)
        try:
            page = response.decode()
        finally:
            response.close()
        remaining = _accept(page, items, max_items)
        cursor = page.next_page_token
        if remaining:
            return PageResult(items, remaining, cursor, number, False, "item-budget")
        if not cursor:
            return PageResult(items, [], None, number, True, "complete")
        if len(items) >= max_items:
            return PageResult(items, [], cursor, number, False, "item-budget")
    return PageResult(items, [], cursor, max_pages, False, "page-budget")


async def fetch_pages_async(fetch_page: Callable, *, max_pages=10, max_items=1000, page_token=None):
    """Await async raw pages; ordinary AsyncResourceIterator is a different API."""
    if max_pages <= 0 or max_items <= 0:
        raise ValueError("Page and item budgets must be positive")
    items, used_tokens, cursor = [], set(), page_token
    for number in range(1, max_pages + 1):
        if cursor is not None:
            if cursor in used_tokens:
                return PageResult(items, [], cursor, number - 1, False, "repeated-token")
            used_tokens.add(cursor)
        response = await fetch_page(page_token=cursor)
        try:
            page = response.decode()
        finally:
            await response.aclose()
        remaining = _accept(page, items, max_items)
        cursor = page.next_page_token
        if remaining:
            return PageResult(items, remaining, cursor, number, False, "item-budget")
        if not cursor:
            return PageResult(items, [], None, number, True, "complete")
        if len(items) >= max_items:
            return PageResult(items, [], cursor, number, False, "item-budget")
    return PageResult(items, [], cursor, max_pages, False, "page-budget")
