"""Minimal Windows compatibility shim for the Home Assistant test stack.

This allows pytest to import modules that expect the Unix ``fcntl`` module
when running inside a non-Unix Python environment.
"""

from __future__ import annotations

import os
from typing import Any


def flock(fd: Any, operation: int) -> int:
    """Return a no-op success value for file locking operations."""
    return 0


def lockf(fd: Any, operation: int, length: int = 0, start: int = 0, whence: int = 0) -> int:
    """Return a no-op success value for lockf compatibility."""
    return 0


def fnctl(fd: Any, op: int, *args: Any, **kwargs: Any) -> int:
    """Provide a generic no-op compatibility function for `fnctl`-style calls."""
    return 0


def ioctl(fd: Any, op: int, *args: Any, **kwargs: Any) -> int:
    """Provide a generic no-op compatibility function for `ioctl`-style calls."""
    return 0


def open(*args: Any, **kwargs: Any) -> Any:
    return os.open(*args, **kwargs)


__all__ = ["flock", "lockf", "fnctl", "ioctl", "open"]
