
__author__ = 'Tom Van den Eede'
__copyright__ = 'Copyright 2018, Palette2 Splicer Post Processing Project'
__credits__ = ['Tom Van den Eede',
               'Tim Brookman'
               ]
__license__ = 'GPL'
__version__ = '3.0.0'
__maintainer__ = 'Tom Van den Eede'
__email__ = 'P2PP@pandora.be'
__status__ = 'Beta'


#########################################
# Variable default values
#########################################

# Filament Transition Table
paletteInputsUsed = [False,
                     False,
                     False,
                     False]

filamentType = ["",
                "",
                "",
                ""]

filamentDescription = ["Unnamed",
                       "Unnamed",
                       "Unnamed",
                       "Unnamed"]
filamentColorCode = ["-",
                     "-",
                     "-",
                     "-"]

usedFilamentTypes = []

defaultSpliceAlgorithm = "D000 D000 D000"
processWarnings = []
spliceAlgorithmTable = []
spliceAlgorithmDictionary = {}

printerProfileString = ''  # A unique ID linked to a printer configuration profile in the Palette 2 hardware.

inputGcode = []
processedGCode = []  # final output array with Gcode

# these  variables are used to build the splice information table (Omega-30 commands in GCode) that will drive the Palette2
# spliceoffset allows for a correction of the position at which the transition occurs.   When the first transition is scheduled
# to occur at 120mm in GCode, you can add a number of mm to push the transition further in the purge tower.  This serves a similar
# function as the transition offset in chroma
splice_offset = 0
spliceExtruderPosition = []
spliceUsedTool = []
spliceLength = []

# SIDE WIPES
side_wipe_loc = ""
side_wipe = False
side_wipe_length = 0
side_wipe_skip = False
defineTower = False
sideWipeMinY = 25
sideWipeMaxY = 175
maxWipe = -1

before_sidewipe_gcode = []
after_sidewipe_gcode = []

bed_size_x = 250
bed_size_y = 220
bed_origin_x = 0
bed_origin_y = -10.00   #eccount for the purge line at the start of the print

wipe_tower_info = {'minx': 9999,
                   'miny': 9999,
                   'maxx': -9999,
                   'maxy': -9999
                   }

wipetower_posx = 0
wipetower_posy = 0

currentPositionX = 0
currentPositionY = 0

# ping text is a text variable to store information about the PINGS generated by P2PP.   this information is pasted after
# the splice information right after the Palette2 header
pingExtruderPosition = []


# Hotswapcount is the number of hotswaps generated during the print.... not sure what this is used for, this variable is
# only used to complete the header
hotSwapCount = 0

# TotalExtrusion keeps track of the total extrusion in mm for the print taking into account the Extruder Multiplier set
# in the GCode settings...
totalMaterialExtruded = 0

# The next 3 variables are used to generate pings.   A ping is scheduled every ping interval.  The LastPing option
# keeps the last extruder position where a  ping was generated.  It is set to -100 to pring the first PING forward...
# Not sure this is a good idea.   Ping distance increases over the print in an exponential way.   Each ping is 1.03 times
# further from the previous one.   Pings occur in random places!!! as the are non-intrusive and don't causes pauses in the
# print they aren ot restricted to the wipe tower and they will occur as soon as the interval length for ping is exceeded.
lastPingExtruderPosition = 0
pingIntervalLength = 350
maxPingIntervalLength = 3000
pingLengthMultiplier = 1.03
sidewipecorrection=1.0
sidewiperetract = 0.4
correctWipeRetract = False
wipeRetracted = False
mmu_unload_remove = False
volumetricE = False


# currenttool/lastLocation are variables required to generate O30 splice info.   splice info is generated at the end of the tool path
# and not at the start hence the requirement to keep the toolhead and lastlocation to perform the magic
currentTool = -1
previousToolChangeLocation = 0

currentLayer = "No Layer Info"  # Capture layer information for short splice texts
extrusionMultiplier = 1.0  # Monitors M221 commands during the print.
currentprintFeedrate = 100  # Monitors the current feedrate
currentprintFeed = 2000
extraRunoutFilament = 150 # Provide extra filament at the end of the print.
minimalSpliceLength = 80  # Minimum overall splice length.
minimalStartSpliceLength = 100  # Minimum first splice length.
withinToolchangeBlock = False  # keeps track if the processed G-Code is part of a toolchange or a regular path.
allowFilamentInformationUpdate = False  # TBA

