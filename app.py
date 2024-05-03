from flask import Flask, request, jsonify  
import requests 

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.form
    name = data['name']
    # Perform validation or processing of user input
    # For simplicity, we'll just print the user's name
    print('User input:', name)
    # Call ChatGPT API using requests (example)
    headers = {
        'Authorization': ,
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': 'Generate a response based on user input',
        'max_tokens': 150,
        'temperature': 0.7,
    }
    try:
        response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
        response_data = response.json()

        # Handle API response
        print('ChatGPT API response:', response_data)

        # Return confirmation or processed data as JSON response
        return jsonify({'message': 'Data received and processed successfully!'})

    except Exception as e:
        print('Error calling ChatGPT API:', str(e))
        return jsonify({'error': 'Error processing data.'}), 500

if __name__ == '__main__':
    app.run(debug=True)

