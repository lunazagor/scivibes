import string
import os
import ads
import scivibes
import glob
import json
import cairo
import copy
import math
import random
import argparse


    
#get input from terminal (ads config token and author orcid/name)
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--ads_config_token", type=str, help = "Please enter your ADS config token",required=True)
arg_parser.add_argument("--ORCID", type=str, help = "Enter either the author's ORCID ID or full name")
arg_parser.add_argument("--author_name", type=str, help = "Enter either the author's ORCID ID or full name")
arg_parser.add_argument("--filename", type=str, help = "Enter a filename for output (result is filename_Vibe)",default="Example")

args = arg_parser.parse_args()  

ads.config.token = args.ads_config_token

#get either author orcid/name
if args.ORCID:
    author_details = args.ORCID
elif args.author_name:
    author_details = args.author_name
else:
    print("Please enter at least one of: Author ORCID ID or Author Name")

# this gets a list of all words in all abstracts with that author
# if the author has a lot of papers this will take a while :)
abstract_list = scivibes.get_abstracts(author_details)
new_wordlist = scivibes.get_abstract_words(abstract_list)

#get stop words
stop_terms = open("scivibes/stopwords.txt",'r').read().splitlines()

# grab all the subreddit names,
subreddits = [os.path.basename(x[:-4]) for x in glob.glob('scivibes/subreddits/*.tsv')]

# dictionary of subreddits to vibes,
reddit2vibe = json.load(open("scivibes/reddit2vibe.txt"))

#calculate Vibes
tot_vibes = scivibes.total_vibe_check(new_wordlist, stop_terms, subreddits, reddit2vibe)

# generate vibe plots
scivibes.view_vibes(tot_vibes, args.filename)

# a handy histogram of vibes
fig, ax = scivibes.plot_vibestogram(tot_vibes)

print("Your Vibes and Anti_Vibes have been Discovered!")

