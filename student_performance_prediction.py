"""
Task 6: Student Performance Prediction
A beginner-friendly machine-learning classification project.

Dataset note:
student_performance_dataset.csv is synthetic/illustrative data created for learning.
It is not real student data and should not be used to make decisions about real students.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "student_performance_dataset.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
features = [
    "study_hours_per_day",
    "attendance_percentage",
    "previous_exam_score",
    "assignment_completion_percentage",
]
target = "passed"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
])
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Dataset rows: {len(df)}")
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")
print(f"Accuracy: {accuracy:.3f}")
print("\nClassification report:")
print(classification_report(y_test, predictions, zero_division=0))

# Plot 1: distribution of the synthetic target labels.
ax = df["passed"].map({0: "Not passed", 1: "Passed"}).value_counts().plot(
    kind="bar", rot=0, title="Distribution of Illustrative Outcome Labels"
)
ax.set_xlabel("Outcome")
ax.set_ylabel("Number of records")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "outcome_distribution.png", dpi=160)
plt.close()

# Plot 2: confusion matrix on the held-out test split.
ConfusionMatrixDisplay.from_predictions(
    y_test, predictions, display_labels=["Not passed", "Passed"], cmap="Blues"
)
plt.title("Confusion Matrix - Test Set")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "confusion_matrix.png", dpi=160)
plt.close()

# Save test predictions for review.
results = X_test.copy()
results["actual_passed"] = y_test
results["predicted_passed"] = predictions
results.to_csv(OUTPUT_DIR / "test_predictions.csv", index=False)

print(f"\nCharts and test predictions saved in: {OUTPUT_DIR}")
print("Reminder: this is a learning demonstration using synthetic data.")
