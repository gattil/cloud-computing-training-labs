# Import Flask components for creating web services
from flask import Flask, request, jsonify

# Create a Flask application instance
# __name__ tells Flask where to find resources relative to this file
app = Flask(__name__)

# Define a route (URL endpoint) that accepts POST requests
# When someone sends a POST request to '/validate', this function runs
@app.route('/validate', methods=['POST'])
def validate():
    # Extract JSON data from the incoming HTTP request
    # This is similar to the 'event' object in AWS Lambda
    data = request.get_json()
    
    # Get the DNA sequence from the request data
    # If 'sequence' key doesn't exist, use 'ACGT' as default
    # This is the same logic as in Lab 1's Lambda function
    sequence = data.get('sequence', 'ACGT')

    # Analyze the DNA sequence - same logic as Lab 1
    # Count the total length and individual nucleotides
    result = {
        'sequence_length': len(sequence),
        'nucleotide_counts': {
            'A': sequence.count('A'),  # Count adenine
            'C': sequence.count('C'),  # Count cytosine
            'G': sequence.count('G'),  # Count guanine
            'T': sequence.count('T')   # Count thymine
        }
    }

    # Convert Python dictionary to JSON and return as HTTP response
    # This is similar to returning a value in Lambda, but formatted for web
    return jsonify(result)


# This block only runs when the script is executed directly (not imported)
# It starts the Flask development server for local testing
if __name__ == '__main__':
    # Start the web server
    # host='0.0.0.0' means accept connections from any IP address
    # port=8080 is the port number where the service will listen
    app.run(host='0.0.0.0', port=8080)