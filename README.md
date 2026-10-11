# Task 6: Student Performance Prediction

## Project overview
This capstone demonstrates a basic end-to-end machine-learning workflow. A logistic regression classifier uses four input features to predict an illustrative binary outcome (`passed`).

## Dataset
`student_performance_dataset.csv` contains 240 **synthetic/illustrative** records with:
- `study_hours_per_day`
- `attendance_percentage`
- `previous_exam_score`
- `assignment_completion_percentage`
- `passed` (0 = not passed, 1 = passed)

The dataset is generated for educational practice; it is not real student data and must not be used to judge real students.

## Tools
Python, pandas, scikit-learn, matplotlib.

## Run the project
1. Install Python 3.10 or later.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python student_performance_prediction.py
   ```

The script prints evaluation metrics and creates an `outputs/` folder containing the outcome distribution chart, confusion matrix, and test predictions.

## Workflow
1. Load the CSV dataset.
2. Separate input features and target label.
3. Split the data into training and test sets.
4. Standardize features and train logistic regression.
5. Evaluate using accuracy and a classification report.
6. Save visualizations and test predictions.

## Limitations and responsible use
The dataset is synthetic and the labels are based on a simplified artificial rule. Results do not establish real-world predictive performance. Real educational data would require permission, privacy protection, bias checks, and careful human review.
