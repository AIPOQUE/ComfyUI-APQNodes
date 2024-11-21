# ComfyUI APQNodes

## Introduction
Without fine-tuning, FLUX.1 Dev model cannot understand exact color codes. 
However, it is known that FLUX.1 Dev can repeatedly produce certain colors with certain prompt(color name). 
Fortunately, on CVITAI, [“novuschroma” shared 155 pre-tested color names](https://civitai.com/models/879997/color-wildcards-for-flux-and-sdxl) that FLUX.1 Dev can handle.
Thanks to his resource, color palette consists exclusively of 155 colors can be configured.
‘ColorPalette’ node from ComfyUI APQNodes converts input hex color code to pre-tested 155 color names of which FLUX.1 Dev is aware.


## Installation
Clone this repo into `custom_nodes` folder.


## Usage 
‘ColorPalette’ node consists of two inputs and two outputs.
![ColorPalette Node](https://github.com/AIPOQUE/ComfyUI-APQNodes/blob/main/src/ColorPalette_nodes_info.jpg)

* __Inputs__
    * __prompt__ : User text prompt
    * __hexcodes__ : any text hex color codes without any delimiter. For example,  #FF0000 #00FF00 #0000FF can generate color palette consisting of 3 colors(RED, BLUE, GREEN) 

* __Outputs__
    * __Prompt__ : Text prompt(User text prompt with color palettes applied) to connect to CLIP Text Encode.
    * __solor_palettes__ : Image of generated color palette
