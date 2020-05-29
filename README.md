# Color Palette Ramp
A Houdini HDA that creates a ramp based on a color palette from an image using
k-means clustering.

## [Get the HDA](https://github.com/jamesrobinsonvfx/colorpaletteramp/raw/0.3.0/source/otls/bin/jamesr_colorpaletteramp.hda)

Since the OTL is pretty straightforward, all the Python code lives in the
``Scripts`` section on the HDA itself. It's also included here in the
``Python2.7libs`` directory.

The VEX code is also included, but lives on the wrangles themselves also.

Compatible with __Houdini 18.0__

# Usage Examples

See this video for a quick rundown on how it works.

# Features

#### Input Detection
Color Palette Ramp can take an input, but does not require one. You can use the
ramp all on its own if you want to channel reference it elsewhere from within
Houdini.

![Gif of adding/removing input](https://github.com/jamesrobinsonvfx/colorpaletteramp/blob/gifs/docs/images/auto_input.gif)

#### \# of Stops

#### HSV Sorting

#### ACES Detection

#### K-Means clustering: VEX or Houdini Cluster SOP

#### Output Colors Array

#### Ramp Updates Automatically


#### Help
* Help card and tooltips provided just like normal Houdini help.
* Embedded example (<kbd>RMB</kbd> > __Examples__)



