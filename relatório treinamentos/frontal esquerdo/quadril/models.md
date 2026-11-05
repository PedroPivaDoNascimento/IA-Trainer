        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: F1_SCORE
============================================================
Acuracia(CV - accuracy)      79.22%
Acuracia(CV - f1_score)      86.24%
Acuracia(CV - precision)     81.70%
Acuracia(CV - recall)        91.63%
Acuracia(CV - roc_auc)       73.97%
Acuracia(CV - mcc)           46.24%
Desvio Padrão (CV - f1_score) 2.0377%
------------------------------------------------------------
              precision    recall  f1-score   support

   CERTO (0)       0.90      0.75      0.82        12
  ERRADO (1)       0.91      0.97      0.94        30

    accuracy                           0.90        42
   macro avg       0.90      0.86      0.88        42
weighted avg       0.90      0.90      0.90        42
ROC AUC: 0.86
MCC: 0.76

Parâmetros: {'clf': SVC(class_weight='balanced', random_state=42), 'clf__C': 2.5, 'clf__degree': 3, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': StandardScaler()}
Random State usado: 470
