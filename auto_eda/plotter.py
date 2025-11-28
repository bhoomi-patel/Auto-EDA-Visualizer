import os
import matplotlib.pyplot as plt
import seaborn as sns
def plot_distributions(df,out_dir):
    os.makedirs(out_dir,exist_ok=True)
    plots = []
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        plt.figure(figsize=(4,3))
        sns.histplot(df[col].dropna(), kde=True , bins=30)
        plt.title(f"Distribution of {col}")
        fname = os.path.join(out_dir,f"{col}_dist.png")
        plt.savefig(fname)
        plt.close()
        plots.append(fname)
    return plots
def plot_boxplots(df,out_dir):
    os.makedirs(out_dir,exist_ok=True)
    plots=[]
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        plt.figure(figsize=(4,3))
        sns.boxplot(x=df[col].dropna())
        plt.title(f"Boxplot of {col}")
        fname = os.path.join(out_dir, f"{col}_box.png")
        plt.savefig(fname)
        plt.close()
        plots.append(fname)
    return plots
def plot_correlation_matrix(df, out_dir):
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) < 2:
        return None
    plt.figure(figsize=(8,6))
    corr = df[num_cols].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    fname = os.path.join(out_dir, "correlation_matrix.png")
    plt.title("Correlation Matrix")
    plt.savefig(fname)
    plt.close()
    return fname