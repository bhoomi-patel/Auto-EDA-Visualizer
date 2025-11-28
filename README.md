# Auto‑EDA Visualizer

A simple and powerful Python tool for automated **Exploratory Data Analysis (EDA)** on CSV datasets.

This tool helps you quickly understand your dataset by generating **visual summaries, statistics, and an HTML report** — all with a single command.

---

## Features

- **Basic Summary**: View row count, column count, data types, and missing value percentages.
- **Numerical Insights**: Automatically compute key statistics (mean, median, standard deviation, min, max).
- **Categorical Insights**: Display unique counts and top frequent categories.
- **Auto Visualizations**: Generate histograms, boxplots, and a correlation heatmap automatically.
- **HTML Report**: Combines key insights and charts into one easy-to-read web report.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto-eda.git
   cd auto-eda
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy seaborn matplotlib jinja2
   ```

---

## Usage

Run Auto‑EDA on any CSV file:

```bash
python auto_eda.py path/to/your/file.csv
```

By default, this will:

- Generate charts inside an `eda_plots/` folder  
- Create a report file named `eda_report.html` in the project directory  

Then simply open the HTML file in your browser to explore the automatic EDA results.

---

## Example

```bash
python auto_eda.py examples/sample.csv
```
