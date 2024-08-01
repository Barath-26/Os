import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Load dataset
df = pd.read_csv('dataset.csv')

# Prepare data
X = df['text']
y = df['is_distracting']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with TfidfVectorizer and LogisticRegression
model = make_pipeline(TfidfVectorizer(), LogisticRegression())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save the model
import joblib
joblib.dump(model, 'distraction_classifier.pkl')
