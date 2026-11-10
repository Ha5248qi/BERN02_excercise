# Report

## Introduction

This is a report about weather prediction model created by Haoyang Qian & Ruowen Xiao.

The main idea is to make a binary conclusion about whether there will be precipitation(≥0.1 mm) on the second day based on the weather conditions from the first day. The workflow includes data acquisition & processing, exploratory data analysis, feature engineering, model training & validation and model application & result presentation.

The weather data applied in this project is retrieved from an open-source website Open-Meteo (website:https://open-meteo.com).

## Methods

The project applies K-Means clustering for unsupervised learning and Random Forest and Neural Networks for supervised classification.

K-Means was selected to identify different weather patterns, while Random Forest and Neural Networks were used to compare two supervised learning approaches. These methods can capture non-linear relationships in weather data. However, the models may not capture all factors influencing precipitation.

Histograms were used to examine feature distributions, while a correlation heatmap was used to show relationships between variables. PCA scatter plots were used to visualise the K-Means clusters in two dimensions. Confusion matrices and ROC curves were used to evaluate classification performance, and feature importance plots were used to interpret the Random Forest
model.

## FAIR Principles

This project was developed following the FAIR principles:

- Findable: The datasets and generated results are saved with descriptive names, making different parts of the project easier to locate. The project can be easily found on Github
- Accessible: The workflow uses openly available weather data from the Open-Meteo Archive API. The processed datasets and analysis results can also be accessed through the project files on Github.
- Interoperable: The data is stored in standard tabular formats such as CSV and processed using common Python libraries, making it easy to reuse with other tools.
- Reusable: The environment requirement to run this project are documented in the README.md file. This allows others to easily reproduce the analysis.

The complete workflow is implemented in a Jupyter Notebook [main.ipynb](main.ipynb). The code and explanations are organised to make the analysis reproducible.

This project is with a [MIT license](LICENSE) open-source license.

## Checklist

1. A well-defined problem
2. Use data from an existing source, or generate data as part of a simulation experiment
3. Include data analysis with one or more methods of statistical learning from the course
4. Justify the choice and discussion of limitations of the method
5. Data visualisation and a discussion of why particular graph styles were chosen.
6. Reflection on FAIR principles, and how each concept of the acronym relates to the project (data and workflow).
7. All of the above should be implemented in a reproducible workflow, e.g. a Jupyter Notebook. Please upload it to complete the final assignment.
8. Must have a license