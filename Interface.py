from tkinter import * 
import threading, time



class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('QPC SESAME')
        self.root.geometry('1200x600')

    
    def __final__(self):
        self.root.mainloop()


class Intro(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        self.etat = True
        import anim
        self.etat = False  



if __name__ =='__main__':
    thread1 = Intro()
    thread1.start()
    time.sleep(2)

    while thread1.etat: # J'attend que le thread s'arrete
        time.sleep(0.1)    
    
    print('hello guys')

    fen = Interface()
    fen.__final__()
    