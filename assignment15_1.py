#11-1
def city_functions(city, country):
    print(f'{city}, {country}')
    return f'{city}, {country}'

#11-2
def city_functions_Populations(city, country, population):
    a = city_functions(city, country)
    return f'City at: {a} with population of: {population} people'