# CSEC 491 Project Guide

### Repository Layout

- **code**: a folder for any scripts written regarding NLP
- **data**: a folder for data files and any scripts written for data collection/cleaning
- **references**: a folder for any references used in the writeups or coding process
- **writeups**: a folder for any written materials such as the proposal and final report

### Log File

**2/9/24**: I sucessfully scraped courses using the GraphQL endpoint with a python script. I set it up so that it reads the cookie signature from another file so that a new signature can be easily copy pasted when the other one expires. I then converted the raw json data into a CSV. Then, I wrote an RMarkdown document where I cleaned the raw CSV and analyzed the data a bit. The important part of this R analysis was that I discovered two unique identifiers for the courses: course id and course number. These will play an important role for the next step: scraping the reviews. They will allow me to automate the process of collecting and then merging the data with its corresponding class.

**2/10/24** This was a successful session. I wrote a python script that scraped the reviews from CourseTable using the course ids that
I identified earlier. I was able to make the script dynamic so that it reads in a list of course ids. I can also change the question code
(which determines what question the responses are for) and a few other parameters at the top of the file to change what is pulled. With just
a couple of tweaks, I was able to pull the skills responses and strengths/weaknesses responses. Each of these categories had 4000+ replies
which is certainly plenty to start our analysis with. My next step will be to read just the review responses into R to do some basic analysis
and then follow that up with some python sentiment analysis. I currently have each response stored on its own row with the corresponding course id. For example, a course with a 100 replies has 100 rows that belong to it.

**2/12/24**: I didn't quite complete everything I wanted to. On the bright side, I identified three popular preexisting sentiment analysis models that I will test before moving to models trained from scratch. I was able to implement one of them (VADER) and took a brief look at the results. It was fairly simple to code and actually works surprisingly well. I started working on the roBERTa model which is more complex but should yield better results. I didn't finish it yet and will do so in the next session. There is another popular library called TextBlob that I also want to try.
