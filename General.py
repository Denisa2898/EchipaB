f = client.process_document("Files/72.JPG")
pprint.pprint(f)

print("------------------------------------------")

print(f['ocr_text'])


numar_fact = re.search('[A-Z][/]\d{3}', f['ocr_text'])
print(numar_fact.group())
furnizor = re.search('[A-z]{4}\s\d[A-z]{7}', f['ocr_text'])
print(furnizor.group())
CUI = re.findall('[A-Z]{2}\s?[0-9]{6,10}', f['ocr_text'])
print(CUI[0])
print(CUI[1])
client_fact = re.search('(Cumparator:\s)([A-Z]{2}\s[A-z]{7}\s[A-z]{2}\s[A-z]{5}\s[A-Z]{3})', f['ocr_text'])
print(client_fact.group(2))
total = re.findall('[0-9]{3}\.[0-9]{2}', f['ocr_text'])
print(total[4])


# Sumar date furnizor, client, total
from prettytable import PrettyTable
Denumire = ['Serie factra', 'Numar Factura', 'Furnizor', 'CUI','Client', 'CUI', 'Total']
Valoare = [serie.group(2), numar_fact.group(2), furnizor.group(2), CUI[0], client_fact.group(2), CUI[1], total[4]]
table = PrettyTable(['Denumire', 'Valoare'])
for i in range(0, 7):
    table.add_row([Denumire[i], Valoare[i]])
print(table)

# Extragerea liniilor privind produsele
inv_prod_re = re.compile('\d{1}.?\s[A-z].*')
furnizor_client = table.get_string()
result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
with open("test.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(result)
    wr.writerows(' ')
    for line in f["ocr_text"].split('\n'):
     if inv_prod_re.match(line):
            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for splitline
                  in [l.split("\t")] if len(splitline) > 1]
            print(result1)
            wr.writerows(result1)