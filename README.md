# Heart_disease_analysis using Python
This project analyzes a heart disease dataset using Python with data cleaning, EDA, and visualizations. As part of my data science learning journey, the goal is to practice handling data, explore different graphs, and gain insights through real-world health data.

**1. Import the Libraries and Dataset:**
The project begins by importing essential Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn. The heart disease dataset is then loaded, providing the foundation for further exploration and analysis.

**2. Display First 5 Rows:**
The first five rows of the dataset are displayed to get an initial understanding of the data and its structure.

**3. Display Last 5 Rows:**
The last five rows are viewed to check data consistency and verify that the dataset has been loaded correctly.

**4. Shape of Dataset:**
The shape of the dataset is examined to identify the total number of rows and columns for a quick overview.

**5. Display Number of Rows:**
The total number of rows is calculated to understand how many data records are available for analysis.

**6. Display Number of Columns:**
The number of columns is displayed to know how many features or attributes exist in the dataset.

**7. Display Column Names:**
Column names are listed to understand the attributes available and plan which features to analyze.

**8. Information About Dataset:**
Dataset information is checked to review data types, non-null counts, and overall structure for proper preprocessing.

**9. Check Null Values:**
Null values are identified in each column to handle missing data before analysis and visualization.

**10. Check and Drop Duplicated Values:**
The dataset is checked for duplicate rows, and any duplicates found are removed to ensure data quality and accurate analysis.

**11. Describe Dataset:**
Descriptive statistics of the dataset are generated to summarize key metrics like mean, median, minimum, maximum, and standard deviation for numeric columns.


**12. Heart Disease Count:**
Bar plot showing number of patients with and without heart disease; clearly indicates prevalence.

**13. Count of Male and Female:**
Countplot of gender distribution; helps understand dataset gender balance.

**14. Age Distribution:**
Histogram of patient ages; shows which age ranges are most common in dataset.

**15. Gender Distribution According to Target:**
Stacked barplot of gender vs heart disease; shows male/female risk differences.

**16. Age Group with Highest Heart Disease:**
Barplot of age groups vs heart disease count; identifies high-risk age ranges.

**17. Cholesterol Level Differences:**
Boxplot of cholesterol by heart disease; highlights higher levels in affected patients.

**18. Resting Blood Pressure Differences:**
Boxplot of resting BP for both groups; shows variation between healthy and diseased.

**19. Fasting Blood Sugar Relation:**
Countplot of high FBS (>120 mg/dl) vs heart disease; indicates higher risk correlation.

**20. Chest Pain Frequency Differences:**
Countplot of chest pain types by heart disease; shows specific pain types more associated.

**21. Maximum Heart Rate and Heart Disease Risk:**

A scatter or boxplot showing maximum heart rate, highlighting whether lower or higher rates relate to heart disease.

**22. Exercise-Induced Chest Pain:**

A countplot examining chest pain during exercise, indicating increased likelihood of heart disease among affected patients.

**23. “Oldpeak” (ST Depression) Relation:**

A boxplot showing ST depression values (“oldpeak”) by heart disease status, reflecting exercise-induced cardiac stress.

**24. Resting ECG Result Differences:**

A countplot comparing resting ECG results for patients with and without heart disease, identifying potential diagnostic patterns.

**25. Slope of Peak Exercise ST Segment:**

A barplot illustrating the relationship between ST segment slope during peak exercise and heart disease occurrence.

**26. Thalassemia Types and Heart Disease:**

A countplot evaluating different thalassemia (thal) types, highlighting their association with heart disease prevalence.

**27. Age and Cholesterol Combined Risk:**

A scatterplot of age versus cholesterol, showing how higher values together may increase heart disease risk.

**28. Sex and Chest Pain Type Influence:**

A grouped barplot analyzing how gender and chest pain types jointly impact heart disease likelihood.

**29. Dataset Balance for Target Variable:**

A bar chart showing distribution of the target variable, identifying whether the dataset is balanced or skewed.

**30. Features Most Strongly Correlated with Heart Disease:**

A heatmap or correlation matrix highlighting features with strongest positive or negative correlations to heart disease.

**31. Distribution of Serum Cholesterol:**

A histogram or boxplot showing serum cholesterol distribution across all patients in the dataset.

**32. Resting Blood Pressure Comparison by Sex:**

Boxplots comparing resting blood pressure between male and female patients, highlighting sex-based differences.

**33. Continuous Variables Plot:**

Pairplots or histograms visualizing all continuous features, providing an overview of distributions and relationships.
