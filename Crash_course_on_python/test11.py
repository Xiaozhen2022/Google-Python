# Write a function that extracts an IPv4 address from unittest import result
# from a string and verifies thai it is valid. 
# The function should be a valid IPv4 or an empty string if no valid exists.
#Example: "1.1.1.1 is a valid IPv4 address" result: 1.1.1.1  "1.1.1.255" result: 1.1.1.255 "1.1.1.226 is an invalid IPv4 address" result:""
import re

class IPv4Extractor():
    
    def __init__(self, input_str):
        self.target = input_str
    
    def extract(self):
        result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", self.target)
        print(result)
        if result:
            return result[0]
        else:
            return '""'

if __name__ == '__main__':
  ipv4 = IPv4Extractor("1.1.1.0 is 11.1.2.256 invalid IPv4 address")
  print("Result: " + ipv4.extract())