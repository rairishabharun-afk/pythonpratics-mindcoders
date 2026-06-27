import random

# ------------------------------------------
# JOKES
# ------------------------------------------

jokes = [
    "{name} Bhai, tumse toh calculator bhi zyada accurate hai. Kabhi kabhi lagta hai tumhe bhi update karwana padega'",
    "{name} bhai, tumhare time pe aana matlab time ka mazak banana. Tumhare liye toh ghadi bhi confuse ho jati hogi.",
    "{name}  tumhari memory toh Google se bhi weak hai. Kabhi kabhi lagta hai tumhare dimaag mein bhi cache clear ho gaya hai!.",
    "{name} padhne baitha tha, lekin YouTube ne motivational video ke naam par 3 ghante kha liye.",
    "{name} Padhai ke naam pe tum toh Netflix ke CEO ban jaoge. Kabhi socha hai ki tumhara asli talent kya hai.",
    "{name} exam ke ek din pehle syllabus dekhkar bolta hai: 'Challenge accepted.'",
    "{name} Exam mein tumhara performance dekh ke toh lagta hai tumne question paper ko hi confuse kar diya tha.",
    "{name} tum help mangne aaye ho? Tumse toh Siri bhi zyada intelligent lagti hai.",
    "{name} Bhai, tumhari flirting skills dekh ke toh lagta hai tumne Shakespeare ki kitaabein sirf cover dekh ke padhi hain.",
    "{name} ka relationship status: Wi-Fi se zyada unstable.",
    "{name} Tumhari jokes sun ke toh lagta hai tumne comedy ka course online free mein liya hoga.",
    "{name} Dance floor pe tumhara performance dekh ke toh lagta hai tumne apne pair ghar pe hi chhupa diye hain.",
    "{name} ka future plan itna clear hai jitna India mein winter sunlight.",
    
]

# ------------------------------------------
# ROASTS
# ------------------------------------------

roasts = [
    "{name}, tu toh itna slow hai ki agar race mein participate karega toh finish line tak pahunchte pahunchte retirement le lega!.",
    "{name}, excuses banana band kar aur kaam pe lag ja. Teri excuses toh Modi ke sher se bhi zyada hain!.",
    "{name}, tu toh itna dramatic hai ki agar Bollywood mein hota toh Oscar pakka tha!.",
    "{name}, tu padhai ke time itna busy ho jata hai jaise PM ka schedule ho.",
    "{name}, tere marks toh itne kam hain ki agar zero ko double karun toh bhi zyada ho jayenge.",
    "{name}, tu toh itna procrastinate karta hai ki agar exam ki date aaj ho toh tu kal padhna shuru karega",
    "{name}, tu toh itna irresponsible hai ki agar tujhe ek plant ki care karne ko bolun toh woh bhi sukh jayega.",
    "{name}, tu toh itna toxic hai ki agar tere aas paas koi rahe toh uski life bhi fucked up ho jayegi.",
    "{name}, teri ex toh itni gandi hai ki agar usko dustbin mein dalun toh dustbin bhi protest karega.",
    "{name},  tu toh itna selfish hai ki agar tujhe ek chocolate mile toh tu woh bhi kisi se share nahi karega.",
    "{name}, teri cooking skills itni legendary hain ki microwave bhi tere saath kaam karne se darta hai.",
    "{name},bhai, tera WiFi aur tera dimaag dono same hain — jab sabse zyada zaroorat hoti hai tabhi disconnect ho jaate hain.",
    
]

# ------------------------------------------
# FUNCTIONS
# ------------------------------------------

def generate_joke(name):
    return random.choice(jokes).format(name=name)

def generate_roast(name):
    return random.choice(roasts).format(name=name)

name = input("Enter Name: ")

if not name:
    print("Error: Name cannot be empty!")
    exit()

while True:
    print("\n" + "=" * 50)
    print(f"Current Name: {name}")
    print("=" * 50)
    print("1. Generate Joke")
    print("2. Generate Roast")
    print("3. Random Mode")
    print("4. Change Name")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        print(generate_joke(name))

    elif choice == "2":
        print(generate_roast(name))

    elif choice == "3":
        if random.choice([True, False]):
            print(generate_joke(name))
        else:
            print(generate_roast(name))

    elif choice == "4":
        name = input("Enter New Name: ")

    elif choice == "5":
        break
 
