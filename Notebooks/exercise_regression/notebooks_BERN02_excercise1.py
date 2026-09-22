# 
# Excercise 1
# 
# Author:Haoyang Qian
# 
# Date:2026/09/01
# 


import numpy as np
import matplotlib as plt
import csv

def find_nearest_points(x:np.array,y:np.array,k:int,x0:np.array):
    se=[]
    pred=[]
    for xa in x0:
        d_=[]
        x_nearest=[]
        y_nearest=[]
        d=[]
        x_bar_w=[]
        w=[]
        for i in range(len(x)):
            d_=np.append(d_,np.abs(x[i]-xa))

        d_sorted=np.sort(d_)
        d_total=np.sum(d_sorted[:k])
        d_thres=d_sorted[k]

        for i in range(len(x)):
            if x[i]-xa<=d_thres:
                x_nearest=np.append(x_nearest,x[i])
                d=np.append(d,x[i]-xa)
                y_nearest=np.append(y_nearest,y[i])
                
        for i in range(len(x_nearest)):
        #w=np.append(w,1-d[i]/d_total)
        #x_bar_w=np.sum(np.array(w)*np.array(x_nearest))
        #y_bar_w=np.sum(np.array(w)*np.array(y_nearest))
        #beta_1=sum(k*(x-x_bar_w)*(y-y_bar_w))/sum(k*(x-x_bar_w)**2)
        #beta_0=y_bar_w-beta_1*x_bar_w
            x_bar=np.mean(x_nearest)
            y_bar=np.mean(y_nearest)
            beta_1=sum(k*(x-x_bar)*(y-y_bar))/sum(k*(x-x_bar)**2)
            beta_0=y_bar-beta_1*x_bar
    
        pred=np.append(pred,beta_0+beta_1*xa)
        y_nearest_fit=beta_0+beta_1*x_nearest
        residuals=y_nearest_fit-y_nearest
        se_a=np.sqrt(np.mean(residuals**2))
        se=np.append(se,se_a)
    
    return pred,se
        

pollution_data = np.genfromtxt('pollution_cleaneddata.csv', delimiter=',', skip_header=1)

#print(pollution_data)
poor=pollution_data[:,10]
mort=pollution_data[:,15]
print(poor)
print(mort)
len

len(poor)==len(mort)

print(find_nearest_points(poor,mort,k=2,x0=[10,18,25]))







