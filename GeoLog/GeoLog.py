# Script to export information for a Excel borehole log
# Inputs: Excel file with the asbuilt information
# Outputs:
#   - csv file with the geographical coordinates
#   - csv file with the x,y,z coordinates
#   - kml file
#   - dxf file

import time
import pandas as pd
import simplekml
import ezdxf

geo = pd.read_excel('geo.xlsx')
geo_LATLON = pd.DataFrame([geo.BoreholeNumber, geo.LAT,geo.LON]).transpose()
geo_LATLON.to_csv('geoLATLON.csv', index = 0)
print("CSV file with the lat and lon coordinates created: geoLATLON.csv")

geo_xyz = pd.DataFrame([geo.BoreholeNumber, geo.ProjectEasting,geo.ProjectNorthing, geo.Elevation]).transpose()
geo_xyz.to_csv('geo_xyz.csv', index = 0, header = False)
print("CSV file with the x,y,z coordinates created: geo_xyz.csv")

kml = simplekml.Kml()
for borehole in geo.index:
    kml.newpoint(name=geo["BoreholeNumber"][borehole],
                 coords=[(geo["LON"][borehole],
                          geo["LAT"][borehole]
                          )
                         ]
                 )
kml.save("geo.kml")
print("KML file created: geo.kml")

data = pd.read_csv("geo_xyz.csv", names =['ID', 'X', 'Y', 'Z'])
doc = ezdxf.new('R12')
msp = doc.modelspace()
doc.layers.new('POINTS')
doc.layers.new('ID')
doc.layers.new('ELEVATIONS')

# DXF points will be created as linew of zero length
for point in data.index:
    msp.add_line((data["X"][point],data["Y"][point],data["Z"][point]),
                 (data["X"][point],data["Y"][point],data["Z"][point]),
                 dxfattribs={'layer': 'POINTS'})
    msp.add_text(data["ID"][point],
                 dxfattribs={
                     'style': 'STANDARD',
                     'layer': 'ID',
                     'height': 0.10}
                 ).set_pos((data["X"][point]+0.10,data["Y"][point]+0.10,data["Z"][point]),align='MIDDLE_LEFT')
doc.saveas('geo.dxf')
print("DXF file created: geo.dxf")

input(print("Push enter to end"))

# End of script

