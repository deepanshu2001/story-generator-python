# story generator in python
print("Welcome to this Story created by me!")

l=[]
while True:
    name=input("Enter the name of character:")
    l.append(name)
    treasure=input("Enter the treasure name:")
    l.append(treasure)
    age=int(input("Enter the age of treasure:"))
    l.append(age)
    worth=int(input("Enter worth:"))
    l.append(worth)
    people_died=int(input("Enter no of people who died:"))
    l.append(people_died)
    member=input("Enter family member")
    l.append(member)
    mountain=input("Enter the name of mountain:")
    l.append(mountain)
    break

#print(l)


print(f"The story begins with {l[0]} who went into the jungle to search for {l[1]}s treasure.It is believed that the treasure was around {l[2]}years old and it's worth was {l[3]} million dollars.But the way to the treasure was so dangerous that around {l[4]} no of people lost their lifes finding the treasure.{l[0]} lost his {l[5]} who was also searching for the treasure.So this was the reason for his motivation of finding the treasure.The way to the treasure was in a secret cave that was beneath the ground and the only way to find the treasure was to find the treasure's map,which was known to be behind the back of constitution of india.But {l[0]} was  motivated and decided to steal it so that he can find the map.He was successfull in stealing the constitution and he found the map.But he was wanted by the the police for his act.As he had very less time,{l[0]} quickly started the search for the treasure.He found out that the treausre was on the top of {l[6]} mountain.He quickly reached there at the top and started diiging to find the enterence of the cave.He had to hurry because the police also reached there.But {l[0]} found the cave and in order to keep the treasure a secret,sealed the enterence of the cave as he went in.On going inside,He found the treasure.{l[0]} was so happy that there there were tears of joy on his face.Sadly there was no other exit on the cave and {l[0]} died due to lack of oxygen in the cave.")
