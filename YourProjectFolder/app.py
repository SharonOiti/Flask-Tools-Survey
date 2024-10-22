from flask import Flask, render_template, request, redirect, session, flash, url_for
from survey import satisfaction_survey  # Import the satisfaction survey instance

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def start_survey():
    """Render the start page for the survey."""
    return render_template('start.html', survey=satisfaction_survey)

@app.route('/start_survey', methods=["POST"])
def start_survey_post():
    """Initialize the responses in the session."""
    session['responses'] = []  # Start with an empty list of responses
    return redirect(url_for('question', question_id=0))  # Redirect to the first question

@app.route('/questions/<int:question_id>')
def question(question_id):
    """Render the question page."""
    responses = session.get('responses', [])

    if question_id < len(satisfaction_survey.questions):
        if question_id == len(responses):  # User is on the correct question
            question = satisfaction_survey.questions[question_id]
            return render_template('question.html', question=question, question_id=question_id)
        else:
            flash("You can't skip questions! Please answer them in order.")
            return redirect(url_for('question', question_id=len(responses)))  # Redirect to the correct question
    else:
        flash("You've already completed the survey.")
        return redirect(url_for('thank_you'))  # Redirect to thank you page

@app.route('/thank_you')
def thank_you():
    """Render the thank you page."""
    return render_template('thank_you.html')

@app.route('/answer', methods=['POST'])
def answer():
    """Process the user's answer and redirect to the next question."""
    answer = request.form['answer']  # Get the selected answer from the form
    responses = session.get('responses', [])
    responses.append(answer)  # Add the answer to the list of responses
    session['responses'] = responses  # Update the session with the new list of responses

    # Check if there are more questions to answer
    if len(responses) < len(satisfaction_survey.questions):
        return redirect(url_for('question', question_id=len(responses)))  # Redirect to the next question
    else:
        return redirect(url_for('thank_you'))  # Redirect to the thank you page if done

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to any unused port if needed

