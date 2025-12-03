# Import the Lambda function we want to test
# This allows us to call lambda_handler() directly in our tests
from lambda_function import lambda_handler

# Test function 1: Test with a specific DNA sequence
# Function names starting with 'test_' are automatically discovered by pytest
def test_lambda_handler():
    """
    Test the Lambda function with a known DNA sequence.
    
    This test verifies that our function correctly counts nucleotides
    in the sequence 'ACGTACGT' (which has 2 of each nucleotide).
    """
    # Create a mock event object (simulates what AWS Lambda would send)
    # This is the same format as the event.json file
    event = {'sequence': 'ACGTACGT'}
    
    # Call our Lambda function directly (no AWS needed for testing)
    # Pass empty dict {} as context since we don't use it
    result = lambda_handler(event, {})
    
    # Assert statements check if our expectations are met
    # If any assert fails, the test fails and tells us what went wrong
    
    # Check that the function returned success status
    assert result['statusCode'] == 200
    
    # Check that the sequence length is calculated correctly
    # 'ACGTACGT' has 8 characters
    assert result['body']['sequence_length'] == 8
    
    # Check that each nucleotide is counted correctly
    # 'ACGTACGT' contains exactly 2 of each nucleotide (A, C, G, T)
    assert result['body']['nucleotide_counts']['A'] == 2
    assert result['body']['nucleotide_counts']['C'] == 2
    assert result['body']['nucleotide_counts']['G'] == 2
    assert result['body']['nucleotide_counts']['T'] == 2

# Test function 2: Test the default behavior
def test_default_sequence():
    """
    Test the Lambda function when no sequence is provided.
    
    This test verifies that our function uses the default sequence 'ACGT'
    when the input event doesn't contain a 'sequence' key.
    """
    # Create an empty event object (no 'sequence' key)
    # This tests our error handling and default value logic
    event = {}
    
    # Call the Lambda function with empty event
    result = lambda_handler(event, {})
    
    # Check that the function still works (doesn't crash)
    assert result['statusCode'] == 200
    
    # Check that it used the default sequence 'ACGT' (length = 4)
    assert result['body']['sequence_length'] == 4
    
    # Additional verification: check that default sequence 'ACGT' is used correctly
    # 'ACGT' should have 1 of each nucleotide
    assert result['body']['nucleotide_counts']['A'] == 1
    assert result['body']['nucleotide_counts']['C'] == 1
    assert result['body']['nucleotide_counts']['G'] == 1
    assert result['body']['nucleotide_counts']['T'] == 1
    
    # Note: We could also check the individual nucleotide counts for 'ACGT'
    # but this test focuses on verifying the default behavior works
