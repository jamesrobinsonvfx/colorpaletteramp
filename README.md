# Color Palette Ramp
A Houdini HDA that creates a ramp based on a color palette from an image.

# [Get the HDA](https://github.com/jamesrobinsonvfx/colorpaletteramp/raw/0.8.0/source/otls/jamesr_colorpaletteramp.hda)

*Compatible with __Houdini 18.0+__*

*You do not need to download the repo for the tool to work*.

Since the OTL is pretty straightforward, all the code lives inside the HDA. I
added all the Python/Vex/Help here because it's easier to track changes.

This node can be used on its own to create ramps to use elsewhere, or to modify
the color of the incoming geometry. It uses k-means clustering in Lab space to
group visually-similar colors into a set number of clusters, resulting in a
color palette from the input image.

If you are using a Houdini build < 18.0.460, and you are using an ACES workflow,
be sure to tick on "Convert Image to ACEScg Colorspace". If you are using
18.0.460+, this step is done for you.

* 18.0.460+ includes the [`hou.Color.ocio_activeDisplays()`](https://www.sidefx.com/docs/houdini/hom/hou/Color.html)
method. If you're using build 460 or later, the ACEScg toggle
will be automatically enabled for you if necessary according to
your OCIO environment.

[![Overview Video](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/vimeo_screenshot.png)](https://vimeo.com/423896113 "Color Palette Ramp Demo")

# Features

### Input Detection
Color Palette Ramp can take an input, but does not require one. You can use the
ramp all on its own if you want to channel reference it elsewhere from within
Houdini.

![Gif of adding/removing input](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/auto_input.gif)

### \# of Stops & HSV Sorting
You can control the number of swatches you want your ramp to have. 5 - 8 is
usually plenty!

Choose to sort by __Hue__, __Saturation__, __Value__, or nothing at all.

![Gif of sliding stops and sorting](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/stops_and_sort.gif)

### ACES Detection
__Color Palette Ramp__ detects your environment's OCIO settings, and automatically
enables sRGB -> ACEScg conversion.

![Gif of dropping the node down and checking the ACES box](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/aces_detect.gif)

### Luma Key
Key out luminance areas that don't interest you to avoid having too many overly
dark or bright swatches.

![Gif sliding the luminance min/max values](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/luma_keyer.gif)

### Clustering
#### VEX or Houdini Cluster SOP
Under the hood, the color clusters are calculated using the K-Means algorithm.
You can choose between a VEX implementation or the Houdini Cluster SOP. All
calculations are done in Lab space using [Delta E 76](http://zschuessler.github.io/DeltaE/learn/). In the future, this
would hopefully be changed to [Delta E 2000](http://zschuessler.github.io/DeltaE/learn/)

#### Optimization Tweaks
You have control over how accurate the resulting palette is. The defaults are
balanced between quality and speed, leaning a little more towards quality. You
can drastically downsample the incoming image and still get pretty good results.

![Gif of clustering settings](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/cluster_settings.gif)

### Output Colors Array
You can output the color swatches as a Detail Array attribute for use elsewhere.

![Image of Export Array Setting](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/export_array1.png)

![Image of wrangle using array](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/export_array2.png)

![Gif of particle system picking from the array](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/export_array3.gif)

### Ramp Updates Automatically
All changes to the ramp update automatically, so you don't need to press anything
extra. The ramp creation itself is not time-dependent, so inputting animated geometry should not incur much of a performance hit


### Help
* Help card and tooltips provided just like normal Houdini help.
* Embedded example (<kbd>RMB</kbd> > __Examples__)

![Gif of RMB Examples](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/master/docs/images/embedded_example.gif)


# Installation

At the repo root, there is a [Houdini
Package](https://www.sidefx.com/docs/houdini/ref/plugins.html) called
`colorpaletteramp.json`.
1. Copy this file to wherever you want to search for packages. Typically, this
   would be in `$HOUDINI_USER_PREF_DIR/packages`.
2. On line 4, change the value of `INSTALL_DIR` to be the folder containing the
   repo. In this case, it's just in my Downloads folder
3. Launch Houdini