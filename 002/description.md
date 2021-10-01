# Predicting the rank od animes in myanimelist.net
Yonga lhamo

## Abstract

The goal of this project was to use regression models to predict the rank of animes on myanimelsit in order to help anime creators understand how to predict if an anime could be succesful given certain features

## Design

This project goes through various itirations of various regression models and utilises feature engeneering,feature selection and regularization accordingly with the given output from the models.

## Data

The dataset contains 1000 rows  with 14 features for each from myanimelist.net scraped using beautiful soup. It contains 8 categorical features and 6 numerical features.

## Algorithms

Feature Engineering
grouping together categorial values that have too many unique values and fall below a value count threshhold.
Converting categorical features to binary dummy variables
binning features
tranforming features to polynomials

Feature Selection 
 kbest,50th percentile,lasso,randomforest,manually selecting features based on feature relation to target.


## Models

Logistic regression,ridge,Lasso, random forest classifiers

## Model Evaluation and Selection

The final model included 25 features ,filtered by random forest, and included a standardized dataset transformed into polynomial 2nd degree with Lasso regression as the classifier. Mean absolute error and R-squared metrics were used to evaluate the models.


Accuracy: 0.59
MAE:523.50


## Tools

Numpy and Pandas for data manipulation

Scikit-learn for modeling

Matplotlib and Seaborn for plotting

Tableau for visualizations

## Communication

presentation,written explanation,code with comments.
