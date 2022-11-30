# %%
from os.path import dirname, abspath
from pathlib import Path

# %%
base_dir = dirname(abspath(__file__))
root_dir = str(Path(base_dir).parent)
print(root_dir)

!curl -o $root_dir/data/sylhet-diabetes.csv 'https://archive.ics.uci.edu/ml/machine-learning-databases/00529/diabetes_data_upload.csv'
!curl -o $root_dir/data/lmch-diabetes.csv 'https://prod-dcd-datasets-public-files-eu-west-1.s3.eu-west-1.amazonaws.com/e205d80e-2bc6-49ed-bfcc-4215b6b516fd'

# need to add API token to kaggle to use this comman.... just go here to download
# https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

# !kaggle datasets download -d uciml/pima-diabetes.csv