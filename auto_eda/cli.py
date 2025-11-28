import argparse
from datetime import datetime
import os
from auto_eda.profile import DataProfiler
from auto_eda.plotter import plot_distributions,plot_boxplots,plot_correlation_matrix
from auto_eda.insights import detect_imbalance,find_outliers,detect_skewed
from auto_eda.report import generate_html_report

def main():
    parser = argparse.ArgumentParser(description="Auto-EDA Visualizer: Generate visual EDA report for your CSV.")
    parser.add_argument("csv_path", help="Path to your CSV file")
    parser.add_argument("--output",default="reports/autoeda_report.html",help="HTML report output path")
    parser.add_argument("--images",default="reports/plots",help="Directory for images")
    parser.add_argument("--target",default=None,help="Target column for imbalance detection")
    args = parser.parse_args()
    profiler = DataProfiler(args.csv_path)
    overview = profiler.data_overview()
    missing = profiler.missing_values()

    dist_plots=plot_distributions(profiler.df,args.images)
    box_plots = plot_boxplots(profiler.df,args.images)
    corr_plot = plot_correlation_matrix(profiler.df,args.images)

    insights = [
        detect_imbalance(profiler.df,args.target),
        find_outliers(profiler.df),
        detect_skewed(profiler.df)
    ]

    generate_html_report(
        args.output,
        timestamp=str(datetime.now()),
        overview=overview,
        missing_values=missing,
        dist_plots=[os.path.relpath(p,os.path.dirname(args.output)) for p in dist_plots],
        box_plots=[os.path.relpath(p, os.path.dirname(args.output)) for p in box_plots],
        corr_plot=os.path.relpath(corr_plot, os.path.dirname(args.output)) if corr_plot else None,
        insights=insights
    )

    print(f"Auto-EDA HTML report generated: {args.output}")

if __name__ == "__main__":
    main()