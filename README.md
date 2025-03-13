# Heart Disease Data Analysis

## Overview
This project performs exploratory data analysis (EDA) and preprocessing on a heart disease dataset. The script loads the dataset, cleans missing values, removes outliers, computes basic statistics, and visualizes key relationships between features.

## Dependencies
Make sure you have the following Python libraries installed before running the script:
- numpy
- pandas
- matplotlib
- seaborn

You can install them using:
```bash
pip install numpy pandas matplotlib seaborn
```

## Dataset
The dataset used in this project is expected to be in CSV format. Ensure that the dataset file `heart.csv` is correctly placed at the specified path:
```
C:\Users\user\Desktop\Intelligent Programming\Tasks\Task 3\heart.csv
```

## Features Analyzed
- **Cholesterol (chol)**: Outliers are detected and removed using the IQR method.
- **Blood Pressure (trestbps)**: Mean values are computed separately for patients with and without heart disease.
- **Maximum Heart Rate (thalach)**: Identifies min and max values.
- **Chest Pain Type (cp)**: Visualized as a pie chart.
- **Heart Disease Indicator (target)**: Visualized using a count plot.

## Preprocessing Steps
1. **Handling Missing Values:** Missing data is filled using column means.
2. **Outlier Removal:** IQR method is used to remove extreme values in cholesterol levels.
3. **Sorting & Searching:**
   - Sorts dataset by cholesterol levels.
   - Identifies patients with high cholesterol (>300).
   - Filters elderly patients (>60 years) with abnormal ECG results.

## Visualizations
The script generates the following plots:
- **Histogram of Cholesterol Distribution**
- **Scatter Plot of Age vs Maximum Heart Rate**
- **Count Plot of Patients with/without Heart Disease**
- **3D Scatter Plot of Cholesterol, Age, and Heart Disease**
- **Pie Chart of Chest Pain Type Distribution**

## Running the Script
Simply execute the Python script:
```bash
python script.py
```
Ensure the dataset file is present and accessible in the specified directory.

## License
This project is for educational purposes and does not include any proprietary data. You are free to modify and use it as needed.

