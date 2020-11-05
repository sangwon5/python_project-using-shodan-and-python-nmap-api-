import shodan
from terminaltables import AsciiTable


SHODAN_KEY = input("[+]insert shodan key: ")
api = shodan.Shodan(SHODAN_KEY)

Search_list = []

def _Table():
    Search_list.append(['Organization', 'port', 'ip address'])
    Search_table = AsciiTable(Search_list)
    print(Search_table.table)


try:
    insert_search = input("[+] search: ")
    results = api.search(insert_search)
    _Table()

except Exception as e:
    print("error", e)
