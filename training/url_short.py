'''
url = []

print("Welcome to the URL shortener")
input("Enter the URL you want to shorten: ")

url.append(input)
print(url)
url = []  # List to store the URLs

print("Welcome to the URL shortener")
user_input = input("Enter the URL you want to shorten: ")  # Read input as a string

url.append(user_input)  # Append the string to the list
print(url)  # Print the list with the stored URL

'''
import random
import string

# Dictionary to store URL mappings
url_storage = {}

def generate_short_code(length=6):
    """
    Generates a random short code of a given length.

    Args:
        length (int): The length of the short code to generate. Defaults to 6.

    Returns:
        str: A randomly generated short code.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(long_url):
    """Shortens a given URL and stores it in the mapping.

    Args:
        long_urlurl_mapping = {} (str): The URL to shorten.

    Returns:
        str: The shortened URL.
    """
    # Generate a short code
    short_code = generate_short_code()

    # Store the mapping of short code to long URL
    url_storage[short_code] = long_url

    # Return the shortened URL
    return f"http://short.ly/{short_code}"

def expand_url(short_code):
    """
    Retrieves the original URL from the short code.

    Args:
        short_code (str): The short code associated with the original URL.

    Returns:
        str: The original URL if found, otherwise a not found message.
    """
    # Attempt to get the original URL from the url_mapping dictionary
    # using the provided short code. Return "URL not found" if the short code
    # is not present in the dictionary.
    return url_storage.get(short_code, "URL not found")

# Example usage
if __name__ == "__main__":
    long_url = input("Enter the URL to shorten: ")
    short_url = shorten_url(long_url)
    print(f"Shortened URL: {short_url}")
    
    # Testing expansion
    short_code = short_url.split("/")[-1]
    print(f"Expanded URL: {expand_url(short_code)}")


