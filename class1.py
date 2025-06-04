print("hello! i am AI bot. Whats your name?")
name=input()
print(f"nice to meet you,{name}!")
print("how are you feeling today?(good or bad)")
mood=input().lower()
if mood=="good":
    print("i am glad to hear that")
elif mood=="bad":
    print("im sorry to hear that,hope things get better soon")
else:
    print("i see sometimes its hard to put feelings into words")
print(f"it was nice chatting with you {name} bye")
