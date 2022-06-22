#from pydoc import replace
import string
import ads
import re

def flatten_list(unflat_list):
    return [item for sublist in unflat_list for item in sublist]

def get_abstract_words(author_ORCID):
  """Returns a list of every single word in the abstracts of the author.

  Inputs: 
  author_ORCID: a string containing the ORCID of interest

  Returns:
  allwords_lower: a list of words in all abstracts in lower-case with punctuation removed and common acronyms expanded
  """

  papers = list(ads.SearchQuery(orcid=author_ORCID))

  # the below returns a list of lists...
  abslist = [paper.abstract for paper in papers]
  
  # ...and this removes empty abstracts...
  noempty_abslist = [abst for abst in abslist if abst]

  # ...then we split all the abstracts up into individual words...
  allwords_raw = [re.split(" |-", f) for f in noempty_abslist]
  
  # ...and this flattens the list.
  allwords_flat = flatten_list(allwords_raw)

  # let's remove punctuation
  # basically goes through each letter of each word and joins/'allows' it if it isn't in the string.punctuation list
  allwords_nopunc = ["".join(letter for letter in word if letter not in string.punctuation) for word in allwords_flat]

  # before we lowercase, let's replace abbreviations with their constituent words
  allwords_abbrev = replace_abbreviations_with_words(allwords_nopunc)

  # and lowercase.
  allwords_lower = [word.lower() for word in allwords_abbrev]

  return allwords_lower

def replace_abbreviations_with_words(wordlist):

    abbreviations = {}
    with open("abbreviations.txt") as f:
        for line in f:
            (key, val) = line.split(",")
            val = val.rstrip()
            abbreviations[key] = val

    for i, word in enumerate(wordlist):
        for v in abbreviations:
            if word == v:
                wordlist[i] = abbreviations[v]

    wordlist_split = [f.split(" ") for f in wordlist]
    wordlist_flat = flatten_list(wordlist_split)

    return wordlist_flat