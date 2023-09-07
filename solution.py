import re

#Task 1

pattern = r'\d+$'
input_string = str(input("Enter string: "))
if re.search(pattern, input_string):
    print("The string ends with a number.")
else:
    print("The string does not end with a number.")

#Task 2
pattern = r'\b\d{1,3}\b'
sample_text = "Exercises number 1, 12, 13, and 345 are important"
result = re.findall(pattern, sample_text)
print("Numbers found in the string:")
for i in result:
    print(i)

#Task 3
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
for word in searched_words:
    result = re.findall(word, sample_text)
    if result:
        print(f"Word '{word}' found in the sample text.")
    else:
        print(f"Word '{word}' not found in the sample text")

#Task 4 Still using task 3
for word in searched_words:
    pattern = re.compile(word)
    for match in pattern.finditer(sample_text):
        start = match.start()
        end = match.end()
        print(f"Word '{word}' found at position {start}-{end}.")

#Task 5
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
result = re.finditer(pattern, sample_text)
for match in result:
    start = match.start()
    end = match.end()
    print(f"Substring '{pattern}' found at position {start}-{end}")


#Task 6 using same sample and pattern as task 5
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
result = re.finditer(pattern, sample_text)
count = 0
for match in result:
    start = match.start()
    end = match.end()
    count += 1
    print(f"Occurrence {count}: Substring '{pattern}' found at position {start}-{end}")

#Task 7
input_string = str(input("Enter string: "))

    ## Replace whitespaces with underscores
result = re.sub(r'\s', '_', input_string)
print("After replacing whitespaces with underscores:")
print(result)

    ## Replace underscores with whitespaces
result = re.sub(r'_', ' ', result)
print("\nAfter replacing underscores with whitespaces:")
print(result)