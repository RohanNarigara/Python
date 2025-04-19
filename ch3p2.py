letter = '''
Dear <|name|>,
You are Selected for the <|job|> position!
<|date|>'''

print(letter.replace("<|name|>", "Rohan").replace("<|job|>", "CEO").replace("<|date|>", "22 Aug 2025"))

# letter = '''
# Dear {name},
# Thank you for your letter. We are happy to inform you that we have received your application for the {job} position. We will get back to you shortly.'''

# name = input("Enter your name: ")
# job = input("Enter the job title: ")

# print(letter.format(name=name, job=job))

# This code takes a letter template and fills in the placeholders with user input.
# The user is prompted to enter their name and the job title they are applying for.
# The letter is then printed with the placeholders replaced by the provided values.
# This is a simple example of string formatting in Python.
# The code uses the format() method to replace placeholders in the letter template with actual values.
# The placeholders are defined using curly braces {} in the letter string.
# The format() method takes keyword arguments that match the placeholders in the string.
# The resulting string is then printed to the console.
# This code is a simple example of string formatting in Python.
# It uses the format() method to replace placeholders in the letter template with actual values.
# The placeholders are defined using curly braces {} in the letter string.