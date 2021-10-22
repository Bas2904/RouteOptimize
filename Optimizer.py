import requests
# getting HTML
r = requests.get('/optimized-trips/v1/{profile}/{coordinates}')
r.text; # HTML code
