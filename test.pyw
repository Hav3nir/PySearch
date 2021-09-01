from io import open_code
from os import close, name, system, waitpid
from time import sleep
from tkinter import *

if name  == "nt":
    system("color 7")
    def clear():
        clear()
else:
    def clear():
        system("clear")
def pip():
    system("pip install selenium")
    sleep(5)
    s.destroy
try:
    import selenium
    print("Modules installés, démarrage du navigateur")
except:
    s = Tk()
    s.title("Outil de recherche google !")
    s.geometry("500x150")
    label = Label(s, fg="red", text="Modules non-installés. Voulez-vous les installer ?")
    label.pack()
    btn = Button(s, text="Oui", command=pip)
    btn.pack()
    btn2 = Button(s, text="Non", command=s.destroy)
    btn2.pack()
    s.mainloop()
        
def main():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    import time
    now = time.localtime(time.time())
    heure = time.strftime("%y/%m/%d|%H:%M", now)
    if my_entry.get() == "":
        label = Label(root, fg="red", text="Erreur, aucun mot sasie !")
        label.pack()        
        return
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options = options)
    driver.get("http://google.com/")
    button = driver.find_element_by_id("L2AGLb")
    button.click()
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(my_entry.get())
    elem.send_keys(Keys.ENTER)
    sleep(3)
    url = driver.current_url
    fichier = open("urls.txt", "a")
    fichier.write(heure + " website url: " + url + "\n")
    fichier.close()
    f = open(my_entry.get() + ".txt", "w")
    all_titles = driver.find_elements_by_tag_name("h3")
    for title in all_titles:
        f.write(title.text + "\n")
    f.close()
    label = Label(root, fg="green", text="Recherche terminé et enregistrée")
    label.pack()
    driver.close()
    

root = Tk()
root.title("Outil de recherche google !")
root.geometry("500x150")
my_entry = Entry(root)
my_entry.pack()
btn = Button(root, text="Lancer la recherche", command=main)
btn.pack()
btn2 = Button(root, text="Quitter", command=root.destroy)
btn2.pack()
root.mainloop()
