
# Introduction

Being an Anime nerd,I spend more time on anime sites than all other sites combined.while on these sites, 
I cant help but wonder why some animes that in my opinion are super lukewarm get scored so highly. Although there are numerous 
contingent factors that determine the likability of an anime , I,for the benefit of my own curiosity, am going to attempt to understand 
how some defined features may contribute to the score of an anime and eventually use that understanding to predict scores of other animes.

# Data Description:

Data scraped from myanimelist with alternate pages scraped so there is a more variety in data scores .The site has a comprehensive list of animes and details everthing from title,score ,genre to how many members each anime has and how many people favorited it,production house,release dates etc.
Given these features, I hope to understand its significance regarding the score and attept at predicting the score for animes 
in the test dataset.


## Abstract

The goal of this project was to use regression models to predict the score of animes on myanimelsit in order to help anime creators understand how to predict if an anime could be succesful given certain features and understand why my favorite anime is scored so poorly.:p

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


## Tools

Numpy and Pandas for data manipulation

Scikit-learn for modeling

Matplotlib and Seaborn for plotting

Tableau for visualizations






