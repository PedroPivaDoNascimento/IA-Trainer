        ====== MODELO 10 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: F1_SCORE
============================================================
Acuracia(CV - accuracy)      81.82%
Acuracia(CV - balanced_accuracy) 67.20%
Acuracia(CV - f1_score)      88.85%
Acuracia(CV - precision)     84.52%
Acuracia(CV - recall)        93.69%
Acuracia(CV - roc_auc)       80.59%
Acuracia(CV - mcc)           41.40%
Desvio Padrão (CV - f1_score) 3.2431%
------------------------------------------------------------
              precision    recall  f1-score   support

   CERTO (0)       1.00      0.56      0.71         9
  ERRADO (1)       0.89      1.00      0.94        33

    accuracy                           0.90        42
   macro avg       0.95      0.78      0.83        42
weighted avg       0.92      0.90      0.89        42
ROC AUC: 0.78
MCC: 0.70
Balanced Accuracy: 0.78

Parâmetros: {'clf': SVC(class_weight='balanced', random_state=42), 'clf__C': 2.5, 'clf__degree': 3, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': StandardScaler()}
Random State usado: 814