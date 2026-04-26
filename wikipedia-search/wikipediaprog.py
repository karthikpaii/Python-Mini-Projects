import wikipedia


while(True):
    print("======Wikipedia Search ======\n")
    print("-----Title Should Be Correct and Match The Wikipedia Article Title------")
    query=input("Enter Title To Search: ")
   
    try:
        result=wikipedia.summary(query, sentences=8)

        print("\nResult: \n")
        print(result,"\n")
        print("---------------------------------\n")

    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple results Found, Select any One:")
        print(e.options[:6])

    except wikipedia.exceptions.PageError:
        print("This Page is Not Found")
        print("---------------------------------\n")

    except Exception as e:
        print("Error:",e)
