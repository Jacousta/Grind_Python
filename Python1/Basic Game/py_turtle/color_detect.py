import colorgram
rgb_list = []
colors = colorgram.extract('randall-ruiz-272502.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colour_set = (r, g, b)
    rgb_list.append(colour_set)

print(rgb_list)
