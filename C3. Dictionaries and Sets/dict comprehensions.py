# cu phap thuc hien tuong tu nhu list comprehension. 

DIAL_CODES = [            # list of tuples
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}

for country, code in country_code.items(): 
    print('%s:    %d' % (country, code))


dictcomp = {code: country.upper() for country, code in country_code.items() if code < 66}

print(dictcomp.keys())
print(dictcomp.values())
print(dictcomp.items())

for code, country in dictcomp.items(): 
    print('%d:    %s' % (code, country))




















