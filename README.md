# 📧 Phishing Email Detector

## Overview

Phishing Email Detector is a Machine Learning-based cybersecurity project developed to identify phishing emails by analyzing their content and detecting common phishing indicators.

The system combines Natural Language Processing (NLP) with cybersecurity-focused feature extraction to classify emails as either **Safe** or **Phishing**. It also provides a basic security analysis by examining URLs, suspicious keywords, shortened links, and other characteristics commonly found in phishing attacks.

---

## Features

- Machine Learning-based phishing email detection
- Random Forest Classification
- TF-IDF text vectorization
- URL detection
- IP-based URL detection
- URL shortener detection
- Suspicious keyword analysis
- Email security feature extraction
- Confidence score prediction
- Interactive command-line email scanner
- Model evaluation using:
  - Accuracy
  - Confusion Matrix
  - Classification Report

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Regular Expressions (re)

---

## Project Structure

```
phishing-email-detector/
│
├── phishing_detector.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/raghavdev4/phishing_email_detector.git
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python phishing_detector.py
```

---

## Dataset

The project was trained using a phishing email dataset containing thousands of email samples.

**Note:** The dataset is not included in this repository because it exceeds GitHub's 100 MB file size limit.

After downloading the dataset, place it in the project folder as:

```
phishing_email.csv
```

---

## Project Status

✅ **This project successfully meets the requirements of the assigned cybersecurity mini project.**

The current implementation includes:

- Complete machine learning pipeline
- Email preprocessing
- TF-IDF vectorization
- Random Forest classifier
- Custom phishing feature extraction
- Email security analysis
- Performance evaluation
- Interactive phishing detection

Beyond the project requirements, future updates will focus on improving the application with additional cybersecurity features, enhanced detection techniques, and a graphical web interface.

---

## Future Enhancements

Planned improvements include:

- Flask-based web application
- Modern user interface
- Drag-and-drop email upload
- Risk score visualization
- Scan history
- Detailed phishing explanation engine
- Advanced feature engineering
- Model optimization

---

## Project Objective

The objective of this project is to develop a phishing email detection system using Machine Learning techniques that can assist users in identifying potentially malicious emails through automated analysis and classification.

---

## Author

**Raghavdev**

BCA Cyber Security

GitHub: https://github.com/raghavdev4/phishing_email_detector.git

---

## License

This project was developed for educational and academic purposes.