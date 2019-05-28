"""Die Aufgabe Eurobanknoten aus dem Workshop05
    erstellt: 20.05.2019
    author: ######
    
    Beschreibungstext
    

"""

def test_seriennummer(tup):
    #iterieren durch Elemente des Tupels        
    for var in tup:
        serien_string = (tup.index(var), var)
        print(serien_string)

        #Laenge des Strings, zwei Buchstaben am Anfang [0] und [1], Rest sind Ziffern[2] - [11]
        laenge_string = len(serien_string)
        buchstabe_erste_stelle = " "
        buchstabe_zweite_stelle = " "
        quer_summe = 0
        
        #Laenge des Strings muss 12 sein
        if laenge_string == 12:
            
            erster_buchstabe = serien_string[0]
            zweiter_buchstabe = serien_string[1]
            #erste zwei Stellen muessen Buchstaben sein
            if type(erster_buchstabe) == str and type(zweiter_buchstabe) == str:
            #if buchstabe_erste_stelle == erster_buchstabe and buchstabe_zweite_stelle == zweiter_buchstabe:
                #ermitteln der Position der ersten beiden Buchstaben mithilfe der ASCII-Tabelle
                pos_erster_buchstabe = ord(erster_buchstabe)
                pos_zweiter_buchstabe = ord(zweiter_buchstabe)
                
                print(pos_erster_buchstabe, " ", pos_zweiter_buchstabe)
                
                #int in String umwandeln
                string_erster_buchstabe = str(pos_erster_buchstabe)
                string_zweiter_buchstabe = str(pos_zweiter_buchstabe)
                
                #Iteriere durch den String
                for zifferBuchstabe in string_erster_buchstabe:
                    quer_summe = quer_summe + int(zifferBuchstabe)
                    
                for zifferBuchstabe in string_zweiter_buchstabe:
                    quer_summe = quer_summe + int(zifferBuchstabe)
                    
                print(quer_summe)
                
                #Rest String wird ausgegeben
                for i in range(2, len(serien_string)):
                    rest_string = str(serien_string[i])
                    
                    #Iteriere durch diesen Reststring
                    for e in rest_string:
                        quer_summe = quer_summe + int(e)

                print(quer_summe)

            #Quersummen-String in int umwandeln           
            int_quer_summe = int(quer_summe)
            
            if int_quer_summe / 9 == 7:
                print("Der String", serien_string, "entspricht einer gültigen Seriennummer.")
                
            else:
                print("Keine gueltige Seriennummer.")
                

        
        else:
            print("Der String", serien_string, "entspricht keiner gültigen Seriennummer.")
            

tuple = ("VAZUI321", "VAZ473965038", "X80402108303", "XA0384560721", "XA0473965058",
                    "VA2237393612", "XA0473965038")

print(test_seriennummer(tuple))
#print(tuple)