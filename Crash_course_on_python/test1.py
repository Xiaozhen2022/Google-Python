#字符串翻转是否相等判断
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for s in input_string:
		if s != ' ':
			new_string = new_string+s
			
	reverse_string = new_string[::-1]
	new_string = new_string.upper()
	reverse_string = reverse_string.upper()
	# Compare the strings
	if reverse_string == new_string:
		return True
	return False

#print(is_palindrome("Never Odd or Even")) # Should be True
#print(is_palindrome("abc")) # Should be False
#print(is_palindrome("kayak")) # Should be True

#字符串的format应用
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {___} km".format(str(miles),str(round(km,1)))
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#替换字符串末尾某个子串
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rfind(old)
		new_sentence = sentence[:i]+new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"