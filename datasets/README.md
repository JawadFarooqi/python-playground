# Datasets for Python Playground

This directory contains sample datasets for hands-on practice in the data science notebooks. All datasets are either synthetic (generated for learning) or from public domain sources.

## Available Datasets

### 📊 Basic Practice Data
- **`sales_data.csv`** - Monthly sales data for practicing pandas basics
- **`student_scores.csv`** - Student test scores for statistics and visualization
- **`weather_data.csv`** - Temperature and weather data for time series analysis

### 🏢 Business Analytics
- **`employee_data.csv`** - HR data for grouping and analysis practice
- **`customer_data.csv`** - Customer demographics and purchase behavior

### 🌍 Real-World Practice
- **`world_population.csv`** - Country population data for advanced analysis
- **`stock_prices.csv`** - Sample stock price data for financial analysis

## Usage in Notebooks

Each dataset is designed to be used with specific notebooks:

- **Notebooks 21-22**: Use basic practice data
- **Notebooks 23-24**: Use business analytics data  
- **Notebook 25**: Use real-world practice data for final project

## Loading Data

```python
import pandas as pd

# Load any dataset
df = pd.read_csv('datasets/sales_data.csv')

# Or use the playground utility (coming soon)
from playground import load_dataset
df = load_dataset('sales_data')
```

## Data Sources

All datasets are either:
- Synthetically generated for educational purposes
- Derived from public domain sources
- Used with appropriate attribution

See individual dataset documentation for specific sources and licenses.
