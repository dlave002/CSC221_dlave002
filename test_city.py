from assignment15_1 import city_functions, city_functions_Populations

def test_city_functions():
    print('Enter q to quit')
    while True:
        
        a = city_functions("San Jose", "USA")
        print(f"Its at: {a}")
        assert f"Its at: {a}"
        break

test_city_functions()
    
def test_city_functions_population():
    
    a = city_functions_Populations("San Jose", "USA", 4000000)
    print(a)
    assert a

test_city_functions_population()