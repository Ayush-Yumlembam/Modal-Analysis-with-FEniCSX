# trace generated using paraview version 5.13.2
# in Tools -> Start Trace
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get color transfer function/color map for 'real_u'
real_uLUT = GetColorTransferFunction('real_u')

# Rescale transfer function
real_uLUT.RescaleTransferFunction(3.6204913903024204e-13, 0.019916524362366177)

# get opacity transfer function/opacity map for 'real_u'
real_uPWF = GetOpacityTransferFunction('real_u')

# Rescale transfer function
real_uPWF.RescaleTransferFunction(3.6204913903024204e-13, 0.019916524362366177)

# Properties modified on real_uLUT

real_uLUT.NumberOfTableValues = 5 # change the nnumber here

# get 2D transfer function for 'real_u'
real_uTF2D = GetTransferFunction2D('real_u')

# get active view
renderView3 = GetActiveViewOrCreate('RenderView')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#-----------------------------------
# saving camera placements for views

renderView2 = GetActiveViewOrCreate('RenderView')
# layout/tab size in pixels
layout1.SetSize(1429, 542)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView2
renderView2.CameraPosition = [4.163666501339875, 7.159444948425433, -8.882615734215845]
renderView2.CameraFocalPoint = [2.7533558780137946, 0.25115758369284585, 1.3378765959383376]
renderView2.CameraViewUp = [0.8206782370432973, 0.41442762313695974, 0.3933662115949407]
renderView2.CameraParallelScale = 3.0634928440365132


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------