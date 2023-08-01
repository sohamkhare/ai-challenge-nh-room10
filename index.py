import random
import string
import nltk
from nltk.corpus import stopwords

def summarize(text, length):
  """Summarizes a given piece of text to a specified length.

  Args:
    text: The text to be summarized.
    length: The desired length of the summary in letter count.

  Returns:
    The summarized text.
  """

  stopwords = set(stopwords.words('english'))
  words = text.split()
  filtered_words = [word for word in words if word not in stopwords]
  summary = ' '.join(filtered_words[:length])
  return summary

def generate_share_links(summary):
  """Generates links to share the summary on social media.

  Args:
    summary: The summary to be shared.

  Returns:
    A list of links to share the summary.
  """

  links = []
  links.append('https://www.facebook.com/sharer/sharer.php?u=https://www.example.com/summary/' + summary)
  links.append('https://twitter.com/intent/tweet?text=' + summary)
  return links

def main():
  """The main function of the website."""

  text = input('Enter the text to be summarized: ')
  length = int(input('Enter the desired length of the summary in letter count: '))
  summary = summarize(text, length)
  links = generate_share_links(summary)
  print('The summary is: ' + summary)
  print('You can share the summary using the following links: ' + links)

if __name__ == '__main__':
  main()
