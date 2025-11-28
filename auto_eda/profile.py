import pandas as pd
class DataProfiler:
    def __init__(self,file_path):
        self.df=pd.read_csv(file_path)
    def data_overview(self):
        # return basic information about the dataset
        return {
            "n_rows":len(self.df),
            "n_cols":len(self.df.columns),
            "columns":list(self.df.columns),
            "dtypes":self.df.dtypes.astype(str).to_dict()
        }
    def missing_values(self):
        #  return missing value summary
        return (self.df.isnull().sum() / len(self.df)*100).round(2).to_dict()
    def numeric_summary(self):
        #  stats for numeric columns
        return self.df.describe().to_dict()
    def categorical_summary(self):
        #  stats for categorical columns
        cat_cols = self.df.select_dtypes(include=['object','category']).columns
        summary = {}
        for col in cat_cols:
            summary[col] = {"unique":self.df[col].nunique(),
                            "top_fre":self.df[col].value_counts().head(1).to_dict()}
        return summary