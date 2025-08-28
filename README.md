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

A countplot was used to compare the number of patients with and without heart disease. This gives a quick idea of dataset balance.

<img width="640" height="480" alt="Heart disease incidence" src="https://github.com/user-attachments/assets/3b7ef27f-4072-4ec9-9014-fb5ccd0bd819" />

**13. Count of Male and Female:**

A countplot was created to show the number of male and female patients. This helps understand gender representation in the dataset.

<img width="640" height="480" alt="Gender Distribution" src="https://github.com/user-attachments/assets/1642a596-ab6b-4c9b-81ed-240b13b78165" />

**14. Age Distribution of Patients:**

A histogram was plotted to show the distribution of patient ages. It highlights which age ranges have the most patients.

<img width="640" height="480" alt="age distribution" src="https://github.com/user-attachments/assets/4ac5da59-7c5f-48d1-9cc4-922f100ad6a0" />

**15. Gender Distribution According to Target Variable**

A countplot with `hue=target` was used to compare males and females across heart disease and non-heart disease groups.

<img width="640" height="480" alt="Gender Distribution According to heart disease" src="https://github.com/user-attachments/assets/94e0193e-0397-451d-b0c4-ab7c7439485c" />

**16. Age Group with Highest Heart Disease:**

Age was divided into bins (20–29, 30–39, etc.), and a countplot showed heart disease occurrence across groups. This reveals age-based risk.

<img width="640" height="480" alt="age group distribution heart disease" src="https://github.com/user-attachments/assets/f05555ee-ac62-4d7d-9d01-bd0e099ec125" />

**17. Cholesterol Level Differences:**

Cholesterol values were grouped into ranges, and a countplot was plotted. It shows how cholesterol levels differ between patients with and without disease.

<img width="640" height="480" alt="cholesterol level" src="https://github.com/user-attachments/assets/62711941-1f58-49e0-a7a8-2db446d27989" />

**18. Resting Blood Pressure Differences:**

Blood pressure was grouped into categories (Normal, High, etc.) and compared with target values using a countplot. It highlights blood pressure patterns.

<img width="640" height="480" alt="Resting blood pressure" src="https://github.com/user-attachments/assets/eac1c312-d645-4172-8a51-efbb065ace69" />

**19. Fasting Blood Sugar Relation:**

A countplot was used to compare patients with fasting blood sugar >120 mg/dl against heart disease. This helps assess diabetes-related risks.

<img width="640" height="480" alt="fasting blood sugar" src="https://github.com/user-attachments/assets/9beb1929-4f60-4cd9-9e1e-9cef79f082c3" />

**20. Chest Pain Frequency Differences:**

A countplot was used to analyze chest pain categories. This shows which chest pain types are most linked to heart disease.

<img width="640" height="480" alt="chest pain" src="https://github.com/user-attachments/assets/487726f2-0566-4618-bcf1-39f7e3c50751" />

**21. Maximum Heart Rate and Heart Disease Risk:**

A boxplot compared maximum heart rate across target groups. It reveals whether higher or lower heart rates are related to disease.

<img width="800" height="600" alt="Maximum Heart Rate" src="https://github.com/user-attachments/assets/31f2de9e-46fe-4477-a94b-8ce11efa0257" />

**22. Exercise-Induced Angina vs Heart Disease:**

A countplot analyzed the effect of exercise-induced angina on heart disease. This highlights exercise-related heart strain patterns.

<img width="640" height="480" alt="Exercise-Induced Chest Pain" src="https://github.com/user-attachments/assets/679098ba-f03f-44b7-b282-e99e49c0416c" />

**23. “Oldpeak” (ST Depression) Relation:**

A histogram compared oldpeak values for both groups. This shows how ST depression measurements differ in patients with and without disease.

<img width="640" height="480" alt="Oldpeak" src="https://github.com/user-attachments/assets/67560eb1-26be-48ef-a523-8de1b19d31a0" />

**24. Resting ECG Result Differences:**

A countplot compared ECG results with target values. It helps analyze the effect of abnormal ECG patterns on disease.

<img width="640" height="480" alt="Resting ECG" src="https://github.com/user-attachments/assets/59732f03-adbf-44ec-9096-f0a8f5cf871e" />

**25. Slope of Peak Exercise ST Segment:**

A countplot checked slope categories against target. This helps visualize exercise test results related to heart risk.

<img width="640" height="480" alt="Slope of Peak Exercise" src="https://github.com/user-attachments/assets/f7f7f35e-b251-43f7-a739-8d465a6967ae" />

**26. Thalassemia Types and Heart Disease:**

We used a bar plot (countplot with percentages) to compare thalassemia (thal) types with heart disease occurrence.

<img width="640" height="480" alt="Thalassemia" src="https://github.com/user-attachments/assets/fba8049a-207b-4338-9e9e-059d64237a95" />

**27. Age and Cholesterol Combined Risk:**

A scatterplot compared age and cholesterol values with the target. This visual shows combined effects of age and cholesterol on heart disease.

<img width="640" height="480" alt="Age and Cholesterol" src="https://github.com/user-attachments/assets/d2710066-e60b-4daf-9501-202d47c2c218" />

**28. Sex and Chest Pain Type Influence:**

A grouped countplot compared chest pain type and sex with heart disease. It helps understand gender-specific symptom differences.

<img width="1057" height="500" alt="Sex and Chest Pain" src="https://github.com/user-attachments/assets/aa816761-9901-4823-9ccc-908c09f71737" />

**29. Dataset Balance for Target Variable:**

A countplot of the target column checked dataset balance. It shows if the dataset is balanced or imbalanced for prediction.

<img width="640" height="480" alt="Balance for Target Variable" src="https://github.com/user-attachments/assets/20254f4c-932a-4c20-b015-8112f106451e" />

**30. Features Most Strongly Correlated with Heart Disease:**

A barplot displayed correlation strength of features with the target. This highlights which features are most useful for prediction.

<img width="800" height="500" alt="Correlated with Heart Disease" src="https://github.com/user-attachments/assets/4a34e455-503f-43e5-a61f-5f2fd9e5b63d" />

**31. Distribution of Serum Cholesterol:**

A histogram was created to check cholesterol distribution. It shows how cholesterol values are spread among patients.

<img width="640" height="480" alt="Serum Cholesterol" src="https://github.com/user-attachments/assets/5ace02c7-9e27-4e0f-b8c4-7b1ad3da3de4" />

**32. Resting Blood Pressure Comparison by Sex:**

A KDE plot was used to compare resting blood pressure between males and females. It highlights gender-based BP differences.

<img width="1200" height="300" alt="Resting Blood Pressure sex" src="https://github.com/user-attachments/assets/4c7ddfd4-9990-4d7e-a46e-ebc3bacbd386" />

**33. Continuous Variables Plot:**

Histograms were plotted for all continuous variables in the dataset. This helps understand the overall distribution of numerical features.

** 📌 Conclusion **

This project systematically explored the heart disease dataset through data cleaning, visualization, and analysis. The findings reveal patterns in age, gender, cholesterol, blood pressure, and other health indicators linked to heart disease. Each step provided clear insights, building practical data analysis skills while highlighting key medical risk factors. The study serves as a foundation for deeper exploration and future predictive modeling.
