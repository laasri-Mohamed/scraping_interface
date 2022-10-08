import random
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import back
import csv
from ttkbootstrap import *
from datetime import datetime


 
 
class window:
     
    def __init__(self, root, geo, title) -> None:
        self.root = root
        self.root.title(title)
        self.root.geometry(geo)
        self.root.resizable(width=False, height=False)
 
        
        Label(self.root, text='Url').grid(row=0, column=0, padx=10, pady=10)
        
        
        self.url = StringVar()
      
        ttk.Entry(self.root, width=55, textvariable=self.url
                 ).grid(row=0, column=1, padx=4, pady=4)
        ttk.Entry(self.root, width=30, textvariable=self.data
                 ).grid(row=8, column=1, padx=4, pady=4)
        self.length = StringVar()
 
        

        ttk.Button(self.root, text='Search', width=20, style='danger.TButton',
                   padding=5, command=self.search).grid(row=5, column=2)
        ttk.Button(self.root, text='view', width=20, padding=5,style='success.TButton',
                   command=self.view).grid(row=5, column=0)
        ttk.Button(self.root, text='Data', width=20, padding=5,style='success.TButton',
                   command=self.data).grid(row=6, column=1)
    
 
        # ========self.tree view=============
        self.tree = ttk.Treeview(self.root, height=10)
        

        self.tree['columns'] = ('nom', 'adresse','ville','numero')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('nom', width=220, anchor=W)
        self.tree.column('adresse', width=700, anchor=W)
        self.tree.column('ville', width=150, anchor=W)
        self.tree.column('numero', width=270, anchor=W)
        self.tree.heading('#0', text='')
        self.tree.heading('nom', text='Nom')
        self.tree.heading('adresse', text='Adresse')
        self.tree.heading('ville', text='Ville')
        self.tree.heading('numero', text='Numéro')
 
        self.tree.grid(row=4, column=0, columnspan=3, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.catch)
        #  cette commande appellera la fonction catch
 
        # ceci est le menu contextuel du clic droit
        self.menu = Menu(self.root, tearoff=False)
        self.menu.add_command(label='Update', command=self.update)
        self.menu.add_separator()
        self.menu.add_command(label='Clear Fields', command=self.clear)
        self.menu.add_command(label='Clear Table', command=self.table)
        self.menu.add_command(label='Export', command=self.export)
        self.menu.add_separator()
        self.menu.add_command(label='Help', command=self.help)
        self.menu.add_separator()
        self.menu.add_command(label='Exit', command=self.root.quit)
        # ceci lie le bouton 3 de la souris avec
        self.root.bind("<Button-3>", self.poppin)
        # fonction poppin
 
    def help(self):
        # cette fonction ouvrira le fichier help.txt dans
        #  bloc-notes lorsqu'il est appelé
        webbrowser.open('help.txt')
 
    def refresh(self):
        # cette fonction rafraîchit essentiellement la table
        # ou arborescence
        self.table()
        self.view()
        self.data()
 
    def table(self):
        # cette fonction effacera toutes les valeurs
        # affiché dans le tableau
        for r in self.tree.get_children():
            self.tree.delete(r)
 
    def clear(self):
        # cette fonction effacera toutes les entrées
        # des champs
        self.nom.set('')
        self.adresse.set('')
        #self.ville.set('')
        #self.numero.set('')
    
    def poppin(self, e):
        # il déclenche le menu contextuel du clic droit
        self.menu.tk_popup(e.x_root, e.y_root)
 
    def catch(self, event):
        # cette fonction prendra toutes les données sélectionnées
        # e la table/arborescence et remplira le
        # champs de saisie respectifs
        self.nom.set('')
        self.adresse.set('')
        selected = self.tree.focus()
        value = self.tree.item(selected, 'value')
        self.nom.set(value[0])
        self.adresse.set(value[1])
        self.ville.set(value[2])
        self.numero.set(value[3])
 
    def update(self):
        # cette fonction mettra à jour la base de données avec de nouveaux
        # valeurs données par l'utilisateur
        selected = self.tree.focus()
        value = self.tree.item(selected, 'value')
        back.edit(self.nom.get(), self.adresse.get(),self.ville.get(),self.numero.get())
        self.refresh()
 
    def view(self):
        # cela affichera toutes les données de la base de données
        # ceci est similaire à "SELECT * FROM TABLE" sql
    
        if back.check() is False:
            messagebox.showerror('Attention Amigo!', 'Database is EMPTY!')
        else:
            for row in back.show():
                self.tree.insert(parent='', text='', index='end',
                                 values=(row[0], row[1], row[2], row[3]))
 
    def erase(self):
        # cela supprimera ou supprimera le tuple sélectionné ou
        # ligne de la base de données
        selected = self.tree.focus()
        value = self.tree.item(selected, 'value')
        back.Del(value[1])
        self.refresh()
 
    def save(self):
        # cette fonction insèrera toutes les données dans le
        # base de données
        back.enter(self.date.get(), self.pa.get())
        self.tree.insert(parent='', index='end', text='',
                         values=(self.date.get(), self.pa.get()))
    
    def data():
        back.data()
    def nom(self):
        back.NOM()
    def adresse(self):
        back.ADRESSE()
    def ville(self):
        back.VILLE()
    def numero(self):
        back.Numero()



    def search(self):
        back.URL(self.url.get())
        messagebox.showerror('Attention Amigo!', 'le scraping est fini')

    def export(self):
        # cette fonction sauvegardera toutes les données du
        # base de données au format csv qui peut être ouvert
        # dans excel

        pop = Toplevel(self.root)
        pop.geometry('300x100')
        self.v = StringVar()
        Label(pop, text='Save File Name as').pack()
        ttk.Entry(pop, textvariable=self.v).pack()
        ttk.Button(pop, text='Save', width=18,
                   command=lambda: exp(self.v.get())).pack(pady=5)
 
        def exp(x):
            with open(x + '.csv', 'w', newline='') as f:
                chompa = csv.writer(f, dialect='excel')
                for r in back.show():
                    chompa.writerow(r)
            messagebox.showinfo("File Saved", "Saved as " + x + ".csv")
 
 
if __name__ == '__main__':
    win = Style(theme='darkly').master
    name = 'Entreprise DATA'
    dimension = '1400x600'
 
    app = window(win, dimension, name)
    win.configure(bg='#7FFF00')
    win.mainloop()