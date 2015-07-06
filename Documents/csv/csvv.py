from csv import DictReader
from math import radians, cos, sin, asin, sqrt
from collections import defaultdict, OrderedDict


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

# part 1 and 3 and 4

idx = open('index.html', 'w')
idx.write('<ul>')
countries_15 = []
continent = defaultdict(list)

with open('countries.csv')as d:
    r = DictReader(d)
    for v in sorted(r, key=lambda v: int(v.get('population')), reverse=True):
        idx.write('<li> <a href="{}.html">{}</a> {:,d} km</li>'.format(
            v.get('short_name'), v.get('name'), int(haversine(34.75, 31.5, float(v['lon']), float(v['lat'])))))
        countries_15.append(['<li> <a href="{}.html">{}</a></li>'.format(
            v.get('short_name'), v.get('name')), int(haversine(34.75, 31.5, float(v['lon']), float(v['lat'])))])
        continent[v.get('continent')].append('<a href="{}.html">{}</a>'.format(v.get('short_name'),v.get('name')))
idx.write('</ul>')
idx.close()





# part 5
def get_15(name, countries_15):
    countries_15 = [v[0] for v in sorted(countries_15, key=lambda v: v[1], reverse=True)]
    for k, country in enumerate(countries_15):
        if name in country:
            return countries_15[k + 1:k + 16]

# part 2 and 3

with open('countries.csv')as d:
    r = DictReader(d)
    for v in r:
        with open('{}.html'.format(v.get('short_name')), 'w') as short_name:
                    short_name.write('''<html><head><title>{}</title></head><body>
                        <h1>{}</h1><dl>
                        <dt>Capital</dt>
                        <dd>{}</dd>
                        <dt>Population</dt>
                        <dd>{}</dd>
                        <dt>Land Area</dt>
                        <dd>{:,d} km<sup>2</sup></dd>
                        <dt>Continent</dt>
                        <dd>{}</dd>
                        <dt>All countries in the same continent:</dt>
                        <dd>{}</dd>
                        <dt><h3>15 countries closest to the state:</h3></dt>
                        <dd>{}</dd>
                        </dl></body></html>'''.format(v.get('name'), v.get('name'), v.get('capital')
                                                  , int(v.get('population')) if v.get('population') else 0
                                                  , int(v.get('land')) if v.get('land') else 0
                                                  , v.get('continent'), continent.get(v.get('continent'))
                                                  , get_15(v.get('name'), countries_15)))



