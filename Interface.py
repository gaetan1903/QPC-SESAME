from tkinter import * 
import threading 



class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('QPC SESAME')
        self.root.mainloop()
    


class Fenetre(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        fen = Interface()

class Intro(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        import anim  


if __name__ =='__main__':
    thread1 = Intro()
    thread2 = Fenetre()
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    