# Phishing URL Detection

## 📌 Overview

Phishing URL Detection is a Machine Learning-based cybersecurity project that identifies whether a given URL is legitimate or phishing. The system analyzes URL characteristics and predicts the likelihood of a phishing attack, helping users avoid fraudulent websites and protect sensitive information.

---

## 🚀 Features

* Detects phishing and legitimate URLs
* Machine Learning-based prediction model
* User-friendly interface
* Fast and accurate URL analysis
* Real-time URL validation
* Easy to deploy and use

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Model Training:** Random Forest / Logistic Regression
* **Frontend:** HTML, CSS
* **Backend:** Flask
* **Development Environment:** Jupyter Notebook / VS Code

---

## 📂 Project Structure

```text
Phishing-URL-Detection/
│
├── dataset/
│   └── phishing_dataset.csv
│
├── model/
│   └── phishing_model.pkl
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/balajinpb10-ops/Phishing-URL-detection.git
```

### 2. Navigate to Project Directory

```bash
cd Phishing-URL-detection
```

### 3. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📊 Machine Learning Workflow

1. Collect phishing and legitimate URL datasets.
2. Perform data preprocessing and cleaning.
3. Extract URL-based features.
4. Train Machine Learning model.
5. Evaluate model performance.
6. Deploy model using Flask.
7. Predict URLs in real time.

---

## 🔍 URL Features Used

* URL Length
* Number of Dots
* Number of Hyphens
* Presence of IP Address
* HTTPS Usage
* Special Characters
* Suspicious Keywords
* Domain Information

---

## 📈 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 95%+  |
| Precision | High  |
| Recall    | High  |
| F1-Score  | High  |

> Note: Performance may vary depending on the dataset and model used.

---

## 🖥️ Usage

1. Enter a URL in the input field.
2. Click **Check URL**.
3. The system analyzes the URL.
4. View the prediction result:

    * ✅ Legitimate URL
    * ⚠️ Phishing URL

---

## 🔮 Future Enhancements

* Deep Learning-based detection
* Domain age analysis
* WHOIS integration
* Browser extension support
* Real-time threat intelligence APIs
* URL reputation scoring

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 👨‍💻 Author

**Balaji P**

* GitHub: [balajinpb10-ops](https://github.com/balajinpb10-ops?utm_source=chatgpt.com)

---



### ⭐ If you found this project useful, please give it a star on GitHub! ⭐
