def main():
    country_city_map = {}

    num_countries = int(input("Введите количество стран: "))
    
    for _ in range(num_countries):
        country = input("Введите название страны: ")
        cities = input(f"Введите города для {country} (через запятую): ").split(", ")
        country_city_map[country] = cities
    
    num_cities_to_check = int(input("Введите количество городов для проверки: "))
    cities_to_check = []
    
    for _ in range(num_cities_to_check):
        city = input("Введите название города: ")
        cities_to_check.append(city)
    
    for city in cities_to_check:
        found = False
        for country, cities in country_city_map.items():
            if city in cities:
                print(f"{city} находится в стране {country}.")
                found = True
                break
        if not found:
            print(f"{city} не найден в списках стран.")

if __name__ == "__main__":
    main()