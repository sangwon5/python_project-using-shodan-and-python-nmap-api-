import shodan
from terminaltables import AsciiTable
import nmap3


SHODAN_KEY = input("[+]insert shodan key: ")
api = shodan.Shodan(SHODAN_KEY)

Search_list = []
Search_list.append(['Organization', 'port', 'ip address'])

_list = {}

nmap_info = [
                ['command', 'info'],
                ['add <ip>', 'add ip_address in to the scan list'],
                ['show list', 'Show the scan list'],
                ['show info', 'print out scan info'],
                ['show tar', 'show target list'],
                ['scan start', 'SYN scan the ip_address in the scan list'],
                ['clear list', 'Clear the scan list'],
                ['exit prog', 'exit the program']
            ]
info_table = AsciiTable(nmap_info)
info_table.inner_row_border = True

target_List = []
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
    Scan_list.append(['Organization',  "ip address"])
    while(1):
        com, val = input(": ").split()
        if(com == 'add'):
           Scan_list.append([_list[val], val])
           target_List.append(val)
           
           print('[+]', _list[val], ': ', val, ' added in the list')
           print("")
        elif(com == 'show' and val == 'list'):
            if(len(Scan_table.table) == 5):
                print("[*] Scan table is emty [*]")
            else:
                print(Scan_table.table)
        elif(com == 'show' and val == 'info'):
            print(info_table.table)

        elif(com == 'show' and val == 'tar'):
            print(Search_table.table)
        elif(com == 'scan' and val == 'start'):
            nmap = nmap3.NmapScanTechniques()
            for Target in target_List:
                results = nmap.nmap_syn_scan(Target)

                #need to add save result on <hostname>.txt
                print('[+] target host name: ', _list[Target])
                print('[+] target ip address: ', Target)
                print('-------------------------------')
                print('[+] raw results: ', results[Target])

            print("")
            
        elif(com == 'clear' and val == 'list'):
            print("[+] clearing the scan list")
            Scan_list.clear()
            target_List.clear()
            Scan_list.append(['Organization', 'ip address'])

        elif(com == 'exit' and val == 'prog'):
            print("++++ Program exit ++++")
            exit(1)

        else:
           print("[*] wrong command")
           print("")
except Exception as e:
    print("error", e)
