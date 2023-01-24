import csv

class Funciones():

    def __init__(self) -> None:
        try:
            with open('mengano/OC.csv', 'w', newline='') as csvfile:
                fieldnames=['ID','Usuario','Sector','OC']
                writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
                
        except Exception as e:
            print(e)
    
    def conexionBBDD():
        
