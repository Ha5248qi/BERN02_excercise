#BERN02 exercise2
#Haoyang Qian
#2026/9/8

!mamba install pandas

import pandas as pd
import numpy as np
from scipy.optimize import minimize

df=pd.read_csv("bird_count.csv")

df["x"]=df["yr"]-1999
y=df["count"].values
x=df["x"].values
print(df,y,x)

def poisson(params,x,y):
    beta_0,beta_1=params
    lambda_=np.exp(beta_0+beta_1*x)
    log_likelihood=sum(lambda_-y*(beta_0+beta_1*x))
            #-np.log(math.factorial(y))，this part is ignored as it doesn't have impact on the minimization result.
    return log_likelihood


#parameter optimization

initial_guess = [0.0, 0.0]
result = minimize(poisson, initial_guess, args=(x, y), method='BFGS')
beta_0_hat,beta_1_hat=result.x
print(f"optimal beta_0_hat and beta_1_hat are {beta_0_hat:.4f}, {beta_1_hat:.4f},respectively")


#generate three samples
lambda_hat=np.exp(beta_0_hat+beta_1_hat*x)
df["lambda_hat"]=np.exp(beta_0_hat+beta_1_hat*x)
np.random.seed(0)
df["prediction_1"]=np.random.poisson(lam=lambda_hat)
np.random.seed(1)
df["prediction_2"]=np.random.poisson(lam=lambda_hat)
np.random.seed(2)
df["prediction_3"]=np.random.poisson(lam=lambda_hat)

df.to_csv("bird_count_predictions.csv", index=False)
print(df)







