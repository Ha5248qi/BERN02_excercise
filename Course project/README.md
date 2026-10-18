# Project: Machine Learning for Next-Day precipitation Prediction in Lund

This is a report about weather prediction model created by Haoyang Qian\& Ruowen Xiao. The main idea is to make a binary conclusion about whether there will be precipitation(≥0.1 mm) on the second day based on the weather conditions from the first day. The workflow includes data acquisition \& processing, exploratory data analysis, feature engineering, model training \& validation and model application \& result presentation. 



## Directory Structure

```text
Course project/
├── final_rf.joblib                                   (trained joblib model)
├── kmeans_weather.joblib                             (K-means clustering feature)
├── 
├── get_data.ipynb                                    (data retrieval script)
├── main.ipynb                                        (main script)
├── run_to_predict.ipynb                              (weather prediction script)
├── lund_daily_weather.csv                            (retrieved data)
├── 
├──
├── environment.yml        
├── LICENSE          
└── README.md              
```

## Setup and Reproduction

   ```bash
   git clone [https://github.com/ha5248qi/Analysis-practice.git](https://github.com/ha5248qi/Analysis-practice.git)
   cd Analysis-practice
   conda env create -f environment.yml
   conda activate climate_env
   jupyter lab
   ```
   
## Key Dependencies

dependencies:
  - python=3.12   #There are some differences in different python versions. To avoid breaking down, a python version 3.12 is recommended
  - numpy>=2.0,<3.0
  - matplotlib>=3.11,<4.0
  - jupyterlab
   
## License
This project is with a [MIT license](LICENSE) open-source license.
   
