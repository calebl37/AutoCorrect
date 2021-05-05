# Loads in a text file, ignoring any lines that start with
# a pound sign '#'.
# In repl.it, this works with path names relative to main.py 
# Files which are in the same folder as main.py need no
# directory prefix.

# Returns the entire filtered text as one string with embedded
# newlines.
def load_text(filename):
  file = open(filename, "r")
  bulk_data = file.read()
  file.close()

  lines = bulk_data.split('\n')
  filtered_lines = []
  for line in lines:
    if not line.startswith('#'):
      filtered_lines.append(line)
  text = '\n'.join(filtered_lines)  
  return text
  

# Takes in a long text and segments it into a list of words.
# This converts all words to lowercase, ignores punctuation and
# line breaks.
def text_to_word_list(text):
  # make all letters lowercase
  text_lower = text.lower()

  # remove all punctuation and new lines.
  text_clean = text_lower.replace("\n", " ")
  text_clean = text_clean.replace(".", "")
  text_clean = text_clean.replace("?", "")
  text_clean = text_clean.replace("!", "")
  text_clean = text_clean.replace(",", " ")
  text_clean = text_clean.replace("-", " ")

  # convert text into a list of individual words.
  word_list = text_clean.split(" ")
  # discard any empty words or words that are all spaces. 
  clean_list = list()
  for word in word_list:
    if word and not word.isspace():
      clean_list.append(word)
  return clean_list


def text_to_line_list(text):
  line_list = text.split("\n")
  return line_list
  