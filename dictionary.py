import csv

while True:

    print( '''Dictionary for a little programmer:
1) Search expllanation by appellation,
2) Add new definition,
3) Show all appellations alphabetically,
4) Show available definitions by first letter of appellation,
5) Exit''')

    pick = input("Choose by number (1-5): ")

    if pick == "1":
        with open('glossary.csv') as csvfile:
            reader = csv.reader(csvfile)
            glossary = dict(reader)
            csvfile.close()
            reply = str(input("Enter appellation: ")).upper()
            if reply in glossary.keys():
                print(glossary.get(reply.strip()))

            else:
                print("There is no that appellation.")

    elif pick == "2":
        appellation = str(input("Enter appellation: ")).upper()
        expllanation = str(input("Enter expllanation: ")).upper()
        source = str(input("Enter a source: ")).upper()
        definition = {}
        definition[appellation] = (expllanation, source)

        with open('glossary.csv', "a") as csvfile:
            writer = csv.writer(csvfile)
            for key, value in definition.items():
                writer.writerow([key, value])
                csvfile.close()
            print("Added a new definition")

    elif pick == "3":
        with open('glossary.csv') as csvfile:
            reader = csv.reader(csvfile)
            glossary = dict(reader)
            csvfile.close()
            print(sorted(glossary))

    elif pick == "4":
        first_letter = str(input("Enter a first letter of appellation: ")).upper()
        with open('glossary.csv') as csvfile:
            reader = csv.reader(csvfile)
            glossary = dict(reader)
            csvfile.close()
            for key in glossary.keys():
                if key.startswith(first_letter):
                    print(key)

    elif pick == "5":
        print("Have a nice day, bye!")
        break

    else:
        print("Stop being stupid and choose by number --> (1-5)")
