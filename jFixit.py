# AtomSoftTech
# Jason Lopez
# Create the sym-lib-table and fp-lib-table files needed for fresh install of KiCAD 6
# Copy the 2 generated files to : C:\Users\%USERNAME%\AppData\Roaming\kicad\6.0
import os

#change these 2 to the paths used for your install
symPath = "C:/Program Files/KiCad/6.0/share/kicad/symbols/"
fpPath = "C:/Program Files/KiCad/6.0/share/kicad/footprints/"

symDir = os.listdir(symPath)
fpDir = os.listdir(fpPath)

symFiles = []
fpFiles = []

symTable = "(sym_lib_table\n"
fpTable = "(fp_lib_table\n"

for file in symDir:
    if file.endswith(".kicad_sym"):
        name = file.split(".")
        symTable += '(lib (name "'+name[0]+'")(type "KiCad")(uri "'+symPath + file +'")(options "")(descr ""))\n'

symTable += ")"

for fpfile in fpDir:
    if fpfile.endswith(".pretty"):
        name = fpfile.split(".")
        fpTable += '(lib (name "'+name[0]+'")(type "KiCad")(uri "'+fpPath + fpfile +'")(options "")(descr ""))\n'

fpTable += ")"

f = open("sym-lib-table", "w")
f.write(symTable)
f.close()

fp = open("fp-lib-table", "w")
fp.write(fpTable)
fp.close()
