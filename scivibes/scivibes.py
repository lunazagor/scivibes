#from pydoc import replace
import string
import ads
import pandas as pd
import os 
import operator 
import re

scivibes_dir = os.path.dirname(__file__)
datadir = os.path.join(scivibes_dir, '')

def flatten_list(unflat_list):
    """Flattens list.
    
    Flattens a list containing sublists into a single 1D list.

    Args:
        unflat_list (list): a list containing sublists

    Returns:
        list: a flattened version of unflat_list

    """
    return [item for sublist in unflat_list for item in sublist]


def get_abstracts(author_ORCID):

    papers = list(ads.SearchQuery(orcid=author_ORCID))
    abslist = [paper.abstract for paper in papers]
    noempty_abslist = [abst for abst in abslist if abst]

    return noempty_abslist


def get_abstract_words(abslist):
    """Get all words from abstracts.

    Returns a list of every single word in the abstracts of the author. Strips punctuation, replaces common
    abbreviations/acronyms with constituent words, and lowercases everything.

    Args: 
        abslist (list): a list containing the abstracts in question, created by get_papers.

    Returns:
        list: a list of words in all abstracts in lower-case with punctuation removed and common acronyms expanded.
    """

    # we split all the abstracts up into individual words...
    allwords_raw = [re.split(" |-", f) for f in abslist]

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
    """Replaces abbreviations with constituent words.
    
    Runs through a list of words and replaces common astronomy acronyms and
    abbreviations with their constituent words.

    Args:
        wordlist (list): A list of words.
    
    Returns:
        list: The same list of words with common acronyms and abbreviations
            replaced by their constituent words.
    """

    abbreviations = {}
    with open(datadir + "abbreviations.txt") as f:
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


def vibe_check(wordlist, stop_terms, reddit_vibe):
    """Get a singular vibe comparison with a given subreddit.
    
    Returns an integer vibe value for a given list of abstract words, 
    stoplist, and sentiment analysis reddit file.

    Args: 
    wordlist (list of strings): a list of abstract words from get_abstract_words()
    stop_terms (list of strings): a list of words to ignore ("the", "a", "of"....)
    reddit_vibe (string): a string corresponding to tsv filename in the /subreddits folder

    Returns:
    int: a total vibe value (can be positive or negative)
    """
    # first remove the stop terms
    for st in stop_terms:
        wordlist = [i for i in wordlist if i != st]

    # make abstract terms and counts DataFrame
    df_abs = pd.DataFrame(wordlist, columns=['term']).value_counts('term').reset_index().rename(columns={0: 'count'})

    # make reddit comparison data frame
    df_reddit = pd.read_csv(scivibes_dir + '/subreddits/'+ reddit_vibe + '.tsv', sep='\t', header=None, names=['term', 'mean_sentiment', 'std_sentiment'])

    # find intersection of two data frames based on 'term' column
    df_int = pd.merge(df_abs, df_reddit, how='inner', on=['term'])

    # calculate weighted 'vibe' column
    df_int['vibe'] = df_int['count'] * df_int['mean_sentiment']

    # retrun overall vibe value as an integer
    return(int(df_int['vibe'].sum()))


def total_vibe_check(wordlist, stop_terms, subreddits, reddit2vibe):
    """Returns a list of 3 most- and least-positive vibes and their values.

    Args: 
    wordlist (list of strings): a list of abstract words from get_abstract_words()
    stop_terms (list of strings): a list of words to ignore ("the", "a", "of"....)
    subreddits (list of strigs): list of subreddits to source vibes from
    reddit2vibe (dictionary): a dictionary converting subreddit names to assigned vibes

    Returns:
    list: sorted values of vibes (ascending)
    """
    # create dictionary of vibes and values
    vibe_dict = {}
    for sr in subreddits:
        vibe_num = vibe_check(wordlist, stop_terms, sr)
        vibe = reddit2vibe[sr]
        vibe_dict[vibe] = vibe_num

    # sort dictionary by value
    vibe_dict = sorted(vibe_dict.items(), key=operator.itemgetter(1))    

    # return vibes
    return(vibe_dict)

