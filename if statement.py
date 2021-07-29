

male= input('are you a male? ')
tall= input("are you tall? ")

if male == "yes" and tall == "yes":
    print("ohh!!!!you are tall male")
elif male == "yes" and tall == "no":
    print('ohhh!!!you are a short male')
elif male == "no" and tall == "yes":
    print('you are tall but not male!')

else:
    print('you are not male and also not tall')
