### Log File

**2/9/24**: I sucessfully scraped courses using the GraphQL endpoint with a python script. I set it up so that it reads the cookie signature from another file so that a new signature can be easily copy pasted when the other one expires. I then converted the raw json data into a CSV. Then, I wrote an RMarkdown document where I cleaned the raw CSV and analyzed the data a bit. The important part of this R analysis was that I discovered two unique identifiers for the courses: course id and course number. These will play an important role for the next step: scraping the reviews. They will allow me to automate the process of collecting and then merging the data with its corresponding class.

**2/10/24** This was a successful session. I wrote a python script that scraped the reviews from CourseTable using the course ids that
I identified earlier. I was able to make the script dynamic so that it reads in a list of course ids. I can also change the question code
(which determines what question the responses are for) and a few other parameters at the top of the file to change what is pulled. With just
a couple of tweaks, I was able to pull the skills responses and strengths/weaknesses responses. Each of these categories had 4000+ replies
which is certainly plenty to start our analysis with. My next step will be to read just the review responses into R to do some basic analysis
and then follow that up with some python sentiment analysis. I currently have each response stored on its own row with the corresponding course id. For example, a course with a 100 replies has 100 rows that belong to it.

**2/12/24**: I didn't quite complete everything I wanted to. On the bright side, I identified three popular preexisting sentiment analysis models that I will test before moving to models trained from scratch. I was able to implement one of them (VADER) and took a brief look at the results. It was fairly simple to code and actually works surprisingly well. I started working on the roBERTa model which is more complex but should yield better results. I didn't finish it yet and will do so in the next session. There is another popular library called TextBlob that I also want to try.

**2/16/24**: I was able to complete the three pretrained models today. I created a random sample of 50 reviews in my script to get a sense of their performance. My takeaways are that TextBlob is fairly bad, VADER is fairly good, and RoBERTa is very good. I also added a file for links in the references folder to keep track of web sources without saving them as PDFs. The RoBERTa model was much better than the VADER and TextBlob models which is what I expected as it's much more advanced. There are many different models offered by HuggingFace, I might try some different ones that could be more applicable to this specific dataset. That script takes almost 10 minutes to go through all 4000+ reviews. My computer gets pretty hot while running it! The next step I want to take is to do some more in depth reading about these various
models and how they work. I want to take notes and outline this in my paper draft. After that, I'll dig into how to label my own dataset and
start labeling it.

**2/17/24**: Today I started labeling my own dataset. I wrote a script that makes the labeling process a lot easier and a lot more fun. It
allows me to label as many reviews as I want and then exit the program, picking back up where I left off the next time. It also lets me
know how many reviews I labeled in a session and how long I spent on that session. I labeled a few hundred reviews today. Currently, I'm
keeping the labels basic with just positive, negative, and neutral.

**2/18/24**: Today I just sat down and labeled a bunch of reviews! This is gonna take a while...

**2/19/24**: I labeled a bunch more reviews today :)

**2/20/24**: More labeling!

**2/21/24**: Labeling.

**2/23/24**: Labeling.

**2/24/24**: Labeling.

**2/25/24**: I finished labeling my dataset and started to assess the accuracy of the pretained models!

**2/26/24**: I finished assessing the accuracy of my pretrained models, created a guide to the file directory, and started
working on the write up. I also worked on some new models. I completed an SVM model and started Naive Bayes.
