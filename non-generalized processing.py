import veryfi
import pprint
import re
#import prettytable

client_id = "vrfdKXRMNCMZPfmFjzpWIt6Pu09Bbwur3ZDXTkZ"
client_secret = "w6cYo0rP4ibph5kmoW7h6ofslcw2udXMW2ySn5D3NWCnkxHhHs4VWsbPTwHTKFUH4EWcsWOrMAK80gm7KtZ6lGsjYjjHjRxhOCiwyh6dXrEwpHrMkP83CCJP4lNfkfAt"
username = "morariumaria98"
api_key = "1e703aea53385c45253ac7cf25d7bf5a"

client = veryfi.Client(client_id,client_secret, username, api_key)

# Extragerea tuturor datelor din 2.jpg
json_result2 = client.process_document(r"invoices\2.jpg")
pprint.pprint(json_result2)

print("------------------------------------------")

print(json_result2['ocr_text'])

serie_factura = re.search('\s([A-Z]){4}\s', json_result2['ocr_text'])
print(serie_factura.group())
nr_factura2 = re.search('[0-9]{12}', json_result2['ocr_text'])
print(nr_factura2.group())
furnizor2 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result2['ocr_text'])
print(furnizor2.group())
CUI2 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result2['ocr_text'])
print(CUI2.group())
client2 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}\s', json_result2['ocr_text'])
print(client2.group())
total2 = re.search('[5-9]{2},[6-9]{2}\n', json_result2['ocr_text'])
print(total2.group())

from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CIF','Client', 'Total_factura']
Valoare = [serie_factura2.group(), nr_factura2.group(), furnizor2.group(), CUI2.group(), client2.group(),total2.group()]
table2 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table2.add_row([Denumire[i], Valoare[i]])
print(table2)

# Extragerea liniilor privind produsele
import csv
inv_prod_re2 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table2.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test2.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result2["ocr_text"].split('\n'):
     if inv_prod_re2.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 5.jpg
json_result5 = client.process_document(r"C:\Users\Maria\Desktop\Master\Anul II\PSDT\invoices\5.jpg")
pprint.pprint(json_result5)

print("------------------------------------------")

print(json_result5['ocr_text'])

serie_factura5 = re.search('[A-Z]{4}', json_result5['ocr_text'])
print(serie_factura5.group())
nr_factura5 = re.search('[0-9]{12}', json_result5['ocr_text'])
print(nr_factura5.group())
furnizor5 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result5['ocr_text'])
print(furnizor5.group())
CUI5 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result5['ocr_text'])
print(CUI5.group())
client5 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}\s', json_result5['ocr_text'])
print(client5.group())
total5 = re.search('[5-9]{2},[6-9]{2}\n', json_result5['ocr_text'])
print(total5.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura5.group(), nr_factura5.group(), furnizor5.group(), CUI5.group(), client5.group(),total5.group()]
table5 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table5.add_row([Denumire[i], Valoare[i]])
print(table5)

# Extragerea liniilor privind produsele
import csv
inv_prod_re5 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table5.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result5["ocr_text"].split('\n'):
     if inv_prod_re5.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 6.jpg
json_result6 = client.process_document(r"invoices\6.jpg")
pprint.pprint(json_result6)

print("------------------------------------------")

print(json_result6['ocr_text'])

serie_factura6 = re.search('[A-Z]{4}[0-9]{1}', json_result6['ocr_text'])
print(serie_factura6.group())
nr_factura6 = re.search('[0-9]{12}', json_result6['ocr_text'])
print(nr_factura6.group())
furnizor6 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result6['ocr_text'])
print(furnizor6.group())
CUI6 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result6['ocr_text'])
print(CUI6.group())
client6 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}\s', json_result6['ocr_text'])
print(client6.group())
total6 = re.search('[1-9]{2},[8-9]{2}\n', json_result6['ocr_text'])
print(total6.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura6.group(), nr_factura6.group(), furnizor6.group(), CUI6.group(), client6.group(),total6.group()]
table6 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table6.add_row([Denumire[i], Valoare[i]])
print(table6)

# Extragerea liniilor privind produsele
import csv
inv_prod_re6 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table6.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test6.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result6["ocr_text"].split('\n'):
     if inv_prod_re6.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 8.jpg
json_result8 = client.process_document(r"invoices\8.jpg")
pprint.pprint(json_result8)

print("------------------------------------------")

print(json_result8['ocr_text'])

serie_factura8 = re.search('[A-Z]{4}[0-9]{1}', json_result8['ocr_text'])
print(serie_factura8.group())
nr_factura8 = re.search('[0-9]{12}', json_result8['ocr_text'])
print(nr_factura8.group())
furnizor8 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result8['ocr_text'])
print(furnizor8.group())
CUI8 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result8['ocr_text'])
print(CUI8.group())
client8 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}\s', json_result8['ocr_text'])
print(client8.group())
total8 = re.search('[0-9]{3},[0-9]{2}\n', json_result8['ocr_text'])
print(total8.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura8.group(), nr_factura8.group(), furnizor8.group(), CUI8.group(), client8.group(),total8.group()]
table8 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table8.add_row([Denumire[i], Valoare[i]])
print(table8)

# Extragerea liniilor privind produsele
import csv
inv_prod_re8 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table8.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test8.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result8["ocr_text"].split('\n'):
     if inv_prod_re8.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 9.jpg
json_result9 = client.process_document(r"invoices\9.jpg")
pprint.pprint(json_result9)

print("------------------------------------------")

print(json_result9['ocr_text'])

serie_factura9 = re.search('[A-Z]{4}[0-9]{1}', json_result9['ocr_text'])
print(serie_factura9.group())
nr_factura9 = re.search('[0-9]{12}', json_result9['ocr_text'])
print(nr_factura9.group())
furnizor9 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result9['ocr_text'])
print(furnizor9.group())
CUI9 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result9['ocr_text'])
print(CUI9.group())
client9 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}\s', json_result9['ocr_text'])
print(client9.group())
total9 = re.search('[1-9]{2},[0-9]{2}\n', json_result9['ocr_text'])
print(total9.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura9.group(), nr_factura9.group(), furnizor9.group(), CUI9.group(), client9.group(),total9.group()]
table9 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table9.add_row([Denumire[i], Valoare[i]])
print(table9)

# Extragerea liniilor privind produsele
import csv
inv_prod_re9 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table9.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test9.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result9["ocr_text"].split('\n'):
     if inv_prod_re9.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 10.jpg
json_result10 = client.process_document(r"invoices\10.jpg")
pprint.pprint(json_result10)

print("------------------------------------------")

print(json_result10['ocr_text'])

serie_factura10 = re.search('[A-Z]{4}', json_result10['ocr_text'])
print(serie_factura10.group())
nr_factura10 = re.search('[0-9]{12}', json_result10['ocr_text'])
print(nr_factura10.group())
furnizor10 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result10['ocr_text'])
print(furnizor10.group())
CUI10 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result10['ocr_text'])
print(CUI10.group())
client10 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{4}\s', json_result10['ocr_text'])
print(client10.group())
total10 = re.search('[0-9]{3},[0-9]{2}\n', json_result10['ocr_text'])
print(total10.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura10.group(), nr_factura10.group(), furnizor10.group(), CUI10.group(), client10.group(),total10.group()]
table10 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table10.add_row([Denumire[i], Valoare[i]])
print(table10)

# Extragerea liniilor privind produsele
import csv
inv_prod_re10 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table10.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test10.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result6["ocr_text"].split('\n'):
     if inv_prod_re10.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 11.jpg
json_result11 = client.process_document(r"invoices\11.jpg")
pprint.pprint(json_result11)

print("------------------------------------------")

print(json_result11['ocr_text'])

serie_factura11 = re.search('[A-Z]{4}[0-9]{1}', json_result11['ocr_text'])
print(serie_factura11.group())
nr_factura11 = re.search('[0-9]{12}', json_result11['ocr_text'])
print(nr_factura11.group())
furnizor11 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result11['ocr_text'])
print(furnizor11.group())
CUI11 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result11['ocr_text'])
print(CUI11.group())
client11 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}\s', json_result11['ocr_text'])
print(client11.group())
total11 = re.search('[4-5]{2},[0-9]{2}\n', json_result11['ocr_text'])
print(total11.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura11.group(), nr_factura11.group(), furnizor11.group(), CUI11.group(), client11.group(),total11.group()]
table11 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table11.add_row([Denumire[i], Valoare[i]])
print(table11)

# Extragerea liniilor privind produsele
import csv
inv_prod_re11 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table11.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test11.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result11["ocr_text"].split('\n'):
     if inv_prod_re11.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)

# Extragerea tuturor datelor din 14.jpg
json_result14 = client.process_document(r"invoices\14.jpg")
pprint.pprint(json_result14)

print("------------------------------------------")

print(json_result14['ocr_text'])

serie_factura14 = re.search('[A-Z]{4}', json_result14['ocr_text'])
print(serie_factura14.group())
nr_factura14 = re.search('[0-9]{12}', json_result14['ocr_text'])
print(nr_factura14.group())
furnizor14 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result14['ocr_text'])
print(furnizor14.group())
CUI14 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result14['ocr_text'])
print(CUI11.group())
client14 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{6}\s', json_result14['ocr_text'])
print(client14.group())
total14 = re.search('[0-9]{3},[0-9]{2}\n', json_result14['ocr_text'])
print(total14.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura14.group(), nr_factura14.group(), furnizor14.group(), CUI14.group(), client14.group(),total14.group()]
table14 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table14.add_row([Denumire[i], Valoare[i]])
print(table14)

# Extragerea liniilor privind produsele
import csv
inv_prod_re14 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table14.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test14.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result14["ocr_text"].split('\n'):
     if inv_prod_re14.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 16.jpg
json_result16 = client.process_document(r"invoices\16.jpg")
pprint.pprint(json_result16)

print("------------------------------------------")

print(json_result16['ocr_text'])

serie_factura16 = re.search('[A-Z]{4}', json_result16['ocr_text'])
print(serie_factura16.group())
nr_factura16 = re.search('[0-9]{12}', json_result16['ocr_text'])
print(nr_factura16.group())
furnizor16 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result16['ocr_text'])
print(furnizor16.group())
CUI16 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result16['ocr_text'])
print(CUI16.group())
client16 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{6}\s', json_result16['ocr_text'])
print(client16.group())
total16 = re.search('[0-9]{3},[0-9]{2}\n', json_result16['ocr_text'])
print(total16.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura16.group(), nr_factura16.group(), furnizor16.group(), CUI16.group(), client16.group(),total16.group()]
table16 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table16.add_row([Denumire[i], Valoare[i]])
print(table16)

# Extragerea liniilor privind produsele
import csv
inv_prod_re16 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table16.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test16.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result16["ocr_text"].split('\n'):
     if inv_prod_re16.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 17.jpg
json_result17 = client.process_document(r"invoices\17.jpg")
pprint.pprint(json_result17)

print("------------------------------------------")

print(json_result17['ocr_text'])

serie_factura17 = re.search('[A-Z]{4}[0-9]{1}', json_result17['ocr_text'])
print(serie_factura17.group())
nr_factura17 = re.search('[0-9]{12}', json_result17['ocr_text'])
print(nr_factura17.group())
furnizor17 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result17['ocr_text'])
print(furnizor17.group())
CUI17 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result17['ocr_text'])
print(CUI17.group())
client17 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{6}\s', json_result17['ocr_text'])
print(client17.group())
total17 = re.search('[2-9]{2},[0-4]{2}\n', json_result17['ocr_text'])
print(total17.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura17.group(), nr_factura17.group(), furnizor17.group(), CUI17.group(), client17.group(),total17.group()]
table17 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table17.add_row([Denumire[i], Valoare[i]])
print(table17)

# Extragerea liniilor privind produsele
import csv
inv_prod_re17 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table17.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test17.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result17["ocr_text"].split('\n'):
     if inv_prod_re11.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)



# Extragerea tuturor datelor din 18.jpg
json_result18 = client.process_document(r"invoices\18.jpg")
pprint.pprint(json_result18)

print("------------------------------------------")

print(json_result18['ocr_text'])

serie_factura18 = re.search('[A-Z]{4}', json_result18['ocr_text'])
print(serie_factura18.group())
nr_factura18 = re.search('[0-9]{12}', json_result18['ocr_text'])
print(nr_factura18.group())
furnizor18 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result18['ocr_text'])
print(furnizor18.group())
CUI18 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result18['ocr_text'])
print(CUI18.group())
client18 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{6}\s', json_result18['ocr_text'])
print(client18.group())
total18 = re.search('[0-9]{3},[0-9]{2}\n', json_result18['ocr_text'])
print(total18.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura18.group(), nr_factura18.group(), furnizor18.group(), CUI18.group(), client18.group(),total18.group()]
table18 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table18.add_row([Denumire[i], Valoare[i]])
print(table18)

# Extragerea liniilor privind produsele
import csv
inv_prod_re18 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table18.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test18.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result11["ocr_text"].split('\n'):
     if inv_prod_re18.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din 19.jpg
json_result19 = client.process_document(r"invoices\19.jpg")
pprint.pprint(json_result19)

print("------------------------------------------")

print(json_result19['ocr_text'])

serie_factura19 = re.search('[A-Z]{4}[0-9]{1}', json_result19['ocr_text'])
print(serie_factura19.group())
nr_factura19 = re.search('[0-9]{12}', json_result19['ocr_text'])
print(nr_factura19.group())
furnizor19 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result19['ocr_text'])
print(furnizor19.group())
CUI19 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result19['ocr_text'])
print(CUI19.group())
client19 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{6}\s', json_result19['ocr_text'])
print(client19.group())
total19 = re.search('[5-8]{2},[3-9]{2}\n', json_result19['ocr_text'])
print(total19.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura19.group(), nr_factura19.group(), furnizor19.group(), CUI19.group(), client19.group(),total19.group()]
table19 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table19.add_row([Denumire[i], Valoare[i]])
print(table19)

# Extragerea liniilor privind produsele
import csv
inv_prod_re19 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table19.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test19.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result19["ocr_text"].split('\n'):
     if inv_prod_re19.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)



#Extragerea datelor din facturile SALUBRIS #1

json_result20 = client.process_document(r"invoices\125202490_377075800252337_5303869627221703176_n.jpg")
pprint.pprint(json_result20)

print("------------------------------------------")

print(json_result20['ocr_text'])

nr_factura20 = re.search('[0-9]{8}', json_result20['ocr_text'])
print(nr_factura20.group())
furnizor20 = re.search('[A-Z]{8}\s+[A-Z].[A-Z].', json_result20['ocr_text'])
print(furnizor20.group())
CUI20 = re.search('[A-Z]{2}[0-9]{8}', json_result20['ocr_text'])
print(CUI20.group())
client20 = re.search('[A-Z]{8}\s+[A-Z]{4}\s+[A-Z]{8}\s', json_result20['ocr_text'])
print(client20.group())
total20 = re.search('\s[0-2]{2}.[4-9]{2}\n', json_result20['ocr_text'])
print(total20.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [nr_factura20.group(), furnizor20.group(), CUI20.group(), client20.group(),total20.group()]
table20 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,5):
    table20.add_row([Denumire[i], Valoare[i]])
print(table20)

# Extragerea liniilor privind produsele
import csv
inv_prod_re20 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table20.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("salubris1.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result20["ocr_text"].split('\n'):
     if inv_prod_re20.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)

##Extragere date factura Salubris #2

json_result21 = client.process_document(r"invoices\125202490_377075800252337_5303869627221703176_n.jpg")
pprint.pprint(json_result21)

print("------------------------------------------")

print(json_result21['ocr_text'])

nr_factura21 = re.search('[1-4]{8}', json_result21['ocr_text'])
print(nr_factura21.group())
furnizor21 = re.search('[A-Z]{8}\s+[A-Z].[A-Z].', json_result21['ocr_text'])
print(furnizor21.group())
CUI21 = re.search('[A-Z]{2}[0-9]{8}', json_result21['ocr_text'])
print(CUI21.group())
client21 = re.search('[A-Z]{8}\s+[A-Z]{4}\s+[A-Z]{8}/[A-Z]{8}', json_result21['ocr_text'])
print(client21.group())
total21 = re.search('[0-1]{2}.[7-8]{2}\n', json_result21['ocr_text'])
print(total21.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [nr_factura21.group(), furnizor21.group(), CUI21.group(), client21.group(),total21.group()]
table21 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,5):
    table21.add_row([Denumire[i], Valoare[i]])
print(table21)

# Extragerea liniilor privind serviciile
import csv
inv_prod_re21 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table21.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("salubris2.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result21["ocr_text"].split('\n'):
     if inv_prod_re21.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)



#Extragerea datelor Salubris #4
json_result23 = client.process_document(r"invoices\125770735_839528160149742_6087859672030191377_n.jpg")
pprint.pprint(json_result23)

print("------------------------------------------")

print(json_result23['ocr_text'])

nr_factura23 = re.search('[0-8]{8}', json_result23['ocr_text'])
print(nr_factura23.group())
furnizor23 = re.search('[A-Z]{8}\s+[A-Z].[A-Z].', json_result23['ocr_text'])
print(furnizor23.group())
CUI23 = re.search('[A-Z]{2}[0-9]{8}', json_result23['ocr_text'])
print(CUI23.group())
client23 = re.search('[A-Z]{8}\s+[A-Z]{6}\s', json_result23['ocr_text'])
print(client23.group())
total23 = re.search('[2-3]{2}.[7-8]{2}\n', json_result23['ocr_text'])
print(total23.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [nr_factura23.group(), furnizor23.group(), CUI23.group(), client23.group(),total23.group()]
table23 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,5):
    table23.add_row([Denumire[i], Valoare[i]])
print(table23)

# Extragerea liniilor privind serviciile
import csv
inv_prod_re23 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table23.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("salubris4.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result23["ocr_text"].split('\n'):
     if inv_prod_re23.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


##Extragerea datelor Salubris #3

json_result22 = client.process_document(r"invoices\125470392_1074747529653061_8958633208963968822_n.jpg")
pprint.pprint(json_result22)

print("------------------------------------------")

print(json_result22['ocr_text'])

nr_factura22 = re.search('[1-7]{8}', json_result22['ocr_text'])
print(nr_factura22.group())
furnizor22 = re.search('[A-Z]{8}\s+[A-Z].[A-Z].', json_result22['ocr_text'])
print(furnizor22.group())
CUI22 = re.search('[A-Z]{2}[0-9]{8}', json_result22['ocr_text'])
print(CUI22.group())
client22 = re.search('[A-Z]{8}\s+[A-Z]{6}\s', json_result22['ocr_text'])
print(client22.group())
total22 = re.search('[2-3]{2}.[7-8]{2}\n', json_result22['ocr_text'])
print(total22.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [nr_factura22.group(), furnizor22.group(), CUI22.group(), client22.group(),total22.group()]
table22 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,5):
    table22.add_row([Denumire[i], Valoare[i]])
print(table22)

# Extragerea liniilor privind serviciile
import csv
inv_prod_re22 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table22.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("salubris3.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result22["ocr_text"].split('\n'):
     if inv_prod_re22.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din factura emag
json_result24 = client.process_document(r"invoices\IMG_4858.jpg")
pprint.pprint(json_result24)

print("------------------------------------------")

print(json_result24['ocr_text'])

serie_factura24 = re.search('[H-Z]{4}', json_result24['ocr_text'])
print(serie_factura24.group())
nr_factura24 = re.search('[0-9]{12}', json_result24['ocr_text'])
print(nr_factura24.group())
furnizor24 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result24['ocr_text'])
print(furnizor24.group())
CUI24 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result24['ocr_text'])
print(CUI24.group())
client24 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{5}\s', json_result24['ocr_text'])
print(client24.group())
total24 = re.search('[0-9]{3},[0-9]{2}\n', json_result24['ocr_text'])
print(total24.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura24.group(), nr_factura24.group(), furnizor24.group(), CUI24.group(), client24.group(),total24.group()]
table24 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table24.add_row([Denumire[i], Valoare[i]])
print(table24)

# Extragerea liniilor privind produsele
import csv
inv_prod_re24 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table24.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test24.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result24["ocr_text"].split('\n'):
     if inv_prod_re24.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din factura emag
json_result25 = client.process_document(r"invoices\IMG_4859.jpg")
pprint.pprint(json_result25)

print("------------------------------------------")

print(json_result25['ocr_text'])

serie_factura25 = re.search('[H-Z]{4}', json_result25['ocr_text'])
print(serie_factura25.group())
nr_factura25 = re.search('[0-9]{12}', json_result25['ocr_text'])
print(nr_factura25.group())
furnizor25 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result25['ocr_text'])
print(furnizor25.group())
CUI25 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result25['ocr_text'])
print(CUI25.group())
client25 = re.search('[A-Z][a-z]{5}\s+[A-Z][a-z]{3}\s+[A-Z][a-z]{5}\s', json_result25['ocr_text'])
print(client25.group())
total25 = re.search('[0-9]{3},[0-9]{2}\n', json_result25['ocr_text'])
print(total25.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura25.group(), nr_factura25.group(), furnizor25.group(), CUI25.group(), client25.group(),total25.group()]
table25 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table25.add_row([Denumire[i], Valoare[i]])
print(table25)

# Extragerea liniilor privind produsele
import csv
inv_prod_re25 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table25.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test25.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result25["ocr_text"].split('\n'):
     if inv_prod_re25.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din factura emag
json_result26 = client.process_document(r"invoices\IMG_4860.jpg")
pprint.pprint(json_result26)

print("------------------------------------------")

print(json_result26['ocr_text'])

serie_factura26 = re.search('[H-Z]{4}', json_result26['ocr_text'])
print(serie_factura26.group())
nr_factura26 = re.search('[0-9]{12}', json_result26['ocr_text'])
print(nr_factura26.group())
furnizor26 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result26['ocr_text'])
print(furnizor26.group())
CUI26 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result26['ocr_text'])
print(CUI26.group())
client26 = re.search('[A-Z][a-z]{5}\s+[A-Z][a-z]{3}\s+[A-Z][a-z]{5}\s', json_result26['ocr_text'])
print(client26.group())
total26 = re.search('[4-9]{3},[0-9]{2}\n', json_result26['ocr_text'])
print(total26.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura26.group(), nr_factura26.group(), furnizor26.group(), CUI26.group(), client26.group(),total26.group()]
table26 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table26.add_row([Denumire[i], Valoare[i]])
print(table26)

# Extragerea liniilor privind produsele
import csv
inv_prod_re26 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table26.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test26.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result26["ocr_text"].split('\n'):
     if inv_prod_re26.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)

# Extragerea tuturor datelor din factura EMAG
json_result28 = client.process_document(r"invoices\IMG_4863.jpg")
pprint.pprint(json_result28)

print("------------------------------------------")

print(json_result28['ocr_text'])

serie_factura28 = re.search('[H-W]{4}', json_result28['ocr_text'])
print(serie_factura28.group())
nr_factura28 = re.search('[0-9]{12}', json_result28['ocr_text'])
print(nr_factura28.group())
nr_factura28 = re.search('[0-9]{12}', json_result28['ocr_text'])
print(nr_factura28.group())
furnizor28 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result28['ocr_text'])
print(furnizor28.group())
CUI28 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result28['ocr_text'])
print(CUI28.group())
client28 = re.search('[A-Z][a-z]{5}\s+[A-Z][a-z]{3}\s+[A-Z][a-z]{5}', json_result28['ocr_text'])
print(client28.group())
total28 = re.search('[0-5].[0-8]{3},[4-9]{2}\n', json_result28['ocr_text'])
print(total28.group())
# Sumar date furnizor, client, total
from prettytable import PrettyTable

Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI', 'Client', 'Total_factura']
Valoare = [serie_factura28.group(), nr_factura28.group(), furnizor28.group(), CUI28.group(), client28.group(),
           total28.group()]
table28 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0, 6):
    table28.add_row([Denumire[i], Valoare[i]])
print(table28)

# Extragerea liniilor privind produsele
import csv

inv_prod_re28 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table28.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in
          [line.split("|")] if len(splitline) > 1]
with open("test28.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result28["ocr_text"].split('\n'):
        if inv_prod_re28.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                       in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din factura EMAG
json_result29 = client.process_document(r"invoices\IMG_4864.jpg")
pprint.pprint(json_result29)

print("------------------------------------------")

print(json_result28['ocr_text'])

serie_factura29 = re.search('[H-W]{4}', json_result29['ocr_text'])
print(serie_factura29.group())
nr_factura29 = re.search('[0-9]{12}', json_result29['ocr_text'])
print(nr_factura29.group())
furnizor29 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result29['ocr_text'])
print(furnizor29.group())
CUI29 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result29['ocr_text'])
print(CUI29.group())
client29 = re.search('[A-Z][a-z]{5}\s+[A-Z][a-z]{3}\s+[A-Z][a-z]{5}', json_result29['ocr_text'])
print(client29.group())
total29 = re.search('[0-5].[0-9]{3},[4-9]{2}\n', json_result29['ocr_text'])
print(total29.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable

Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI', 'Client', 'Total_factura']
Valoare = [serie_factura29.group(), nr_factura29.group(), furnizor29.group(), CUI29.group(), client29.group(),
           total29.group()]
table29 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0, 6):
    table29.add_row([Denumire[i], Valoare[i]])
print(table29)

# Extragerea liniilor privind produsele
import csv

inv_prod_re29 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table29.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in
          [line.split("|")] if len(splitline) > 1]
with open("test29.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result29["ocr_text"].split('\n'):
        if inv_prod_re29.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                       in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din factura EMAG
json_result30 = client.process_document(r"invoices\IMG_4865.jpg")
pprint.pprint(json_result30)

print("------------------------------------------")

print(json_result30['ocr_text'])

serie_factura30 = re.search('[H-W]{4}', json_result30['ocr_text'])
print(serie_factura30.group())
nr_factura30 = re.search('[0-9]{12}', json_result30['ocr_text'])
print(nr_factura30.group())
furnizor30 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result30['ocr_text'])
print(furnizor30.group())
CUI30 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result30['ocr_text'])
print(CUI30.group())
client30 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{5}\s', json_result30['ocr_text'])
print(client30.group())
total30 = re.search('[0-8]{3},[4-9]{2}\n', json_result30['ocr_text'])
print(total30.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable

Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI', 'Client', 'Total_factura']
Valoare = [serie_factura30.group(), nr_factura30.group(), furnizor30.group(), CUI30.group(), client30.group(),
           total30.group()]
table30 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0, 6):
    table30.add_row([Denumire[i], Valoare[i]])
print(table30)

# Extragerea liniilor privind produsele
import csv

inv_prod_re30= re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table30.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in
          [line.split("|")] if len(splitline) > 1]
with open("test30.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result30["ocr_text"].split('\n'):
        if inv_prod_re30.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                       in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)

    # Extragerea tuturor datelor din factura EMAG
json_result31 = client.process_document(r"invoices\IMG_4866.jpg")
pprint.pprint(json_result31)

print("------------------------------------------")

print(json_result31['ocr_text'])

serie_factura31 = re.search('[H-W]{4}', json_result31['ocr_text'])
print(serie_factura31.group())
nr_factura31 = re.search('[0-9]{12}', json_result31['ocr_text'])
print(nr_factura31.group())
furnizor31 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result31['ocr_text'])
print(furnizor31.group())
CUI31 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result31['ocr_text'])
print(CUI31.group())
client31 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{5}\s', json_result31['ocr_text'])
print(client31.group())
total31 = re.search('[4-8]{2},[4-9]{2}\n', json_result31['ocr_text'])
print(total31.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable

Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI', 'Client', 'Total_factura']
Valoare = [serie_factura31.group(), nr_factura31.group(), furnizor31.group(), CUI31.group(), client31.group(),
           total31.group()]
table31 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0, 6):
    table31.add_row([Denumire[i], Valoare[i]])
print(table31)

# Extragerea liniilor privind produsele
import csv

inv_prod_re31 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table31.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in
          [line.split("|")] if len(splitline) > 1]
with open("test31.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result31["ocr_text"].split('\n'):
        if inv_prod_re31.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                       in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)


# Extragerea tuturor datelor din factura emag
json_result32 = client.process_document(r"invoices\IMG_4861.jpg")
pprint.pprint(json_result32)

print("------------------------------------------")

print(json_result32['ocr_text'])

serie_factura32= re.search('[H-Z]{4}', json_result32['ocr_text'])
print(serie_factura32.group())
nr_factura32 = re.search('[0-9]{12}', json_result32['ocr_text'])
print(nr_factura32.group())
furnizor32 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result32['ocr_text'])
print(furnizor32.group())
CUI32 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result32['ocr_text'])
print(CUI32.group())
client32 = re.search('[A-Z][a-z]{5}\s+[A-Z][a-z]{3}\s+[A-Z][a-z]{5}\s', json_result32['ocr_text'])
print(client32.group())
total32 = re.search('-[4-9]{3},[0-9]{2}\n', json_result32['ocr_text'])
print(total32.group())

# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client','Total_factura']
Valoare = [serie_factura32.group(), nr_factura32.group(), furnizor32.group(), CUI32.group(), client32.group(),total32.group()]
table32 = PrettyTable(['Denumire', 'Valoare'])
for i in range(0,6):
    table32.add_row([Denumire[i], Valoare[i]])
print(table32)

# Extragerea liniilor privind produsele
import csv
inv_prod_re32 = re.compile('\d{1}.?\s[A-Z].*')
furnizor_client = table32.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test32.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    for line in json_result32["ocr_text"].split('\n'):
     if inv_prod_re32.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            wr.writerows(result1)



