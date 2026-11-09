from __future__ import annotations

import datetime

from constants import LOG_FILE

_entries: list[str] = []


def log_error(message: str) -> None:
    """Записать сообщение об ошибке ввода с меткой времени."""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{ts}] {message}"
    _entries.append(entry)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except OSError:
        pass


def get_entries() -> list[str]:
    return list(_entries)


def clear() -> None:
    _entries.clear()