def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('Karachi', 'Pakistan')
print(city)

city = city_country('Ankra', 'Turkey')
print(city)

city = city_country('Momby', 'India')
print(city)