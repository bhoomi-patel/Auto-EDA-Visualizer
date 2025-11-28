import numpy as np
def detect_imbalance(df,target_col=None):
    '''check if target is highly imbalanced (for classification).'''
    result = {}
    if target_col and target_col in df.columns:
        counts = df[target_col].value_counts(normalize=True)
        max_class = counts.max()
        if max_class > 0.8:
            result[target_col] = f"Highly imbalanced: top class = {(max_class*100):.1f}%"
    return result
def find_outliers(df,threshold=3.):
    '''flag columns with possible outliers (using z-score).'''
    outliers = {}
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        col_zscore = ((df[col] - df[col].mean()) / df[col].std()).abs()
        if (col_zscore > threshold).sum() > 0:
            outliers[col] = f"Possible outliers detected ( z > {threshold})"
    return outliers
def detect_skewed(df, skew_thresh=1):
    """Flag highly skewed numerical columns."""
    skews = df.skew(numeric_only=True)
    issues = {col: f"Skewed data: {v:.2f}" for col, v in skews.items() if abs(v) > skew_thresh}
    return issues