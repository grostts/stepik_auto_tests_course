expected_result = 11
actual_result = 11

def test_input_text(expected_result, actual_result):
    if expected_result != actual_result:
        print(f'expected {expected_result}, got {actual_result}')

test_input_text(expected_result, actual_result)