#DLL 

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.start=None
        self.end=None

    def creation(self,val):
        newnode=Node(val)
        newnode.next=None
        newnode.prev=None
        self.start=newnode
        self.end=newnode
        print("DLL has been created")
    
        

    def insertion(self,value):#only from left side 
        newnode=Node(value)
        newnode.next=self.start
        self.start.prev=newnode#without creating self.start, it  is null so it throw an error since None.prev is not quite right to look up
        self.start=newnode
    def traverse(self):
        tmp=self.start
        if self.start==None:
            print("linked list is empty")
            return
        else:
            while tmp is not None: 
                print(tmp.value)
                tmp=tmp.next
                

    def deletion(self):#only from left side
        tmp=self.start
        if self.start==None:
            print("can't delete empty linked list")
            return
        else:
            self.start=tmp.next
            print("deleted item is ",tmp.value)

    def search(self,ele):
        tmp=self.start
        if tmp.value == ele:
            print("data found")
        else:
            print("not found the data you want to search")
            
        
            
def main():
    s=DLL()

    while True:
        print("****MENU****")
        print("1.create a first DLL element \n 2.insert \n 3.traverse \n 4.delete \n 5.search \n 6.delete")
        a=int(input("enter any choice: "))
        if a==1:
            b=input("enter a element to push: ")
            s.creation(a)
        elif a==2:
            c=input("enter data element: ")
            s.insertion(c)
        
        elif a==3:
            s.traverse()
        elif a==4:
            s.deletion()
        elif a==5:
            d=input("enter element to search: ")
            s.search(d)
        else:
            return

if __name__=="__main__":
    main()

    # s.creation(20)
    # s.insertion(50)
    # s.insertion(60)
    # s.traverse()
    # s.deletion()
    # s.traverse()


