import colorgram

colors = colorgram.extract("image.jpeg", 16 * 25)

rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

print(rgb_colors)
