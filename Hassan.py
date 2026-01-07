
from tkinter import *
from tkinter import colorchooser
#import PIL.ImageGrab as ImageGrab
from PIL import ImageGrab
from tkinter import filedialog
from PIL import Image,ImageDraw,ImageTk






class PaintApp:
    def __init__(self,width,height,title):
       self.screen=Tk()
       self.screen.title=(title)
       self.screen.geometry(str(width)+'x'+str(height))
       self.screen.resizable(False,False)
       self.zoom_scale = 1.0
       self.min_zoom_scale = 0.5
       self.max_zoom_scale = 2.0
       self.start_x = None
       self.start_y = None
       self.end_x = None
       self.end_y = None
       self.size=IntVar()
       self.size.set(1)
       self.brush_color="black"
       self.fill_color = "white"
       self.last_x,self.last_y=None,None
       self.shape_Id=None
       self.undo = []
       selected_region = None
       selected_image = None


      
       # Frame_1
       self.frame_1=Frame(self.screen,height=150,width=1000,bg="grey")
       self.frame_1.grid(row=0,column=0)
       # Frame_2
       
       self.frame_2=Frame(self.frame_1,height=150,width=120,bg="brown",relief="solid",borderwidth=5,highlightbackground="red")
       self.frame_2.grid(padx=5,pady=5)
       self.frame_2.grid(row=0,column=0)
     
       #Frame_3
       self.frame_3=Frame(self.frame_1,height=150,width=120,bg="cyan",relief="solid",borderwidth=5)
       self.frame_3.grid(padx=5,pady=5)
       self.frame_3.grid(row=0,column=1)
       heading = Label(self.frame_3, text="Tools", font=("Arial", 10, "bold"))
       heading.place(relx=0.5,rely=1.0,anchor="s")
       #Frame_4
       self.frame_4=Frame(self.frame_1,height=150,width=300,bg="magenta",relief="solid",borderwidth=5)
       self.frame_4.grid(padx=5,pady=5)
       self.frame_4.grid(row=0,column=2)
       heading = Label(self.frame_4, text="Shapes", font=("Arial", 10, "bold"))
       heading.place(relx=0.5,rely=1.0,anchor="s")
       #Frame_5
       self.frame_5=Frame(self.frame_1,height=150,width=100,bg="pink",relief="solid",borderwidth=5)
       self.frame_5.grid(padx=5,pady=5)
       self.frame_5.grid(row=0,column=3)
    #    heading = Label(self.frame_5, text="Width", font=("Arial", 10, "bold"))
    #    heading.place(relx=0.5,rely=1.0,anchor="s")

       #Frame_6
       self.frame_6=Frame(self.frame_1,height=150,width=300,bg="light green",relief="solid",borderwidth=5)
       self.frame_6.grid(padx=5,pady=5)
       self.frame_6.grid(row=0,column=4)
       heading = Label(self.frame_6, text="Colors", font=("Arial", 12, "bold"))
       heading.place(relx=0.1,rely=1,anchor="sw")

    

                               

        # Treat as single unit
    #    def on_click(event):
           
    #       start_x = event.x
    #       start_y = event.y

    #    def on_release(event):
        
    #       end_x = event.x
    #       end_y = event.y
          
    #    def on_selection_click(event):
    # # Handle click events on the selection item
    # # You can treat the selection as a single unit here
    #       print("Selection clicked")

    #    self.canvas.bind("<Button-1>", on_click)
    #    self.canvas.bind("<ButtonRelease-1>", on_release)
    #    selection_item = self.canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, outline='red', tags='selection')
    #    self.canvas.tag_bind(selection_item, '<Button-1>', on_selection_click)

       

       # Reset button
       clear_image = Image.open("Button_clear_1.png")
       resized_image = clear_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.reset_button=Button(self.frame_1,image=photo,command=self.Reset_All)
       self.reset_button.image = photo
       self.reset_button.place(x=145,y=75)
      
       # Pencil
       pencil_image = Image.open("Button_pencil.png")
       resized_image = pencil_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.pencil=Button(self.frame_1,image=photo,command=self.pencil_pressed)
       self.pencil.image = photo
       self.pencil.place(x=145,y=20)
       # Erasor 
       erase_image = Image.open("Button_erasor_1.png")
       resized_image = erase_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.erase=Button(self.frame_1,image=photo,command=self.erase_pressed)
       self.erase.image = photo
       self.erase.place(x=200,y=20)
       # Color Button
       color_image = Image.open("w6.jpg")
       resized_image = color_image.resize((130,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.color=Button(self.frame_1,image=photo,command=self.color_pressed)
       self.color.image = photo
       self.color.place(x=830,y=110)

       # Default Button
       self.default=Button(self.frame_1,text="Width",command=self.options)
       self.default.place(x=600,y=18)
       # Canvas Button
       self.canvas = Button(self.frame_1,text="Canvas",command=self.canvas_color)
       self.canvas.place(x=600,y=50)
       # circle Button
       circle_image = Image.open("Button_circles.png")
       resized_image = circle_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.circle=Button(self.frame_1,image=photo,command=self.circle_pressed)
       self.circle.image = photo
       self.circle.place(x=273,y=20)
       
       # Straight  Button
       line_image = Image.open("Button_line.png")
       resized_image = line_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.line=Button(self.frame_1,image=photo,command=self.straight_line_pressed)
       self.line.image = photo
       self.line.place(x=273,y=70) 
       # Hexagon Button
       hexagon_image = Image.open("Button_hexagon.png")
       resized_image = hexagon_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.hexagon=Button(self.frame_1,image=photo,command=self.hexagon_pressed)
       self.hexagon.image = photo
       self.hexagon.place(x=320,y=20)
       # Rectangle Button
       rectangle_image = Image.open("Button_rectangle.png")
       resized_image = rectangle_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.rectangle = Button(self.frame_1,image=photo,command=self.rectangle_pressed)
       self.rectangle.image = photo
       self.rectangle.place(x=370,y=20)
       # Oval Button
       oval_image = Image.open("Button_oval.png")
       resized_image = oval_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.oval = Button(self.frame_1,image=photo,command=self.oval_pressed)
       self.oval.image = photo
       self.oval.place(x=320,y=70)
       # Triangle Button
       triangle_image = Image.open("Button_triangle.png")
       resized_image = triangle_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.triangle = Button(self.frame_1,image=photo,command=self.triangle_pressed)
       self.triangle.image = photo
       self.triangle.place(x=370,y=70)
       # Pentagon Button
       pentagon_image = Image.open("Button_pentagon.png")
       resized_image = pentagon_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.pentagon = Button(self.frame_1,image=photo,command=self.pentagon_pressed)
       self.pentagon.image = photo
       self.pentagon.place(x=420,y=70)
       # Star Button
       star_image = Image.open("Button_star.png")
       resized_image = star_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.star=Button(self.frame_1,image=photo,command=self.star_pressed)
       self.star.image = photo
       self.star.place(x=420,y=20)

       # picker Button
       picker_image = Image.open("Button_picker.png")
       resized_image = picker_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.picker=Button(self.frame_1,image=photo,command=self.picker_pressed)
       self.picker.image = photo
       self.picker.place(x=15,y=75)
       # Save Button
       save_image = Image.open("Button_save_1.png")
       resized_image = save_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.save=Button(self.frame_1,image=photo,command=self.save_image)
       self.save.image = photo
       self.save.place(x=15,y=20)
       # Load Button
       load_image = Image.open("Button_load.png")
       resized_image = load_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.load=Button(self.frame_1,image=photo,command=self.load_image)
       self.load.image = photo
       self.load.place(x=70,y=20)
       # Hp Button
       hp_image = Image.open("Button_heptagon.png")
       resized_image = hp_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.hp = Button(self.frame_1,image=photo,command=self.hp_pressed)
       self.hp.image = photo
       self.hp.place(x=470,y=20)
      # Oc Button
       oc_image = Image.open("Button_octagon.png")
       resized_image = oc_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.oc = Button(self.frame_1,image=photo,command=self.oc_pressed)
       self.oc.image = photo
       self.oc.place(x=520,y=20)
       # Na Button
       na_image = Image.open("Button_nanogon.png")
       resized_image = na_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.na = Button(self.frame_1,image=photo,command=self.na_pressed)
       self.na.image = photo
       self.na.place(x=470,y=70)
       # Dc Button
       dc_image = Image.open("Button_decagon.png")
       resized_image = dc_image.resize((30,20))
       photo = ImageTk.PhotoImage(resized_image)
       self.dc = Button(self.frame_1,image=photo,command=self.dc_pressed)
       self.dc.image = photo
       self.dc.place(x=520,y=70)
       # Fill button
       fill_image = Image.open("Button_bucket.png")
       resized_image = fill_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.fill = Button(self.frame_1,image=photo)
       self.fill.image = photo
       self.fill.place(x=200,y=75)
       self.is_fill_pressed = False
       self.fill.config(command=self.yes_no_pressed)
       # Selected color show
       self.clr = Button(self.frame_1,width=10,height=3,bg="black",command=self.show_color)
       self.clr.place(x=585,y=85)
       self.clr.invoke()
       self.frame_1.bind("<Button-1>",self.show_color)
       self.screen.after(1000,self.show_color)
       # UNDO BUTTON
       undo_image = Image.open("Button_undo.png")
       resized_image = undo_image.resize((40,30))
       photo = ImageTk.PhotoImage(resized_image)
       self.undo_button = Button(self.frame_1,image=photo,command=self.undo_pressed)
       self.undo_button.image = photo
       self.undo_button.place(x=70,y=75)
       # AREA SELECTION BUTTON
       self.area_button=Button(self.frame_1,text="area",command=self.area_pressed)
       self.area_button.place(x=273,y=120)

 

       # OUTLINES BUTTONS
      
       self.Red_color=Button(self.frame_1,height=1,width= 5,command=self.Red_outline)
       self.Red_color.place(x=695,y=20)
       self.Red_color.config(bg="red")

       self.Blue_color=Button(self.frame_1,height=1,width= 5,command=self.Blue_outline)
       self.Blue_color.place(x=740,y=20)
       self.Blue_color.config(bg="blue")
       
       self.Green_color=Button(self.frame_1,height=1,width= 5,command=self.Green_outline)
       self.Green_color.place(x=785,y=20)
       self.Green_color.config(bg="green")

       self.Purple_color=Button(self.frame_1,height=1,width= 5,command=self.Purple_outline)
       self.Purple_color.place(x=830,y=20)
       self.Purple_color.config(bg="purple")

       self.Yellow_color=Button(self.frame_1,height=1,width= 5,command=self.Yellow_outline)
       self.Yellow_color.place(x=875,y=20)
       self.Yellow_color.config(bg="yellow")

       self.Brown_color=Button(self.frame_1,height=1,width= 5,command=self.Brown_outline)
       self.Brown_color.place(x=920,y=20)
       self.Brown_color.config(bg="brown")

       self.Grey_color=Button(self.frame_1,height=1,width= 5,command=self.Grey_outline)
       self.Grey_color.place(x=695,y=70)
       self.Grey_color.config(bg="grey")

       self.Cyan_color=Button(self.frame_1,height=1,width= 5,command=self.Cyan_outline)
       self.Cyan_color.place(x=740,y=70)
       self.Cyan_color.config(bg="cyan")

       self.Orange_color=Button(self.frame_1,height=1,width= 5,command=self.Orange_outline)
       self.Orange_color.place(x=785,y=70)
       self.Orange_color.config(bg="orange")

       self.Light_blue_color=Button(self.frame_1,height=1,width= 5,command=self.Light_blue_outline)
       self.Light_blue_color.place(x=830,y=70)
       self.Light_blue_color.config(bg="light blue")

       self.Pink_color=Button(self.frame_1,height=1,width= 5,command=self.Pink_outline)
       self.Pink_color.place(x=875,y=70)
       self.Pink_color.config(bg="pink")

       self.Blue_Grey_color=Button(self.frame_1,height=1,width= 5,command=self.Blue_Grey_outline)
       self.Blue_Grey_color.place(x=920,y=70)
       self.Blue_Grey_color.config(bg="magenta")
     
         # CANVAS
       self.canvas_bg = "white"
       self.canvas = Canvas(self.screen, height=450, width=1000, bg=self.canvas_bg)
       self.canvas.grid(row=1, column=0)
       

       # Fill color of shapes
       self.fill_shape_color = self.canvas_bg

       # ZOOM bind
       self.zoom = self.canvas.bind("<MouseWheel>",self.zoom)

    def canvas_color(self):
        self.options = ["White","Black","Blue","Red","Purple","Green"]
        
        self.size_1 = StringVar(self.screen)
       # self.size_1.set("Black")
        self.size_1list = OptionMenu(self.frame_1,self.size_1,*self.options,command=self.color_selected)
        self.size_1list.grid(row=0,column=3)
        self.size_1list.place(x=600,y=60)

    # YES NOT FILL PRESSED
    def yes_no_pressed(self):
        self.is_fill_pressed = not self.is_fill_pressed


    def color_selected(self,selection):
        self.size_1list.destroy()
        if(selection == "White"):
            self.canvas_bg = "white"
            self.fill_shape_color = self.canvas_bg
            self.canvas.delete("all")
        elif(selection == "Black"):
            self.canvas_bg = "black"
            self.fill_shape_color = self.canvas_bg
            self.canvas.delete("all")
        elif(selection == "Blue"):
            self.canvas_bg = "blue"
            self.fill_shape_color = self.canvas_bg
            self.canvas.delete("all")
        elif(selection == "Green"):
            self.canvas_bg = "green"
            self.fill_shape_color = self.canvas_bg
            self.canvas.delete("all")
        elif(selection == "Red"):
            self.canvas_bg = "red"
            self.fill_shape_color = self.canvas_bg
            self.canvas.delete("all")
        elif(selection == "Purple"):
            self.canvas_bg = "purple"
            self.fill_shape_color = self.canvas_bg
            self.canvas.delete("all")

        self.canvas.config(bg=self.canvas_bg)    
 

    # def options(self):
    #     self.choices=[1,2,3,4,5,7,8,9,10]
    #     self.sizelist=OptionMenu(self.frame_1,self.size,*self.choices)
    #     self.sizelist.grid(row=0,column=3)

    def options(self):
        self.choices=[1,2,3,4,5,7,8,9,10]
        self.sizelist=OptionMenu(self.frame_1,self.size,*self.choices,command=self.size_selected)
        self.sizelist.grid(row=0,column=3)
        self.sizelist.place(x=600,y=20)

    def size_selected(self,selection):
        self.sizelist.destroy()

    def area_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.create_area)
        self.canvas.bind("<ButtonRelease-1>",self.end_area)

    def create_area(self,event):
        if self.shape_Id is not None:
            self.canvas.delete(self.shape_Id)

        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y
            return 
        self.shape_Id = self.canvas.create_rectangle(self.last_x,self.last_y,event.x,event.y,width=1,outline="black",fill="")
       # self.undo.append(self.shape_Id)

    def end_area(self,event):
        x = IntVar()
        y = IntVar()
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()

        x1 = self.last_x
        y1 = self.last_y
        x2 = event.x
        y2 = event.y
        if(x1 > x2):
            x1,x2 = x2, x1
        if(y1 > y2):
            y1, y2 = y2, y1

        self.image = ImageGrab.grab(bbox=(x1,y1,x2,y2))
      #  self.image.show()
        items_in_region = self.canvas.find_overlapping(x1,y1,x2,y2)
        self.canvas.delete(*items_in_region) 
        self.canvas.delete(self.shape_Id)
        self.last_x,self.last_y = None,None
        self.shape_Id = None   
  
            
          
    

    def Red_outline(self):
        self.brush_color="red"
        self.fill_color="red"
    def Blue_outline(self):
        self.brush_color="blue"
        self.fill_color = "blue"
    def Green_outline(self):
        self.brush_color="green"
        self.fill_color="green"
    def Brown_outline(self):
        self.brush_color="brown"
        self.fill_color="brown"
    def Yellow_outline(self):
        self.brush_color="yellow"
        self.fill_color="yellow"
    def Purple_outline(self):
        self.brush_color="purple"
        self.fill_color="purple"
    def Pink_outline(self):
        self.brush_color="pink"
        self.fill_color="pink"
    def Grey_outline(self):
        self.brush_color="grey"
        self.fill_color="grey"
    def Light_blue_outline(self):
        self.brush_color="light blue"
        self.fill_color="light blue"
    def Orange_outline(self):
        self.brush_color="orange"
        self.fill_color="orange"
    def Cyan_outline(self):
        self.brush_color="cyan"
        self.fill_color="cyan"
    def Blue_Grey_outline(self):
        self.brush_color="magenta"
        self.fill_color="magenta"

  
    def fill_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")


     # Which color is selected
    def show_color(self):
        self.clr.config(bg=self.brush_color)
       
    def undo_pressed(self):
        if(self.undo):
            Id = self.undo.pop()
            self.canvas.delete(Id)
            


    # Heptagon
    def hp_pressed(self):   
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_hp)
        self.canvas.bind("<ButtonRelease-1>",self.end_hp)
    def draw_hp(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y = event.x,event.y
            return
        h = event.y - self.last_y
        w = event.x - self.last_x
        x1 = self.last_x + (w/2)
        y1 = self.last_y
        x2 = event.x - (w/8)
        y2 = y1 + (h/4)
        x3 = event.x
        y3 = y1 + (h/2 + h/8)
        x4 = event.x - (w/4)
        y4 = y1 + h
        x5 = self.last_x + (w/4)
        y5 = y4
        x6 = self.last_x
        y6 = y3
        x7 = self.last_x + (w/8)
        y7 = y2
      
        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,fill= self.fill_color ,outline="black",width=self.size.get())
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,fill="",outline=self.brush_color,width=self.size.get())
            self.undo.append(self.shape_Id)

    def end_hp(self,event):
        self.last_x,self.last_y = None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"

    # OCTAGON
    def oc_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_oc)
        self.canvas.bind("<ButtonRelease-1>",self.end_oc)
    def draw_oc(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y = event.x,event.y
            return
        h = event.y - self.last_y
        w = event.x - self.last_x
        x1 = self.last_x + (w/4)
        y1 = self.last_y
        x2 = self.last_x + (w/2 + w/4)
        y2 = self.last_y
        x3 = event.x
        y3 = y1 + (h/2 - (h/4 - h/16))
        x4 = event.x 
        y4 = y1 + (h/2 + (h/4 - h/16))
        x5 = event.x - (w/4)
        y5 = y1 + h
        x6 = self.last_x + (w/4)
        y6 = y5
        x7 = self.last_x
        y7 = y4
        x8 = self.last_x
        y8 = y3
      
        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,fill=self.fill_color,outline="black",width=self.size.get())
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,fill="",outline=self.brush_color,width=self.size.get())
            self.undo.append(self.shape_Id)

 
    def end_oc(self,event):
        self.last_x,self.last_y = None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"

    # NONANE
    
    def na_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_na)
        self.canvas.bind("<ButtonRelease-1>",self.end_na)
    def draw_na(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y = event.x,event.y
            return
        h = event.y - self.last_y
        w = event.x - self.last_x
        x1 = self.last_x + (w/2)
        y1 = self.last_y
        x2 = event.x - (w/4 - w/16)
        y2 = y1 + (h/8)
        x3 = event.x
        y3 = y1 + (h/2 - h/16)
        x4 = event.x - w/16
        y4 = y1 + (h/2 + h/4)
        x5 = event.x - (w/4 + w/16)
        y5 = y1 + h
        x6 = self.last_x + (w/4 + w/16)
        y6 = y5
        x7 = self.last_x + (w/16)
        y7 = y4
        x8 = self.last_x
        y8 = y3
        x9 = self.last_x + (w/4 - w/16)
        y9 = y2
     
        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,fill=self.fill_color,outline="black",width=self.size.get())
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,fill="",outline=self.brush_color,width=self.size.get())
            self.undo.append(self.shape_Id)


    def end_na(self,event):
        self.last_x,self.last_y = None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"

    # DECANE
    
    def dc_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_dc)
        self.canvas.bind("<ButtonRelease-1>",self.end_dc)
    def draw_dc(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y = event.x,event.y
            return
        h = event.y - self.last_y
        w = event.x - self.last_x
        x1 = self.last_x + (w/4 + w/16)
        y1 = self.last_y
        x2 = self.last_x + (w/2 + w/4 - w/16)
        y2 = self.last_y
        x3 = event.x - (w/16)
        y3 = y1 + (h/4 - h/16)
        x4 = event.x
        y4 = y1 + (h/2)
        x5 = x3
        y5 = y1 + (h/2 + h/4 + h/16)
        x6 = event.x - (w/4 + w/16)
        y6 = y1 + h
        x7 = self.last_x + (w/4 + w/16)
        y7 = y6
        x8 = self.last_x + (w/16)
        y8 = y5
        x9 = self.last_x
        y9 = y4
        x10 = x8
        y10 = y3
   

        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,fill=self.fill_color,outline="black",width=self.size.get())
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,fill="",outline=self.brush_color,width=self.size.get())
            self.undo.append(self.shape_Id)
 

    def end_dc(self,event):
        self.last_x,self.last_y = None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"


    def picker_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.pick_screen_color)

        #self.canvas.bind("<ButtonRelease-1>",self.Remove_end_brush)

    def pick_screen_color(self,event):
        self.closest_item = self.canvas.find_closest(event.x, event.y)[0]
        self.pixel_color = self.canvas.itemcget(self.closest_item, "fill")
        self.brush_color = self.pixel_color

        self.canvas.unbind("<B1-Motion>")

        self.canvas.bind("<B1-Motion>",self.draw_brush)
        self.canvas.bind("<ButtonRelease-1>",self.Remove_end_brush)
       

    def pencil_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_brush)
        self.canvas.bind("<ButtonRelease-1>",self.Remove_end_brush)
    def erase_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.Erase)
        self.canvas.bind("<ButtonRelease-1>",self.Erase_end)
    def color_pressed(self):
        self.selected_color=colorchooser.askcolor()
        self.brush_color=self.selected_color[1]
        self.fill_color=self.selected_color[1]
        if(self.selected_color is None):
            return
    def circle_pressed(self):

        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_circle)
        self.canvas.bind("<ButtonRelease-1>",self.end_circle)
    def straight_line_pressed(self):

        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_straight_line)
        self.canvas.bind("<ButtonRelease-1>",self.end_straight_line)
    def rectangle_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>",self.end_rectangle)    
    def oval_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_oval)
        self.canvas.bind("<ButtonRelease-1>",self.end_oval)    
    def triangle_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_triangle)
        self.canvas.bind("<ButtonRelease-1>",self.end_triangle)  
    def pentagon_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_pentagon)
        self.canvas.bind("<ButtonRelease-1>",self.end_pentagon)     

    def hexagon_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_hexagon)
        self.canvas.bind("<ButtonRelease-1>",self.end_hexagon)

    def star_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_star)
        self.canvas.bind("<ButtonRelease-1>",self.end_star)


        
    def draw_hexagon(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y    
            return  
        
        w=event.x-self.last_x
        h=event.y-self.last_y
        x1=self.last_x+(w/2)
        y1=self.last_y
        x2=event.x
        y2=y1+(h/4)
        x3=event.x
        y3=y2+(h/2)
        x4=x1
        y4=event.y
        x5=self.last_x
        y5=y3
        x6=self.last_x
        y6=y2
      
        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,width=self.size.get(),outline="black",fill=self.fill_color)
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,width=self.size.get(),outline=self.brush_color,fill="")
            self.undo.append(self.shape_Id)

    def end_hexagon(self,event):
        self.last_x,self.last_y=None,None
        self.shape_Id = None 
        self.is_fill_pressed = False
        self.brush_color = "black"

    # PENTAGON
    def draw_pentagon(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y= event.x,event.y
            return
        h = event.y - self.last_y
        w = event.x - self.last_x
        x1 = self.last_x+(w/2)
        y1 = self.last_y
        x2 = event.x
        y2 = y1+(h/2-h/8)
        x3 = (event.x - w/4) + w/16
        y3 = y1+h
        x4 = (self.last_x + w/4) - w/16
        y4 = y1+h
        x5 = self.last_x
        y5 = y2
      
        if (self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,width=self.size.get(),fil=self.fill_color,outline="black")
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,width=self.size.get(),fil="",outline=self.brush_color)
            self.undo.append(self.shape_Id)

    def end_pentagon(self,event):
        self.last_x,self.last_y=None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"


    # TRIANGLE     
    def draw_triangle(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y
            return
        w=event.x - self.last_x
        h=event.y - self.last_y
        x1=self.last_x + (w/2)
        y1 = self.last_y
        x2=event.x
        y2=y1+h
        x3=self.last_x
        y3=y2
      
        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,width=self.size.get(),outline="black",fill=self.fill_color)
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,width=self.size.get(),outline=self.brush_color,fill="")
            self.undo.append(self.shape_Id)
        
        
    def end_triangle(self,event):
        self.last_x,self.last_y= None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"

    # RECTANGLE
    def draw_rectangle(self,event):
        if self.shape_Id is not None:
            self.canvas.delete(self.shape_Id)

        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y
            return 
       
        if(self.is_fill_pressed):
           self.shape_Id = self.canvas.create_rectangle(self.last_x,self.last_y,event.x,event.y,width=self.size.get(),outline="black",fill=self.fill_color)
           self.undo.append(self.shape_Id)
        else:
             self.shape_Id = self.canvas.create_rectangle(self.last_x,self.last_y,event.x,event.y,width=self.size.get(),outline=self.brush_color,fill="")
             self.undo.append(self.shape_Id)
       # self.last_x,self.last_y=event.x,event.y
    def end_rectangle(self,event):
        self.last_x,self.last_y=None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"

    # OVAL
    def draw_oval(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y
            return
       
        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_oval(self.last_x,self.last_y,event.x,event.y,width=self.size.get(),outline="black",fill=self.fill_color)
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_oval(self.last_x,self.last_y,event.x,event.y,width=self.size.get(),outline=self.brush_color,fill="")
            self.undo.append(self.shape_Id)
    def end_oval(self,event):
        self.last_x,self.last_y=None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"

    # STAR
    def draw_star(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y
            return
        h= event.y - self.last_y
        w = event.x - self.last_x
        x1 = self.last_x + (w/2)
        y1 = self.last_y
        x2 = (event.x-(w/2))+(w/8)
        y2 = y1 + (h/4 + h/8)
        x3 = event.x
        y3 = y2
        x4 = event.x - (w/4)
        y4 = y1 + (h/2 + h/8)
        x5 = event.x - w/8
        y5 = y1 + h
        #x6 = event.x - h/2
        x6 = (event.x - w/2)
        y6 = y1 + (h/2 + h/4 )
        x7 = self.last_x+(w/8)
        y7 = y1 + h
        x8 = self.last_x + (w/4)
        y8 = y1 + (h/2 + h/8)
        x9 = self.last_x
        y9 = y1 + (h/4 + h/8)
        x10 = self.last_x + (w/2 - w/8)
        y10 = y9
     
        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,width=self.size.get(),fill=self.fill_color,outline="black")
            self.undo.append(self.shape_Id)

        else:
            self.shape_Id = self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,width=self.size.get(),fill="",outline=self.brush_color)
            self.undo.append(self.shape_Id)



    def end_star(self,event):
        self.last_x,self.last_y=None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"
      

    def Reset_All(self):
        self.canvas_bg = "white"
        self.canvas.delete("all")
       
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    # BRUSH
    def draw_brush(self,event):
        if self.last_x == None:
            self.last_x,self.last_y=event.x,event.y
            return
        self.shape_Id = self.canvas.create_line(self.last_x,self.last_y,event.x,event.y,width=self.size.get(),capstyle=ROUND,fill=self.brush_color)
        self.undo.append(self.shape_Id)
        self.last_x,self.last_y=event.x,event.y

    def Remove_end_brush(self,event):
        self.last_x,self.last_y=None,None

    def Erase(self,event):
        if self.last_x == None:
            self.last_x,self.last_y=event.x,event.y
            return
        self.canvas.create_line(self.last_x,self.last_y,event.x,event.y,width=self.size.get(),capstyle=ROUND,fill=self.canvas_bg)
        self.last_x,self.last_y=event.x,event.y
        self.canvas["cursor"]=DOTBOX
    def Erase_end(self,event):
        self.last_x,self.last_y=None,None

    # Shapes 
    def draw_circle(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)

        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y
            return
        self.radius=abs(self.last_x - event.x) + abs(self.last_y - event.y)
        self.x1,self.y1 = (self.last_x - self.radius),(self.last_y - self.radius)
        self.x2,self.y2 = (self.last_x + self.radius),(self.last_y + self.radius)

        if(self.is_fill_pressed):
            self.shape_Id = self.canvas.create_oval(self.x1,self.y1,self.x2,self.y2,width=self.size.get(),outline="black",fill=self.fill_color)
            self.undo.append(self.shape_Id)
        else:
            self.shape_Id = self.canvas.create_oval(self.x1,self.y1,self.x2,self.y2,width=self.size.get(),outline=self.brush_color,fill="")
            self.undo.append(self.shape_Id)

    def end_circle(self,event):
        self.last_x,self.last_y=None,None
        self.shape_Id = None
        self.is_fill_pressed = False
        self.brush_color = "black"

    # ZOOM FUNCTION
    def zoom(self, event):
        if event.delta > 0:
            if(self.zoom_scale < self.max_zoom_scale):
              self.zoom_scale *= 1.1
        else:
            if(self.zoom_scale > self.min_zoom_scale):
              self.zoom_scale /= 1.1
        self.canvas.scale("all", event.x, event.y, self.zoom_scale, self.zoom_scale)
   
  
    
    # STRAIGHT LINE
    def draw_straight_line(self,event):
        if(self.shape_Id is not None):
            self.canvas.delete(self.shape_Id)
        if(self.last_x is None):
            self.last_x,self.last_y=event.x,event.y
            return
       
        self.shape_Id = self.canvas.create_line(self.last_x,self.last_y,event.x,event.y,width=self.size.get(),fill=self.brush_color)
        self.undo.append(self.shape_Id)
      #  self.last_x,self.last_y=event.x,event.y

    def end_straight_line(self,event):
        self.last_x,self.last_y=None,None
        self.shape_Id = None


    # SAVE IMAGE 
    def save_image(self):
        self.file_location = filedialog.asksaveasfilename(defaultextension="jpg")
        x = IntVar()
        y = IntVar()
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()

        self.image = ImageGrab.grab(bbox=(x+23,y+63,x+1272,y+606))
        self.image.save(self.file_location)                                                     

        self.image.show()
    def load_image(self):
        canvas_width = 1000
        canvas_height = 450
        self.canvas.config(width=canvas_width, height=canvas_height)
        self.filename = filedialog.askopenfilename(filetypes=[("Image files","*.png"),("Image files" ,"*.jpg"), ("Image files" ,"*.jpeg")])
        if self.filename:
            self.canvas_image = Image.open(self.filename)
            self.canvas_image.thumbnail((canvas_width, canvas_height), Image.ANTIALIAS)
            # self.canvas.config(width=self.canvas_image.width, height=self.canvas_image.height)
            # self.draw = ImageDraw.Draw(self.canvas_image)
            # self.canvas.delete("all")
            self.canvas.image = ImageTk.PhotoImage(self.canvas_image)
            self.canvas.create_image(0,0,anchor=NW,image = self.canvas.image)


    def Paint_run(self):
        self.screen.mainloop()

paint=PaintApp(1000,600,"Hassan Paint")
paint.Paint_run()




