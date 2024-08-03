## Inspiration
We attended a workshop on mentorship, where we learned that individuals grow exponentially when they have the guidance of another. We had heard that “having someone to talk to lightens adversities and serves as great help…. You matter! Communication and relationships are power!”. This inspired us to make something that would help connect struggling students and help guide them.

## What it does
Allows first-generation low-income students to find current college students or professors with similar experiences and connect as mentors during the college application process or in general. This would relieve the pressure that many first-generation students have as they struggle to find proper guidance

## How we built it
We originally built it using Replit as an easy tool that allowed us to collaborate. We first started with the base site and then migrated to other pages with HTML. The backend functions of our website are built in Python and some of the styles are in css.

## Challenges we ran into
A challenge we faced was using Openai for our chatbot and its functions. Our method: ChatCompletion was stated to be in a newer version, however, no installation version of Openai would work. Later, we figured out that the technique was deprecated and would no longer work. Additionally, we had to use mock data as it was challenging to find API/real-time individuals. 

## Accomplishments that we're proud of
Considering that this is our first hackathon, we would say that the UI and features like "find others" are a significant accomplishment for us.

## What we learned
For many of us, we learned how to use HTML and Python with very little prior experience. We also learned about the trial and error involved in designing a website. Such as tweaking both the CSS and HTML files to work well with and complement each other.

## What's next for AlumniLink
We would personalize our chatbots to help students specifically and allow them to take information from other sites to give back accurate feedback. We would also appropriate the user profile function and add other functions like a dark mode or some statistical charts representing different information.

## Setup Instructions
Create a GitHub Codespace, and then within the terminal, individually enter:
pip install flask
pip install openai
pip install python-dopenv

Next, enter "python main.py" in the terminal and click "open in browser" to access the website.

## Usage Instructions
To create a profile, click "Get Started", and then "User Profile." Then, enter in specific data and submit to create the profile.
To find other profiles, mainly professors or college students, click "Get Started", and then "Find Others." Then, toggle through each individual while viewing their descriptions, with provided contact information.
To interact with the AI chatbot, click "Get Started", and then "Need Help? Ask Bibble?" to be directed to a specific webpage. Then, ask questions (Unfortunately, AI chatbox currently does not work due to a limited quota). 
