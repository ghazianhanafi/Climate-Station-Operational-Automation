#MOD WRITTEN BY: GHAZIAN_HANAFI
import os
import shutil
import arcpy
import pandas as pd

########## UBAH BAGIAN INI!!! ###########
#print("Tanggal Bulan Tahun: (contoh:20240113)")
#tanggal= input()
filename = "BlendGSMAP_POS.20240721.xls"
#TIDAK PERLU DOWNLOAD DATA CUKUP NYALAKAN VPN
#filename = f"BlendGSMAP_POS.{tanggal}.xls"
vars = ["CH"]#,"SH%","SHpercentil"]
prov = "PAPSEL"
print("JANGAN LUPA NYALAKAN VPN")
print("modified by: Ghazian_Hanafi")
print("kalau error jangan lupa nyalakan vpn")
##########setting idw##########
outgrid = "0.005"
power = "2"
ch_reclass = "-10000 1, 1;1 20, 2;20 50, 3;50 100, 4;100 150, 5;150 1000, 6"#;200 1000"#300 7;300 500 8;500 10000 9"
#ch_reclass = "-10000 1 1;-1 1 2;1 10 3;10 20 4;20 50 5;50 75 6;75 100 7;100 150 8;150 10000 9"
#sh_reclass = "-100000 30 1;30 50 2;50 85 3;85 115 4;115 150 5;150 200 6;200 100000 7"
#shp_reclass = "-100000 11 1;11 22 2;22 33 3;33 66 4;66 77 5;77 88 6;88 100 7"

##########set working directory##########
wd =  os.getcwd()+"\\"
map_dir = "E:\\BIMTEK_MERAUKE\\00_MASTERPETA\\"
tmpdir = wd+"temp\\"
mapdir = map_dir+"SHP\\"
indir = wd+"data_blend\\harian\\"
mxddir = wd+"mxd\\"

###### DOWNLOAD DATA #########
import ftplib
from ftplib import FTP
ftp=FTP('172.19.1.208')
un=**********
pw=**********
ftp.login(un,pw)
print("connect")
ftp.cwd('/Analisis_CH_BLENDING/Data_Analisis_Late_Perpulau/HARIAN/XLSX/')
ftp.retrbinary("RETR " +filename,open(filename,'wb').write)
ftp.quit()

shutil.move(wd+filename,indir+filename)

xlch = tmpdir+'temp.csv'
batas = pd.read_excel("BATAS_PROV.xlsx") 
idx = batas[batas['PROV']==prov]['NO'].item()-1
df = pd.read_excel(indir+filename)
dfU = pd.read_excel(wd+'ACHARG.xlsx')
dfx=pd.DataFrame()
dfx['LON']=dfU['LON']
dfx['LAT']=dfU['LAT']
dfx['CH']=dfU['CH']
dfx=dfx.dropna()
#df=pd.concat([df,dfx])
data = df[df['LON'].between(batas['LON1'][idx], batas['LON2'][idx]) & df['LAT'].between(batas['LAT1'][idx], batas['LAT2'][idx])]

#KOREKSI
for i,x,y in zip(dfx['CH'],dfx['LON'],dfx['LAT']):
        kore=data['CH'].loc[(data['LON']>x-0.05)&(data['LON']<x+0.05)&(data['LAT']>y-0.05)&(data['LAT']<y+0.05)]
        for ch in kore:
            if i > 0:
                data['CH'].loc[(data['CH']>ch-0.5)&(data['CH']<ch+0.5)&(data['CH']<ch+0.5)&(data['LON']>x-0.1)&(data['LON']<x+0.1)&(data['LAT']>y-0.1)&(data['LAT']<y+0.1)]=(i/ch)*data['CH'].loc[(data['CH']>ch-0.5)&(data['CH']<ch+0.5)&(data['LON']>x-0.1)&(data['LON']<x+0.1)&(data['LAT']>y-0.1)&(data['LAT']<y+0.1)]
            
             
data = data.to_csv(tmpdir+'temp.csv')

##########baca semua file########## BlendGSMAP_POS.202207dec01.xls
for var in vars:
	thn = filename[-12:-8]
	bln = filename[-8:-6]
	har = filename [-6:-4]
	##########buat folder output##########
	outdir = wd+"hasil\\harian\\"+thn+"."+bln+".har."+har+"\\"
	try:
		os.makedirs(outdir)
	except OSError:
		pass	
	##########buat judul##########
	if bln == "01" :
		mon = "JANUARI"
		monid = "JAN"
		month = "JANUARY"
	elif bln == "02" :
		mon = "FEBRUARI"
		month = "FEBRUARY"
		monid = "FEB"
	elif bln == "03" :
		mon = "MARET"
		month = "MARCH"
		monid = "MAR"
	elif bln == "04" :
		mon = "APRIL"
		month = "APRIL"
		monid = "APR"
	elif bln == "05" :
		mon = "MEI"
		month = "MAY"
		monid = "MEI"
	elif bln == "06" :
		mon = "JUNI"
		month = "JUNE"
		monid = "JUN"
	elif bln == "07" :
		mon = "JULI"
		month = "JULY"
		monid = "JUL"
	elif bln == "08" :
		mon = "AGUSTUS"
		month = "AUGUST"
		monid = "AGT"
	elif bln == "09" :
		mon = "SEPTEMBER"
		month = "SEPTEMBER"
		monid = "SEP"
	elif bln == "10" :
		mon = "OKTOBER"
		month = "OCTOBER"
		monid = "OKT"
	elif bln == "11" :
		mon = "NOVEMBER"
		month = "NOVEMBER"
		monid = "NOV"
	elif bln == "12" :
		mon = "DESEMBER"
		month = "DECEMBER"
		monid = "DES"
		
#	if har == "01" :
#		dekad = "I"
#	elif har == "02" :
#		dekad = "II"
#	elif das == "03":
#		dekad = "III"
		
	##########buat judul##########
	if prov == "TIMORLESTE" or prov == "PNG" or prov == "BRUNEI" or prov == "MALAYSIA":
		judulch = "RAINFALL ANALYSIS"+"\n"+"DEKAD "+har+" "+month+" "+thn+"\n"
		judulsh = "RAINFALL ANOMALY"+"\n"+"DEKAD "+har+" "+month+" "+thn+"\n"
	else :
		judulch = "AKUMULASI CURAH HUJAN"+"\n"+"HARIAN "+har+" "+mon+" "+thn+"\n"
		judulsh = "ANALISIS SIFAT HUJAN"+"\n"+"HARIAN "+har+" "+mon+" "+thn+"\n"
		
	##########
	arcpy.env.overwriteOutput =  True
	
	##########Local variables: ##########
	chlayer = tmpdir+"CH_Layer"
	idw = tmpdir+var
	shp = mapdir+"prov_indo.shp"
	prov_shp = mapdir+prov+".shp"
	if var=="CH":
		reclass_value=ch_reclass
		judul = judulch
		mxd_dir = mxddir+var.lower()+"\\harian\\"
		reclass = tmpdir+var+"_reclassdy"
	#elif var=="SH%":
	#	reclass_value=sh_reclass
	#	judul = judulsh
	#	var2 = var[:2].lower()
	#	mxd_dir = mxddir+var.lower()+"\\"
	#	reclass = tmpdir+var2+"_reclass"
	#elif var=="SHpercentil":
	#	reclass_value=shp_reclass
	#	judul = judulsh
	#	var2 = var[:3].lower()
	#	mxd_dir = mxddir+var.lower()+"\\"
	#	reclass = tmpdir+var2+"_reclass"
	
	##########Process: Make XY Event Layer##########
	print("Read : "+filename+" as "+var+" Layer")
	arcpy.MakeXYEventLayer_management(xlch, "lon", "lat", chlayer, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", var)

	##########Process: IDW##########
	arcpy.CheckOutExtension("spatial")
	tempEnvironment0 = arcpy.env.mask
	arcpy.env.mask = prov_shp
	arcpy.gp.Idw_sa(chlayer, var, idw, outgrid, power, "VARIABLE 12", "")
	arcpy.env.mask = tempEnvironment0

	##########Process: Reclassify CH##########
	arcpy.gp.Reclassify_sa(idw, "VALUE", reclass_value, reclass, "DATA")
	arcpy.CheckInExtension("spatial")
	
	##########export peta ch ke jpeg##########
	print("Export : "+var+"_"+prov+"_"+thn+"."+bln+"."+har+".jpg")
	mxd = arcpy.mapping.MapDocument (mxd_dir+prov+".mxd")
	mxd.title = (judul)
	arcpy.mapping.ExportToJPEG (mxd,outdir+var+"_"+prov+"_"+thn+"."+bln+"."+har+".jpg",resolution=200)
	
	#if prov=="PAPSEL":#MOD WRITTEN BY: GHAZIAN_HANAFI
	kabs = ["ASMAT","BOVEN_DIGOEL","MAPPI","MERAUKE","MIMIKA"]
	for kab in kabs:
		if var=="CH":
			extract_kab = tmpdir+"kab_chrec"
		elif var=="SH%":
			extract_kab = tmpdir+"kab_shrec"
		elif var=="SHpercentil":
			extract_kab = tmpdir+"kab_shprec"
		
		arcpy.env.overwriteOutput =  True
		#Masking CH Kabupaten
		kab_shp = map_dir + "SHP\\SHP_KAB\\"+kab+".shp"

		#Masking SH Kabupaten
		arcpy.gp.ExtractByMask_sa(reclass, kab_shp, extract_kab)
		arcpy.env.overwriteOutput =  True
		##########export peta sh ke jpeg##########
		#import arcpy
		print("Export : "+var+"_"+kab+"_"+thn+"."+bln+"."+har+".jpg")
		mxd = arcpy.mapping.MapDocument (mxd_dir+kab+".mxd")
		mxd.title = (judul)
		arcpy.mapping.ExportToJPEG (mxd,outdir+var+"_"+kab+"_"+thn+"."+bln+".har."+har+".jpg",resolution=200)
			
	
	###############-------------------------THE END----------------------------##################
#MOD WRITTEN BY: GHAZIAN_HANAFI
