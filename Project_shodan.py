import shodan
from terminaltables import AsciiTable


SHODAN_KEY = input("[+]insert shodan key: ")
api = shodan.Shodan(SHODAN_KEY)

Search_list = []
Search_list.append(['Organization', 'port', 'ip address'])

_list = {}


nmap_info = [
                ['command', 'info'],
                ['add <ip>', 'add ip_address in to the scan list'],
                ['remove <ip>', 'remove selected ip in the scan list'],
                ['show list', 'Show the scan list'],
                ['scan start', 'scan the ip_address in the scanlist'],
                ['clear list', 'Clear the scan list'],
                ['exit program', 'exit the program']
            ]
info_table = AsciiTable(nmap_info)

try:
    insert_search = input("[+] search: ")
    results = api.search(str(insert_search))
    Search_table = AsciiTable(Search_list)
    Search_table.inner_row_border = True

    for target_options in results['matches']:
        _list[target_options['ip_str']] = target_options['org']
        Search_list.append([target_options['org'],target_options['port'],str(target_options['ip_str'])])
    print(Search_table.table)
    file = open('result.txt', 'w')
    file.write(Search_table.table)
    file.close()

    print("")
    print("[+] file is saved in result.txt")
    print("===starting nmap===")
    print("")

    print(info_table.table)
    Scan_list = []
    Scan_table = AsciiTable(Scan_list)
    Scan_table.inner_row_border = True
    Scan_list.append(['Organization', 'ip address'])
    while(1):
        com, val = input(": ").split()
        if(com == 'add'):
           Scan_list.append([_list[val], val])
           print('[+]', _list[val], ': ', val, ' added in the list')
           print("")
        elif(com == 'remove'):
            print('[+] remove', _list[val], ': ',val, 'in the list' )
            print(Scan_list)
        elif(com == 'show' and val == 'list'):
            if(len(Scan_table.table) == 5):
                print("[*] Scan table is emty [*]")
            else:
                print(Scan_table.table)
        elif(com == 'clear' and val == 'list'):
            print("[+] clearing the scan list")
            Scan_list.clear()
        elif(com == 'exit' and val == 'program'):
            exit(1)

        else:
           print("[*] wrong command")
           print("")
except Exception as e:
    print("error", e)
