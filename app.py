from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for survey responses (this could be replaced by a real database)
responses = []

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    feedback = request.form['feedback']
    
    # Store the feedback in the list (replace with database logic if needed)
    responses.append({'name': name, 'feedback': feedback})
    
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/responses')
def view_responses():
    return render_template('responses.html', responses=responses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
