# Module: gef_branding.py
# This module provides utilities for working with the GEF brand guidelines,
# including color palettes and typography.

from typing import NamedTuple

# Define a class for color information
class Color(NamedTuple):
    pantone: str
    cmyk: tuple
    rgb: tuple
    hex: str

# Colors
PRIMARY_GREEN = Color("7483", (83, 16, 83, 54), (0, 88, 51), "#005833") #One of main 5 colors
SUPPORTING_BLUE = Color("288", (100, 87, 27, 19), (29, 56, 109), "#1D386D") #One of main 5 colors
SUPPORTING_GREEN1 = Color("348", (100, 4, 87, 18), (0, 138, 82), "#008A52") #One of main 5 colors
SUPPORTING_GREEN2 = Color("377", (58, 22, 100, 4), (121, 155, 22), "#799B3E")
SUPPORTING_GREEN3 = Color("383", (26, 3, 93, 17), (169, 181, 51), "#A9B533")
SUPPORTING_RED1 =  Color("200", (16, 100, 87, 7), (194, 32, 50), "#C22032")
SUPPORTING_RED2 = Color("7418", (3, 80, 48, 9), (213, 82, 96), "#D55260")
SUPPORTING_YELLOW = Color("143", (3, 32, 91, 0), (244, 179, 51), "#F4B333")
SUPPORTING_BROWN = Color("470", (26, 70, 97, 16), (166, 90, 41), "#A65A29")
SUPPORTING_VIOLET = Color("667", (58, 63, 22, 3), (123, 105, 145), "#7B6991")

# Focal Area Colors
INTERNATIONAL_WATERS = Color("660", (91, 53, 0, 0), (0, 112, 185), "#0070B9") #One of main 5 colors
BIODIVERSITY_GREEN = Color("362", (78, 2, 98, 9), (38, 161, 70), "#26A146") #One of main 5 colors
CLIMATE_CHANGE = Color("145", (0, 58, 100, 8), (227, 124, 29), "#E37C1D")
CHEMICALS_WASTE = Color("612", (26, 24, 100, 0), (198, 178, 47), "#C6B22F")
LAND_DEGRADATION = Color("463", (30, 56, 100, 37), (128, 86, 27), "#80561B")

# Typography
MUSEO_WEIGHTS = ["100", "300", "500", "700", "900"]
MUSEO_SANS_WEIGHTS = ["100", "300", "500", "700", "900"]
HEEBO_WEIGHTS = ["THIN", "LIGHT", "REGULAR", "MEDIUM", "BOLD", "EXTRA BOLD", "BLACK"]