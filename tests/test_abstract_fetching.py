
def test_get_abstracts():
    from scivibes import get_abstracts
    
    ads.config.token = 'tVMB0TgzQmmwxI6q3TfSrNRMqis5KmvK5C2nDq7s'
    author_ORCID = "0000-0001-5930-2829"
    
    actual_abstract = 'Ultrahot Jupiters (UHJs) present excellent targets for atmospheric characterization. Their hot dayside temperatures (T ≳ 2200 K) strongly suppress the formation of condensates, leading to clear and highly inflated atmospheres extremely conducive to transmission spectroscopy. Recent studies using optical high-resolution spectra have discovered a plethora of neutral and ionized atomic species in UHJs, placing constraints on their atmospheric structure and composition. Our recent work has presented a search for molecular features and detection of Fe I in the UHJ WASP-121b using Very Large Telescope (VLT)/UV-Visual Echelle Spectrograph (UVES) transmission spectroscopy. Here, we present a systematic search for atomic species in its atmosphere using cross-correlation methods. In a single transit, we uncover potential signals of 17 atomic species that we investigate further, categorizing five as strong detections, three as tentative detections, and nine as weak signals worthy of further exploration. We confirm previous detections of Cr I, V I, Ca I, K I, and exospheric H I and Ca II made with the High Accuracy Radial velocity Planet Searcher (HARPS) and the Echelle SPectrograph for Rocky Exoplanets and Stable Spectroscopic Observations (ESPRESSO), and independently re-recover our previous detection of Fe I at 8.8σ using both the blue and red arms of the UVES data. We also add a novel detection of Sc II at 4.2σ. Our results further demonstrate the richness of UHJs for optical high-resolution spectroscopy.'

    test_abstract = scivibes.get_abstracts(author_ORCID)

    assert test_abstract[0] == actual_abstract


def test_get_abstract_words():
    from scivibes import get_abstract_words

    test_single_abstract = ['This is my test abstract. It has punctuat!on, hyphenated-words and an abbreviation: UHJs.']

    expected_wordlist = ['this',
                        'is',
                        'my',
                        'test',
                        'abstract',
                        'it',
                        'has',
                        'punctuaton',
                        'hyphenated',
                        'words',
                        'and',
                        'an',
                        'abbreviation',
                        'ultra',
                        'hot',
                        'jupiters']
    
    test_wordlist = get_abstract_words(test_single_abstract)

    assert test_wordlist == expected_wordlist

