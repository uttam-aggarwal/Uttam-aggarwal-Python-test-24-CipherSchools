class Classy:
    def __init__(self,items):
        self.items=items
    def getclassiness(self):
        count=0
        count+=2*self.items.count("tophat")
        count+=4*self.items.count("bowtie")
        count+=5*self.items.count("monocle")
        return count
    def addItem(self,new_item):self.items.append(new_item)
items=[]
me=Classy(items)
while True:
    print("0.Exit","1.add another item","2.see your classiness points",sep="\n")
    select=int(input("select: "))
    if select==0:
        print("-"*20,"EXIT","-"*20)
        break
    if select==1:
        a=input("ENTER: ").lower()
        me.addItem(a)
    if select==2:print("your classiness point is ",me.getclassiness())
    print("-"*40)