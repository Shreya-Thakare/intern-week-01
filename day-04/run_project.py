from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
ROOT=Path(__file__).resolve().parent
raw=pd.read_csv(ROOT/'dataset/facility_hygiene_raw.csv')
# Cleaning: remove duplicate IDs, coerce invalid numeric values to missing, then median-impute.
df=raw.drop_duplicates(subset='facility_id').copy()
features=['cleanliness_score','odor_score','waste_level','complaints','footfall','hours_since_cleaning']
for col in features: df[col]=pd.to_numeric(df[col],errors='coerce')
for col in ['cleanliness_score','odor_score','waste_level']:
    df.loc[~df[col].between(0,10),col]=np.nan
for col in ['complaints','footfall','hours_since_cleaning']:
    df.loc[df[col]<0,col]=np.nan
df[features]=df[features].fillna(df[features].median())
# Feature engineering before split is deterministic and uses no target values.
df['cleaning_delay_ratio']=df['hours_since_cleaning']/(df['footfall']+1)*100
model_features=features+['cleaning_delay_ratio']
df.to_csv(ROOT/'preprocessing/facility_hygiene_cleaned.csv',index=False)
# EDA figures.
plt.figure(figsize=(6,4));df['hygiene_risk'].value_counts().plot(kind='bar',color=['#ef4444','#22c55e']);plt.title('Hygiene risk classes');plt.ylabel('Facility count');plt.tight_layout();plt.savefig(ROOT/'visualizations/risk_distribution.png',dpi=140);plt.close()
plt.figure(figsize=(6,4));plt.scatter(df['cleanliness_score'],df['odor_score'],c=(df.hygiene_risk=='High').map({True:'#ef4444',False:'#22c55e'}));plt.xlabel('Cleanliness score');plt.ylabel('Odor score');plt.title('Cleanliness vs odor');plt.tight_layout();plt.savefig(ROOT/'visualizations/cleanliness_vs_odor.png',dpi=140);plt.close()
X,y=df[model_features],df['hygiene_risk'].eq('High').astype(int)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
results=[]; trained={}
for name,estimator in {'Logistic Regression':LogisticRegression(max_iter=1500,random_state=42),'Random Forest':RandomForestClassifier(n_estimators=250,max_depth=7,random_state=42)}.items():
 pipe=Pipeline([('imputer',SimpleImputer(strategy='median')),('scale',StandardScaler()),('model',estimator)])
 pipe.fit(X_train,y_train); pred=pipe.predict(X_test);prob=pipe.predict_proba(X_test)[:,1]
 results.append({'model':name,'accuracy':accuracy_score(y_test,pred),'precision':precision_score(y_test,pred),'recall':recall_score(y_test,pred),'f1_score':f1_score(y_test,pred)})
 trained[name]=(pipe,pred,prob)
 pd.DataFrame(confusion_matrix(y_test,pred),index=['Actual Low','Actual High'],columns=['Predicted Low','Predicted High']).to_csv(ROOT/f'evaluation/{name.lower().replace(" ","_")}_confusion_matrix.csv')
 (ROOT/f'evaluation/{name.lower().replace(" ","_")}_classification_report.txt').write_text(classification_report(y_test,pred,target_names=['Low','High']))
comparison=pd.DataFrame(results).sort_values('f1_score',ascending=False);comparison.to_csv(ROOT/'evaluation/model_comparison.csv',index=False)
best_name=comparison.iloc[0]['model'];best,pred,prob=trained[best_name];dump(best,ROOT/'models/best_hygiene_risk_model.joblib')
output=X_test.copy();output['actual_risk']=np.where(y_test==1,'High','Low');output['predicted_risk']=np.where(pred==1,'High','Low');output['high_risk_probability']=prob.round(3);output.to_csv(ROOT/'predictions/test_predictions.csv',index=False)
(ROOT/'evaluation/selected_model.txt').write_text(f'Selected model: {best_name}\nSelection metric: F1 score\nF1 score: {comparison.iloc[0]["f1_score"]:.3f}\n')
print(comparison.to_string(index=False))
