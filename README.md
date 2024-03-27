# CSEC 491 Project Guide

### Repository Layout

- **sentiment_analysis**: a folder for any scripts written regarding sentiment analysis
    - `evaluations.Rmd`: a file for evaluating model performance
    - `logit.py`: a file for the logit model
    - `neuralnet.py`: a file for the neural network model
    - `roberta.py`: a file for running the pretrained RoBERTa model
    - `tblob.py`: a file for running the rule based TextBlob model
    - `vader.py`: a file for running the rule based VADER model
    - `svm.py`: a file for the support vector machine (SVM) model
    - `random_forest.py`: a file for the random forest model
    - `reevaluations.Rmd`: a file for cleaning the evaluations CSV
- **keyword_extraction**: a folder for any scripts written regarding keyword extraction
- **data**: a folder for data files and any scripts written for data collection/cleaning
    - `courses.Rmd`: a file for narrowing down which courses we will scrape reviews for and analyzing other relevant information
    - `label.py`: a file to assist me in the manual labeling process
    - `relabel.py`: a file to assist me with the new manual labeling process
    - `scrape_courses.py`: a file to scrape our set of courses and other necessary information
    - `scrape_reviews.py`: a file to scrape reviews for our courses
    - `scrape_skills.py`: a file to scrape the skills responses for our courses
    - `scrape_swi.py:` a file to scrape the strengths/weaknesses/improvements for our courses
- **dashboard**: a folder for any scripts to implement the dashboard
- **references**: a folder for any references used in the writeups or coding process
- **writeups**: a folder for any written materials such as the proposal and final report

