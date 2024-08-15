# Roman Technical Information Repository

### Note: Most files here are either in a .yaml or .ecsv format. Either can be easily read in with Python3.
#### Yaml files can be read in with the [pyyaml packge](https://pyyaml.org). For more details, please see the [pyyaml documentation](https://pyyaml.org/wiki/PyYAMLDocumentation).
For example, here's how to read in the yaml file `MissionandObservatory.yaml` located in `roman-technical-information/data/Observatory/MissionandObservatoryTechnicalOverview/`:
```
# import the yaml package (installed via the pyyaml package)
import yaml

# read in the file
with open('MissionandObservatory.yaml', 'r') as file:
    # the data will be stored as the Python dictionary "Roman"
    Roman = yaml.safe_load(file)
    
# Roman is a Python dictionary
print(Roman)
print(Roman.keys())
print(Roman['Mission_and_Spacecraft_Parameters'])
print(Roman['Mission_and_Spacecraft_Parameters']['orbit'])
```

#### Ecsv (Enhanced Character-Separated Values) files can be read in with the [astropy package](https://www.astropy.org). For more details, please see [astropy's ecsv documentation](https://docs.astropy.org/en/stable/io/ascii/ecsv.html) and the [astropy example on reading Gaia ecsv files](https://docs.astropy.org/en/stable/io/ascii/read.html#reading-gaia-data-tables).
For example, here's how to read in the ecsv file `nominal_roll_angles_dec_1_observatory.ecsv` located in `roman-technical-information/data/Observatory/RollAngles/`: 
```
# You can use either Table or QTable, both of which are part of the astropy package
from astropy.table import Table
from astropy.table import QTable

# Read in the ecsv file
Roman = Table.read("nominal_roll_angles_dec_1_observatory.ecsv",format="ascii.ecsv")

# "Roman" is now an astropy data table (https://docs.astropy.org/en/stable/table/)
type(Roman)
dir(Roman)
print(Roman.keys())
print(Roman['Month'])
print(Roman['RA_sun'].unit)

# You can alternatively use QTable instead
Roman = QTable.read("nominal_roll_angles_dec_1_observatory.ecsv",format="ascii.ecsv")

```

# Included folders


| Folder name         | Description                                                               | Last Updated |
|---------------------|---------------------------------------------------------------------------|--------------|
| data                | Roman technical data on the Observatory, Orbit, and Wide Field Instrument | 2024-Aug-05  |
| notebooks           | Python Notebooks                                                          | 2021-Aug-26  |
| WideFieldInstrument | placeholder for now                                                       | TBD          |