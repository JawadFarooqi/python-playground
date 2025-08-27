"""Simple utility functions for Python learning notebooks."""

import contextlib
import os
import platform
import sys
import time
from dataclasses import dataclass


@dataclass
class TimingResult:
    """Result from timing a code block."""
    label: str
    seconds: float

    def __str__(self) -> str:
        return f"{self.label}: {self.seconds:.4f}s"


def describe_env() -> dict:
    """Get information about your Python environment.
    
    Returns:
        dict: Python version, platform, and current directory
    
    Example:
        >>> env = describe_env()
        >>> print(f"Python {env['python']} on {env['platform']}")
    """
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "executable": sys.executable,
        "cwd": os.getcwd(),
    }


@contextlib.contextmanager
def timer(label: str = "operation"):
    """Time how long code takes to run.
    
    Args:
        label: Name for this timing measurement
    
    Example:
        >>> with timer("my calculation") as t:
        ...     result = sum(range(1000))
        >>> print(t)
        my calculation: 0.0001s
    """
    start = time.perf_counter()
    result = TimingResult(label=label, seconds=0.0)
    try:
        yield result
    finally:
        result.seconds = time.perf_counter() - start
