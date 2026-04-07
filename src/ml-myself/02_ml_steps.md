# Machine Learning

https://www.geeksforgeeks.org/machine-learning/machine-learning/

- **Problem Definition**: The first step is identifying and clearly defining the business problem.
- **Data Collection**: Collection of datasets that can be used as raw data to train model. The quality and
  variety of data directly affect the model’s performance.
- **Data Cleaning and Preprocessing**: Standardize formats, scale values and encode categorical variables for
  consistency
- **Exploratory Data Analysis (EDA)**: understand the dataset's structure. Trends and insights.
- **Feature Engineering and Selection**: Create new features or transform existing ones to capture better patterns
  and relationships.
- **Model Selection**: We need to find model that aligns with our defined problem, nature of the data, complexity of
  problem and the desired outcomes. Experiment with different models to find the best fit for the problem.
- **Model Training**: Train the model iteratively, adjusting parameters to minimize errors and enhance accuracy.
- **Model Evaluation and Tuning**: If the model fails to achieve desired performance levels we may need to tune
  model again and adjust its hyperparameters to enhance predictive accuracy. Use metrics like accuracy, precision,
  recall and F1 score to evaluate model performance.
- **Model Deployment**: Now model is ready for deployment for real-world application.Provide APIs or pipelines
  for production use.
- **Model Monitoring and Maintenance**

## Data Collection

## Data Cleaning and Preprocessing

Data cleaning involves identifying and removing any missing, duplicate or irrelevant data.

## Feature Extraction

Feature extraction involves creating new features by combining or transforming the original features.

Common feature extraction methods are:

- Principal Component Analysis (PCA)
- Missing Value Ratio: Variables with missing data beyond a set threshold are removed
- Backward Feature Elimination: Starts with all features and removes the least significant ones in each iteration.
- Forward Feature Selection: It begins with one feature, adds others incrementally and keeps those improving model
  performance.
- Random forest: uses decision trees to evaluate feature importance, automatically selecting the most relevant features
  without the need for manual coding
- Factor Analysis: Groups variables by correlation and keeps the most relevant ones for further analysis
- Independent Component Analysis (ICA): Identifies statistically independent components, ideal for applications like
  ‘blind source separation’ where traditional correlation-based methods fall short.

**Statistical methods** are used in feature extraction to summarize and explain patterns of data.

**Dimensionality reduction** reduces the number of features without losing important information.
It converts high-dimensional data into a lower-dimensional space while preserving important details.

...

## Model Evaluation

- **Precision** is the ratio between the True Positives and all the Positives. It shows how many of the “yes”
  predictions made by the model were actually correct.
