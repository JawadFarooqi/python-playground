"""Simple utility functions for Python learning notebooks."""

import contextlib
import os
import platform
import sys
import time
from dataclasses import dataclass
from pathlib import Path


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


def load_dataset(name: str, return_path: bool = False):
    """Load a sample dataset for practice.
    
    Args:
        name: Dataset name (without .csv extension)
        return_path: If True, return file path instead of loading data
    
    Returns:
        pandas.DataFrame or str: Dataset or path to dataset file
    
    Available datasets:
        - sales_data: Monthly sales data
        - student_scores: Student test scores  
        - weather_data: Temperature and weather data
        - employee_data: HR data for analysis
        
    Example:
        >>> df = load_dataset('sales_data')
        >>> print(df.head())
    """
    # Find the datasets directory
    current_file = Path(__file__)
    repo_root = current_file.parent.parent.parent
    datasets_dir = repo_root / "datasets"
    
    dataset_file = datasets_dir / f"{name}.csv"
    
    if not dataset_file.exists():
        available = [f.stem for f in datasets_dir.glob("*.csv")]
        raise FileNotFoundError(
            f"Dataset '{name}' not found. Available datasets: {available}"
        )
    
    if return_path:
        return str(dataset_file)
    
    try:
        import pandas as pd
        return pd.read_csv(dataset_file)
    except ImportError:
        raise ImportError(
            "pandas is required to load datasets. Install with: pip install pandas"
        )
