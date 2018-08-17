import urllib2

def get_sat_NORAD(url):
	sat_NORAD = []
	name_data = urllib2.urlopen(url)
	for line in name_data:
		if "Planet Labs" in line:
			norad = line.split("	")[25]
			#norad = norad[25]
			print norad
	return sat_NORAD


def main():
	url = "https://s3.amazonaws.com/ucs-documents/nuclear-weapons/sat-database/8-10-18-update/UCS_Satellite_Database_officialname_5-1-2018.txt"
	get_sat_NORAD(url)



main()