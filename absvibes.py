import string
import ads

def get_abstract_words(author_ORCID):
  """Returns a list of every single word in the abstracts of the author.
  """

  papers = list(ads.SearchQuery(orcid=author_ORCID))

  # the below returns a list of lists...
  abslist = [paper.abstract for paper in papers]
  
  # ...and this removes empty abstracts...
  noempty_abslist = [abst for abst in abslist if abst]

  # ...then we split all the abstracts up into individual words...
  allwords_raw = [f.split(" ") for f in noempty_abslist]
  
  # ...and this flattens the list.
  allwords_flat = [item for sublist in allwords_raw for item in sublist]

  # let's remove punctuation
  # basically goes through each letter of each word and joins/'allows' it if it isn't in the string.punctuation list
  allwords_nopunc = ["".join(letter for letter in word if letter not in string.punctuation) for word in allwords_flat]

  # and lowercase.
  allwords_lower = [word.lower() for word in allwords_nopunc]

  return allwords_lower