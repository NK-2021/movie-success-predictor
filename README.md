# 🎬 Movie Success Predictor

Predict whether a movie will be a box-office hit using data from TMDB!  
This end-to-end data science project walks through data cleaning, feature engineering, and training a logistic regression model to classify a movie as successful or not.

---

## 📌 Project Objective

To build a machine learning model that predicts movie success (binary classification: success/failure) using key features like budget, popularity, runtime, genre, and director.

---

## 📂 Folder Structure

movie-success-predictor/
│
├── data/ # Raw and cleaned datasets
├── notebooks/ # Jupyter notebooks for EDA, engineering, and modeling
├── src/ # Python scripts for reusable code
├── outputs/ # Trained models and visual outputs
├── README.md # Project overview (this file)
└── requirements.txt # Python dependencies


---

## 🔍 Dataset

- Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Files used:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

---

## 🛠️ Key Technologies

- **Python** (Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib)
- **Jupyter Lab** for development
- **Logistic Regression** for binary classification

---

## 🚀 Workflow Summary

1. **📥 Data Loading & Merging**
   - Combined movies and credits datasets from TMDB.
2. **🧹 Data Cleaning**
   - Handled null values, removed duplicates, dropped irrelevant columns.
3. **🔧 Feature Engineering**
   - Extracted main genre from nested JSON.
   - Extracted director from crew list.
   - Created binary `success` target based on revenue vs budget.
4. **🤖 Model Training**
   - Used Logistic Regression to classify movie success.
   - Evaluated with accuracy, precision, recall, and confusion matrix.
5. **💾 Model Saving**
   - Exported trained model using `joblib`.

---

## 🧪 Model Performance

| Metric       | Value     |
|--------------|-----------|
| Accuracy     | ~78–82%   |
| Model Used   | Logistic Regression |
| Features     | Budget, Popularity, Runtime |

> *Note: Results may vary based on train-test split and scaling.*

---

## 📈 Visual Insights

- Scatterplot of Budget vs Revenue
- Runtime distribution
- Most common genres
- Confusion matrix

---

## 📁 How to Run This Project

1. Clone this repo  
   `git clone https://github.com/your-username/movie-success-predictor.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Launch Jupyter Lab  
   `jupyter lab`

4. Run the notebooks in order:
   - `01_data_exploration.ipynb`
   - `02_feature_engineering.ipynb`
   - `03_model_training.ipynb`

---

## 🙋‍♀️ About Me

I'm **Neena Khan**, a frontend engineer turned generative AI and data science enthusiast.  
This project is part of my portfolio to showcase my skills in end-to-end machine learning with Python.

🔗 [LinkedIn](https://linkedin.com/in/your-profile)  
📫 [Email me](mailto:youremail@example.com)

---

## 📌 License

This project is licensed under the MIT License.


