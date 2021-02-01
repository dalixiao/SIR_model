import tkinter
import threading
CANVAS_SIZE = 500
PERSON_SIZE = 4
POPULATION_SIZE = 100
from backend import Population
class Interface:
    def __init__(self):
        self.root = tkinter.Tk()
        #self.root.Title("SIR MODEL SIMULATION")
        self.set_input_box()
        self.canvas = tkinter.Canvas(self.root,width = CANVAS_SIZE, height = CANVAS_SIZE)
        self.canvas.pack(side = 'top')
        self.population = Population(POPULATION_SIZE,CANVAS_SIZE)
        self.draw_people()
        self.startButton = tkinter.Button(self.root,text = "start",command = self.start)
        self.startButton.pack(expand = 'yes')
        self.root.mainloop()

    def set_input_box(self):
        label1 = tkinter.Label(self.root,text="Population Size:").pack(side = 'top',expand = 'yes',anchor = 'ne')
        entry1 = tkinter.Entry(self.root,textvariable =tkinter.StringVar(self.root,value = 10000),width=8).pack(after = label1,side = 'top',expand = 'no',anchor = 'ne')
        label2 = tkinter.Label(self.root,text="Person Moving Speed:").pack(side = 'top',expand = 'yes',anchor = 'ne')
        entry2 = tkinter.Entry(self.root,width = 8).pack(after = label2,side = 'top',expand ='no',anchor = 'ne')
        label3 = tkinter.Label(self.root,text="Person Moving Range:").pack(side = 'top',expand = 'yes',anchor = 'ne')
        entry3 = tkinter.Entry(self.root,width = 8).pack(after = label1,side = 'top',expand = 'no',anchor = 'ne')
        label4 = tkinter.Label(self.root,text="Susceptible Intimacy Range:").pack(side = 'top',expand = 'yes',anchor = 'ne')
        entry4 = tkinter.Entry(self.root,width = 8).pack(after = label1,side = 'top',expand = 'no',anchor = 'ne')
        label5 = tkinter.Label(self.root,text="Recover Count Down:").pack(side = 'top',expand = 'yes',anchor = 'ne')
        entry5 = tkinter.Entry(self.root,width = 8).pack(after = label1,side = 'top',expand = 'no',anchor = 'ne')
        label6 = tkinter.Label(self.root,text="Initial Infected Size:").pack(side = 'top',expand = 'yes',anchor = 'ne')
        entry6 = tkinter.Entry(self.root,width = 8).pack(after = label1,side = 'top',expand = 'no',anchor = 'ne')
        label7 = tkinter.Label(self.root,text="Infection Rate:").pack(side = 'top',expand = 'yes',anchor = 'ne')
        entry7 = tkinter.Entry(self.root,width = 8).pack(after = label1,side = 'top',expand = 'no',anchor = 'ne')
    def draw_people(self):
        for person in self.population.people:
            x_loc = person.current_location.x
            y_loc = person.current_location.y
            status = person.status
            self.canvas.create_rectangle(x_loc-PERSON_SIZE/2,y_loc-PERSON_SIZE/2,x_loc+PERSON_SIZE/2,y_loc+PERSON_SIZE/2,fill = status)

    def next_frame(self):
        self.canvas.delete("all")
        self.population.people_move()
        self.draw_people()
        self.root.after(50,self.next_frame)
        print(self.population.day,self.population.infected_num)

    def start(self):
        self.root.after(50,self.next_frame)


if __name__ == "__main__":
    interface = Interface()

    #interface.start()
