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

<img width="640" height="480" alt="Heart disease incidence" src="https://github.com/user-attachments/assets/3b7ef27f-4072-4ec9-9014-fb5ccd0bd819" />

**13. Count of Male and Female:**

Countplot of gender distribution; helps understand dataset gender balance.

<img width="640" height="480" alt="Gender Distribution" src="https://github.com/user-attachments/assets/1642a596-ab6b-4c9b-81ed-240b13b78165" />

**14. Age Distribution:**

Histogram of patient ages; shows which age ranges are most common in dataset.

<img width="640" height="480" alt="age distribution" src="https://github.com/user-attachments/assets/4ac5da59-7c5f-48d1-9cc4-922f100ad6a0" />

**15. Gender Distribution According to Target:**

Stacked barplot of gender vs heart disease; shows male/female risk differences.

<img width="640" height="480" alt="Gender Distribution According to heart disease" src="https://github.com/user-attachments/assets/94e0193e-0397-451d-b0c4-ab7c7439485c" />

**16. Age Group with Highest Heart Disease:**

Barplot of age groups vs heart disease count; identifies high-risk age ranges.

<img width="640" height="480" alt="age group distribution heart disease" src="https://github.com/user-attachments/assets/f05555ee-ac62-4d7d-9d01-bd0e099ec125" />

**17. Cholesterol Level Differences:**

Boxplot of cholesterol by heart disease; highlights higher levels in affected patients.

<img width="640" height="480" alt="cholesterol level" src="https://github.com/user-attachments/assets/62711941-1f58-49e0-a7a8-2db446d27989" />

**18. Resting Blood Pressure Differences:**

Boxplot of resting BP for both groups; shows variation between healthy and diseased.

<img width="640" height="480" alt="Resting blood pressure" src="https://github.com/user-attachments/assets/eac1c312-d645-4172-8a51-efbb065ace69" />

**19. Fasting Blood Sugar Relation:**

Countplot of high FBS (>120 mg/dl) vs heart disease; indicates higher risk correlation.

<img width="640" height="480" alt="fasting blood sugar" src="https://github.com/user-attachments/assets/9beb1929-4f60-4cd9-9e1e-9cef79f082c3" />

**20. Chest Pain Frequency Differences:**
Countplot of chest pain types by heart disease; shows specific pain types more associated.

<img width="640" height="480" alt="chest pain" src="https://github.com/user-attachments/assets/487726f2-0566-4618-bcf1-39f7e3c50751" />

**21. Maximum Heart Rate and Heart Disease Risk:**

A scatter or boxplot showing maximum heart rate, highlighting whether lower or higher rates relate to heart disease.

<img width="800" height="600" alt="Maximum Heart Rate" src="https://github.com/user-attachments/assets/31f2de9e-46fe-4477-a94b-8ce11efa0257" />

**22. Exercise-Induced Chest Pain:**

A countplot examining chest pain during exercise, indicating increased likelihood of heart disease among affected patients.

<img width="640" height="480" alt="Exercise-Induced Chest Pain" src="https://github.com/user-attachments/assets/679098ba-f03f-44b7-b282-e99e49c0416c" />

**23. “Oldpeak” (ST Depression) Relation:**

A boxplot showing ST depression values (“oldpeak”) by heart disease status, reflecting exercise-induced cardiac stress.

<img width="640" height="480" alt="Oldpeak" src="https://github.com/user-attachments/assets/67560eb1-26be-48ef-a523-8de1b19d31a0" />

**24. Resting ECG Result Differences:**

A countplot comparing resting ECG results for patients with and without heart disease, identifying potential diagnostic patterns.

<img width="640" height="480" alt="Resting ECG" src="https://github.com/user-attachments/assets/59732f03-adbf-44ec-9096-f0a8f5cf871e" />

**25. Slope of Peak Exercise ST Segment:**

A barplot illustrating the relationship between ST segment slope during peak exercise and heart disease occurrence.

<img width="640" height="480" alt="Slope of Peak Exercise" src="https://github.com/user-attachments/assets/f7f7f35e-b251-43f7-a739-8d465a6967ae" />

**26. Thalassemia Types and Heart Disease:**

A countplot evaluating different thalassemia (thal) types, highlighting their association with heart disease prevalence.

<img width="640" height="480" alt="Thalassemia" src="https://github.com/user-attachments/assets/fba8049a-207b-4338-9e9e-059d64237a95" />

**27. Age and Cholesterol Combined Risk:**

A scatterplot of age versus cholesterol, showing how higher values together may increase heart disease risk.

<img width="640" height="480" alt="Age and Cholesterol" src="https://github.com/user-attachments/assets/d2710066-e60b-4daf-9501-202d47c2c218" />

**28. Sex and Chest Pain Type Influence:**

A grouped barplot analyzing how gender and chest pain types jointly impact heart disease likelihood.

<img width="1057" height="500" alt="Sex and Chest Pain" src="https://github.com/user-attachments/assets/aa816761-9901-4823-9ccc-908c09f71737" />

**29. Dataset Balance for Target Variable:**

A bar chart showing distribution of the target variable, identifying whether the dataset is balanced or skewed.

<img width="640" height="480" alt="Balance for Target Variable" src="https://github.com/user-attachments/assets/20254f4c-932a-4c20-b015-8112f106451e" />

**30. Features Most Strongly Correlated with Heart Disease:**

A heatmap or correlation matrix highlighting features with strongest positive or negative correlations to heart disease.

<img width="800" height="500" alt="Correlated with Heart Disease" src="https://github.com/user-attachments/assets/4a34e455-503f-43e5-a61f-5f2fd9e5b63d" />

**31. Distribution of Serum Cholesterol:**

A histogram or boxplot showing serum cholesterol distribution across all patients in the dataset.
<img width="640" height="480" alt="Serum Cholesterol" src="https://github.com/user-attachments/assets/5ace02c7-9e27-4e0f-b8c4-7b1ad3da3de4" />

**32. Resting Blood Pressure Comparison by Sex:**

Boxplots comparing resting blood pressure between male and female patients, highlighting sex-based differences.

<img width="1200" height="300" alt="Resting Blood Pressure sex" src="https://github.com/user-attachments/assets/4c7ddfd4-9990-4d7e-a46e-ebc3bacbd386" />

**33. Continuous Variables Plot:**

Pairplots or histograms visualizing all continuous features, providing an overview of distributions and relationships.

<img width="1536" height="754" alt="Continuous Variables Plot" src="https://github.com/user-attachments/assets/e76e60c8-41de-4286-80a3-0db4396a8d75" />
