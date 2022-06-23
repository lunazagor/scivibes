import cairo, sys, argparse, copy, math, random

# TODO: Remove name and vibe_score when merging things
name = "StephBoss"
vibe_score = [[('anime', 367), ('musical', 445), ('science', 451)],
 [('cringe', -71), ('Tumblr', -56), ('wholesome', -51)]]

float_gen = lambda a, b: random.uniform(a, b)

def color_picker(vibe_score):

    """
    Color Picker: selects colors corresponding to the vibe and their rank (top vibe has darkest/most
    intense color).

    Args:
        vibe_score (list of lists of tuples): A list containing two lists (the top 3 vibes and the 
        bottom 3 vibes). 

    Returns:
        (array): 6 arrays containg the rgb codes for colors used in the abstract art. First three
        arrays are the top 3 vibes, second three are the 3 vibes (anti_vibes). 

    """

    color_samples = {'geek': {'High': (24,106,59), 'Med': (46,204,113), 'Low': (213, 245, 227)},
    'fantasy': {'High': (74, 35, 90), 'Med': (165, 105, 189), 'Low': (232, 218, 239)},
    'anarcho Capitalism': {'High': (66, 73, 73), 'Med': (127, 140, 141), 'Low': (242, 244, 244)},
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
    
    c_1 = color_samples[vibe_score[0][0][0]]['High']
    c_2 = color_samples[vibe_score[0][1][0]]['Med']
    c_3 = color_samples[vibe_score[0][2][0]]['Low']

    c_4 = color_samples[vibe_score[1][0][0]]['High']
    c_5 = color_samples[vibe_score[1][1][0]]['Med']
    c_6 = color_samples[vibe_score[1][2][0]]['Low']


    return c_1,c_2,c_3,c_4,c_5,c_6

# colors = []
# for i in range(15):
#     colors.append((float_gen(.4, .75), float_gen(.4, .75), float_gen(.4, .75)))

# TODO: Create a color pallete for each aesthetic 
        # Pick color pallete based on chosen vibes
        # this code randomly generates a watercolor piece based on randomly chosen colors from the pallete 


def octagon(x_orig, y_orig, side):
    x = x_orig
    y = y_orig
    d = side / math.sqrt(2)

    oct = []

    oct.append((x, y))

    x += side
    oct.append((x, y))

    x += d
    y += d
    oct.append((x, y))

    y += side
    oct.append((x, y))

    x -= d
    y += d
    oct.append((x, y))

    x -= side
    oct.append((x, y))

    x -= d
    y -= d
    oct.append((x, y))

    y -= side
    oct.append((x, y))

    x += d
    y -= d
    oct.append((x, y))

    return oct

def deform(shape, iterations, variance):
    for i in range(iterations):
        for j in range(len(shape)-1, 0, -1):
            midpoint = ((shape[j-1][0] + shape[j][0])/2 + float_gen(-variance, variance), (shape[j-1][1] + shape[j][1])/2 + float_gen(-variance, variance))
            shape.insert(j, midpoint)
    return shape


def main(vibe_score, name):
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", default=1000, type=int)
    parser.add_argument("--height", default=1500, type=int)
    parser.add_argument("-i", "--initial", default=120, type=int)
    parser.add_argument("-d", "--deviation", default=50, type=int)
    parser.add_argument("-bd", "--basedeforms", default=1, type=int)
    parser.add_argument("-fd", "--finaldeforms", default=3, type=int)
    parser.add_argument("-mins", "--minshapes", default=20, type=int)
    parser.add_argument("-maxs", "--maxshapes", default=25, type=int)
    parser.add_argument("-sa", "--shapealpha", default=.02, type=float)
    args = parser.parse_args()

    width, height = args.width, args.height
    initial = args.initial
    deviation = args.deviation

    basedeforms = args.basedeforms
    finaldeforms = args.finaldeforms

    minshapes = args.minshapes
    maxshapes = args.maxshapes

    shapealpha = args. shapealpha

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)


    brightness = (0.1,0.1,0.1)
    cr.set_source_rgb(brightness[0],brightness[1],brightness[2])
    cr.rectangle(0, 0, width, height)
    cr.fill()

    cr.set_line_width(1)

    vibe_1, vibe_2, vibe_3, vibe_4, vibe_5, vibe_6 = color_picker(vibe_score)

    colors = [list(vibe_1), list(vibe_2), list(vibe_3)]
    anti_colors = [list(vibe_4), list(vibe_5), list(vibe_6)]

    for p in range(-int(height*.2), int(height*1.2), 60):
        cr.set_source_rgba((random.choice(colors)[0])/255, (random.choice(colors)[1])/255, (random.choice(colors)[2])/255, shapealpha)

        shape = octagon(random.randint(-100, width+100), p, random.randint(100, 300))
        baseshape = deform(shape, basedeforms, initial)

        for j in range(random.randint(minshapes, maxshapes)):
            tempshape = copy.deepcopy(baseshape)
            layer = deform(tempshape, finaldeforms, deviation)

            for i in range(len(layer)):
                cr.line_to(layer[i][0], layer[i][1])
            cr.fill()

    ims.write_to_png(name+'_Vibe'+'.png')

    for p in range(-int(height*.2), int(height*1.2), 60):
        cr.set_source_rgba((random.choice(anti_colors)[0])/255, (random.choice(anti_colors)[1])/255, (random.choice(anti_colors)[2])/255, shapealpha)

        shape = octagon(random.randint(-100, width+100), p, random.randint(100, 300))
        baseshape = deform(shape, basedeforms, initial)

        for j in range(random.randint(minshapes, maxshapes)):
            tempshape = copy.deepcopy(baseshape)
            layer = deform(tempshape, finaldeforms, deviation)

            for i in range(len(layer)):
                cr.line_to(layer[i][0], layer[i][1])
            cr.fill()

    ims.write_to_png(name+'_AntiVibe'+'.png')

if __name__ == "__main__":
    main(vibe_score, name)