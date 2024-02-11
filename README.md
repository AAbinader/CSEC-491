# CSEC 491 Project Guide

### Repository Layout

- **code**: a folder for any scripts written regarding NLP
- **data**: a folder for data files and any scripts written for data collection/cleaning
- **references**: a folder for any references used in the writeups or coding process
- **writeups**: a folder for any written materials such as the proposal and final report

### Log File

**2/9/24**: I sucessfully scraped courses using the GraphQL endpoint with a python script. I set it up so that it reads the cookie signature from another 
file so that a new signature can be easily copy pasted when the other one expires. I then converted the raw json data into a CSV. Then, I wrote an RMarkdown
document where I cleaned the raw CSV and analyzed the data a bit. The important part of this R analysis was that I discovered two unique identifiers for the
courses: course id and course number. These will play an important role for the next step: scraping the reviews. They will allow me to automate the process of
collecting and then merging the data with its corresponding class.
