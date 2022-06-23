# SciVibes 1.0.0

This is a scientific vibe estimator based on [ADS](https://ui.adsabs.harvard.edu/) abstracts!

Project for Code/Astro 2022 by Mireya Arora, Steph Merritt, and Luna Zagorac.

[![codeastro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

## Notes for running

This code requires that you provide your own ADS API key. This is easy to generate: go to your account settings and choose "API Token" on the right-hand menu, then click the "Generate a new key" button.

This code uses the [ads package](https://ads.readthedocs.io/en/latest/#). However, this package also requires the use of a downgraded version of the [werkzeug package](https://werkzeug.palletsprojects.com/en/2.1.x/). To install:

```
pip install ads
pip install werkzeug==1.0.1
```

This works around the issue noted in [this](https://github.com/andycasey/ads/pull/119) pull request.
