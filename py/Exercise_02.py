text = """Python is a powerful programming language. It's easy to learn and versatile! You can use Python for web development, data science, and automation. The syntax is clean and readable. This makes Python perfect for beginners and experts alike"""

print(len(text))
word_count = len (text.split())
print (word_count)
sentence_count = text.count('.') + text.count('!') + text.count('?')
print (sentence_count)