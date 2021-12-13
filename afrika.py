#HOZZ LÉTRE EGY LISTÁT ÉS A TARTALMÁT ÍRD KI AZ AFRIKA.TXT ÁLLOMÁNYBA

afrika=["párduc", "oroszlán", "gorilla", "makákó", "bambusznád", "majomkenyérfa", "kókuszdió"]
celfajl=open("afrika.txt" ,"w", encoding="utf-8")
afrika.append("szavannák")
afrika.append("fekete nők")
for elem in afrika:
            print(elem,file=celfajl)
celfajl.close()

