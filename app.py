import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = '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'

conversations = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('main.html')
    if request.form['question']:
        question = 'Yo: '+ request.form['question']

        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt= question,
            temperature=0.5,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6
        )

        answer = 'AI: ' + response.choices[0].text.strip()

        conversations.append(question)
        conversations.append(answer)

        return render_template('main.html', chat = conversations)

if __name__ == '__main__':
    app.run(debug=True, port=4000)