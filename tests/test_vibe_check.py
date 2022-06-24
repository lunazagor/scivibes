import scivibes
import os
import glob
import json

#scivibes_dir = os.path.dirname(__file__)
#datadir = os.path.join(scivibes_dir, '')

def test_vibe_check():
    """
    Tests the basic functionality of scivibes.test_vibe_check() in scivibes.py
    for returning a single subreddit vibe.
    """
    # define input 
    test_wordlist = ["this", "is", "a", "list", "of", "words", "for", "testing"]
    test_stop = ["this", "is", "a", "list", "of", "words", "for", "testing"]

    # run function 
    test_vibe = scivibes.vibe_check(test_wordlist, test_stop, "anime")

    # the vibe should be zero due to all stop words being removed
    assert test_vibe==0


def test_total_vibe_check():
    """
    Tests the basic functionality of scivibes.test_vibe_check() in scivibes.py
    for returning a single subreddit vibe.
    """
    # define input 
    test_wordlist = open("test_wordlist.txt",'r').read().splitlines()

    # import stopword list
    filepath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'scivibes/stopwords.txt'))
    print(filepath)
    test_stop = open(filepath,'r').read().splitlines()

    # grab the dictionary of subreddits to vibes
    filepath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'scivibes/reddit2vibe.txt'))
    print(filepath)
    reddit2vibe = json.load(open(filepath))

    # grab all the available subreddits to compare
    filepath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'scivibes/subreddits/*.tsv'))
    print(filepath)
    subreddits = [os.path.basename(x[:-4]) for x in glob.glob(filepath)]

    # run function 
    test_vibes = scivibes.total_vibe_check(test_wordlist, test_stop, subreddits, reddit2vibe)

    # the vibe should be zero due to all stop words being removed
    assert len(test_vibes) == len(subreddits)


## Uncomment below if running tests manually

# print("Testing vibe check")
# test_vibe_check()


# print("Testing total vibe check")
# test_total_vibe_check()


