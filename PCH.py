import xarray as xr
import pandas as pd
import geopandas as gpd
#from google.colab import drive
import os
import rasterio
import cartopy

#drive.mount('/content/drive/',force_remount=True)
#wdir = '/content/drive/My Drive/00_MAPBMKG/'
wdir = '/Users/developer/Library/CloudStorage/GoogleDrive-ghazianhanafi35@gmail.com/My Drive/00_MAPBMKG/'
shpdir = wdir+'basemap/temp_dir/'
shpkcdir = wdir+'basemap/tempkecs_dir/'
shpfile="Indonesia.shp"
shpkecfile="/kecshppapsel.shp"
#shpkecfile="Batas_Kecamatan_BIG.shp"
papselfile="/kabshppapsel.shp"

local_dir = shpdir+"lokaldir"
#if not os.path.exists(local_dir):
#    os.makedirs(local_dir)


#print(os.listdir(shpdir))
kabshp=gpd.read_file(shpdir+shpfile)
papselkecshp=gpd.read_file(local_dir+shpkecfile)
#papselkecshp=gpd.read_file(shpkcdir+shpkecfile)
#papselkecshp=kecshp[kecshp["WADMKK"].isin(["MERAUKE",'ASMAT','BOVEN DIGOEL',"DEIYAI","DOGIYAI",'MIMIKA','MAPPI','NDUGA'])]
#papselkecshp=papselkecshp[papselkecshp["WADMKK"].isin(["Merauke",'Asmat','Boven Digoel',"Deiyai","Dogiyai",'Mimika','Mappi','Nduga'])]
#print(papselkecshp["WADMKK"])
#papselkecshp.to_file(f'{local_dir}/kecshppapsel.shp', driver='ESRI Shapefile')
papselshp=gpd.read_file(local_dir+papselfile)
pathlaut=wdir+'basemap/basemap/LAUT/'

laut=pathlaut+"HGT.tif"
raster=rasterio.open(laut)
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import cartopy.crs as ccrs
from rasterio.plot import show
import numpy as np

# Load shapefile and raster data
# (Assume malpapx and raster are already loaded as in your original code)


# Filter for Papua Selatan
provpap = papselshp
minx, miny, maxx, maxy = provpap.total_bounds

# Map colors and fill NaNs with a default color (e.g., grey)
#default_color = '#808080'  # Grey color for unmatched entries
#malpapx['color'] = malpapx['Model'].map(color_mapping).fillna(default_color)

# Set up the plot with cartopy projection
fig, ax = plt.subplots(figsize=(16, 24), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot the raster data
show(raster, ax=ax, cmap='Blues_r', transform=raster.transform)

# Add labels for each geometry based on the "Nama ZOM" column
for idx, row in provpap.iterrows():
    # Get the centroid of the geometry to place the label
    centroid = row['geometry'].centroid
    # Annotate the map with the label
    ax.annotate(row['KABUPATEN'], xy=(centroid.x, centroid.y), xytext=(0, 0),
                textcoords="offset points", fontsize=8, color='black', weight='bold',)
for idx, row in papselkecshp.iterrows():
    # Get the centroid of the geometry to place the label
    centroid = row['geometry'].centroid
    # Annotate the map with the label
    ax.annotate(row['WADMKC'], xy=(centroid.x, centroid.y), xytext=(0, 0),
                textcoords="offset points", fontsize=5, color='black', )
    #texts.append(ax.text(centroid.x, centroid.y, row['WADMKC'], fontsize=5, color='black'))
#adjust_text(texts, ax=ax)

# Create legend elements for models (colored squares)
#legend_patches = [Patch(facecolor=color, edgecolor='white', label=model) for model, color in color_mapping.items()]

# Create legend elements for boundaries (lines)
#legend_lines = [
#    Line2D([0], [0], color='red', lw=1, label='Batas Negara'),
#    Line2D([0], [0], color='black', lw=1, label='Batas Kabupaten'),
#    Line2D([0], [0], color='red', lw=1, linestyle='--', label='Batas Provinsi')]

# Combine both lines and patches for the legend
#legend_elements = legend_patches + legend_lines

# Create the legend
#legend = ax.legend(handles=legend_elements, title='Klasifikasi dan Keterangan', bbox_to_anchor=(1.00, 0.7), loc='upper left', borderaxespad=0.5)

# Adjust the x and y limits
ax.set_xlim(np.round(minx, 1) - 0.15, np.round(maxx, 1) + 0.0)
ax.set_ylim(np.round(miny, 1) - 0.15, np.round(maxy, 1) + 0.15)

# Set axis labels and titles
#ax.set_title('Prediksi Musim Kemarau 2024 - Awal Musim Kemarau Wilayah Papua Selatan', fontsize=14, fontweight='bold')

# Customize gridlines and labels
gridlines = ax.gridlines(draw_labels=True, linewidth=0.5)
gridlines.left_labels = True
gridlines.right_labels = False
gridlines.top_labels = False
gridlines.bottom_labels = True

# Adjust the plot to make room for the legend
#plt.subplots_adjust(right=0.8)


from datetime import datetime, timedelta, date
from datetime import date
#Panggil Data CSV/Xlsx
patheccoba = wdir+f'data/DATA_ECMWF/DASARIAN_COR/'

cek=[]
for entry in os.scandir(patheccoba):
  i=entry.stat().st_mtime_ns
  cek.append(i)
wes=max(cek)
for iy,w in zip(os.scandir(patheccoba),os.listdir(patheccoba)):
  x=iy.stat().st_mtime_ns
  if x==wes:
    print(f'inilah endgame:{w[:-9]}')
    folder=f"{w[:-9]}"

#folder=f"{w[:-9]}"

pathecmwfds = wdir+f'data/DATA_ECMWF/DASARIAN_COR/{folder}_dasarian/CSV/'
cok=[]
for entry in os.scandir(pathecmwfds):
  i=entry.stat().st_mtime_ns
  cok.append(i)
wes=max(cok)
for iy,wi in zip(os.scandir(pathecmwfds),os.listdir(pathecmwfds)):
  x=iy.stat().st_mtime_ns
  #if x==wes:
    #print(f'inilah endgame:{wi[:-9]}')
txt=date.today().day-1
te=[]
if txt<10:
  te="das.2"
elif txt>20:te="das.1"
else: te="das.3"
fil=""
if txt<10:fil=folder[:-2]
elif txt>20:fil=f"{datetime.today().year}.{str(datetime.today().month+1).zfill(2)}."
else: fil=folder[:-2]

csvfile=f'pch_det.{fil}{te}_ver_{folder}.csv'
probcsvfile=f'pch_prob.{fil}{te}_ver_{folder}.csv'
print(csvfile)


#Interpolasi
# Mengimpor library/package yang diperlukan
from pyinterpolate import inverse_distance_weighting as IDW
import rioxarray

dfprov=pd.read_csv(pathecmwfds+csvfile)
dfprob=pd.read_csv(pathecmwfds+probcsvfile)
# Menentukan target grid yang akan diinterpolasi
minx, miny, maxx, maxy = provpap.total_bounds
grid_space = 0.1
x_grid = np.arange(np.round(minx,1)-0.02, np.round(maxx,1)+0.02, grid_space)
y_grid = np.arange(np.round(miny,1)-0.02, np.round(maxy,1)+0.02, grid_space)
grid_lon, grid_lat = np.meshgrid(x_grid, y_grid)
#
## Menentukan data yang akan diinterpolasi
dfprov=dfprov[(dfprov["LON"]>minx)&(dfprov["LON"]<maxx)&(dfprov["LAT"]>miny)&(dfprov["LAT"]<maxy)]
dfprob=dfprob[(dfprob["LON"]>minx)&(dfprob["LON"]<maxx)&(dfprob["LAT"]>miny)&(dfprob["LAT"]<maxy)]
dfprov.to_csv(f"{csvfile[:-4]}_papsel.csv")


#--------------------------------------------------
#known_points = dfprov[['LAT', 'LON','VAL']].to_numpy()
known_points = dfprob[['LAT', 'LON','b50']].to_numpy()
#--------------------------------------------------



# Interpolasi IDW pada target grid
print("INTERPOLASI...")
idw = np.zeros(grid_lat.shape)
for i in range(len(y_grid)):
  for j in range(len(x_grid)):
    idw[i,j] = IDW(known_points, [y_grid[i],x_grid[j]], number_of_neighbours=9, power=2.0)
shp_crs=provpap.crs
grid_lat.shape, idw.shape
import xarray as xr
print("CLIPPING....")
# Menyimpan hasil interpolasi kedalam xarray dataarray
data_array = xr.DataArray(idw, coords={'lat': y_grid,'lon': x_grid},
                          dims=['lat', 'lon'])
data_array = data_array.rio.set_spatial_dims("lon", "lat", inplace=True)
data_array = data_array.rio.write_crs(shp_crs)
clipped_data = data_array.rio.clip(provpap.geometry)
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import rioxarray
# Menampilkan hasil masking
# Membuat custom colormap (warna bmkg)
#levels = [0,20,50,100,150,200,300,400,500,1000]
levels = [0,10,20,50,75,100,150,200,300,1000]#,'#EBE100'
levelsprob = [0,10,20,30,40,50,60,70,80,90,100]#,'#EBE100'
color = ['#681109','#9C4019','#D45725','#F3AE3D','#FFFF54','#BDFD50','#7CE344','#7CA631','#267300']
colorprob = ['#FEFFFC','#0101FA','#387FEE','#74FAF6','#9EFA8D','#FEFC55','#F5CE46','#E98939','#C8552B','#941E14']
custom_cmap = mcolors.ListedColormap(color)
custom_cmab = mcolors.ListedColormap(colorprob)
norm = mcolors.BoundaryNorm(levels, custom_cmap.N)
normp = mcolors.BoundaryNorm(levelsprob, custom_cmab.N)
# Manggambar hasil interpolasi yg telah di masking ke Provinsi terpilih
kabshp.plot(ax=ax,  edgecolor='black', linewidth=0.4, snap=False, color='gray')#color=provpap['color'],


#--------------------------------------------------
clipped_data.plot(ax=ax, levels=levelsprob, norm=normp, cmap=custom_cmab, zorder=1,add_colorbar=False)
#clipped_data.plot(ax=ax, levels=levels, norm=norm, cmap=custom_cmap, zorder=1,add_colorbar=True)
#--------------------------------------------------



papselkecshp.plot(ax=ax,  edgecolor='black', linewidth=0.3, snap=False, color='none')#color=provpap['color'],
provpap.plot(ax=ax,  edgecolor='black', linewidth=0.5, snap=False, color='none',aspect='auto')#color=provpap['color'],
#ax.set_aspect('equal', adjustable='box') 
#plt.savefig(f'{probcsvfile}.png',bbox_inches='tight', dpi=500)
#plt.savefig(f'{csvfile}.png',bbox_inches='tight', dpi=500)

#PLOT LOGO BMKG
import matplotlib.image as mpimg
img_path=wdir+"atribut/"
img = mpimg.imread(img_path+"Picture1.png")
#img_position = [0.23, 0.13, 0.1, 0.1]  # [left, bottom, width, height] in figure coordinates
img_position = [0.9, 0.13, 0.1, 0.1]  # [left, bottom, width, height] in figure coordinates
img_ax = fig.add_axes(img_position, zorder=3)  # zorder ensures it's on top of other elements

# Display the image
img_ax.imshow(img)
#ax.imshow(img,zorder=3)
img_ax.axis('off')
ax.set_title("")
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
plt.show()

#probcsvfile
