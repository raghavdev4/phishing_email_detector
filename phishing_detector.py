import re
import numpy as np
import pandas as pd

from scipy.sparse import hstack

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv("phishing_email.csv")
print(data.columns)
print("Dataset Loaded Successfully!\n")
print(data.head())

# ==========================================
# FEATURES AND LABELS
# ==========================================

X = data["text_combined"]
y = data["label"]

# ==========================================
# FEATURE EXTRACTION FUNCTION
# ==========================================

def extract_features(email):

    email = str(email)

    urls = re.findall(r'https?://\S+|www\.\S+', email)

    url_count = len(urls)

    ip_url = int(
        bool(
            re.search(
                r'https?://\d+\.\d+\.\d+\.\d+',
                email
            )
        )
    )

    shortener = int(
        bool(
            re.search(
                r'bit\.ly|tinyurl|goo\.gl|t\.co|ow\.ly|is\.gd',
                email,
                re.IGNORECASE
            )
        )
    )

    keywords = [
        "verify","login","password","bank","urgent",
        "click","account","update","confirm","security",
        "winner","claim","free","gift","limited",
        "offer","otp","invoice","payment","paypal",
        "netflix","amazon"
    ]

    keyword_count = sum(
        email.lower().count(word)
        for word in keywords
    )

    exclamation_count = email.count("!")

    digit_count = sum(
        c.isdigit()
        for c in email
    )

    email_length = len(email)

    return [
        url_count,
        ip_url,
        shortener,
        keyword_count,
        exclamation_count,
        digit_count,
        email_length
    ]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ==========================================
# TF-IDF
# ==========================================

vectorizer = TfidfVectorizer(stop_words="english")

X_train_text = vectorizer.fit_transform(X_train)
X_test_text = vectorizer.transform(X_test)

# ==========================================
# CUSTOM SECURITY FEATURES
# ==========================================

X_train_features = np.array(
    [extract_features(email) for email in X_train]
)

X_test_features = np.array(
    [extract_features(email) for email in X_test]
)

X_train_final = hstack((X_train_text, X_train_features))
X_test_final = hstack((X_test_text, X_test_features))

# ==========================================
# MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train_final, y_train)

print("\nModel Trained Successfully!")

# ==========================================
# EVALUATION
# ==========================================

y_pred = model.predict(X_test_final)

accuracy = accuracy_score(y_test, y_pred)

print("\n========== MODEL PERFORMANCE ==========")

print(f"Accuracy : {accuracy:.4f}")

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ==========================================
# USER INPUT
# ==========================================

print("\n========== EMAIL DETECTION ==========")
print("\nPaste the email below.")
print("Type END on a new line when finished.\n")

lines = []

while True:

    line = input()

    if line.upper() == "END":
        break

    lines.append(line)

user_email = "\n".join(lines)

# ==========================================
# SECURITY ANALYSIS
# ==========================================

feature_values = extract_features(user_email)

print("\n========== SECURITY ANALYSIS ==========")

print(f"URLs Found           : {feature_values[0]}")
print(f"IP Address URL       : {'Yes' if feature_values[1] else 'No'}")
print(f"Shortened URL        : {'Yes' if feature_values[2] else 'No'}")
print(f"Keyword Matches      : {feature_values[3]}")
print(f"Exclamation Marks    : {feature_values[4]}")
print(f"Digits               : {feature_values[5]}")
print(f"Email Length         : {feature_values[6]}")

# ==========================================
# FINAL PREDICTION
# ==========================================

sample_text = vectorizer.transform([user_email])

sample_features = np.array(
    [extract_features(user_email)]
)

sample_final = hstack(
    (sample_text, sample_features)
)

prediction = model.predict(sample_final)[0]

confidence = np.max(
    model.predict_proba(sample_final)
) * 100

print("\n========== CYBERSHIELD AI RESULT ==========")

if prediction == 1:
    print("⚠️ HIGH RISK PHISHING EMAIL")
else:
    print("✅ SAFE EMAIL")

print(f"\nConfidence : {confidence:.2f}%")
print(f"Prediction : {'Phishing' if prediction == 1 else 'Safe'}")