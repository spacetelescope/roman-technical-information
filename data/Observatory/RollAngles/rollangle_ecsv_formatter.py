# Python3 script to convert a single text file of various roll and Sun angles into multiple machine-readable ecsv files
# Rob Zellem - August 2, 2024

import numpy as np
import pandas as pd
from astropy.table import Table
from astropy import units as u

obs_last_updated = "2024-June-03"
uv_last_updated = "2024-June-03"

obs_comments = ["Roman observatory roll angle and body axes to Sun angles for declination = ", " right ascension = 90 degrees."]
uv_comments = ["Roman unit vectors for Sun and normal to Solar Array/Sun Shield for declination = ", " right ascension = 90 degrees."]


df = pd.read_table("roman_nomroll_sunang_test.txt")

obs_RA_BA = {}
uv_Sun_SASS = {}

switch = 'comment'
for i in np.arange(np.shape(df.values)[0]):
    if "Observatory roll angle and body axes to Sun angles for declination" in df.values[i][0]:
        switch = 'obs'
        dec = df.values[i][0].split("=")[-1].strip()
        continue
    elif "Unit vectors for Sun and normal to Solar Array/Sun Shield" in df.values[i][0]:
        switch = 'uv'

    if switch == 'obs' and ("declination = " not in df.values[i][0]) and ("dec=" not in df.values[i][0]):
        if dec not in obs_RA_BA:
            obs_RA_BA[dec] = []
        obs_RA_BA[dec].append(df.values[i][0])

    if switch == 'uv' and ("Unit vectors" not in df.values[i][0]) and ("dec=" not in df.values[i][0]) and ("--" not in df.values[i][0]):
        if dec not in uv_Sun_SASS:
            uv_Sun_SASS[dec] = []
        uv_Sun_SASS[dec].append(df.values[i][0])

# Convert the strings into csv format
for i in obs_RA_BA.keys():
    for j in np.arange(np.shape(obs_RA_BA[i])[0]):
        if obs_RA_BA[i][j] == "Month  Day  RA_sun   DEC_sun  roll   x2sun  y2sun  z2sun  OK    roll   x2sun  y2sun  z2sun  OK":
            obs_RA_BA[i][j] = "Month  Day  RA_sun   DEC_sun  roll_pos   x2sun_pos  y2sun_pos  z2sun_pos  pitch_OK_pos    roll_neg   x2sun_neg  y2sun_neg  z2sun_neg  pitch_OK_neg"

        obs_RA_BA[i][j] = obs_RA_BA[i][j].split()

# Convert the strings into csv format
for i in uv_Sun_SASS.keys():
    for j in np.arange(np.shape(uv_Sun_SASS[i])[0]):
        if uv_Sun_SASS[i][j] == "Month  Day  RA_sun   DEC_sun    XSun     YSun     ZSun   roll     XSASS    YSASS    ZSASS   roll     XSASS    YSASS    ZSASS":
            uv_Sun_SASS[i][j] = "Month  Day  RA_sun   DEC_sun    XSun     YSun     ZSun   roll_pos     XSASS_pos    YSASS_pos    ZSASS_pos   roll_neg     XSASS_neg    YSASS_neg    ZSASS_neg"

        uv_Sun_SASS[i][j] = uv_Sun_SASS[i][j].split()

# Make double-nested dictionary
obs_RA_BA_dn = {}
uv_Sun_SASS_dn = {}

for i in obs_RA_BA.keys():
    for j in np.arange(np.shape(obs_RA_BA[i])[0]):
        if j == 0:
            obs_keys = obs_RA_BA[i][j]
            obs_RA_BA_dn[i] = {}
            for k in obs_RA_BA[i][j]:
                obs_RA_BA_dn[i][k] = []
        else:
            for (k,v) in zip(obs_keys, obs_RA_BA[i][j]):
                if v == 'yes':
                    obs_RA_BA_dn[i][k].append(True)
                elif v == 'no':
                    obs_RA_BA_dn[i][k].append(False)
                else:
                    obs_RA_BA_dn[i][k].append(float(v))

for i in uv_Sun_SASS.keys():
    for j in np.arange(np.shape(uv_Sun_SASS[i])[0]):
        if j == 0:
            uv_keys = uv_Sun_SASS[i][j]
            uv_Sun_SASS_dn[i] = {}
            for k in uv_Sun_SASS[i][j]:
                uv_Sun_SASS_dn[i][k] = []
        else:
            for (k,v) in zip(uv_keys, uv_Sun_SASS[i][j]):
                if v == 'yes':
                    uv_Sun_SASS_dn[i][k].append(True)
                elif v == 'no':
                    uv_Sun_SASS_dn[i][k].append(False)
                else:
                    uv_Sun_SASS_dn[i][k].append(float(v))

# Now convert everything to Qtables and save as ecsv
for i in obs_RA_BA_dn.keys():
    t = Table()
    for j in obs_keys:
        if (j == "Month") or (j == "Day"):
            t[j] = [int(k) for k in obs_RA_BA_dn[i][j]]
            if j == 'Month':
                t[j].description = 'Calendar month.'
            if j == 'Day':
                t[j].description = 'Calendar date.'

        elif j == "RA_sun":
            t[j] = [float(k) for k in obs_RA_BA_dn[i][j]] * u.deg
            t[j].description = 'Right ascension of the Sun.'
        elif j == "DEC_sun":
            t[j] = [float(k) for k in obs_RA_BA_dn[i][j]] * u.deg
            t[j].description = 'Declination of the Sun.'
        elif "roll" in j:
            t[j] = [float(k) for k in obs_RA_BA_dn[i][j]] * u.deg
            t[j].description = 'Roll angle for '+j.split("roll_")[-1]+". declination."
        elif "2sun" in j:
            t[j] = [float(k) for k in obs_RA_BA_dn[i][j]] * u.deg
            t[j].description = 'Body axes to Sun angle for '+j.split("_")[-1]+". declination."
        elif "pitch_OK" in j:
            t[j] = [bool(k) for k in obs_RA_BA_dn[i][j]]
            t[j].description = 'Denotes if the RA and DEC is (==True) or is not (==False) within the field of regard for ' + j.split("_")[-1] + ". declination."
        else:
            t[j] = [float(k) for k in obs_RA_BA_dn[i][j]] * u.deg

    t.meta['comments'] = obs_comments[0]+i+" degrees and"+obs_comments[-1]
    t.meta['last updated'] = obs_last_updated
    t.write('nominal_roll_angles_dec_'+str(int(float(i.split("+/-")[-1])))+'_observatory.ecsv', overwrite=True, delimiter=',')


for i in uv_Sun_SASS_dn.keys():
    t = Table()
    for j in uv_keys:
        if (j == "Month") or (j == "Day"):
            t[j] = [int(k) for k in uv_Sun_SASS_dn[i][j]]
            if j == 'Month':
                t[j].description = 'Calendar month.'
            if j == 'Day':
                t[j].description = 'Calendar date.'
        elif "roll" in j:
            t[j] = uv_Sun_SASS_dn[i][j] * u.deg
            if j == "roll_pos":
                t[j].description = 'Nominal roll angle for pos. declination.'
            if j == "roll_neg":
                t[j].description = 'Nominal roll angle for neg. declination.'
        elif (j in ["XSASS", "YSASS", "ZSASS"]):
            t[j] = uv_Sun_SASS_dn[i][j] * u.dimensionless_unscaled
            t[j].description = 'Unit vectors for normal to Solar Array/Sun Shield.'

        elif (j in ["XSun", "YSun", "ZSun"]):
            t[j] = [float(k) for k in uv_Sun_SASS_dn[i][j]] * u.dimensionless_unscaled
            t[j].description = 'Unit vectors for Sun.'

        else:
            t[j] = [float(k) for k in uv_Sun_SASS_dn[i][j]] * u.deg

            if "sun" in j:
                t[j].description = j.split("_sun")[0]+" of the Sun."

            if ("SASS" in j):
                t[j] = [float(k) for k in uv_Sun_SASS_dn[i][j]] * u.dimensionless_unscaled
                if "_pos" in j:
                    t[j].description = 'Unit vectors for normal to Solar Array/Sun Shield for pos. declination.'
                if "_neg" in j:
                    t[j].description = 'Unit vectors for normal to Solar Array/Sun Shield for neg. declination.'


    t.meta['comments'] = uv_comments[0]+i+" degrees and"+uv_comments[-1]
    t.meta['last updated'] = uv_last_updated
    t.write('nominal_roll_angles_dec_'+str(int(float(i.split("+/-")[-1])))+'_Sun_SASS.ecsv', overwrite=True, delimiter=',')
