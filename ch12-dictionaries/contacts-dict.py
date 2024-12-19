contacts = {
    "Joel": {"address": "1500 Anystreet", "city": "San Francisco",
         "state": "California", "postalCode": "94110", 
         "phone": "555-555-1111"},
    "Anne":
        {"address": "1000 Somestreet", "city": "Fresno",
         "state": "California", "postalCode": "93704", 
         "phone": "555-555-2222"},
    "Ben": {"address": "1400 Another Street", "city": "Fresno",
         "state": "California", "postalCode": "93704", 
         "phone": "555-555-4444"}
}

anne = contacts["Anne"]
print(f"Anne's Contact: {anne}")
#print(f"Anne's Phone #: {anne["phone"]}")
print(f"Anne's Phone #: {contacts["Anne"]["phone"]}")
print(f"Anne's Email: {contacts["Anne"].get("email")}")

print(f"Ben's address: {contacts.get("Ben").get("address")}")
