# Extreme-Climate-Early-Warning
In order to solve operational repetition every specific period of times, 
## 07_PERDINKMRK
my office need to put the early warning status on district level .shapefile, so i use python to do this repetitively in seamless way
Disclaimer: this just automation for extracting data from ECMWF output to district level shpfile, the real computation are in model process, the real thing that ive done are just:
1. labelling specific criteria
2. write it on shpfile
3. export shpfile
4. identify the area/district that need to be warn
## WRK000_IKROKMRK
our office having a monthly bulletin report about climate condition on our responsible administration area, one of the product is analyzing automatic weather station data, in order to easily do that, this is what my effort automating that task. 
1. agroclimate automatic weather station data cleaning
2. separate for monthly analysis
3. visualization (timeseries, piechart, windrose, histogram)
## ACH_GHZ
This script doing are:
1. automating download from specific ftp
2. doing arcgis interpolation and plot
3. save the plot into .jpg file
overall script is already written by somebody else, im just modified it the variable that being plotted and the download automation
## SPI_GHZ
1. automating download from specific ftp
2. doing arcgis interpolation and plot
3. save the plot into .jpg file
overall script is already written by somebody else, im just modified it the variable that being plotted and the download automation
## PCH
its always been my dream to do spatial plot mapping without using GIS apps like: arcgis or qgis. and today that dream comes true. thanks to my mentor in my organization that teach me,
how to do geospatial analyst using multiple interpolation, is gonna be usefull for me forever. what this script do is this step:
1. automating call data from google drive directory that have been prepared by HQ team
2. call the atribute that needed like sea raster, city shp, and district level shp
3. calculate IDW interpolation
4. set the colours into usual plot
5. spatial plot
