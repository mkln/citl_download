# convert all files to csv
# requires xmlutils
# 
# pip install xmlutils

import os
import sys

source_folder = sys.argv[1]
out_folder = sys.argv[2]

inside_folder = os.listdir(out_folder)

years = [str(y) for y in xrange(2005,2013)]

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
        
        filename = '%s_%s.csv' % (country, year)
        
        input_file = source_folder + '%s_%s.xml' % (country, year)
        output_file = out_folder + filename
        
        print 'converting ' + input_file
        
        if not filename in inside_folder:
            command_to_exec = 'xml2csv --input %s --output %s --tag "allocationTableOperator"' % (input_file, output_file)
            os.system(command_to_exec)
    
        else:
            print '>> file already found.'





