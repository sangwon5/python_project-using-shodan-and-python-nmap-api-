import shodan

SHODAN_KEY = "2lKwmuzaaqeD921rVTC0Vtid79dYZTBy"
api = shodan.Shodan(SHODAN_KEY)


def  result(com, val):
    if(com == "add"):
        for val in list():
            print(val)

    elif(com == "show"):
        print("it will show list"):

    elif(com == "scan start"):
        print("for sca start")



Search_list[]
try:
    insert_search = input("[+] search: ")
    results = api.search(insert_search)
    print(result.items())
    for Target in result.keys():
        print(Target)

except(Exception as e):
    print(e)
