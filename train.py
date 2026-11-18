import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from preprocess import get_splits

# 1. Get the training data (the 80%)
train_df, test_df = get_splits()
X_train = train_df["clean_text"]
y_train = train_df["label"]

# 2. Build the pipeline: TF-IDF -> Logistic Regression
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),   # look at single words AND word pairs ("ignore previous")
        min_df=1,             # keep every word (our dataset is small)
        sublinear_tf=True,    # dampens words repeated many times
    )),
    ("clf", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",  # treat safe and malicious fairly
    )),
])

# 3. Train
model.fit(X_train, y_train)

# 4. Save the trained model to a file
joblib.dump(model, "models/model.joblib")

print("Training complete!")
print("Trained on", len(X_train), "prompts")
print("Training accuracy:", round(model.score(X_train, y_train), 3))
print("Model saved to models/model.joblib")