
rivers = {
    'nile' : 'egypt',
    'mississippi' : 'the united states',
    'tigris' : 'iraq',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n")

for river in rivers:
    print(river.title())

print("\n")

for country in rivers.values():
    print(country.title())