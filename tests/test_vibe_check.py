import scivibes
import os
import glob
import json

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
    # will want to import these + subreddits + reddit2vibe!
    test_wordlist = ["this", "is", "a", "list", "of", "words", "for", "testing"]
    test_stop = ["this", "is", "a", "list", "of", "words", "for", "testing"]

    # grab all the subreddit names & dictionary of subreddits to vibes
    subreddits = [os.path.basename(x[:-4]) for x in glob.glob('../scivibes/subreddits/*.tsv')]
    reddit2vibe = json.load(open("../scivibes/reddit2vibe.txt"))

    # run function 
    [most, least] = scivibes.total_vibe_check(test_wordlist, test_stop, subreddits, reddit2vibe)

    # the vibe should be zero due to all stop words being removed
    assert len(most) == 3
    assert len(least) == 3


## Uncomment below if running tests manually

# print("Testing vibe check")
# test_vibe_check()


# print("Testing total vibe check")
# test_total_vibe_check()

