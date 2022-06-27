# SciVibes 1.1.0

This is a scientific vibe estimator based on [ADS](https://ui.adsabs.harvard.edu/) abstracts!

Project for Code/Astro 2022 by Mireya Arora, Steph Merritt, and Luna Zagorac.

[![codeastro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

## Notes for installing

This code requires that you provide your own ADS API key. This is easy to generate: go to your account settings and choose "API Token" on the right-hand menu, then click the "Generate a new key" button.

All the dependencies are specified in requirements.txt, so cloning the git directory onto your computer and running

```
pip install scivibes -r requirements.txt
```
within the directory should take care of all dependencies. 

## Notes for running

Please see demo Jupyter notebook to test your vibes!

You can also run the software directly from the terminal. You need either the author's name or ORCID ID (the example includes both, please only use one!).
```
python scivibes_.py --ads_config_token [Your ADS Configuration Token] --ORCID [Your ORCID id here] --author_name [Your author name here] --filename [optional name for file]
```
The vibe files are saved in the format "filename_Vibe.png" and "filename_AntiVibe.png". The vibestogram of total vibes is saved as "vibestogram.jpg".

## Sentiment Analysis Data Source

The files in the subreddits/ folder were created by the authors of the [SocialSent](https://nlp.stanford.edu/projects/socialsent/) project. The process between producing these domain-specific lexicons is described in their paper, [Inducing Domain-Specific Sentiment Lexicons from Unlabeled Corpora](https://arxiv.org/abs/1606.02820).

## Vibe Image Data Source

The code used to create the Vibe and Anti_Vibe images is based on this [package](https://github.com/erdavids/WatercolorClouds) by Eric Davidson.
