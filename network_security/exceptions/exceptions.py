import sys
import logging

# Get logger for this module
logger = logging.getLogger(__name__)


def error_message_detail(error, error_detail: sys):
    """
    Generate detailed error message with file name and line number
    
    Args:
        error: The exception object
        error_detail: sys module to extract traceback information
        
    Returns:
        str: Formatted error message with location details
    """
    # Extract traceback information
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the file name where error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Get the line number where error occurred
    line_number = exc_tb.tb_lineno
    
    # Format the error message
    error_message = (
        f"Error occurred in python script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"error message: [{str(error)}]"
    )
    
    return error_message


class CustomException(Exception):
    """
    Custom Exception class that captures detailed error information
    including file name, line number, and error message
    """
    
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize custom exception with detailed error information
        
        Args:
            error_message: Original error message
            error_detail: sys module for traceback extraction
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, 
            error_detail=error_detail
        )
    
    def __str__(self):
        """
        Return string representation of the exception
        
        Returns:
            str: Detailed error message
        """
        return self.error_message


# ============================================
# EXAMPLE USAGE - Different Scenarios
# ============================================

def divide_numbers(a, b):
    """Example function that might raise an exception"""
    try:
        result = a / b
        return result
    except Exception as e:
        logger.error("Error in divide_numbers function")
        raise CustomException(e, sys)


def read_file(file_path):
    """Example function for file operations"""
    try:
        with open(file_path, 'r') as f:
            data = f.read()
        return data
    except Exception as e:
        logger.error(f"Failed to read file: {file_path}")
        raise CustomException(e, sys)


def process_data(data_list):
    """Example function for data processing"""
    try:
        result = []
        for item in data_list:
            result.append(item * 2)
        return result
    except Exception as e:
        logger.error("Error during data processing")
        raise CustomException(e, sys)


# ============================================
# DEMONSTRATION
# ============================================

if __name__ == "__main__":
    # Configure logging to see the output
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("=" * 60)
    print("EXCEPTION HANDLING DEMONSTRATION")
    print("=" * 60)
    
    # Example 1: Division by zero
    print("\n1. Testing Division by Zero:")
    try:
        divide_numbers(10, 0)
    except CustomException as e:
        print(f"Caught CustomException:\n{e}\n")
    
    # Example 2: File not found
    print("2. Testing File Not Found:")
    try:
        read_file("non_existent_file.txt")
    except CustomException as e:
        print(f"Caught CustomException:\n{e}\n")
    
    # Example 3: Type error
    print("3. Testing Type Error:")
    try:
        process_data([1, 2, "invalid", 4])
    except CustomException as e:
        print(f"Caught CustomException:\n{e}\n")
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)
        