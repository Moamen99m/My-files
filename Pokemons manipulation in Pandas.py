import pandas as pd

# Load the Pokemon dataset
pokemons = pd.read_csv("C:\\Users\\moame\\Downloads\\pokemon.csv")

# Function to print the count of legendary and non-legendary Pokemon
def print_legendary_pokemon(pokemons):
    is_legendary = {'legendary': 0, 'non_legendary': 0}
    for index, row in pokemons.iterrows():
        if row['is_legendary'] == 0:
            is_legendary['non_legendary'] += 1
        else:
            is_legendary['legendary'] += 1
    print(is_legendary)

# Function to find and print the 5 most common primary types of Pokemon
def find_5_most_common_types(pokemons):
    pokemon_type = pokemons['type1'].value_counts()
    pokemon_type = pokemon_type.head(5)
    type_count = [f'{ptype} - {count}' for ptype, count in pokemon_type.items()]
    print(type_count)

# Function to get the average weight of legendary or non-legendary Pokemon
def get_average_weight(pokemons, is_legendary):
    if is_legendary == 1:
        avg_weight = pokemons[pokemons['is_legendary'] == 1]['weight_kg'].mean()
    else:
        avg_weight = pokemons[pokemons['is_legendary'] == 0]['weight_kg'].mean()
    return avg_weight

# Function to get the average height of legendary or non-legendary Pokemon
def get_average_height(pokemons, is_legendary):
    if is_legendary == 1:
        avg_height = pokemons[pokemons['is_legendary'] == 1]['height_m'].mean()
    else:
        avg_height = pokemons[pokemons['is_legendary'] == 0]['height_m'].mean()
    return avg_height

# Function to get the heaviest Pokemon's name (either legendary or non-legendary)
def get_heaviest_pokemon(pokemons, is_legendary):
    if is_legendary == 1:
        heaviest_pokemon = pokemons[pokemons['is_legendary'] == 1]['weight_kg'].idxmax()
    else:
        heaviest_pokemon = pokemons[pokemons['is_legendary'] == 0]['weight_kg'].idxmax()

    # Fetch the name of the heaviest Pokemon
    heaviest_name = pokemons.loc[heaviest_pokemon, 'name']
    return heaviest_name

# Function to classify Pokemon into difficulty levels based on capture rate
def get_difficulty(capture_rate):
    if capture_rate < 50:
        return 'Hard'
    elif 50 <= capture_rate <= 100:
        return 'Medium'
    else:
        return 'Easy'

# Function to add a 'catch_difficulty' column based on capture rate
def add_catch_difficulty(pokemons):
    pokemons['catch_difficulty'] = pokemons['capture_rate'].apply(get_difficulty)
    return pokemons

# Testing the functions
print_legendary_pokemon(pokemons)
find_5_most_common_types(pokemons)

print("Average weight of legendary Pokemon:", get_average_weight(pokemons, 1))
print("Average weight of non-legendary Pokemon:", get_average_weight(pokemons, 0))

print("Average height of legendary Pokemon:", get_average_height(pokemons, 1))
print("Average height of non-legendary Pokemon:", get_average_height(pokemons, 0))

print("Heaviest legendary Pokemon:", get_heaviest_pokemon(pokemons, 1))
print("Heaviest non-legendary Pokemon:", get_heaviest_pokemon(pokemons, 0))

# Adding and printing the catch difficulty column
pokemons = add_catch_difficulty(pokemons)
print(pokemons[['name', 'catch_difficulty']].head())
