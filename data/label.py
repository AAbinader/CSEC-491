import csv
import os
import time

"""This script is a fun, more interactive way for me to label the reviews. It allows me to see the full review which is very
difficult in XLS/Numbers/R and I can continue where I left off. It also keeps track of how many reviews I label in a given
session and how long I spent on that session. Overall, just more efficient and more fun for this monotonous labor!"""

def label_reviews(csv_file_path):

    try:
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if 'sentiment' not in rows[0]:
            rows[0].append('sentiment')

        start_time = time.time()
        first_review_bool = False
        first_review = 0

        for i in range(1, len(rows)):

            if len(rows[i]) >= 3:
                continue
            else:

                if first_review_bool == False:
                    first_review_bool = True
                    first_review = i

                os.system('clear')
                print("Review:", rows[i][1])
                print()
                sentiment = input("Enter sentiment (pos, neg, neu): ").strip().lower()

                if sentiment in ['q', 'quit']:

                    end_time = time.time()
                    duration = end_time - start_time
                    hours, remainder = divmod(duration, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    minutes = round(minutes)
                    seconds = round(seconds)
                    reviews_completed = i - first_review

                    os.system('clear')
                    print("Finished with Review #" + str(i))
                    print("Completed " + str(reviews_completed) + " Reviews")
                    print("Time Spent: " + str(minutes) + " min " + str(seconds) + " sec")
                    break
                while sentiment not in ['pos', 'neg', 'neu']:
                    sentiment = input("Invalid. Try again: ").strip().lower()
                
                rows[i].append(sentiment)

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    except Exception as e:
        print("An error occurred:", e)

label_reviews('reviews_labeled.csv')
