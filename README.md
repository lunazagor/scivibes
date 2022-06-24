# SciVibes 1.0.1

This is a scientific vibe estimator based on [ADS](https://ui.adsabs.harvard.edu/) abstracts! This fork is for folks who can't install pycairo and only produces a histogram of results instead of the cool visualisation.

Project for Code/Astro 2022 by Mireya Arora, Steph Merritt, and Luna Zagorac.

[![codeastro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

## Notes for running

This code requires that you provide your own ADS API key. This is easy to generate: go to your account settings and choose "API Token" on the right-hand menu, then click the "Generate a new key" button.

To run:

```
git clone https://github.com/astronomerritt/uglyscivibes.git
cd uglyscivibes
pip install -e .
pip install -r requirements.txt 
```

Then open the demo notebook, insert your own API token in the required cell, and run :)

## Sentiment Analysis Data Source

The files in the subreddits/ folder were created by the authors of the [SocialSent](https://nlp.stanford.edu/projects/socialsent/) project. The process between producing these domain-specific lexicons is described in their paper, [Inducing Domain-Specific Sentiment Lexicons from Unlabeled Corpora](https://arxiv.org/abs/1606.02820).
