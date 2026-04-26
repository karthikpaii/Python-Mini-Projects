import wikipedia

while True:
    print("\n====== Wikipedia Menu ======")
    print("1. Search Article Sections")
    print("2. Random Article")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            query = input("Enter Title To Search: ")

            try:
                page = wikipedia.summary(query,sentences=10)

                print("\n Contents:\n")
                print(page)

                print("\n---------------------------------\n")

            except wikipedia.exceptions.DisambiguationError as e:
                print("Multiple results found:")
                print(e.options[:5])

            except wikipedia.exceptions.PageError:
                print(" Page not found")

            except Exception as e:
                print("Error:", e)

        case "2":
            print("\n Random Article:")
            title=wikipedia.random()
            page=wikipedia.page(title)
            print("Random Page Title:",title)
            print("Content:")
            sum=wikipedia.summary(title,sentences=10)
            print(sum)
            

        case "3":
            print("Exiting...")
            break

        case _:
            print(" Invalid choice")
