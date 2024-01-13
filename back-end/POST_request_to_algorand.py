from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GENERATE_TOKENS_ENDPOINT = 'http://localhost:4001//Create_NFT'

@app.route('/Get_metadata', methods=['POST'])
def Get_metadata():
    try:
        # Extracting parameters from the request
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        middle_name = request.form.get('middle_name')
        training_program = request.form.get('training_program')
        date_of_completion = request.form.get('date_of_completion')
        duration_of_training = request.form.get('duration_of_training')
        issuing_organization = request.form.get('issuing_organization')
        serial_no_of_certificate = request.form.get('serial_no_of_certificate')

        # Prepare the data to send to the Generate_Tokens endpoint
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'training_program': training_program,
            'date_of_completion': date_of_completion,
            'duration_of_training': duration_of_training,
            'issuing_organization': issuing_organization,
            'serial_no_of_certificate': serial_no_of_certificate
        }

        # Make a POST request to the Generate_Tokens endpoint
        response = requests.post(GENERATE_TOKENS_ENDPOINT, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({'error': 'Failed to generate tokens'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
