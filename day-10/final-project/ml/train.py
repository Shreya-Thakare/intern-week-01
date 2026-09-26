from pathlib import Path
import numpy as np,pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,f1_score
from joblib import dump
root=Path(__file__).parent; rng=np.random.default_rng(42); n=300
x=pd.DataFrame({'cleanliness_score':rng.uniform(1,10,n),'odor_score':rng.uniform(1,10,n),'waste_level':rng.uniform(0,10,n),'complaints':rng.poisson(3,n),'footfall':rng.integers(30,1000,n),'hours_since_cleaning':rng.uniform(1,72,n)})
risk=(10-x.cleanliness_score)+.7*x.odor_score+.8*x.waste_level+.4*x.complaints+.015*x.footfall+.11*x.hours_since_cleaning
y=(risk>risk.median()).astype(int); x['cleaning_delay_ratio']=x.hours_since_cleaning/(x.footfall+1)*100
Xtr,Xte,ytr,yte=train_test_split(x,y,test_size=.25,random_state=42,stratify=y)
models={'logistic':LogisticRegression(max_iter=1500),'forest':RandomForestClassifier(n_estimators=200,max_depth=7,random_state=42)}; results=[]
for name,model in models.items():
 p=Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler()),('model',model)]);p.fit(Xtr,ytr);pred=p.predict(Xte);results.append((name,accuracy_score(yte,pred),f1_score(yte,pred),p))
best=max(results,key=lambda r:r[2]);dump(best[3],root/'hygiene_model.joblib');pd.DataFrame([{ 'model':a,'accuracy':b,'f1_score':c} for a,b,c,_ in results]).to_csv(root/'model_evaluation.csv',index=False);print('Selected:',best[0],'F1:',round(best[2],3))
