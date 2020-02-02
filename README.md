# hackSC 2020: MedChat

## How to run

UI: open run Chat/Chat.xcworkspace
Backend: run fireBaseTest2.py

## Inspiration

We chose to tackle the equity vertical and found that there are many inequalities in the healthcare industry. Specifically, with the emergence of "e-health" as a result of "advances in communication and computer technologies have revolutionized the way health information is gathered, disseminated, and used by healthcare providers, patients, citizens, and mass media."

There is abundant medical information on the web, however, according to the National Institute of Health "few websites are designed to facilitate easy navigation, and most are designed for those with far above 8th grade reading level, the average reading level of US adults." As a result, a tool meant to act as an information equalizer for those in lower-socioeconomic and lower-educated groups has ended up further widening the equity gap.

Observing these facts, we set out to create an interface that is easy to navigate, informative, and accessible for those who are unable to currently take advantage of "e-health."  

quotes from: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2043145/

## What it does

MedChat is a simple mobile interface for everyone to easily access and understand medical information. The user asks medical questions through an imessage-like interface and is given answers through an NLP AI trained chatbot with access to a dataset of 1+ million Q&A answers from doctors.

## How we built it

The front end was built in swift using JSQMessagesViewController API and was connected to the back end through the firebase database which stores the messages so they can be received and sent. A python listener was used to detect updates to the database and deliver a response to the database which would be displayed on the front end. The back end comprised of ranking, searching, and intersection preprocessed data to deliver a coherent answer to the user. In particular, the back end received a query from the user, parsed it for keywords using the Google Natural Language API, matched it to the keywords in the data set which were preprocessed by the spacy natural language API for keywords, and returned the best match.

## Challenges we ran into

The biggest challenge was processing the data efficiently. The sheer volume of data we had require us to process over 1.6 million questions. Google's Natural Language API only allowed 600 calls per minute and 800,000 calls per day which did not allow us to parse every question, therefore we had to use spacy and process the data offline. Even then, building the offline map took almost 6 hours, and loading the data takes a few minutes. Learning the API's themselves was also an arduous task because of the sheer amount of documentation we had to sift through. Lastly, although our dataset does simulate more life-like questions and responses, it becomes hard to parse and understand the slang that exists in our dataset which does not allow us to make full use of the 1.6 million questions.

## Accomplishments that we're proud of

Something we are proud of is linking the UI to the backend through Firebase for the chatbot to work as well as utilizing the Google NLP to recognize the important keywords from user input.

## What we learned

We learned how to develop iOS apps in Swift, connect them to a firebase database, and listen to that firebase from python. We also learned how to use Google Cloud Natural Language API, spacy natural language API, and efficiently search and rank queries.

## MedChat in the future

In the future for this to be a tangible product we would need to improve the ranking algorithm and have access to a more complete dataset (quality/quantity).
