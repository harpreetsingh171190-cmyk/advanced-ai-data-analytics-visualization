# 26-Chart Professional Visual Research Notebook

**Author & Maintainer:** Harpreet Singh  
**Format:** Jupyter Notebook (`.ipynb`) + PNG figures + CSV comparison tables  
**Scope:** CPU/CUDA/MPS research notebook with a separately runnable 26-chart demonstration and export section.

> **Data provenance:** Some chart data is synthetic/demonstration data, including OHLC prices, Gantt task schedules and Sankey flows. These values must not be interpreted as measured hardware benchmarks or real financial records.

## Architecture diagram

```mermaid
flowchart TD
  A[Research Notebook] --> B[Original CPU / CUDA / MPS sections]
  A --> C[26-chart visualization section]
  C --> D[Chart-specific data]
  D --> E[26 PNG figures]
  D --> F[26 CSV comparison tables]
  E --> G[Export ZIP]
  F --> G
  C --> H[Audit CSV and SHA-256 manifest]
  H --> G
```

## Chart data pipeline

```mermaid
flowchart LR
  A[Input or synthetic data] --> B[Data validation]
  B --> C[Chart rendering]
  C --> D[PNG output]
  B --> E[Comparison table]
  E --> F[CSV output]
  D --> G[Audit and archive]
  F --> G
```

## Chart gallery and corresponding tables

Every thumbnail below links to a generated PNG. Each table link opens the corresponding exported CSV.

### Comparison

| Chart | Figure | Comparison data |
|---|---|---|
| Bar Chart | [![Bar Chart](professional_26_charts/bar_chart.png)](professional_26_charts/bar_chart.png) | [CSV](professional_26_charts/comparison_tables/bar_chart.csv) |
| Grouped Bar Chart | [![Grouped Bar Chart](professional_26_charts/grouped_bar_chart.png)](professional_26_charts/grouped_bar_chart.png) | [CSV](professional_26_charts/comparison_tables/grouped_bar_chart.csv) |
| Stacked Bar Chart | [![Stacked Bar Chart](professional_26_charts/stacked_bar_chart.png)](professional_26_charts/stacked_bar_chart.png) | [CSV](professional_26_charts/comparison_tables/stacked_bar_chart.csv) |
| Bullet Graph | [![Bullet Graph](professional_26_charts/bullet_graph.png)](professional_26_charts/bullet_graph.png) | [CSV](professional_26_charts/comparison_tables/bullet_graph.csv) |
| Lollipop Chart | [![Lollipop Chart](professional_26_charts/lollipop_chart.png)](professional_26_charts/lollipop_chart.png) | [CSV](professional_26_charts/comparison_tables/lollipop_chart.csv) |

### Change over time

| Chart | Figure | Comparison data |
|---|---|---|
| Line Graph | [![Line Graph](professional_26_charts/line_graph.png)](professional_26_charts/line_graph.png) | [CSV](professional_26_charts/comparison_tables/line_graph.csv) |
| Area Chart | [![Area Chart](professional_26_charts/area_chart.png)](professional_26_charts/area_chart.png) | [CSV](professional_26_charts/comparison_tables/area_chart.csv) |
| Stacked Area Chart | [![Stacked Area Chart](professional_26_charts/stacked_area_chart.png)](professional_26_charts/stacked_area_chart.png) | [CSV](professional_26_charts/comparison_tables/stacked_area_chart.csv) |
| Candlestick Ohlc Chart | [![Candlestick Ohlc Chart](professional_26_charts/candlestick_ohlc_chart.png)](professional_26_charts/candlestick_ohlc_chart.png) | [CSV](professional_26_charts/comparison_tables/candlestick_ohlc_chart.csv) |
| Gantt Chart | [![Gantt Chart](professional_26_charts/gantt_chart.png)](professional_26_charts/gantt_chart.png) | [CSV](professional_26_charts/comparison_tables/gantt_chart.csv) |

### Part-to-whole

| Chart | Figure | Comparison data |
|---|---|---|
| Pie Chart | [![Pie Chart](professional_26_charts/pie_chart.png)](professional_26_charts/pie_chart.png) | [CSV](professional_26_charts/comparison_tables/pie_chart.csv) |
| Donut Chart | [![Donut Chart](professional_26_charts/donut_chart.png)](professional_26_charts/donut_chart.png) | [CSV](professional_26_charts/comparison_tables/donut_chart.csv) |
| Treemap | [![Treemap](professional_26_charts/treemap.png)](professional_26_charts/treemap.png) | [CSV](professional_26_charts/comparison_tables/treemap.csv) |
| Population Pyramid | [![Population Pyramid](professional_26_charts/population_pyramid.png)](professional_26_charts/population_pyramid.png) | [CSV](professional_26_charts/comparison_tables/population_pyramid.csv) |

### Distribution

| Chart | Figure | Comparison data |
|---|---|---|
| Histogram | [![Histogram](professional_26_charts/histogram.png)](professional_26_charts/histogram.png) | [CSV](professional_26_charts/comparison_tables/histogram.csv) |
| Box Plot | [![Box Plot](professional_26_charts/box_plot.png)](professional_26_charts/box_plot.png) | [CSV](professional_26_charts/comparison_tables/box_plot.csv) |
| Violin Plot | [![Violin Plot](professional_26_charts/violin_plot.png)](professional_26_charts/violin_plot.png) | [CSV](professional_26_charts/comparison_tables/violin_plot.csv) |
| Dot Plot | [![Dot Plot](professional_26_charts/dot_plot.png)](professional_26_charts/dot_plot.png) | [CSV](professional_26_charts/comparison_tables/dot_plot.csv) |
| Stem And Leaf Plot | [![Stem And Leaf Plot](professional_26_charts/stem_and_leaf_plot.png)](professional_26_charts/stem_and_leaf_plot.png) | [CSV](professional_26_charts/comparison_tables/stem_and_leaf_plot.csv) |

### Relationships

| Chart | Figure | Comparison data |
|---|---|---|
| Scatter Plot | [![Scatter Plot](professional_26_charts/scatter_plot.png)](professional_26_charts/scatter_plot.png) | [CSV](professional_26_charts/comparison_tables/scatter_plot.csv) |
| Bubble Plot | [![Bubble Plot](professional_26_charts/bubble_plot.png)](professional_26_charts/bubble_plot.png) | [CSV](professional_26_charts/comparison_tables/bubble_plot.csv) |
| Parallel Coordinates Plot | [![Parallel Coordinates Plot](professional_26_charts/parallel_coordinates_plot.png)](professional_26_charts/parallel_coordinates_plot.png) | [CSV](professional_26_charts/comparison_tables/parallel_coordinates_plot.csv) |

### Flow and networks

| Chart | Figure | Comparison data |
|---|---|---|
| Flowchart | [![Flowchart](professional_26_charts/flowchart.png)](professional_26_charts/flowchart.png) | [CSV](professional_26_charts/comparison_tables/flowchart.csv) |
| Sankey Diagram | [![Sankey Diagram](professional_26_charts/sankey_diagram.png)](professional_26_charts/sankey_diagram.png) | [CSV](professional_26_charts/comparison_tables/sankey_diagram.csv) |
| Network Graph | [![Network Graph](professional_26_charts/network_graph.png)](professional_26_charts/network_graph.png) | [CSV](professional_26_charts/comparison_tables/network_graph.csv) |
| Waterfall Chart | [![Waterfall Chart](professional_26_charts/waterfall_chart.png)](professional_26_charts/waterfall_chart.png) | [CSV](professional_26_charts/comparison_tables/waterfall_chart.csv) |

## Export workflow

```mermaid
flowchart TD
  A[Open project directory] --> B[Install dependencies]
  B --> C[Run export_26_charts.sh]
  C --> D[Execute visualization cells]
  D --> E{All 26 completed?}
  E -->|Yes| F[Create ZIP archive]
  E -->|No| G[Inspect errors and dependencies]
  G --> C
```

## Quick start (Linux, Kaggle or Jupyter terminal)

Keep the `.ipynb`, `run_export_26_charts.py`, and `export_26_charts.sh` files in the same folder.

```bash
bash export_26_charts.sh
```

In a Kaggle/Jupyter code cell:

```python
!bash export_26_charts.sh
from IPython.display import FileLink, display
display(FileLink("Harpreet_Singh_26_Charts_Exports.zip"))
```

The export script executes the **26-chart section only**. It does not run or validate the original CPU/CUDA/MPS notebook end-to-end. It will regenerate the ZIP file in the current project directory.

## Directory structure

```text
project/
├── README.md
├── 22-3834-harpreet-singh-26-chart-professional-edition.ipynb
├── export_26_charts.sh
├── run_export_26_charts.py
└── professional_26_charts/
    ├── <26 chart-name>.png
    ├── chart_audit.csv
    ├── sha256_manifest.json
    └── comparison_tables/
        └── <26 chart-name>.csv
```

## Validation and limitations

- The packaged output includes 26 PNG figures and 26 corresponding CSV comparison tables.
- The audit CSV and SHA-256 manifest support review of exported artifacts.
- Synthetic demonstration data should be replaced with measured/real data for scientific conclusions.
- Figures are generated from chart-specific datasets; cross-chart comparisons are not necessarily comparable without harmonized units.
- Original CPU/CUDA/MPS code may need supported hardware and additional dependencies.

## License and attribution

Author/maintainer: **Harpreet Singh**. Preserve original third-party attribution and licenses present in the notebook; no new license is implied by this README.
