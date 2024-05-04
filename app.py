from flask import Flask, render_template, request, jsonify
import openai  

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    
    response = generate_response(name)
    
    return jsonify({'response': response})

def generate_response(name):
    prompt = f'Hi, I\'m Tenali. Nice to meet you, {name}!'
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )
    
    return response['choices'][0]['message']['content'].strip()

if __name__ == '__main__':
    app.run(debug=True)


