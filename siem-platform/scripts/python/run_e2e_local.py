import os
import subprocess

def run_e2e_tests():
    # Define the command to run end-to-end tests
    command = ["pytest", "tests/e2e/test_alert_flow.py"]

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output and error (if any)
    print("Output:\n", result.stdout)
    print("Error:\n", result.stderr)

if __name__ == "__main__":
    run_e2e_tests()