import numpy as np
import pytest
import scivibes
import math
import random

def test_color_picker():

    """
    Test the ability of scivibes.color_picker() to work properly on vibe_score (a list of list of tuples).
    
    """
    #dictionary used for vibes
    color_samples = {'geeky': {'High': (24,106,59), 'Med': (46,204,113), 'Low': (213, 245, 227)},
    'fantasy': {'High': (74, 35, 90), 'Med': (165, 105, 189), 'Low': (232, 218, 239)},
    'anarcho-capitalist': {'High': (66, 73, 73), 'Med': (127, 140, 141), 'Low': (242, 244, 244)},
    'cursed': {'High': (176, 58, 46), 'Med': (231, 76, 60), 'Low': (245, 183, 177)},
    'musical': {'High': (81, 46, 95), 'Med': (155, 89, 182), 'Low': (215, 189, 226)},
    'Tumblr': {'High': (21, 67, 96), 'Med': (41, 128, 185), 'Low': (169, 204, 227)},
    'cute': {'High': (245, 101, 201), 'Med': (243, 152, 216), 'Low': (248, 194, 232)},
    'Disney': {'High': (40, 116, 166), 'Med': (93, 173, 226), 'Low': (174, 214, 241)},
    'jock': {'High': (175, 96, 26), 'Med': (230, 126, 34), 'Low': (245, 203, 167)},
    'wholesome': {'High': (243, 156, 18), 'Med': (248, 196, 113), 'Low': (250, 215, 160)},
    'British': {'High': (146, 43, 33), 'Med': (205, 97, 85), 'Low': (230, 176, 170)},
    'funny': {'High': (241, 196, 15), 'Med': (247, 220, 111), 'Low': (249, 231, 159)},
    'cringe': {'High': (46, 64, 83), 'Med': (93, 109, 126), 'Low': (174, 182, 191)},
    'anime': {'High': (11, 83, 69), 'Med': (22, 160, 133), 'Low': (115, 198, 182)},
    'science': {'High': (14, 98, 81), 'Med': (26, 188, 156), 'Low': (163, 228, 215)}
    }

    #create sample vibe_score
    vibe_score = [[('anime', 98), ('musical', 134), ('science', 196)],
    [('cringe', -48), ('wholesome', -13), ('Tumblr', -12)]]

    #select appropriate colors for each vibe and anti_vibe
    exp_c_1 = color_samples[vibe_score[0][0][0]]['High']
    exp_c_2 = color_samples[vibe_score[0][1][0]]['Med']
    exp_c_3 = color_samples[vibe_score[0][2][0]]['Low']
    exp_c_4 = color_samples[vibe_score[1][0][0]]['High']
    exp_c_5 = color_samples[vibe_score[1][1][0]]['Med']
    exp_c_6 = color_samples[vibe_score[1][2][0]]['Low']

    #use scivibes.color_picker()
    c_1,c_2,c_3,c_4,c_5,c_6 = scivibes.color_picker(vibe_score)

    #check values match

    assert exp_c_1 == c_1
    assert exp_c_2 == c_2
    assert exp_c_3 == c_3
    assert exp_c_4 == c_4
    assert exp_c_5 == c_5
    assert exp_c_6 == c_6

def test_octagon():

    """
    Test the ability of scivibes.octagon() to create a shape object using specific start coords and side length.
    
    """

    x_orig = 50
    y_orig = 2
    side = 200

    #previously calculated expected result
    exp_oct = [(50, 2),(250, 2),(391.4213562373095, 143.42135623730948),(391.4213562373095, 343.4213562373095),
    (250.00000000000003, 484.842712474619),(50.00000000000003, 484.842712474619),(-91.42135623730945, 343.4213562373095),
    (-91.42135623730945, 143.4213562373095),(50.00000000000003, 2.0000000000000284)]

    #calculate result
    oct = scivibes.octagon(x_orig, y_orig, side)

    #check results match
    assert exp_oct == oct

def test_deform():

    """
    
    
    """
