# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView5 = GetActiveViewOrCreate('RenderView')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout3 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout3.SetSize(1429, 542)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView5
renderView5.CameraPosition = [-3.9776174286904245, -7.102087274628018, -4.3226465070574855]
renderView5.CameraFocalPoint = [3.3070151094405533, 1.8112155378442891, 0.3312803935621545]
renderView5.CameraViewUp = [0.7702041395359642, -0.3516410659139828, -0.5321035089195926]
renderView5.CameraParallelScale = 3.0634928440365132


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