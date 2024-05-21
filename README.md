# ai-project
This is a repository for our AI project for Spring 2024. The authors are Jackson, Hunter, Aaron, and Alex (jcm4bsq, hhn9vn, ata8w, and aga8fs). 

## What is this project for? 

This is a final project for our Artificial Intelligence (CS 4710) class at UVA. The theme for the projects this year is "AI for Social Good". We chose to tackle the problem of identifying "hate speech" in comments that are posted to online forums and social medias (mainly, Reddit). The inspiration for this project came from wanting to dive into Natural Language Processing and our interests in Reddit's moderation system. 

## Goals

To develop a system that uses machine learning to identify whether a post contains hate speech or not. 

## Methods

At this stage in the project, we are analyzing the outcomes from a few different machine learning/artificial intelligence methods. Specifically, we are implementing the following models: convolutional neural networks, decision trees, logistical regression, markov models, and naive bayes models.

Something to quickly recognize here is our input and output formatting. First, we are not generating anything, we simply want to classify. Second, our input is text and our output is a simple classification. Further this is the simplest form of classification - binary classification. This means that we are essentially classes into two categories: a simple yes or no for the sake of this project. 

For the sake of a neural network implementation, our output neurons layer would be of size two. For linear regression, we would just be attempting to find a line to separate the text into different classifications. Etc. It is helpful to think about these for the models.

## Dataset

We are using a few datasets. For training: 
1. [Ethos Dataset](https://www.kaggle.com/datasets/konradb/ethos-hate-speech-dataset) as our main training dataset.
2. [WallStreeBets](https://www.kaggle.com/datasets/curiel/rwallstreetbets-posts-and-comments) As potential test data.
3. [Malignant Comment Classification](https://www.kaggle.com/datasets/surekharamireddy/malignant-comment-classification) as more training data and test data. 

The Ethos and Malignant datasets each label their entries into different buckets. The Ethos dataset directly labels as hate speech whereas the Malignant dataset labels as "malignant", which is more broad than hate speech as it can encompass cyber-bullying and other "less-intense" forms of cyber-aggression. Additionally, each dataset is sourced from different areas of the internet (ie, the comments from one dataset come from a set of individuals that is likely quite different from another group of individuals). Therefore, when using these datasets, it is important to keep that in mind. 

### Results so far