**Credit Card Fraud Detection API**

 **Project Objective**
This project aims to detect fraudulent credit card transactions using machine learning. It includes a trained classification model and a FastAPI endpoint for real-time predictions.
Note: Dataset not included in repo due to size. You can download it from Kaggle:
https://www.kaggle.com/mlg-ulb/creditcardfraud

 **Technologies Used**
- Model: LightGBM, RandomSearchCV
- Preprocessing: SMOTE Oversampling
- API: FastAPI, Pydantic
- Model Saving: joblib
  
 **Project Structure**
credit-fraud-detection-api/
├── app/              ← FastAPI app 
├── notebooks/        ← Model development (CreditFraud.ipynb)
├── saved_models/     ← Saved model (best_model.pkl)
├── requirements.txt  ← Required packages
├── README.md         ← Documentation
└── .gitignore


 **How to Run**
1. Create virtual environment (optional):
   python -m venv venv
   source venv/bin/activate (or venv\Scripts\activate on Windows)
2. Install packages:
   pip install -r requirements.txt
3. Run the API:
   uvicorn app:app --reload
4. API Docs:
   Swagger UI → http://127.0.0.1:8000/docs

   

  
**References**
- Dataset: https://www.kaggle.com/mlg-ulb/creditcardfraud
- FastAPI: https://fastapi.tiangolo.com
- LightGBM: https://lightgbm.readthedocs.io

  
**Author**
Made with ❤️ by Maryam Khosravi
GitHub: https://github.com/maryamkhosravii

