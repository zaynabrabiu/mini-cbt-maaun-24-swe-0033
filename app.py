from flask import Flask, render_template, request, redirect, url_for
from models import MiniCBT

app = Flask(__name__)

# Global quiz instance to manage the complete test session across routes
# Global quiz object to manage test state (simple for assignment)
quiz = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start', methods=['POST'])
def start():
    global quiz
    quiz = MiniCBT()
    return redirect(url_for('question'))

@app.route('/question')
def question():
    global quiz
    if quiz is None:
        return redirect(url_for('home'))
    
    q = quiz.load_next_question()
    if not q:
        return redirect(url_for('result'))
    
    return render_template('question.html', question=q)

@app.route('/submit', methods=['POST'])
def submit():
    global quiz
    if quiz is not None and 'answer' in request.form:
        quiz.submit_current_answer(request.form['answer'])
    return redirect(url_for('question'))

@app.route('/result')
def result():
    global quiz
    if not quiz:
        return redirect(url_for('home'))
    
    quiz.finish_test()
    result_data = quiz.get_result()
    return render_template('result.html', result=result_data)

if __name__ == '__main__':
    print("🚀 Mini CBT is running!")
    print("Open this link in your browser: http://127.0.0.1:5000")
    app.run(debug=True)
