# CSEC 491 Project Guide

### Repository Layout

- **code**: a folder for any scripts written regarding NLP
    - `evaluations.Rmd`: a file for evaluation model performance
    - `roberta.py`: a file for running the pretrained RoBERTa model
    - `tblob.py`: a file for running the rule based TextBlob model
    - `vader.py`: a file for running the rule based VADER model
- **data**: a folder for data files and any scripts written for data collection/cleaning
    - `courses.Rmd`: a file for narrowing down which courses we will scrape reviews for and analyzing other relevant information
    - `label.py`: a file to assist me in the manual labeling process
    - `scrape_courses.py`: a file to scrape our set of courses and other necessary information
    - `scrape_reviews.py`: a file to scrape reviews for our courses
    - `scrape_skills.py`: a file to scrape the skills responses for our courses
    - `scrape_swi.py:` a file to scrape the strengths/weaknesses/improvements for our courses
- **references**: a folder for any references used in the writeups or coding process
- **writeups**: a folder for any written materials such as the proposal and final report

