def case_offer():
    print("\n--- Case Offer ---\n")
    print("Detective Aayan Patil, you’ve been summoned by the museum director with an urgent case.")
    print("A priceless scroll, signed by the legendary Chhatrapati Shivaji Maharaj himself, has vanished overnight.")
    print("Will you take the case?\n")
    
    while True:
        choice = input("Do you accept the case? (yes/no): ").strip().lower()
        if choice == "yes":
            print("\nAayan: This is the kind of case I live for. Let’s get to work.")
            return True
        elif choice == "no":
            print("\nAayan: A scroll? Really? This is too boring for me.")
            print("Game Over: Detective Aayan Patil walks away, the mystery remains unsolved.")
            return False
        else:
            print("Please type 'yes' or 'no'.")

def crime_scene():
    print("\n--- Crime Scene ---\n")
    print("Aayan arrives at the museum’s artifact room — shattered glass litters the floor, and a chilling silence hangs in the air.")
    print("Among the debris, a strange symbol is scrawled on the wall in red paint.")
    print("Nearby, muddy footprints trail toward the back exit.\n")
    
    while True:
        print("What would you like to examine?")
        print("1. Examine the broken glass")
        print("2. Follow the footprints")
        print("3. Inspect the strange symbol")
        choice = input("Enter 1, 2, or 3: ").strip()
        
        if choice == "1":
            print("\nAayan kneels down to examine the shattered glass.")
            print("The glass carries a strange white powder. It might be important, but no solid leads yet.")
            return "powder"
        
        elif choice == "2":
            print("\nAayan follows the fresh footprints leading to a window.")
            print("There, he finds a torn piece of shirt. DNA analysis will be done, but no immediate leads.")
            return "footprints"
        
        elif choice == "3":
            print("\nAayan studies the red symbol on the wall carefully.")
            print("It matches an ancient secret code from the Maratha empire — this could crack the case wide open!")
            return "symbol"
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def secret_code_scene():
    print("\n--- Scene 2: Hidden Clue ---\n")
    print("Aayan spends the night decoding the ancient symbol...")
    print("It’s a Maratha-era cipher — used only for high-security scrolls.")
    print("After careful analysis, he extracts coordinates: RA-21-FG — a secret chamber in Raigad Fort!\n")
    
    print("Aayan prepares his gear and drives toward the fort early morning.")
    print("As he steps into the ruins, a voice echoes from inside...\n")
    
    print("Voice: 'You're not supposed to be here, detective.'")
    print("Aayan draws his flashlight and steps forward...\n")

    fort_encounter()

def fort_encounter():
    print("--- Scene 3: Raigad Fort Confrontation ---\n")
    print("A mysterious figure stands near an ancient lockbox.")
    print("You must decide how to approach the situation...\n")
    
    while True:
        print("1. Confront the stranger directly")
        print("2. Sneak around silently")
        print("3. Pretend to be an archaeology intern")
        choice = input("Enter 1, 2, or 3: ").strip()
        
        if choice == "1":
            print("\nAayan: 'Step away from the box. You’re done here.'")
            print("The man turns — an ex-historian turned artifact smuggler.")
            print("He pulls a gun. Aayan barely dodges, but is forced to flee.")
            print("The scroll is lost.\n")
            print("Case Status: ❌ Mission Failed.\n")
            break
        
        elif choice == "2":
            print("\nAayan ducks behind ancient pillars, silently observing.")
            print("The smuggler opens the lockbox and makes a call.")
            print("While he's distracted, Aayan sneaks in, grabs the scroll, and disappears into the shadows.")
            print("Victory!\n")
            print("Case Status: ✅ Scroll Recovered. Justice Served.\n")
            break
        
        elif choice == "3":
            print("\nAayan: 'Sir, I’m from the ASI, here to document the western wing?'")
            print("The smuggler is confused, but lets Aayan get close.")
            print("Spotting the scroll in a bag, Aayan seizes it and bolts.")
            print("He escapes with a minor injury — but the mission’s a success.\n")
            print("Case Status: ✅ Scroll Recovered (but not without pain).\n")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def failed_path_outcome(clue):
    if clue == "footprints":
        print("\nAayan waits as the DNA results are processed...")
        print("Days pass. No matches found in the database.")
        print("Then one evening, a news ticker flashes: ‘Rare Shivaji Scroll Sold for ₹5 Cr in Black Market Auction.’")
        print("Aayan clenches his fists. He was so close — yet the trail went cold.")
        print("Case Status: ❌ Unsolved\n")
    elif clue == "powder":
        print("\nForensics reports the white powder is a powdered form of museum-grade glass.")
        print("Used to fool the security systems. A red herring.")
        print("With no new leads, the case stalls.")
        print("A few days later, international news reports the scroll surfaced in an underground European auction.")
        print("Case Status: ❌ Unsolved\n")

def main():
    if case_offer():
        clue = crime_scene()
        
        if clue == "symbol":
            secret_code_scene()
        else:
            failed_path_outcome(clue)
    
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()