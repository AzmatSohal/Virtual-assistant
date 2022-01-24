# Virtual-assistant
                                      FEATURES OF VIRTUAL ASSISTANT

1.	Queries from the web:

Making queries is an essential part of one’s life, and nothing changes even for a developer working on Linux. We have addressed the essential part of a netizen’s life by enabling our voice assistant to search the web. Here we have used Node JS and Selenium framework for extracting the result from the web as well as displaying it to the user. Jarvis supports a plethora of search engines like Google, Bing and Yahoo and displays the result by scraping the searched queries.
In order to make queries from different search engines, the given format should be adopted:
<search engine name> <query>

Jarvis supports Google, Bing and Yahoo, which should precede the desired query. 
2.	Accessing youtube videos

Videos have remained as a main source of entertainment, one of the most prioritized tasks of virtual assistants. They are equally important for entertainment as well as educational purposes as most teaching and research activities in present times are done through Youtube. This helps in making the learning process more practical and out of the four walls of the classroom.
Jarvis implements the feature through a subprocess module which is handled by the main Golang service. This service initiates the subprocess for Node JS which serves the Selenium WebDriver, and scraps the searched YouTube query.
In order to access videos from youtube format is:

youtube <video you want to search for>

 
3.	Get weather for a location

Getting live weather conditions about a place remains an important task of virtual assistants. It helps the user charter the course of their action. Jarvis addresses this issue with the help of Python.
In order to access the live weather condition format is:

Weather <city> <state/country>

 
4.	Retrieve images

Users could get images directly through the Jarvis interface. This implementation is done using the Selenium WebDriver. The images are derived as iframes from the entire web code received from Google images. These are formatted according to use and displayed in a compact manner in the Jarvis interface.
In order to retrieve image format is:

Image <image you want to search>

 
5.	Dictionary meaning

One of the usages of the web is to find word meaning and its usage in our day to day life. Instead of going through the bulky books, our users can simply search for it using the voice assistant and get the meaning within a fraction of seconds.
For retrieving the meaning of a word format is,

meaning <word>



6.	Medicine Details

One of the important issue Jarvis addresses is of healthcare, and medicine in general. The user can query either the medicine or the symptoms. The former lets you know the complete details of the medicine, like indications, contradictions, trade or brand names, dosage, the process of consumption, warning and precautions, storage conditions, etc. On the other hand, the symptom feature lets
 
you query about the symptoms while Jarvis lists various diseases one is likely to be affected along with their medicine. This is helpful for people who are quite busy with their life and find trouble visiting the doctor immediately, thus relying on the web to find the best result for short term cause.
Here we use Node JS framework along with Selenium to scrap the required data from the web and display it to the user. We have a huge database of various medicines and symptoms which helps Jarvis respond to the queries of the user at ease. The syntax to be used for querying the necessary are:
In order to get details about medicine format is,

Medicine <medicine name>

In order to re-track the causes of symptoms format is,

Symptoms <disease/ailment>

 
 

7.	Set Reminders

One of the main features of a voice assistant is to set a reminder for the user accordingly. Jarvis is no different when it comes to this. The user can set reminders to be notified about a task at a particular time. This will help users, especially developers to schedule their time and resources easily. All the user have to do is to input Set reminder to the assistant. A form will be displayed. Fill the form with the required details and click on set reminder button.
 
 

8.	Sending Emails

Integrating mailing features to Jarvis eases the job of mailing, which otherwise would have to be done by opening the concerned email address. With Jarvis, you do not need to go for another tab to do one of the major task of your day to day affairs. The user can send emails to the desired receiver. He should input Send mail, after which a form will be displayed. Fill the form with the required details and click on the send mail button.
