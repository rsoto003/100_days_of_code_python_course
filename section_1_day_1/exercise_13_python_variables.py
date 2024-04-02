name = input("What is your name?")
city = input("Where do you live?")
favorite_sports_team = input("What is your favorite sports team?")
pet_name = input("Do you have any pets? If so, what is their name?")

print(f"Hello, {name}. I see you are residing in {city}. That is awesome. Is that why your favorite team is the {favorite_sports_team}?")

if(pet_name != ''):
    print(f"Give {pet_name} a treat for me!")