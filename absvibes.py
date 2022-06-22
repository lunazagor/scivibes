import string
import ads
import pandas as pd
import glob
import os 
import operator 

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


def vibe_check(wordlist, stop_terms, reddit_vibe):
  """Returns an integer vibe value for a given list of abstract words, 
  stoplist, and sentiment analysis reddit file.

  inputs: 
    wordlist = list of abstract words
    stop_terms: list of words to ignore ("the", "a", "of"....)
    reddit_vibe: string corresponding to tsv filename in the /subreddits folder

  """
  # first remove the stop terms
  for st in stop_terms:
      wordlist = [i for i in wordlist if i != st]

  # make abstract terms and counts DataFrame
  df_abs = pd.DataFrame(wordlist, columns=['term']).value_counts('term').reset_index().rename(columns={0: 'count'})

  # make reddit comparison data frame
  df_reddit = pd.read_csv('subreddits/'+ reddit_vibe + '.tsv', sep='\t', header=None, names=['term', 'mean_sentiment', 'std_sentiment'])

  # find intersection of two data frames based on 'term' column
  df_int = pd.merge(df_abs, df_reddit, how='inner', on=['term'])

  # calculate weighted 'vibe' column
  df_int['vibe'] = df_int['count'] * df_int['mean_sentiment']

  # retrun overall vibe value as an integer
  return(int(df_int['vibe'].sum()))

  