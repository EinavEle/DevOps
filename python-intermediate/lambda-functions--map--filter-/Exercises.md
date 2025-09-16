# Pokemon


To practice our new tools, we're going to be working with this incredible [**pokemon.json**](https://github.com/Elevationacademy/python-spotcheck-solutions/blob/master/Filter-Map-Lambdas/pokemon.json) file (also available here in Codio).

Use this code to access the data for the exercises:

```python
import json

with open("pokemon.json") as pokemon_file:
    pokemon_data = json.load(pokemon_file)
```



Now `pokemon_data` is a list with several dicts, each representing a different Pokémon.


## Ex 1


There is too much data inside of each dict right now, and we want to slim it down.

Perform a `map` operation that overwrites the `pokemon_data` variable (**not** the file) so that each dict only has the following keys:
- id
- name
- type
- weight
- height
- weaknesses


Once your done, printing `pokemon_data[0]`` should output the following dict:


```python
{
    'id': 1,
    'name': 'Bulbasaur',
    'type': ['Grass', 'Poison'],
    'weight': 6.9,
    'height': 0.71,
    'weaknesses': ['Fire', 'Ice', 'Flying', 'Psychic']
}
```
<details>
<summary>Solution</summary>
<div> 

```python
import json

with open("pokemon.json") as pokemon_file:
    pokemon_data = json.load(pokemon_file)

pokemon_data = list(map(lambda pokemon:
                        {"id": pokemon["id"],
                         "name": pokemon["name"],
                         "type": pokemon["type"],
                         "weight": pokemon["weight"],
                         "height": pokemon["height"],
                         "weaknesses": pokemon["weaknesses"]
                        }, pokemon_data))

print(pokemon_data[0])
```
</div>
</details>

##  Pokemon Names
Now create a list of only the Pokémon names. If you output it, it should look like

```python
['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', '...]
```
<details>
<summary>Solution</summary>
<div> 

```python
import json

with open("pokemon.json") as pokemon_file:
    pokemon_data = json.load(pokemon_file)

pokemon_data = list(map(lambda pokemon: pokemon["name"], pokemon_data))

print(pokemon_data)
```
</div>
</details>

## Strong Pokemons

Now let's get rid of the really skinny Pokémon; they're probably too weak anyway.

Use a `filter` to create a list of `heavy_pokemon` - only keep the ones that are above 100 in weight.



If you do it right, you should find that there are 15 Pokémon left.
<details>
<summary>Solution</summary>
<div> 

```python
import json

with open("pokemon.json") as pokemon_file:
    pokemon_data = json.load(pokemon_file)

heavy_pokemon = list(filter(lambda pokemon: pokemon["weight"] > 100, pokemon_data))

print(len(heavy_pokemon))
```
</div>
</details>


## Water Pokemons

Create an array that only has the names of Pokemon which are weak against Water.



If you do it right, this should be your result:


```python
['Charmander', 'Charmeleon', 'Charizard', 'Sandshrew', 
 'Sandslash', 'Nidoqueen', 'Nidoking', 'Vulpix', 'Ninetales',
 'Diglett', 'Dugtrio', 'Growlithe', 'Arcanine', 'Geodude', 
 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Magnemite', 
 'Magneton', 'Onix', 'Cubone', 'Marowak', 'Rhyhorn', 'Rhydon', 
 'Magmar', 'Flareon', 'Aerodactyl', 'Moltres']
```

<details>
<summary>Hint</summary>
<div> 
remember that you can use in to test if an item exists in a list.

</div>
</details>

<details>
<summary>Solution</summary>
<div> 

```python
import json

with open("pokemon.json") as pokemon_file:
    pokemon_data = json.load(pokemon_file)

weak_against_water_pokemon = list(map(lambda pokemon: pokemon["name"],
                                      (filter(lambda pokemon: "Water" in pokemon["weaknesses"], pokemon_data))))


print(weak_against_water_pokemon)

# Check if the result is correct
res = ['Charmander', 'Charmeleon', 'Charizard', 'Sandshrew', 'Sandslash', 'Nidoqueen', 'Nidoking', 'Vulpix', 'Ninetales', 'Diglett', 'Dugtrio', 'Growlithe', 'Arcanine', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Magnemite', 'Magneton', 'Onix', 'Cubone', 'Marowak', 'Rhyhorn', 'Rhydon', 'Magmar', 'Flareon', 'Aerodactyl', 'Moltres']
print(res == weak_against_water_pokemon)
```
</div>
</details>


### Challenge 
you can do this in one line ;)


<details>
<summary>Solution</summary>
<div> 

```python
[p["name"] for p in pokemon_data if "Water" in p["weaknesses"]]
```
</div>
</details>











