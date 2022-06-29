import cairo, copy, math, random

float_gen = lambda a, b: random.uniform(a, b)

def color_picker(vibe_score, vibe_color):

    """Color Picker 
    
    Selects colors corresponding to the vibe and their rank (top vibe has darkest/most
    intense color).

    Args:
        vibe_score (lists of tuples): A list containing two lists (the top 3 vibes and the 
        bottom 3 vibes). 
        vibe_color (dict): A dictionary connecting vibes to colors (different color intensities
        for top 3 ranks)

    Returns:
        (array): 6 arrays containg the rgb codes for colors used in the abstract art. First three
        arrays are the top 3 vibes, second three are the 3 vibes (anti_vibes). 

    """

    #selecting the appropriate colors for each vibe
    c_1 = vibe_color[vibe_score[-1][0]]['High']
    c_2 = vibe_color[vibe_score[-2][0]]['Med']
    c_3 = vibe_color[vibe_score[-3][0]]['Low']

    #selecting the appropriate colors for each antivibe
    c_4 = vibe_color[vibe_score[0][0]]['High']
    c_5 = vibe_color[vibe_score[1][0]]['Med']
    c_6 = vibe_color[vibe_score[2][0]]['Low']


    return c_1,c_2,c_3,c_4,c_5,c_6


def octagon(x_orig, y_orig, side):

    """Octagon
    
    Makes an octagon shape for the watercolor splotches. 

    Args:
        x_orig (int): x-coordinate start point for octagon
        y_orig (int): y-coordinate start point for octagon.
        side (int): side length.

    Return:
        (list): octagon shape object.
    
    """

    x = x_orig
    y = y_orig

    #shape diagonal
    d = side / math.sqrt(2)

    oct = []

    #working around the octagon adding each side using append
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

    """ Deform

    Defroms the edges of the octagon to make the shape look similar to a watercolor splotch. It moves
    the midpoint of each side of the octagon by a certain amount determined by the variance

    Args:
        shape (list of tuples): the octagon shape (output of the octagon function)
        iterations (int): number of times the midpoint of the side should be shifted
        variance (float): the amount the midpoint of each side should be moved

    Return: 
        (list): deformed octagon shape 
    
    """

    #loop through for the number of iterations
    for i in range(iterations):
        #loop through for each side
        for j in range(len(shape)-1, 0, -1):
            #get the midpoint for each side and shift it based on the variance
            midpoint = ((shape[j-1][0] + shape[j][0])/2 + float_gen(-variance, variance), (shape[j-1][1] + shape[j][1])/2 + float_gen(-variance, variance))
            shape.insert(j, midpoint)
    return shape


def view_vibes(vibe_score, name, vibe_color):

    """main

    Uses the other functions (octagon, deform, and color_picker) to build the image.

    Args:
        vibe_score (list of tuples): list containing two lists each containing 3 tuples 
        defining the rgb values for the top 3 vibes and lowest 3 vibes. This is the output from the
        total_vibe_check().
        name (string): name for the resulting image file. Images are name in the format (name_Vibe) 
        and (name_AntiVibe)
        vibe_color (dict): A dictionary connecting vibes to colors (different color intensities 
        for top 3 ranks)

    Return:
        none; two png images are saved to the scivibes folder.

    """
    #size of image
    width=1000
    height=1500
    #initial deformation placed on the base shape before layering
    initial=120
    #deviation for each layer 
    deviation=50
    #how many times shape is deformed before layering
    basedeforms=1
    #how many time deformation occurs during layering
    finaldeforms=3
    #min and max number of layers per octagon
    minshapes=20
    maxshapes=25
    #how transparent octagons are: high number is more clear 
    shapealpha=.02

    #create image surface being drawn on
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    #context
    cr = cairo.Context(ims)

    #background (image surface) color (bg)
    bg = (0.1,0.1,0.1)
    cr.set_source_rgb(bg[0],bg[1],bg[2])
    #image surface shape
    cr.rectangle(0, 0, width, height)
    cr.fill()

    cr.set_line_width(1)

    # selecting vibe colors
    vibe_1, vibe_2, vibe_3, vibe_4, vibe_5, vibe_6 = color_picker(vibe_score,vibe_color)

    colors = [list(vibe_1), list(vibe_2), list(vibe_3)]
    anti_colors = [list(vibe_4), list(vibe_5), list(vibe_6)]

    #starting above and ending below image to prevent white spaces
    #p rows for drawing
    for p in range(-int(height*.2), int(height*1.2), 60):

        #define colors and transparancy (alpha)
        cr.set_source_rgba((random.choice(colors)[0])/255, (random.choice(colors)[1])/255, (random.choice(colors)[2])/255, shapealpha)

        #create octagon shape 
        shape = octagon(random.randint(-100, width+100), p, random.randint(100, 300))
        #create deformed octagon shape
        baseshape = deform(shape, basedeforms, initial)

        #layering shapes to make art
        for j in range(random.randint(minshapes, maxshapes)):
            tempshape = copy.deepcopy(baseshape)
            layer = deform(tempshape, finaldeforms, deviation)

            for i in range(len(layer)):
                cr.line_to(layer[i][0], layer[i][1])
            cr.fill()

    ims.write_to_png(name+'_Vibe'+'.png')

    #repeat process for lowest ranked vibes --> anti_vibes
    for p in range(-int(height*.2), int(height*1.2), 60):

        #define colors and transparancy (alpha)
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
    