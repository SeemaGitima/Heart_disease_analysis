# 🧰 Step 1: Import important libraries
import pandas as pd    # To load and work with data
import seaborn as sns  # For beautiful graphs
import matplotlib.pyplot as plt  # For basic graphs

# 🧰 Step 2: Load the datset
df = pd.read_csv(r'd:/New folder/Heart Disease Dataset/heart.csv')


# Explore the dataset

# Show first 5 rows of dataset
df.head()
print(df.head())

# Print last 5 rows of dataset
print(df.tail())

# Find the shape of the datset ( number of rows and columns)
print(df.shape)

# Print number of rows 
print("Number of rows :", df.shape[0])

# Print number of Columns
print("Number of columns :",df.shape[1])

# See Columns name 
print(df.columns)
print()
# Get information about our Dataset like "Total number of Columns" , "Total number of rows", "datatypes of each columns" , "memory requirement" and missing values
print(df.info())
print()
# Print/Check Null Values in the Dataset
print(df.isnull().sum())
print()
# Check duplicate data
duplicate_data =df.duplicated().any() # this will is their any duplicate data is presnt in the dataset
print("Duplicate Data :",duplicate_data) # if output is True, there's some duplicates
print()
# Count duplicate rows
print("Count of duplicate rows :",df.duplicated().sum())
print()
# print duplicate data
print(df.duplicated())
print()
# Remove duplicate data
df =df.drop_duplicates()
print(df.shape)
print()
# Quick statistics for each column. Gives statistics like mean, min, max — useful for spotting outliers.
print(df.describe())
print()

# How Many People Have Heart Disease, And How Many Don't Have Heart Disease In This Dataset?

counts = df['target'].value_counts()
print(counts)
#Plots the counts
sns.countplot(x='target', data=df, palette="coolwarm")
plt.xlabel("Target(0 = No Heart Disease, 1 = Heart Disease)")
plt.ylabel("Counts")
plt.title("Heart Disease vs No Heart Disease Count")
plt.show()
print()
# Find Count of Male & Female in this Dataset
counts_gender = df['sex'].value_counts()
print(counts_gender)
# use countplot to visualize it
sns.countplot(x = df['sex'] ,palette="coolwarm")
# let me change this x labeLS. [0,1] is replaced by ['Female','Male']
plt.xticks([0,1],["Female", "Male"])
plt.title('Gender Count')
plt.show()
print()

# What is the age distribution of patients?

sns.histplot(df['age'],bins=20, palette ='coolwarm', edgecolor ='black')
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# Find Gender Distribution According to The Target Variable
sns.countplot(x='sex', hue='target', data=df, palette="coolwarm")
plt.xticks([0,1],["Female","Male"])
plt.title("Gender Distribution According to Heart Disease")
plt.legend(labels =['No Heart Disease', 'Heart Disease'])
plt.show()

# Which age group has the highest proportion of heart disease cases?
# Create a age groups column
bins=[20, 30, 40, 50, 60, 70, 80]
labels=['20-29', '30-39', '40-49', '50-59','60-69','70-79']
df['age_groups'] = pd.cut(df['age'], bins = bins, labels = labels)
# visualization
sns.countplot(x='age_groups', hue='target', data=df, palette="coolwarm")
plt.xlabel("Age Groups")
plt.title("Age Group Distribution According to Heart Disease")
plt.legend(labels =['No Heart Disease', 'Heart Disease'])
plt.show()


# How does cholesterol level differ in patients with and without heart disease?

bins =[0, 199, 299, 399, 499, df['chol'].max()]
labels = ['0-199', '200-299', '300-399', '400-500', '500+']
df['Cholesterol_groups'] = pd.cut(df['chol'], bins = bins, labels = labels, include_lowest=True)
sns.countplot(x='Cholesterol_groups', hue='target', data=df ,palette="coolwarm")
plt.xlabel("Cholesterol Groups (mg/dL)")
plt.title("Cholesterol Levels vs Heart Disease")
plt.legend(labels=['No Heart Disease', 'Heart Disease'])
plt.show()

# How does resting blood pressure vary between the two groups?

bins = [0, 90, 120, 140, 160, df['trestbps'].max()]
labels = ['Low', 'Normal', 'Elevated', 'High Stage 1', 'High Stage 2+']
df['Resting_BP'] = pd.cut(df['trestbps'], bins = bins, labels = labels,include_lowest=True)
sns.countplot(x='Resting_BP', hue='target', data=df, palette="coolwarm")
plt.xlabel("Resting Blood Pressure (mmHg)")
plt.title("Resting Blood Pressure vs Heart Disease")
plt.legend(labels=['No Heart Disease', 'Heart Disease'])
plt.show()


# Does fasting blood sugar level (>120 mg/dl) relate to higher heart disease risk?

sns.countplot(x='fbs', hue='target', data=df, palette="coolwarm")
plt.title("Fasting Blood Sugar (>120 mg/dl) vs Heart Disease")
plt.xlabel("Fasting Blood Sugar (0 = <=120, 1 = >120)")
plt.ylabel("Count")
plt.legend(labels=['No Heart Disease', 'Heart Disease'])
plt.show()



#### Symptom/Condition Analysis (Body signs & symptoms)
# How does chest pain frequency differ between the two groups('Heart Disease' and 'No Heart Disease')?
#  Does chest pain type matter for heart disease?
sns.countplot(x='cp', hue= 'target', data=df, palette="coolwarm")
plt.title("Chest Pain Type vs Heart Disease")
plt.xlabel("Chest Pain Type (0=Typical Angina, 1=Atypical, 2=Non-anginal, 3=Asymptomatic)")
plt.ylabel("Count")
plt.legend(labels=['No Heart Disease', 'Heart Disease'])
plt.show()


# Does a higher maximum heart rate reduce or increase heart disease risk?

plt.figure(figsize=(8,6))
sns.boxplot(x='target', y='thalach', data=df, palette="coolwarm")
plt.title("Maximum Heart Rate vs Heart Disease")
plt.xlabel("Target (0 = No Heart Disease, 1 = Heart Disease)")
plt.ylabel("Maximum Heart Rate (thalach)")
plt.show()

# If exercise causes chest pain, is heart disease more likely?
sns.countplot(x='exang', hue='target', data= df, palette="coolwarm")
plt.title("Exercise-Induced Angina vs Heart Disease")
plt.xlabel("Exercise-Induced Angina (0 = No, 1 = Yes)")
plt.ylabel("Number of Patients")
plt.legend(title="Heart Disease (0=No, 1=Yes)")
plt.show()

# Does the “oldpeak” test result (ST depression) relate to heart disease?
sns.histplot(data=df, x='oldpeak', hue='target', bins=20, kde=True, element= 'step')
plt.title("Distribution of ST Depression (Oldpeak) by Heart Disease")
plt.xlabel("ST Depression (Oldpeak)")
plt.ylabel("Number of Patients")
plt.show()


# Categorical vs Target

# Q11. Does resting ECG result differ between people with and without heart disease?
sns.countplot(x='restecg', hue='target', data= df, palette="coolwarm")
plt.title("Resting ECG Result vs Heart Disease")
plt.xlabel("Resting ECG Result (0=Normal, 1=ST-T Abnormality, 2=LVH)")
plt.ylabel("Number of Patients")
plt.legend(title="Heart Disease", labels=["No", "Yes"])
plt.show()

# Q12. How does slope of peak exercise ST segment relate to heart disease?
# 🔹 Chart idea: Countplot or Grouped Bar Plot.
# 👉 Helps in analyzing categorical medical test results with target.
sns.countplot(x='slope', hue='target', data= df, palette="coolwarm")
plt.title("Slope of Peak Exercise ST Segment vs Heart Disease")
plt.xlabel("Slope (0=Upsloping, 1=Flat, 2=Downsloping)")
plt.ylabel("Count")
plt.legend(labels=['No Heart Disease', 'Heart Disease'])
plt.show()

# Q13. Is there any connection between thalassemia (thal) types and heart disease?
# 🔹 Chart idea: Countplot with % on bars.
# 👉 New learning: proportional comparison across categories.

# Calculate percentages
counts = df.groupby(['thal', 'target']).size().reset_index(name='count')
total = counts.groupby('thal')['count'].transform('sum')
counts['percentage'] = counts['count'] / total * 100

sns.barplot(x='thal', y='percentage', hue='target', data=counts, palette="coolwarm")
plt.title("Thalassemia Types vs Heart Disease (%)")
plt.xlabel("Thalassemia (1=Fixed Defect, 2=Normal, 3=Reversible Defect)")
plt.ylabel("Percentage")
plt.legend(labels=['No Heart Disease', 'Heart Disease'])
plt.show()

# Multivariate Analysis
# Does the combination of age and cholesterol increase risk?

sns.scatterplot(x='age', y='chol', hue= 'target', data= df , palette="coolwarm")
plt.title("Age vs Cholesterol by Heart Disease")
plt.xlabel("Age")
plt.ylabel("Cholesterol (mg/dl)")
plt.legend(labels=['No Heart Disease', 'Heart Disease'])
plt.show()

# How do sex and chest pain type together influence heart disease?
g = sns.catplot(x="cp", hue="target", palette="coolwarm", col="sex", data=df, kind="count")
g.set_axis_labels("Chest Pain Type (0=Typical,1=Atypical,2=Non-anginal,3=Asymptomatic)", "Count")
g.set_titles("Sex = {col_name}")
plt.show()


# Statistical/Distribution Checks
# Is the dataset balanced or imbalanced for the target variable?
sns.countplot(x='target' , data =df, palette="coolwarm")
plt.title("Target Variable Distribution (Balanced vs Imbalanced)")
plt.xlabel("Target (0=No Disease, 1=Disease)")
plt.ylabel("Count")
plt.show()

# Which features are most strongly correlated with heart disease?

# Drop extra non-numeric/derived columns if needed
correlation_matrix = df.drop(columns=['age_groups','Resting_BP','Cholesterol_groups']).corr()

# Get only correlations with target
cor_target = correlation_matrix['target'].drop('target').sort_values(key=abs, ascending=False)

# Plot as barplot
plt.figure(figsize=(8,5))
sns.barplot(x=cor_target.values, y=cor_target.index, palette="coolwarm")
plt.title("Correlation of Features with Heart Disease (Target)")
plt.xlabel("Correlation Strength")
plt.ylabel("Features")
plt.show()

# Show Distribution of Serum cholesterol

# we are using histogram to check distribution of the column

df['chol'].hist(color='skyblue', edgecolor='black') 
plt.title("Distribution of Serum Cholesterol")
plt.xlabel("Serum Cholesterol (mg/dl)")
plt.ylabel("Frequency")
plt.legend(["Cholesterol"])  # legend label
plt.show()


# Resting Blood Pressure Comparison by Sex

g = sns.FacetGrid(df, hue="sex", aspect=4)
g.map(sns.kdeplot, 'trestbps', shade=True)
plt.title("Resting Blood Pressure Distribution by Sex")
plt.legend(labels=['Male','Female'])
plt.show()

# Plot Continuous Variables 
# lets create to empty list.

categ_val=[]
cont_val=[]

for column in df.columns:
    if df[column].nunique() <=10:
        categ_val.append(column)
    else:
        cont_val.append(column) # Contiuous variables

print(categ_val)
print(cont_val)  # Contiuous variables

df.hist(cont_val, figsize=(15,8))
plt.tight_layout()
plt.show()
