# a small script that downloads data from CITL: European Union Transaction Log
# into xml files that can be easily opened with MS Excel or other software

import mechanize
import sys
import os

folder = sys.argv[1]
os.system('mkdir ' + folder + 'downloaded_from_citl')

out_folder = folder + 'downloaded_from_citl/'

years = [str(y) for y in xrange(2005,2013)]

# list of countries as it appears in the previous page
# after selecting a period on the right dropdown list
# http://ec.europa.eu/environment/ets/allocationComplianceMgt.do?languageCode=en

country_dict = {'AT': 'Austria',
            'BE': 'Belgium',
            'BG': 'Bulgaria',
            'HR': 'Croatia',
            'CY': 'Cyprus',
            'CZ': 'Czech Republic',
            'DK': 'Denmark',
            'EE': 'Estonia',
            'EU': 'European Commission',
            'FI': 'Finland',
            'FR': 'France ',
            'DE': 'Germany',
            'GR': 'Greece',
            'HU': 'Hungary',
            'IS': 'Iceland',
            'IE': 'Ireland ',
            'IT': 'Italy ',
            'LV': 'Latvia',
            'LI': 'Liechtenstein',
            'LT': 'Lithuania',
            'LU': 'Luxembourg ',
            'MT': 'Malta',
            'NL': 'Netherlands',
            'NO': 'Norway',
            'PL': 'Poland',
            'PT': 'Portugal ',
            'RO': 'Romania',
            'SK': 'Slovakia',
            'SI': 'Slovenia',
            'ES': 'Spain',
            'SE': 'Sweden',
            'GB': 'United Kingdom'}

countries = [el for el in country_dict]


for country in countries:
    for year in years:
        
        # the country/year data export page can be opened directly on browser
        # without previously going through earlier forms
        
        url = ('http://ec.europa.eu/environment/ets/napYearInformation.do?' + 
               'languageCode=en&napId=13612&periodYear=%s&action=periodYear&' + 
               'installationId=&registryCode=%s&periodCode=1') % (year, country)

        filename = country + '_' + year + '.xml'
        print 'now downloading data to ' + filename
        br = mechanize.Browser()
        resp = br.open(url)

        # clicks the 'export' button
        
        br.select_form('nap')
        resp = br.click(type="submit", nr=1)
        resp = br.open(resp)

        # clicks the 'ok' button to download the xml file
        
        br.select_form('export')
        resp = br.click(type="submit", nr=0)
        resp = br.open(resp)
        
        # saves downloaded data to xml file
        
        data = resp.read()
        with open(out_folder + filename, 'w') as f: 
            f.write(data)
    
    
