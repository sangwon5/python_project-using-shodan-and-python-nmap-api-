import shodan
from terminaltables import AsciiTable


SHODAN_KEY = input("[+]insert shodan key: ")
api = shodan.Shodan(SHODAN_KEY)

Search_list = []
Search_list.append(['Organization', 'port', 'ip address'])

_list = {}


<<<<<<< HEAD
=======
nmap_info = [
                ['command', 'info']
                ['add <ip>', 'add ip_address in to the scan list'],
                ['show list', 'Show the scan list'],
                ['scan start', 'scan the ip_address in the scanlist'],
                ['clear list', 'Clear the scan list'] 
            ]
info_table = AsciiTable(nmap_info)

>>>>>>> workspace
try:
    insert_search = input("[+] search: ")
    results = api.search(str(insert_search))
    Search_table = AsciiTable(Search_list)
    Search_table.inner_row_border = True

    for target_options in results['matches']:
        _list[target_options['ip_str']] = {target_options['org']}
        Search_list.append([target_options['org'],target_options['port'],str(target_options['ip_str'])])
    print(Search_table.table)
    file = open('result.txt', 'w')
    file.write(Search_table.table)
    file.close()
    print("[+] file is saved in result.txt")
    print("===starting nmap===")
    print(info_table.table)


except Exception as e:
    print("error", e)
