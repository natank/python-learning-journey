def fizzbuzz(number):
    """
    Return Fizz, Buzz, FizzBuzz, or the number based on divisibility rules.
    
    Args:
        number (int): The number to check
        
    Returns:
        str: "Fizz" if divisible by 3, "Buzz" if divisible by 5,
             "FizzBuzz" if divisible by both 3 and 5, otherwise the number as string
             
    Raises:
        ValueError: If number is not a positive integer
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    if number <= 0:
        raise ValueError("Input must be a positive integer")
    
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    
    return str(number)


def fizzbuzz_range(start=1, end=100):
    """
    Generate FizzBuzz sequence for a range of numbers.
    
    Args:
        start (int): Starting number (default: 1)
        end (int): Ending number (default: 100)
        
    Returns:
        list: List of FizzBuzz results for the range
        
    Raises:
        ValueError: If start or end are invalid, or if start > end
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end must be integers")
    
    if start <= 0 or end <= 0:
        raise ValueError("Start and end must be positive integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    results = []
    for num in range(start, end + 1):
        results.append(fizzbuzz(num))
    
    return results


def print_fizzbuzz(start=1, end=100):
    """
    Print FizzBuzz sequence for a range of numbers.
    
    Args:
        start (int): Starting number (default: 1)
        end (int): Ending number (default: 100)
    """
    results = fizzbuzz_range(start, end)
    
    for i, result in enumerate(results, start=start):
        print(f"{i}: {result}")


def main():
    """
    Main function to run the FizzBuzz program.
    """
    print("🎯 FizzBuzz Challenge")
    print("======================")
    print("Printing numbers from 1-100 with FizzBuzz rules:")
    print("- Divisible by 3: Fizz")
    print("- Divisible by 5: Buzz") 
    print("- Divisible by both 3 and 5: FizzBuzz")
    print("- Otherwise: the number")
    print()
    
    print_fizzbuzz()


if __name__ == "__main__":
    main()
