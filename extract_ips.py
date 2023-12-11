import re
import sys

def extract_ip_addresses(input_file_path):
    # Define the regular expression pattern for matching IP addresses
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

    # Open the input file and read its content
    with open(input_file_path, 'r') as file:
        content = file.read()

    # Find all IP addresses in the content using the pattern
    ip_addresses = ip_pattern.findall(content)

    return ip_addresses

def save_ip_addresses(output_file_path, ip_addresses):
    # Open the output file and write IP addresses in order
    with open(output_file_path, 'w') as file:
        for ip in ip_addresses:
            file.write(ip + '\n')

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python extract_ips.py <input_file_path> <output_file_path>")
        sys.exit(1)

    # Get input and output file paths from command-line arguments
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    # Extract IP addresses from the input file
    ip_addresses = extract_ip_addresses(input_file_path)

    # Save the IP addresses to the output file
    save_ip_addresses(output_file_path, ip_addresses)

    print(f"IP addresses extracted and saved to {output_file_path}.")
