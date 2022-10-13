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
        #result = re.findall(r"(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])\.){3}([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-5][0-5]))", self.target)
       
        if result:
            return 'IP {} is valid'.format(result[0])
        else:
            return 'IP is invalid'

if __name__ == '__main__':
  ipv4 = IPv4Extractor("250.198.3.266 are invalid IPv4 address")
  print(ipv4.extract())