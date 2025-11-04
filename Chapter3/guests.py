guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
# print("I've invited the following people to dinner: " + ", ".join(guests))
# is the same out put as:
# print(f"I've invited the following people to dinner: {', '.join(guests)}")
guest = guests[0]
print(f"{guest}, would you like to come to dinner?")

guest = guests[1]
print(f"{guest}, would you like to come to dinner?")

guest = guests[2]
print(f"{guest}, would you like to come to dinner?")

popped_guest = guests.pop(2)
print(f"Unfortunately, {popped_guest} can't make it to dinner.")
guests.append("Nikola Tesla")

print("A new guest has been added to the list: " + guests[-1])
print("So, we're expecting the following guests at the dinner: : " + ", ".join(guests))

print("\nGood news! We've found a bigger dinner table! " + ", ".join(guests))
print(f"\nGood news! We've found a bigger dinner table! {', '.join(guests)}")

guests.insert(0, "Galileo Galilei")
guests.insert(1, "Johannes Kepler")
guests.append("Henry Cavendish")

print("So, we're expecting the following guests at the dinner: : " + ", ".join(guests))

guests.remove("Albert Einstein")
print("\nSo, we're expecting the following guests at the dinner: : " + ", ".join(guests))

del guests[4]
print("\nSo, we're expecting the following guests at the dinner: : " + ", ".join(guests))
