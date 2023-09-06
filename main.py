# write your code here
person = {
    "Name" : "Zahraa",
    "Age" : 16,
    "Hobbies" : ["coding", "researching", "swimming"]
}
print(person["Name"])
print(person["Age"])

person["Age"] = 17
person["Country"] = "Kuwait"
print(person)
print(len(person))

person["Hobbies"].append("reading")
def check_hobbies(person):
    if len(person["Hobbies"]) > 3:
        print("WOW!, You are amazing!")
check_hobbies(person)       