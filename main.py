import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv


def adat_bevitel():
    elfogadva = elfogadva_valtozo.get()

    if elfogadva == "Elfogadva":
        # Felhasználói információk
        vezeteknev = vezeteknev_bevitel.get()
        keresztnev = keresztnev_bevitel.get()

        if vezeteknev and keresztnev:
            titulus = titulus_valasztobox.get()
            eletkor = eletkor_valasztospinbox.get()
            nemzetiseg = nemzetiseg_valasztobox.get()

            # Tanfolyami információk
            regisztracio_statusz = regisztracio_statusz_valtozo.get()
            tanfolyamszam = tanfolyamszam_valasztospinbox.get()
            szemeszterszam = szemeszterszam_valasztospinbox.get()

            # Fájlba írás
            with open('Hallgatok.csv', 'a', newline='') as csvfile:
                fieldnames = ['vezeteknev', 'keresztnev', 'titulus', 'eletkor', 'nemzetiseg', 'regisztracio_statusz', 'tanfolyamszam', 'szemeszterszam']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({
                    'vezeteknev': vezeteknev,
                    'keresztnev': keresztnev,
                    'titulus': titulus,
                    'eletkor': eletkor,
                    'nemzetiseg': nemzetiseg,
                    'regisztracio_statusz': regisztracio_statusz,
                    'tanfolyamszam': tanfolyamszam,
                    'szemeszterszam': szemeszterszam
                })
        else:
            tkinter.messagebox.showwarning(title="Hiba", message="A vezetéknév és a keresztnév megadása kötelező.")
    else:
        tkinter.messagebox.showwarning(title="Hiba", message="Nem fogadta el a feltételeket")

ablak = tkinter.Tk()
ablak.title("Adatbeviteli Űrlap")

keret = tkinter.Frame(ablak)
keret.pack()

# Felhasználói információk mentése
felhasznaloi_info_keret = tkinter.LabelFrame(keret, text="Felhasználói Információ")
felhasznaloi_info_keret.grid(row=0, column=0, padx=20, pady=10)

vezeteknev_cimke = tkinter.Label(felhasznaloi_info_keret, text="Vezetéknév")
vezeteknev_cimke.grid(row=0, column=0)
keresztnev_cimke = tkinter.Label(felhasznaloi_info_keret, text="Keresztnév")
keresztnev_cimke.grid(row=0, column=1)

vezeteknev_bevitel = tkinter.Entry(felhasznaloi_info_keret)
keresztnev_bevitel = tkinter.Entry(felhasznaloi_info_keret)
vezeteknev_bevitel.grid(row=1, column=0)
keresztnev_bevitel.grid(row=1, column=1)

titulus_cimke = tkinter.Label(felhasznaloi_info_keret, text="Titulus")
titulus_valasztobox = ttk.Combobox(felhasznaloi_info_keret, values=["", "Úr.", "Hölgy.", "Dr."])
titulus_cimke.grid(row=0, column=2)
titulus_valasztobox.grid(row=1, column=2)

eletkor_cimke = tkinter.Label(felhasznaloi_info_keret, text="Életkor")
eletkor_valasztospinbox = tkinter.Spinbox(felhasznaloi_info_keret, from_=18, to=110)
eletkor_cimke.grid(row=2, column=0)
eletkor_valasztospinbox.grid(row=3, column=0)

nemzetiseg_cimke = tkinter.Label(felhasznaloi_info_keret, text="Nemzetiség")
nemzetiseg_valasztobox = ttk.Combobox(felhasznaloi_info_keret,
                                      values=["Afrika", "Magyar", "Ázsia", "Európa", "Észak-Amerika", "Óceánia",
                                              "Dél-Amerika"])
nemzetiseg_cimke.grid(row=2, column=1)
nemzetiseg_valasztobox.grid(row=3, column=1)

for widget in felhasznaloi_info_keret.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Tanfolyami információk mentése
tanfolyamok_keret = tkinter.LabelFrame(keret)
tanfolyamok_keret.grid(row=1, column=0, sticky="news", padx=20, pady=10)

regisztralt_cimke = tkinter.Label(tanfolyamok_keret, text="Regisztrációs Státusz")

regisztracio_statusz_valtozo = tkinter.StringVar(value="Nem Regisztrált")
regisztralt_jelolonegyzet = tkinter.Checkbutton(tanfolyamok_keret, text="Jelenleg Regisztrált",
                                                variable=regisztracio_statusz_valtozo, onvalue="Regisztrált",
                                                offvalue="Nem regisztrált")

regisztralt_cimke.grid(row=0, column=0)
regisztralt_jelolonegyzet.grid(row=1, column=0)

tanfolyamszam_cimke = tkinter.Label(tanfolyamok_keret, text="Befejezett Tanfolyamok")
tanfolyamszam_valasztospinbox = tkinter.Spinbox(tanfolyamok_keret, from_=0, to=100)
tanfolyamszam_cimke.grid(row=0, column=1)
tanfolyamszam_valasztospinbox.grid(row=1, column=1)

szemeszterszam_cimke = tkinter.Label(tanfolyamok_keret, text=" Szemeszterek")
szemeszterszam_valasztospinbox = tkinter.Spinbox(tanfolyamok_keret, from_=0, to=100)
szemeszterszam_cimke.grid(row=0, column=2)
szemeszterszam_valasztospinbox.grid(row=1, column=2)

for widget in tanfolyamok_keret.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Feltételek elfogadása
feltetelek_keret = tkinter.LabelFrame(keret, text="Feltételek & Kondíciók")
feltetelek_keret.grid(row=2, column=0, sticky="news", padx=20, pady=10)

elfogadva_valtozo = tkinter.StringVar(value="Nem Elfogadva")
feltetelek_jelolonegyzet = tkinter.Checkbutton(feltetelek_keret, text="Elfogadom a feltételeket és kondíciókat.",
                                               variable=elfogadva_valtozo, onvalue="Elfogadva",
                                               offvalue="Nem Elfogadva")
feltetelek_jelolonegyzet.grid(row=0, column=0)

# Gomb
gomb = tkinter.Button(keret, text="Adatbevitel", command=adat_bevitel)
gomb.grid(row=3, column=0, sticky="news", padx=20, pady=10)

ablak.mainloop()
