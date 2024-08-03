import os

import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/another-page')
def another_page():
    return render_template('another_page.html')


@app.route('/find-others')
def find_others():
    mentors = [
        {
            'name':
            'Emily Rodriguez',
            'year':
            2012,
            'major':
            'Computer Science',
            'school':
            'Massachusetts Institute of Technology (MIT)',
            'description':
            'Emily overcame financial hardships to become a leading software engineer at a top tech company. She mentors young women in STEM and advocates for diversity in the tech industry.'
        },
        {
            'name':
            'Michael Nguyen',
            'year':
            2015,
            'major':
            'Mechanical Engineering',
            'school':
            'Stanford University',
            'description':
            'Michael, a first-generation college student, now works at a major aerospace firm. He is passionate about developing sustainable energy solutions and volunteers with engineering outreach programs.'
        },
        # Add more mentor entries as needed
    ]
    return render_template('findothers.html', mentors=mentors)


@app.route('/user-profile')
def user_profile():
    return render_template('userprofile.html')


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    user_input = ""
    bot_response = ""

    if request.method == 'POST':
        user_input = request.form.get("message")

        try:
            # Create a chat completion request
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content":""} #user_input dont work idk
                    
                ],
                max_tokens=60
            )
            bot_response = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            # Handle other exceptions
            bot_response = f"An error occurred: {str(e)}"

    return render_template("chatbot.html",
                           user_input=user_input,
                           bot_response=bot_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
