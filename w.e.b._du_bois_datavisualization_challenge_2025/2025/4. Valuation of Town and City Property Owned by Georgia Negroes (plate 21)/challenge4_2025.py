# 4. DuBois_challenge_2025: VALUATION OF TOWN AND CITY PROPERTY OWNED BY GEORGIA NEGROES.

# IMPORT LIBRAIRIES
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#IMPORT DATA
df = pd.read_csv('https://raw.githubusercontent.com/ajstarks/dubois-data-portraits/refs/heads/master/challenge/2025/challenge04/data.csv')

#DATA PROCESSING
white_years = [1870, 1871, 1872, 1873, 1899]
df['Line color'] = df['Year'].apply(lambda x: 'White' if x in white_years else 'Black') # DEFINE LINE COLOR ACCORDING TO YEAR
df['Highlight'] = df['Year'].apply(lambda x: 'highlight_1870_1874' if x in highlight_years_1870_1874 else ('highlight_1899' if x in highlight_year_1899 else 'no'))

#DESIGN PART #1
fig, ax = plt.subplots(figsize=(12, 15)) # SIZE THE CHART
fig.patch.set_facecolor('oldlace') # OUTER COLOR
ax.set_facecolor('oldlace')  # INNER COLOR
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}")) # CORRECT MATPLOTLIB AUTOMATIC CONVERTING NUMBERS

#(MULTIPLE LINE)PLOT DATA
ax.plot(df['Year'], df['Property Valuation'], linewidth=7.5, color='black', alpha=1)

# PLOT OLDLACE LINE FOR YEARS 1870-1874
highlight_1870_1874_df = df[df['Highlight'] == 'highlight_1870_1874']
ax.plot(highlight_1870_1874_df['Year'], highlight_1870_1874_df['Property Valuation'], linewidth=3, color='oldlace', alpha=1)

# PLOT OLDLACE LINE FOR YEAR 1899
highlight_1899_df = df[df['Highlight'] == 'highlight_1899']
ax.plot(highlight_1899_df['Year'], highlight_1899_df['Property Valuation'], linewidth=3, color='oldlace', alpha=1)

#DESIGN PART #2
ax.minorticks_on()
ax.grid(True, which='major', linestyle=':', linewidth=0.5, color='red', alpha=0.7)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color='red', alpha=0.7)
ax.set_title("VALUATION OF TOWN AND CITY PROPERTY OWNED \nBY GEORGIA NEGROES.", fontsize=18, fontweight='bold')
ax.tick_params(colors='grey')
ax.spines['top'].set_color('grey') # SET GREY SPINES
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.spines['right'].set_color('grey')


#ADD ANNOTATIONS: KU-KLUXISM, POLITICAL UNREST, RISE OF \n    THE NEW \n    INDUSTRIALISM, LYNCHING, FINANCIAL PANIC, DISFRANCHISMENT \nAND PROSCRIPTIVE \nLAWS
ax.text( 0.11, 0.15, "KU-KLUXISM", fontsize=12, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=90)
ax.text( 0.24, 0.48, "POLITICAL\n  UNREST", fontsize=12, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text( 0.43, 0.85, "RISE OF\n  THE NEW\n  INDUSTRIALISM", fontsize=12, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text( 0.73, 0.32, "LYNCHING", fontsize=12, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text( 0.78, 0.19, "FINANCIAL PANIC", fontsize=12, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=90)
ax.text( 0.85, 0.5, "DISFRANCHISMENT \nAND \nPROSCRIPTIVE \nLAWS", fontsize=12, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text( -0.05, 1.01, "DOLLARS", fontsize=10, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
positions = [0.08, 0.12, 0.28, 0.32, 0.48, 0.52, 0.68, 0.72, 0.88, 0.92] # SET $ ANNOTATIONS
for pos in positions:
    ax.text(-0.05, pos, "$", fontsize=13, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="grey", rotation=0)
ax.text(0.5, 0.035, "matplotlib | #DuBoisChallenge2025 | nambo yang", fontsize=10, fontweight='light', fontname="Sans Serif", ha='center', va='top', transform=ax.transAxes, color="black") #SIGNATURE

plt.show()
