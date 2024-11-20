import numpy as np
import torch
from PIL import Image, ImageDraw

class ColorPalette:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "prompt": ("STRING", {"multiline": False, "default": "Hello", "forceInput":True}),
            "hexcodes": ("STRING", {"multiline": False, "default": "World", "forceInput":True}),}
        }

    RETURN_TYPES = ("STRING", "IMAGE",)
    RETURN_NAMES = ("prompt", "color_palettes",)
    FUNCTION = "color_picker"
    CATEGORY = "APQNodes/Color"
    def color_picker(self, prompt, hexcodes):
        splited = hexcodes.split("#")
        treated = []
        for i in splited:
            ii = i.replace("\n", "").strip()
            if len(i)>0:
                treated.append(ii)
        closest_color = []
        color_list_final = ""
        color_list = [[(250, 112, 96), ['coral', '#FA7060']], [(173, 176, 176), ['gray', '#ADB0B0']], [(251, 211, 150), ['sepia', '#FBD396']], [(247, 208, 149), ['buff', '#F7D095']], [(254, 198, 165), ['peach', '#FEC6A5']], [(103, 1, 6), ['maroon', '#670106']], [(252, 252, 251), ['white', '#FCFCFB']], [(53, 208, 66), ['may green', '#35D042']], [(164, 65, 28), ['cocoa', '#A4411C']], [(248, 7, 24), ['carmine', '#F80718']], [(21, 226, 229), ['cyan', '#15E2E5']], [(152, 233, 188), ['celadon', '#98E9BC']], [(6, 152, 226), ['yinmn blue', '#0698E2']], [(0, 30, 92), ['indigo', '#001E5C']], [(168, 167, 165), ['nickel', '#A8A7A5']], [(0, 129, 206), ['dodgerblue', '#0081CE']], [(254, 83, 159), ['hot pink', '#FE539F']], [(0, 27, 69), ['navy blue', '#001B45']], [(8, 177, 233), ['blue', '#08B1E9']], [(250, 194, 126), ['sandy brown', '#FAC27E']], [(1, 94, 162), ['savoy blue', '#015EA2']], [(253, 196, 123), ['tan', '#FDC47B']], [(88, 251, 41), ['spring green', '#58FB29']], [(241, 119, 1), ['amber', '#F17701']], [(91, 100, 4), ['olive green', '#5B6404']], [(102, 0, 111), ['plum purple', '#66006F']], [(187, 9, 103), ['mulberry', '#BB0967']], [(134, 15, 110), ['eggplant', '#860F6E']], [(210, 143, 250), ['wisteria purple', '#D28FFA']], [(254, 246, 114), ['lemon chiffon', '#FEF672']], [(254, 182, 132), ['melon', '#FEB684']], [(254, 180, 5), ['yellow orange', '#FEB405']], [(121, 0, 85), ['aubergine', '#790055']], [(251, 118, 0), ['orange', '#FB7600']], [(173, 0, 37), ['amaranth', '#AD0025']], [(254, 215, 174), ['bisque', '#FED7AE']], [(5, 9, 12), ['ebony', '#05090C']], [(249, 88, 143), ['deep pink', '#F9588F']], [(133, 0, 24), ['burgundy', '#850018']], [(224, 40, 1), ['rust', '#E02801']], [(246, 111, 3), ['persimmon', '#F66F03']], [(0, 87, 192), ['prussian blue', '#0057C0']], [(221, 142, 19), ['brass', '#DD8E13']], [(147, 25, 199), ['purple', '#9319C7']], [(93, 155, 192), ['blue gray', '#5D9BC0']], [(248, 105, 133), ['puce', '#F86985']], [(6, 197, 107), ['caribbean green', '#06C56B']], [(250, 114, 11), ['burnt sienna', '#FA720B']], [(25, 123, 41), ['hunter green', '#197B29']], [(188, 74, 5), ['russet', '#BC4A05']], [(196, 158, 106), ['khaki', '#C49E6A']], [(228, 191, 249), ['lilac', '#E4BFF9']], [(4, 177, 111), ['jade', '#04B16F']], [(0, 29, 76), ['midnight blue', '#001D4C']], [(70, 78, 83), ['slate gray', '#464E53']], [(254, 203, 5), ['goldenrod', '#FECB05']], [(15, 18, 22), ['charcoal', '#0F1216']], [(209, 210, 210), ['silver', '#D1D2D2']], [(20, 197, 176), ['teal', '#14C5B0']], [(0, 145, 74), ['emerald green', '#00914A']], [(165, 45, 215), ['violet', '#A52DD7']], [(146, 229, 249), ['powder blue', '#92E5F9']], [(99, 244, 237), ['aquamarine', '#63F4ED']], [(148, 0, 30), ['claret', '#94001E']], [(254, 230, 106), ['honeydew', '#FEE66A']], [(27, 207, 226), ['cerulean', '#1BCFE2']], [(218, 191, 247), ['lavender', '#DABFF7']], [(254, 218, 3), ['cadmium yellow', '#FEDA03']], [(136, 0, 12), ['oxblood', '#88000C']], [(229, 176, 29), ['gold', '#E5B01D']], [(146, 20, 180), ['amethyst purple', '#9214B4']], [(254, 165, 119), ['rosegold', '#FEA577']], [(241, 11, 134), ['magenta', '#F10B86']], [(203, 0, 3), ['venetian red', '#CB0003']], [(0, 95, 197), ['ultramarine blue', '#005FC5']], [(155, 252, 199), ['mint green', '#9BFCC7']], [(38, 184, 75), ['persian green', '#26B84B']], [(254, 132, 3), ['tangerine orange', '#FE8403']], [(134, 92, 38), ['bronze', '#865C26']], [(29, 31, 40), ['onyx', '#1D1F28']], [(1, 1, 1), ['black', '#010101']], [(105, 226, 252), ['sky blue', '#69E2FC']], [(90, 224, 183), ['sea green', '#5AE0B7']], [(215, 108, 119), ['mauve', '#D76C77']], [(16, 159, 215), ['pacific blue', '#109FD7']], [(81, 49, 228), ['blue violet', '#5131E4']], [(0, 92, 214), ['royal blue', '#005CD6']], [(254, 188, 5), ['saffron', '#FEBC05']], [(252, 222, 0), ['yellow', '#FCDE00']], [(240, 98, 18), ['umber', '#F06212']], [(254, 171, 199), ['pink', '#FEABC7']], [(254, 177, 113), ['apricot', '#FEB171']], [(107, 33, 8), ['chocolate', '#6B2108']], [(244, 239, 228), ['linen', '#F4EFE4']], [(147, 0, 32), ['wine', '#930020']], [(93, 0, 81), ['plum', '#5D0051']], [(162, 254, 16), ['lime green', '#A2FE10']], [(253, 228, 198), ['blanched almond', '#FDE4C6']], [(159, 221, 176), ['sage', '#9FDDB0']], [(157, 25, 2), ['mahogany', '#9D1902']], [(84, 196, 254), ['cornflower blue', '#54C4FE']], [(254, 187, 0), ['turmeric', '#FEBB00']], [(94, 0, 113), ['tyrian purple', '#5E0071']], [(43, 241, 220), ['turquoise', '#2BF1DC']], [(222, 187, 149), ['taupe', '#DEBB95']], [(252, 49, 6), ['carnelian', '#FC3106']], [(254, 192, 195), ['blush', '#FEC0C3']], [(138, 229, 250), ['alice blue', '#8AE5FA']], [(81, 39, 11), ['pullman brown', '#51270B']], [(0, 56, 176), ['lapis lazuli', '#0038B0']], [(254, 193, 50), ['aureolin', '#FEC132']], [(199, 103, 40), ['saddlebrown', '#C76728']], [(254, 66, 7), ['orange red', '#FE4207']], [(254, 205, 23), ['maize', '#FECD17']], [(0, 73, 202), ['cobalt blue', '#0049CA']], [(200, 88, 23), ['chestnut', '#C85817']], [(254, 230, 107), ['cornsilk', '#FEE66B']], [(112, 0, 180), ['royal purple', '#7000B4']], [(231, 86, 28), ['copper', '#E7561C']], [(252, 96, 41), ['terra cotta', '#FC6029']], [(211, 0, 0), ['scarlet', '#D30000']], [(225, 0, 0), ['red', '#E10000']], [(252, 240, 211), ['cream', '#FCF0D3']], [(233, 0, 1), ['vermilion', '#E90001']], [(182, 61, 205), ['rebecca purple', '#B63DCD']], [(138, 238, 236), ['robin egg blue', '#8AEEEC']], [(254, 239, 208), ['vanilla', '#FEEFD0']], [(252, 141, 41), ['sienna', '#FC8D29']], [(254, 66, 119), ['cerise', '#FE4277']], [(250, 238, 220), ['alabaster', '#FAEEDC']], [(160, 237, 254), ['baby blue', '#A0EDFE']], [(250, 225, 187), ['beige', '#FAE1BB']], [(243, 35, 138), ['jazzberry jam', '#F3238A']], [(254, 174, 195), ['carnation pink', '#FEAEC3']], [(164, 246, 229), ['seafoam', '#A4F6E5']], [(246, 148, 2), ['ochre', '#F69402']], [(249, 125, 77), ['salmon', '#F97D4D']], [(2, 171, 65), ['viridian', '#02AB41']], [(254, 217, 158), ['sand', '#FED99E']], [(254, 81, 17), ['rufous', '#FE5111']], [(248, 240, 211), ['ivory', '#F8F0D3']], [(179, 111, 205), ['heliotrope', '#B36FCD']], [(248, 247, 238), ['antique white', '#F8F7EE']], [(13, 89, 132), ['slate blue', '#0D5984']], [(254, 200, 60), ['citrine', '#FEC83C']], [(159, 165, 168), ['ash gray', '#9FA5A8']], [(153, 71, 12), ['brown', '#99470C']], [(150, 188, 250), ['periwinkle', '#96BCFA']], [(55, 223, 66), ['green', '#37DF42']], [(254, 159, 54), ['caramel', '#FE9F36']], [(210, 254, 20), ['yellow green', '#D2FE14']], [(185, 254, 0), ['chartreuse', '#B9FE00']], [(194, 0, 0), ['crimson', '#C20000']], [(249, 184, 0), ['mustard', '#F9B800']], [(254, 240, 27), ['lemon yellow', '#FEF01B']]]

        for hex in treated:
            res = [[999, ["comparison_color", "FFFFFF"]]]
            value = hex.lstrip("#")
            lv = len(value)
            rgb = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
            for i in color_list:
                reading_r, reading_g, reading_b = i[0][0], i[0][1], i[0][2]
                gap = abs(reading_r - rgb[0]) + abs(reading_g - rgb[1]) + abs(reading_b - rgb[2])
                if res[-1][0] > gap:
                    res.append([gap, i[1]])
            closest_color.append(res[-1])
            color_list_final += res[-1][1][0]+", "
        numofcolors = len(closest_color)
        restriction_statement = f"The colors are restricted to following {numofcolors} colors: {color_list_final}"
        text_out = prompt + "\n" + restriction_statement
        image_width = 64*numofcolors
        image_height = 64
        background_color = "#ffffff"
        canvas = Image.new("RGBA", (image_width, image_height), background_color)
        draw = ImageDraw.Draw(canvas)
        for i in range(numofcolors):
            draw.rectangle([(64*i, 0), (64*(i+1), 64)], fill=(closest_color[i][1][1]))
        image_out = torch.from_numpy(np.array(canvas).astype(np.float32) / 255.0).unsqueeze(0)
        return (text_out, image_out)
