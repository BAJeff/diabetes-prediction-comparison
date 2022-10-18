# Midterm Report

https://link.springer.com/chapter/10.1007/978-981-13-8798-2_12

The dataset referenced in this paper contains 520 observations and 17 attributes that are collected using direct questionnaires and diagnosis results from the patients in the Sylhet Diabetes Hospital in Sylhet, Bangladesh. There are 2 demographic features, Age & Gender; the other 15 attributes are binary features that indicate whether the patient experienced a symptom

By the due date of milestone report on 10/23, we should be able to reproduce the results from the first paper. For the milestone report, we will each tackle an algorithm and attempt to reproduce the results from (Islam et al. 2020). With the exception of Decision Tree/Random Forest, this corresponds with the material taught on the syllabus.

# File Structure
```
.
├── README.md
├── data
│   ├── lmch-diabetes.csv
│   ├── pima-diabetes.csv
│   └── sylhet-dataset.csv
├── docs
│   └── annotated-Proposal_for_the_Reproduction_of_Diabetes_Prediction_Methods.pdf
├── notebooks
│   └── 1-jb-sylhet-decision-tree.ipynb
├── output
├── setup.sh
├── spec-file.txt
└── src
    └── pull-data.py
```

## Other Notes
Run
```
chmod +x setup.sh
```
in a terminal to give the shell script permission to be executed from the terminal.
