import shodan
import terminaltables

SHODAN_KEY = input("[+]insert shodan key: ")
api = shodan.Shodan(SHODAN_KEY)


def  result(com, val):
    if(com == "add"):
        for val in list():
            print(val)

    elif(com == "show"):
        print("it will show list")

    elif(com == "scan start"):
        print("for sca start")



try:
    insert_search = input("[+] search: ")
    results = api.search(insert_search)
    print(results)

except Exception as e:
    print("error", e)
