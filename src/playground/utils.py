"""Utility helpers used across notebooks.

Keep functions here deterministic & lightweight so they run quickly in CI.
"""
from __future__ import annotations

import contextlib
import os
import platform
import sys
import time
from dataclasses import dataclass
from typing import Callable, Generator, Iterable, Any


@dataclass
class TimingResult:
    """Result returned by timer context manager."""
    label: str
    seconds: float

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.label}: {self.seconds:.4f}s"


def describe_env() -> dict[str, Any]:
    """Return a snapshot of the Python execution environment.

    Useful for reproducibility sections in notebooks.
    """
    return {
        "python": sys.version.split()[0],
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "executable": sys.executable,
        "cwd": os.getcwd(),
    }


def timer(label: str = "block") -> Generator[TimingResult, None, None]:
    """Context manager that measures execution time of a code block.

    Example::
        with timer("load-data") as t:
            load()
        print(t)
    """
    start = time.perf_counter()
    result = TimingResult(label=label, seconds=0.0)
    try:
        yield result
    finally:
        result.seconds = time.perf_counter() - start


@contextlib.contextmanager
def time_call(label: str, func: Callable[..., Any], *args, **kwargs) -> Iterable[TimingResult]:
    """Time the execution of a callable inside a context for uniform API.

    Example::
        with time_call("sleep", time.sleep, 0.1) as res:
            pass
        print(res)
    """
    with timer(label) as t:
        func(*args, **kwargs)
        yield t
