# Project: Machine Learning for Next-Day precipitation Prediction in Lund

This is a report about weather prediction model created by Haoyang Qian\& Ruowen Xiao. The main idea is to make a binary conclusion about whether there will be precipitation(≥0.1 mm) on the second day based on the weather conditions from the first day. The workflow includes data acquisition \& processing, exploratory data analysis, feature engineering, model training \& validation and model application \& result presentation. 



## Directory Structure

```text
Course project/
├── data
│  └── lund_daily_weather.csv                            (Retrieved data)
├── model
│  ├── final_rf.joblib                                   (Trained joblib model)
│  ├── kmeans_weather.joblib                             (Weather Clustering Model)
│  └── scaler_cluster.joblib                             (Feature Scaler)
├── output (Vitualised results)
│  ├── test_confusion_matrix_nn.png
│  ├── test_confusion_matrix.png  
│  ├── test_feature_importance.png
│  └── test_roc_curve.png         
├── get_data.ipynb                                       (Data retrieval script)
├── main.ipynb                                           (Main script)
├── run_to_predict.ipynb                                 (Weather prediction script)
├── environment.yml        
├── LICENSE          
└── README.md              
```

## Setup & Reproduction

   ```bash
   git clone https://github.com/Ha5248qi/BERN02_excercise.git
   cd "BERN02_excercise/Course project"
   conda env create -f environment.yml
   conda activate climate_env
   jupyter lab
   ```
   
## Dependencies & Requirements

This project was developed and tested using **Python 3.12** on the **JupyterLab** environment. The core dependencies and recommended version ranges required to run the data collection, modeling, and real-time inference pipelines are listed below:

- **python**: `3.12.*` (Core runtime environment)
- **pandas**: `>=2.2, <3.0` (Time-series data cleaning and daily feature engineering)
- **numpy**: `>=2.0, <3.0` (Numerical computation and matrix operations)
- **scikit-learn**: `1.9.1` (K-Means clustering, StandardScaler, Random Forest classification, and evaluation metrics)
- **matplotlib**: `3.11.1` (Plotting feature importance, ROC curves, and confusion matrices)
- **seaborn**: `0.13.2` (Statistical data visualization and plotting themes)
- **requests**: `>=2.34, <3.0` (Fetching historical and live weather data via Open-Meteo API)
- **joblib**: `1.6.0` (Serialization and loading of trained models and scalers)
- **jupyterlab**: `>=4.0, <5.0` (Interactive notebook platform)

### Quick Installation

You can install all required packages at once using `pip`:

```bash
pip install "pandas>=2.2,<3.0" "numpy>=2.0,<3.0" scikit-learn==1.9.1 matplotlib==3.11.1 seaborn==0.13.2 "requests>=2.34,<3.0" joblib==1.6.0 jupyterlab
```
## License
This project is with a [MIT license](LICENSE) open-source license.
   
