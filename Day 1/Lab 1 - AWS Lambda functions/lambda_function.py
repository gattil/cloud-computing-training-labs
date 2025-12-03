# Import json module (not used in this simple example, but often needed for Lambda functions)
import json

# This is the main function that AWS Lambda calls when your function is invoked
# AWS Lambda automatically passes two parameters:
# - event: Contains the input data (like a dictionary/JSON object)
# - context: Contains information about the Lambda execution environment
def lambda_handler(event, context):
    """
    DNA sequence analyzer for AWS Lambda
    
    This function counts nucleotides (A, C, G, T) in a DNA sequence.
    It demonstrates serverless computing where code runs without managing servers.
    """
    
    # Extract the DNA sequence from the event object
    # event.get('sequence', 'ACGT') means:
    # - Look for a key called 'sequence' in the event dictionary
    # - If found, use that value
    # - If not found, use 'ACGT' as the default value
    # This prevents crashes if the input is missing or malformed
    sequence = event.get('sequence', 'ACGT')

    # Analyze the DNA sequence
    # Count the total length and individual nucleotides
    result = {
        'sequence_length': len(sequence),  # Total number of characters
        'nucleotide_counts': {
            'A': sequence.count('A'),  # Count adenine nucleotides
            'C': sequence.count('C'),  # Count cytosine nucleotides
            'G': sequence.count('G'),  # Count guanine nucleotides
            'T': sequence.count('T')   # Count thymine nucleotides
        }
    }

    # Return the result in Lambda's expected format
    # Lambda functions should return a dictionary with:
    # - statusCode: HTTP status code (200 = success)
    # - body: The actual data/result
    return {
        'statusCode': 200,  # HTTP 200 means "OK" or "Success"
        'body': result      # Our analysis results
    }

###
# Example EVENT JSON Payload that triggers this function:
# {
#   "sequence": "ACGTACGT"
# }
#
# This would be passed as the 'event' parameter to lambda_handler()
# The function would then analyze "ACGTACGT" and return the nucleotide counts