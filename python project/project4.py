from modulefinder import Module from select import select from pygame import CONTROLLERBUTTONDOWN 
 
# importing Module import tiknter as tk import datetime import winsound as ws 
 
# creating a countdown class class Countdown(tk.Frame):     def __init__(self,master):         super().__init__(master)         self.create_widgets()         self.show_widgets()         self.seconds_left=0         self._timer_on=False 
     def show_widgets(self):         self.label.pack()         self.entry.pack()         self.start.pack()         self.stop.pack()         self.reset.pack() 
     def create_wedgets(self): 
        self.label=tk.Label(self,text="Enter the time in second.")         self.entry=tk.Entry(self,Justify="sonter")         self.entry.focus_set()         self.reset=tk.Button(self,text="reset timer",command=self.reset_button)         self.stop= tk.Button(self,text="stop timer",command= self.stop_button)         self.start=tk.Button(self,text="start timer",command=self.start_button) 
     def countdown(self): 
        self.label1["text"]=self.convert_second_left_to_time() 
         if self.seconds_left:             self.seconds_left-=1             self._timer_on=self.after(1000,self.countdown) 
         else: 
            self._timer_on=False 
             def reset_button(self):         self.seconds_left=0         self.stop_timer()         self.label["text"]="Enter the timer in second."         self.start.forget()         self.stop.forget() 	
        self.reset.forget()         self.start.pack()         self.stop.pack()         self.reset.pack() 
     def stop_button(self):         self.seconds_left=int(self.entry.get())         self.stop_timer() 
     def start_button(self):         self.seconds_left=int(self.entry.get())         self.stop_timer()         self.countdown()         self.start.forget()         self.stop.forget()         self.reset.forget()         self.start.pack()         self.stop.pack()         self.reset.pack() 
     def stop_timer(self):         if self._timer_on: 
            self.after_candel(self._timer_on)             self._timer_on = False 
         def convert_seconds_left_to_time(self): 
        return datetime.timedelta(second=self.seconds_left)  
#main loop if __name__ == "__main__": 
    root=tk.Tk()     root.reaizable(False,False)     countdown=Countdown(root)     countdown.pack()     root.mainloop() 
 	

