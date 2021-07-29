lucky_number = [4, 8, 55, 9, 6, 11]
friends = [ "kevin", "sourabh", "rohan", "sid", "tom", "kevin"]
print(friends)
#friends.extend(lucky_number)
#print(friends)
friends.append("creed")
print(friends)
friends.insert(1, 'kelly')
print(friends)
friends.remove("sid")
print(friends)
#friends.clear()
#print(friends)
#friends.pop()
#print(friends)
print(friends.index("rohan"))
print(friends.count("kevin"))
friends.sort()
print(friends)
lucky_number.sort()
print(lucky_number)

lucky_number.reverse()
print(lucky_number)

friends2= friends.copy()
print(friends2)



