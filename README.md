# Picademy Worksheets

This repository contains (most of) the worksheets that the Picademy@Google
teams have been using in their Picademy sessions. Each worksheet exists in its
own directory which contains:

* A print-ready (300+DPI) PDF of the worksheet which has a filename equivalent
  to the containing directory

* All source files required to construct the PDF. This usually consists of a
  Scribus source file (*.sla), a series of images (*.jpg, *.png), and Fritzing
  files used to generate wiring diagrams (*.fzz)

If you wish to contribute changes, please read [CONTRIBUTING][] for
instructions on setting up your workstation to work with the sheets.

## Contents

The following worksheets are currently defined in the repository:

|![][camera_thumb][camera_workshop][]|![][explorer_hat_thumb][explorer_hat_workshop][]|
|A workshop introducing the Pi's camera module and how to use it from Python in combination with GPIO components|A workshop introducing the Pimoroni Explorer HAT Pro, and how to use it from Python with LEDs and motors|
|![][gpio_thumb][gpio_workshop][]|![][minecraft_thumb][minecraft_workshop][]|
|A workshop introducing the Pi's GPIO ports and how to use them with LEDs and buttons from Scratch and Python|A workshop introducing Minecraft: Pi Edition, and how to communicate and manipulate the Minecraft world from Python|


[CONTRIBUTING]:          CONTRIBUTING.md

[camera_workshop]:       camera_workshop/camera_workshop.pdf
[explorer_hat_workshop]: explorer_hat_workshop/explorer_hat_workshop.pdf
[gpio_workshop]:         gpio_workshop/gpio_workshop.pdf
[minecraft_workshop]:    minecraft_workshop/minecraft_workshop.pdf

[camera_thumb]:          camera_workshop/thumbnail.png
[explorer_hat_thumb]:    explorer_hat_thumb/thumbnail.png
[gpio_thumb]:            gpio_workshop/thumbnail.png
[minecraft_thumb]:       minecraft_workshop/thumbnail.png
