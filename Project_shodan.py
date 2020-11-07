import shodan
from terminaltables import AsciiTable


SHODAN_KEY = input("[+]insert shodan key: ")
api = shodan.Shodan(SHODAN_KEY)

Search_list = []
Search_list.append(['Organization', 'port', 'ip address'])

_list = {}




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
except Exception as e:
    print("error", e)
