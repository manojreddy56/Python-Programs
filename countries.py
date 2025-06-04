input_filename = "country_info.txt"

with open(input_filename) as country_file:
    country_file.readline()
    country_entered = input("Enter the name of the country:")
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': dialing,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        if country == country_entered:
            print(capital)