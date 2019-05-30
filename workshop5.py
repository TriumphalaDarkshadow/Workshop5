"""Die Aufgabe Eurobanknoten aus dem Workshop05
    erstellt: 20.05.2019
    author: Sarah cutipie kawaiinekogirl
    
    Beschreibungstext
    Awesome python function to test if eurobanknotes are valid or not
    follow my dog on insta: @gremljung

"""

#hilfsfunktion die die anzahl der stellen einer zahl ermittelt
def stellenAnzahl(zahl):
    stelle = 0
    for x in str(zahl):
      stelle += 1

    return stelle


def test_seriennummer(tup):
    #iterieren durch Elemente des Tupels        
    for var in tup:

        quer_summe=0
        #Laenge des Strings, zwei Buchstaben am Anfang [0] und [1], Rest sind Ziffern[2] - [11]
        laenge_string = len(var)
 

        #Laenge des Strings muss 12 sein
        if laenge_string == 12:
#            print ("leange okay")
            erster_buchstabe = var[0]
            zweiter_buchstabe = var[1]

           

            #erste zwei Stellen muessen Buchstaben sein und der rest nur ziffern
            if type(erster_buchstabe) == str and type(zweiter_buchstabe) == str and var[2:].isdigit():
            #if buchstabe_erste_stelle == erster_buchstabe and buchstabe_zweite_stelle == zweiter_buchstabe:
                #ermitteln der Position der ersten beiden Buchstaben mithilfe der ASCII-Tabelle
                
                #ascii repreasentation der erste beiden buchstaben
                pos_erster_buchstabe = ord(erster_buchstabe)
                pos_zweiter_buchstabe = ord(zweiter_buchstabe)
                 
                #ascii repreasentation mit 64 abziehen um die eigentlihce position im alphabet zu bekommen
                string_erster_buchstabe = str(pos_erster_buchstabe-64 )
                string_zweiter_buchstabe = str(pos_zweiter_buchstabe-64)
                

                #mithilfe der hilfsfunktion die anzahl der stellen ermitteln
                stellen = stellenAnzahl(string_erster_buchstabe)
                stellen += stellenAnzahl(string_zweiter_buchstabe)
                
                #Erste zwei zahlen addieren
                quer_summe =  int(string_erster_buchstabe)    
                quer_summe +=  int(string_zweiter_buchstabe)
               
               
           
                #pruefziffern plus pruefzahl zur quersumme addieren 
                for i in var[2:]:
                    quer_summe += int(i)
                    
  
            # ueberpruefen ob der rest der division 7 ergibt und die anzahl der stellen kleiner als 5 ist
            if quer_summe % 9 == 7 and stellen < 5:
                print("Der String", var, "entspricht einer gültigen Seriennummer.")
                
            else:
                print("Der String", var , "Keine gueltige Seriennummer.")
                

        
        else:
            print("Der String", var, "entspricht keiner gültigen Seriennummer.")
            



tuple = ("VAZUI321", "VAZ473965038", "X80402108303", "XA0384560721", "XA0473965058",
                    "VA2237393612", "XA0473965038")

print(test_seriennummer(tuple))
#print(tuple)
