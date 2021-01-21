from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pprint
import re
import prettytable
import collections
import csv
import tkinter as tk


#importam functia de call api
from api_call import procesare

class Window:
    def __init__(self, root):

        self.entry = Entry(root, width=60)
        self.entry.grid(row=4, column=6)
        self.entry.place(relx = 0.5, rely = 0.2,anchor = 'center', height=30)

        #Buttons
        self.buttonProcesare= Button(master=root, text="Extrage datele", font=('Arial', 8), bg='white',fg='Black', command=self.procesare_factura)
        #self.buttonProcesare.grid(row=6, column=9,padx=5, pady=10, sticky=W + E)
        self.buttonProcesare.place(relx=0.92, rely=0.2, anchor='center')

        self.browse_button = Button(root, text="Incarca poza facturii",font=('Arial', 8), bg='white',fg='Black', command=self.browse)
        self.browse_button.place(relx=0.8, rely=0.2, anchor='center')
        #self.browse_button.grid(row=4, column=9, padx=5, pady=10)


        #label mesaj de save
        self.saved = Label(root, text="")
        self.saved.place( relx = 0.5, rely = 0.5,anchor = 'center')
        #self.saved.grid(row=12, column=0)

        self.root_folder_results="C:/Users/alexa/OneDrive/Desktop/ProiectOCR/results/"

        #button deschide fereastra cu datele facturii
        self.buton = Button(root,text="Vizualizeaza rezultatul",bg='white',fg='Black',font=('Arial', 8),command=self.hide_me)
        #self.buton.place(relx = 0.5, rely = 0.6,anchor = 'center')

        # permite navigarea printre foldere si alegere factura, in leg cu butonul browse
    def browse(self):
        Tk().withdraw()
        self.filename = askopenfilename()
        self.entry.insert(0, self.filename)

    #comanda pt butonul care deschide fereastra cu label facturi results

    def openNewWindow(self, text):

        newWindow = Toplevel(root)
        newWindow.title("Datele facturii")
        # label unde se vor afisa rezultatele facturii
        self.results = Label(newWindow, text=text)
        self.results.grid(row=11, column=7)

    #ascundere buton
    def hide_me(self, event):
        event.widget.place_forget()

    #medodele ce vor fi utilizate pentru text factura
    def procesare_factura(self):
        #calea unde va fi returnat csv ul
        number = self.entry.get().split("/")[len(self.entry.get().split("/")) - 1].split(".")[0]
        file_to_write_to = self.root_folder_results + number + ".csv"

        # Extragerea tuturor datelor din 1.jpg
        if(self.entry.get()=="C:/Users/alexa/OneDrive/Desktop/ProiectOCR/bd/1.jpg"):

            json_result1 = procesare("C:\\Users\\alexa\\OneDrive\\Desktop\\ProiectOCR\\bd\\1.jpg")
            pprint.pprint(json_result1)

            print("------------------------------------------")

            print(json_result1['ocr_text'])

            serie_factura = re.search('\s([A-Z]){2}\s', json_result1['ocr_text'])
            print(serie_factura.group())
            nr_factura = re.search('([0-9]){6}\s', json_result1['ocr_text'])
            print(nr_factura.group())
            furnizor = re.search('[A-Z]{5}\s+[A-Z]{10}\s', json_result1['ocr_text'])
            print(furnizor.group())
            CUI = re.search('[A-Z]{2}\s+[0-9]{8}', json_result1['ocr_text'])
            print(CUI.group())
            client = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}\s', json_result1['ocr_text'])
            print(client.group())
            total = re.search('\s[0-9]{3}\.[0-9]{2}\sLei', json_result1['ocr_text'])
            print(total.group())

            # Sumar date furnizor, client, total
            from prettytable import PrettyTable
            Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI','Client', 'Total_factura']
            Valoare = [serie_factura.group(), nr_factura.group(), furnizor.group(), CUI.group(), client.group(),total.group().strip()]
            table = PrettyTable(['Denumire', 'Valoare'])
            for i in range(0,6):
                table.add_row([Denumire[i], Valoare[i]])
            print(table)

            # Extragerea liniilor privind produsele
            line_items = []
            inv_prod_re1 = re.compile('(\d{1}\s)([A-Z].*?\t)([a-z].*?\t)(\d\t)([\d].*?\d{2}\t)(\d*.\d*\s)(\d*%\t)(\d*.\d*)')
            for line in json_result1["ocr_text"].split('\n'):
                if inv_prod_re1.match(line):
                    print(line)

                line = inv_prod_re1.search(line)
                if line:
                    nr_crt = line.group(1)
                    line_items.append(nr_crt)
                    produs = line.group(2)
                    line_items.append(produs)
                    um = line.group(3)
                    line_items.append(um)
                    cantitate = line.group(4)
                    line_items.append(cantitate)
                    pret_unitar = line.group(5)
                    line_items.append(pret_unitar)
                    valoare = line.group(6)
                    line_items.append(valoare)
                    tva = line.group(8)
                    line_items.append(tva)


            print(line_items)

            # Tabel cu produse
            from prettytable import PrettyTable
            Denumire = ['Nr.crt.', 'Produs/Serviciu', 'UM','Cantitate', 'Pret unitar', 'Valoare', 'TVA']
            Produs_1 = [line_items[0], line_items[1], line_items[2], line_items[3], line_items[4], line_items[5], line_items[6]]
            Produs_2 = [line_items[7], line_items[8], line_items[9], line_items[10], line_items[11], line_items[12], line_items[13]]
            table7 = PrettyTable(['Denumire', 'Produs_1'],  align="l")
            table8 = PrettyTable(['Denumire', 'Produs_2'],  align='l')
            for i in range(0,6):
                table7.add_row([Denumire[i], Produs_1[i]])
                table8.add_row([Denumire[i], Produs_2[i]])
            print(table7)
            print("------------------------------------")
            print(table8)


            ### Export csv
            furnizor_client = table.get_string()
            produs1 = table7.get_string()
            produs2 = table8.get_string()
            print(furnizor_client)
            result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
            result1 = [tuple(filter(None, map(str.strip, splitline))) for line in produs1.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
            result2 = [tuple(filter(None, map(str.strip, splitline))) for line in produs2.splitlines() for splitline in [line.split("|")] if len(splitline) > 1]
            print(result1)


            with open(file_to_write_to, 'w', newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerows(result)
                wr.writerow(' ')
                wr.writerows(result1)
                wr.writerows(' ')
                wr.writerows(result2)

            with open(file_to_write_to, "r") as myfile:
                #self.results.configure(text=myfile.read())
                self.saved.configure(text="Un fisier .csv  cu datele facturii tale a fost salvat in "+ file_to_write_to, font="Arial")
                text = myfile.read()
                self.buton.config(command=lambda: self.openNewWindow(text))
                self.buton.place(relx = 0.5, rely = 0.6,anchor = 'center')

#################################################################################

        else:
            if(self.entry.get()=="C:/Users/alexa/OneDrive/Desktop/ProiectOCR/bd/3.jpg"):
                json_result2 = procesare("C:/Users/alexa/OneDrive/Desktop/ProiectOCR/bd/3.jpg")
                pprint.pprint(json_result2)

                print("------------------------------------------")

                print(json_result2['ocr_text'])

                serie_factura2 = re.search('[A-Z]{4}', json_result2['ocr_text'])
                print(serie_factura2.group())
                nr_factura2 = re.search('[0-9]{12}', json_result2['ocr_text'])
                print(nr_factura2.group())
                furnizor2 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result2['ocr_text'])
                print(furnizor2.group())
                CUI2 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result2['ocr_text'])
                print(CUI2.group())
                client2 = re.search('[A-Z][a-z]{6}\s+[A-Z][a-z]{7}', json_result2['ocr_text'])
                print(client2.group())
                total2 = re.search('[0-9]{3},[0-9]{2}\n', json_result2['ocr_text'])
                print(total2.group())

                # Sumar date furnizor, client, total
                from prettytable import PrettyTable
                Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI', 'Client', 'Total_factura']
                Valoare = [serie_factura2.group(), nr_factura2.group(), furnizor2.group(), CUI2.group(),
                           client2.group(), total2.group()]
                table2 = PrettyTable(['Denumire', 'Valoare'])
                for i in range(0, 6):
                    table2.add_row([Denumire[i], Valoare[i]])
                print(table2)

                # Extragerea liniilor privind produsele
                inv_prod_re2 = re.compile('\d{1}.?\s[A-Z].*')
                furnizor_client = table2.get_string()
                result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for
                          splitline in [line.split("|")] if len(splitline) > 1]

                with open(file_to_write_to, 'w', newline='') as myfile:
                    wr = csv.writer(myfile)
                    wr.writerows(result)
                    for line in json_result2["ocr_text"].split('\n'):
                        if inv_prod_re2.match(line):
                            result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for
                                       splitline
                                       in [l.split("\t")] if len(splitline) > 1]
                            wr.writerows(result1)

                with open(file_to_write_to, "r") as myfile:
                    # self.results.configure(text=myfile.read())
                    self.saved.configure(
                        text="Un fisier .csv  cu datele facturii tale a fost salvat in " + file_to_write_to,
                        font="Arial")
                    text = myfile.read()
                    self.buton.config(command=lambda: self.openNewWindow(text))
                    self.buton.place(relx=0.5, rely=0.6, anchor='center')
###########################################################################################
            else:
                if (self.entry.get() == "C:/Users/alexa/OneDrive/Desktop/ProiectOCR/bd/15.jpg"):
                    json_result4 = procesare("C:/Users/alexa/OneDrive/Desktop/ProiectOCR/bd/15.jpg")
                    pprint.pprint(json_result4)
                    print("------------------------------------------")
                    print(json_result4['ocr_text'])
                    serie_factura4 = re.search('[A-Z]{5}', json_result4['ocr_text'])
                    print(serie_factura4.group())
                    nr_factura4 = re.search('[0-9]{12}', json_result4['ocr_text'])
                    print(nr_factura4.group())
                    furnizor4 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{12}\s+[A-Z].[A-Z].', json_result4['ocr_text'])
                    print(furnizor4.group())
                    CUI4 = re.search('[A-Z]{2}\s+[0-9]{8}', json_result4['ocr_text'])
                    print(CUI4.group())
                    client4 = re.search('[A-Z][a-z]{4}\s+[A-Z][a-z]{6}\s', json_result4['ocr_text'])
                    print(client4.group())
                    total4 = re.search('\s[0-9].[0-9]{3},[0-9]{2}\n', json_result4['ocr_text'])
                    print(total4.group())

                    # Sumar date furnizor, client, total
                    from prettytable import PrettyTable
                    Denumire = ['Serie Factura', 'Numar Factura', 'Furnizor', 'CUI', 'Client', 'Total_factura']
                    Valoare = [serie_factura4.group(), nr_factura4.group(), furnizor4.group(), CUI4.group(),
                               client4.group(), total4.group().strip()]
                    table4 = PrettyTable(['Denumire', 'Valoare'])
                    for i in range(0, 6):
                        table4.add_row([Denumire[i], Valoare[i]])
                    print(table4)

                    # Extragerea liniilor privind produsele
                    inv_prod_re4 = re.compile('\d{1}.?\s[A-Z].*')
                    furnizor_client = table4.get_string()
                    result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines() for
                              splitline in [line.split("|")] if len(splitline) > 1]

                    with open(file_to_write_to, 'w', newline='') as myfile:
                        wr = csv.writer(myfile)
                        wr.writerows(result)
                        wr.writerows(' ')
                        for line in json_result4["ocr_text"].split('\n'):
                            if inv_prod_re4.match(line):
                                result1 = [tuple(filter(None, map(str.strip, splitline))) for l in line.splitlines() for
                                           splitline
                                           in [l.split("\t")] if len(splitline) > 1]
                                wr.writerows(result1)
                    with open(file_to_write_to, "r") as myfile:
                         # self.results.configure(text=myfile.read())
                         self.saved.configure(text="Un fisier .csv  cu datele facturii tale a fost salvat in " + file_to_write_to,
                                        font="Arial")
                         text = myfile.read()
                         self.buton.config(command=lambda: self.openNewWindow(text))
                         self.buton.place(relx=0.5, rely=0.6, anchor='center')
   ####################################################################################
                else:
                    #### Facturi  ELEFANT

                    if (self.entry.get() == "C:/Users/alexa/OneDrive/Desktop/ProiectOCR/bd/39.PNG"):
                        fact_elefant= procesare("C:/Users/alexa/OneDrive/Desktop/ProiectOCR/bd/39.PNG")
                        pprint.pprint(fact_elefant)

                        print("------------------------------------------")

                        print(fact_elefant['ocr_text'])

                        serie_elefant = re.search('\s[A-Z]{3}\s', fact_elefant['ocr_text'])
                        print(serie_elefant.group())
                        nr_elefant = re.search('[0-9]{10}', fact_elefant['ocr_text'])
                        print(nr_elefant.group())
                        client_elefant = re.search('[A-Z][a-z]{4,10}\s+[A-Z][a-z]{3,10}', fact_elefant['ocr_text'])
                        print(client_elefant.group())
                        total_elefant = re.search('(TOTAL)(.*\d\slei)', fact_elefant['ocr_text'])
                        print(total_elefant.group(2))

                        # Sumar date furnizor, client, total
                        from prettytable import PrettyTable
                        Denumire = ['Serie Factura', 'Numar Factura', 'Client', 'Total_factura']
                        Valoare = [serie_elefant.group(), nr_elefant.group(), client_elefant.group(),
                                   total_elefant.group(2)]
                        table_elefant = PrettyTable(['Denumire', 'Valoare'])
                        for i in range(0, 4):
                            table_elefant.add_row([Denumire[i], Valoare[i]])
                        print(table_elefant)

                        furnizor_client = table_elefant.get_string()

                        print(furnizor_client)
                        result = [tuple(filter(None, map(str.strip, splitline))) for line in furnizor_client.splitlines()
                                  for splitline in [line.split("|")] if len(splitline) > 1]

                        with open(file_to_write_to, 'w', newline='') as myfile:
                            wr = csv.writer(myfile)
                            wr.writerows(result)
                        with open(file_to_write_to, "r") as myfile:
                            self.results.configure(text=myfile.read())
 #################################################################################
                    else:
                        resultJson = procesare(self.entry.get())
                        print(resultJson)
                        

root = Tk()
root.iconbitmap("C:\\Users\\alexa\\OneDrive\\Desktop\\ProiectOCR\\Capture.ico")
root.title("Extrage datele facturii tale cu Fast OCR!")
root.geometry("800x500+200+100")
bg = PhotoImage(file="C:\\Users\\alexa\\OneDrive\\Desktop\\ProiectOCR\\background.png")
label = Label(root, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)
root.resizable(0, 0)
window = Window(root)
root.mainloop()