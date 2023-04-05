from tkinter import *
from tkinter import messagebox


constand_aire_seco= float(287)
gravedad= float(9.8)
temteratura_inicial=float(288.15)
euler=float(2.71828)
gradiente_troposfera=float(-0.0065)
gradiente_tropopausa= int(0)
presion_inicial=float(101325)
presion_frontera=float(22648.806)
temperatura_tropopausa=float(216.65)
densidad_frontera=float(0.36)
altura_frontera=float(11000)
radio_tierra=float(6371000)





ventana=Tk()
ventana.geometry("750x550")
ventana.title("CALCULADORA AERODINAMICA")
ventana.config(background="#000000")
title_densisdad= Label (text= "Calculadora de Aerodinamica",font=("cambria",18),bg="#151515",fg="white",width="550",height="3")
title_densisdad.pack()
userask_label=Label(text="¿Que tipo de altura tienes?",font=("cambria",14),bg="#4B0082",width="200",height="3")
userask_label.pack()
useraltura_label= Label(text="Altura Geopotencial",font=("arial",12),bg="#4B0082",width="30",height="3")
useraltura_label.place(x=70, y=200)
usergeometrica_label=Label(text="Altura Geometrica",font=("arial",12),bg="#4B0082",width="30",height="3")
usergeometrica_label.place(x=390,y=200)



def ventana_geopotencial():
    


    ventana.destroy()
    ventana_geopotencial_=Tk()
    ventana_geopotencial_.geometry("750x550")
    ventana_geopotencial_.title("ALTURA GEOPOTENCIAL")
    ventana_geopotencial_.config(background="#000000")
    userquestion_label=Label(text="Altura geopotencial",font=("cambria",14),bg="#4B0082",width="200",height="3")
    userquestion_label.pack()
    useralturageopotencial_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="3")
    useralturageopotencial_label.place(x=22,y=100)
    usergradientegeopotencial_label=Label(text="Gradiente Termico",font=("arial",12),bg="#4B0082",width="15",height="3")
    usergradientegeopotencial_label.place(x=330,y=100)

    altura= DoubleVar()
    altura_entry=Entry(textvariable=altura,width=40)
    altura_entry.place(x=22,y=170)

    gradiente=DoubleVar()
    gradiente_entry=Entry(textvariable=gradiente,width=40)
    gradiente_entry.place(x=330,y=170)

    


    def altura_data ():
       altura= altura_entry.get()
       data_sence=float(altura)
       return data_sence
    
    def gradiente_data ():
       gradiente=gradiente_entry.get()
       data_sence=float(gradiente)
       return data_sence
       

    def print_selection (option):
        
        altura_data()
        gradiente_data()




        if altura_data()==0.0:
           messagebox.showerror("error","Tienes que llenar todos los datos")
        
        if gradiente_data()==0.0:
           messagebox.showerror("error","Tienes que llenar todos los datos")






        if option == "metros":
           altura_data_metros=altura_data()
           print(f"altura= {altura_data_metros} m")
           if altura_data_metros<=11000:
                temperatura_altura= temteratura_inicial + (gradiente_data()*altura_data_metros) 
                print(f"T={temperatura_altura:.2f} K")
                presion_altura= presion_inicial*(temperatura_altura/temteratura_inicial)**(-(gravedad/(constand_aire_seco*gradiente_data())))
                print(f"P= {presion_altura:.3f} Pa")
                densidad_altura=presion_altura/(constand_aire_seco*temperatura_altura)
                print(f"D= {densidad_altura:.2f} Km/m**3")
                
                temperatura_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
                temperatura_label.place(x=22,y=260)
                temperatura_altura_show_label=Label(ventana_geopotencial_,text=f"T={temperatura_altura:.2f} K")
                temperatura_altura_show_label.place (x=22,y=300)


                presion_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
                presion_label.place(x=22,y=340)
                presion_altura_show_label=Label(ventana_geopotencial_,text=f"P= {presion_altura:.3f} Pa")
                presion_altura_show_label.place (x=22,y=380)


                densidad_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
                densidad_label.place(x=22,y=420)
                densidad_altura_show_label=Label(ventana_geopotencial_,text=f"D= {densidad_altura:.2f} Km/m**3")
                densidad_altura_show_label.place (x=22,y=460)


                altura_data_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
                altura_data_label.place(x=22,y=500)
                altura_data_show_label=Label(ventana_geopotencial_,text=f"altura= {altura_data_metros} m")
                altura_data_show_label.place(x=22,y=540)


            
           if altura_data_metros>11000 and altura_data_metros<=20000:
               print("estas en tropopausa el gradiente termico es 0 y la temperatura es constante")

               presion_metros_tropopausa=presion_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_data_metros-altura_frontera))
               print(f"P= {presion_metros_tropopausa:.3f} Pa")

               densidad_metros_tropopausa=densidad_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_data_metros-altura_frontera))
               print(f"D= {densidad_metros_tropopausa:.3f} km/m**3")



               aviso_metros_tropopausa_label=Label(ventana_geopotencial_,text="estas en tropopausa el gradiente termico es 0 y la temperatura es constante")
               aviso_metros_tropopausa_label.place(x=22,y=260)
               

               presion_metros_tropopausa_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
               presion_metros_tropopausa_label.place(x=22,y=300)
               presion_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"P= {presion_metros_tropopausa:.3f} Pa")
               presion_metros_tropopausa_show_label.place (x=22,y=340)


               temperatura_metros_tropopausa_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
               temperatura_metros_tropopausa_label.place(x=22,y=380)
               temperatura_metros_tropopausa_show_label=Label(ventana_geopotencial_,text= f" T= {temperatura_tropopausa} k")
               temperatura_metros_tropopausa_show_label.place(x=22,y=420)


               densidad_metros_tropopausa_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
               densidad_metros_tropopausa_label.place(x=22,y=460)
               densidad_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"D= {densidad_metros_tropopausa:.3f} km/m**3")
               densidad_metros_tropopausa_show_label.place(x=22,y=500)


               altura_data_metros_tropopausa_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
               altura_data_metros_tropopausa_label.place(x=22,y=540)
               altura_data_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"altura= {altura_data_metros} m")
               altura_data_metros_tropopausa_show_label.place(x=22,y=580)






        
        if option == "Pies":
           altura_pies_metros=altura_data()*0.3048
           print(f"altura= {altura_pies_metros} m")
           if altura_pies_metros<=11000:
             temperatura_altura_pies_metro= temteratura_inicial + (gradiente_data()*altura_pies_metros) 
             print(f"k= {temperatura_altura_pies_metro:.2f} k")
             presion_altura_pies_metro= presion_inicial*(temperatura_altura_pies_metro/temteratura_inicial)**(-(gravedad/(constand_aire_seco*gradiente_data())))
             print(f"P= {presion_altura_pies_metro:.2f} Pa")
             densidad_altura_pies_metro=presion_altura_pies_metro/(constand_aire_seco*temperatura_altura_pies_metro)
             print(f"D= {densidad_altura_pies_metro:.2f} Km/m**3")



             temperatura_label_pies_metros=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
             temperatura_label_pies_metros.place(x=22,y=260)
             temperatura_altura_show_label_pies_metros=Label(ventana_geopotencial_,text=f"k= {temperatura_altura_pies_metro:.2f} k")
             temperatura_altura_show_label_pies_metros.place (x=22,y=300)


             presion_label_pies_metros=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
             presion_label_pies_metros.place(x=22,y=340)
             presion_altura_show_label_pies_metros=Label(ventana_geopotencial_,text=f"P= {presion_altura_pies_metro:.2f} Pa")
             presion_altura_show_label_pies_metros.place (x=22,y=380)


             densidad_label_pies_metros=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
             densidad_label_pies_metros.place(x=22,y=420)
             densidad_altura_show_label_pies_metros=Label(ventana_geopotencial_,text=f"D= {densidad_altura_pies_metro:.2f} Km/m**3")
             densidad_altura_show_label_pies_metros.place (x=22,y=460)


             altura_data_label_pies_metros=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
             altura_data_label_pies_metros.place(x=22,y=500)
             altura_data_show_label_pies_metros=Label(ventana_geopotencial_,text=f"altura= {altura_pies_metros} m")
             altura_data_show_label_pies_metros.place(x=22,y=540)


           if altura_pies_metros>11000 and altura_pies_metros<=20000:
                print("estas en tropopausa el gradiente termico es 0 y la temperatura es constante")

                presion_pies_metros_tropopausa=presion_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_pies_metros-altura_frontera))
                print(f"P= {presion_pies_metros_tropopausa:.3f} Pa")

                densidad_pies_metros_tropopausa=densidad_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_pies_metros-altura_frontera))
                print(f"D= {densidad_pies_metros_tropopausa:.3f} km/m**3")



                aviso_pies_metros_tropopausa_label=Label(ventana_geopotencial_,text="estas en tropopausa el gradiente termico es 0 y la temperatura es constante")
                aviso_pies_metros_tropopausa_label.place(x=22,y=260)
               

                presion_pies_metros_tropopausa_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
                presion_pies_metros_tropopausa_label.place(x=22,y=300)
                presion_pies_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"P= {presion_pies_metros_tropopausa:.3f} Pa")
                presion_pies_metros_tropopausa_show_label.place (x=22,y=340)


                temperatura_pies_metros_tropopausa_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
                temperatura_pies_metros_tropopausa_label.place(x=22,y=380)
                temperatura_pies_metros_tropopausa_show_label=Label(ventana_geopotencial_,text= f" T= {temperatura_tropopausa} k")
                temperatura_pies_metros_tropopausa_show_label.place(x=22,y=420)


                densidad_pies_metros_tropopausa_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
                densidad_pies_metros_tropopausa_label.place(x=22,y=460)
                densidad_pies_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"D= {densidad_pies_metros_tropopausa:.3f} km/m**3")
                densidad_pies_metros_tropopausa_show_label.place(x=22,y=500)
               

                altura_data_pies_metros_tropopausa_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
                altura_data_pies_metros_tropopausa_label.place(x=22,y=540)
                altura_data_pies_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"altura= {altura_pies_metros} m")
                altura_data_pies_metros_tropopausa_show_label.place(x=22,y=580)




            
           

        if option == "kilometros":
           altura_kilometros_metros=altura_data()*1000
           print(f"altura= {altura_kilometros_metros} m")
           if altura_kilometros_metros<=11000:
              temperatura_altura_kilometro_metro= temteratura_inicial + (gradiente_data()*altura_kilometros_metros) 
              print(f"k= {temperatura_altura_kilometro_metro:.2f} k")
              presion_altura_kilometro_metro= presion_inicial*(temperatura_altura_kilometro_metro/temteratura_inicial)**(-(gravedad/(constand_aire_seco*gradiente_data())))
              print(f"P= {presion_altura_kilometro_metro:.2f} Pa")
              densidad_altura_kilometro_metro= presion_altura_kilometro_metro/(constand_aire_seco*temperatura_altura_kilometro_metro)
              print(f"D= {densidad_altura_kilometro_metro:.2f} Km/m**3")


              temperatura_label_kilometros_metros=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
              temperatura_label_kilometros_metros.place(x=22,y=260)
              temperatura_altura_show_label_kilometros_metros=Label(ventana_geopotencial_,text=f"k= {temperatura_altura_kilometro_metro:.2f} k")
              temperatura_altura_show_label_kilometros_metros.place (x=22,y=300)


              presion_label_kilometros_metros=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
              presion_label_kilometros_metros.place(x=22,y=340)
              presion_altura_show_label_kilometros_metros=Label(ventana_geopotencial_,text=f"P= {presion_altura_kilometro_metro:.2f} Pa")
              presion_altura_show_label_kilometros_metros.place (x=22,y=380)


              densidad_label_kilometros_metros=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
              densidad_label_kilometros_metros.place(x=22,y=420)
              densidad_altura_show_label_kilometros_metros=Label(ventana_geopotencial_,text=f"D= {densidad_altura_kilometro_metro:.2f} Km/m**3")
              densidad_altura_show_label_kilometros_metros.place (x=22,y=460)


              altura_data_label_kilometros_metros=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
              altura_data_label_kilometros_metros.place(x=22,y=500)
              altura_data_show_label_kilometros_metros=Label(ventana_geopotencial_,text=f"altura= {altura_data_metros} m")
              altura_data_show_label_kilometros_metros.place(x=22,y=540)



           if altura_kilometros_metros>11000 and altura_kilometros_metros<=20000:
                 print("estas en tropopausa el gradiente termico es 0 y la temperatura es constante")

                 presion_kilometros_metros_tropopausa=presion_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_kilometros_metros-altura_frontera))
                 print(f"P= {presion_kilometros_metros_tropopausa:.3f} Pa")

                 densidad_kilometros_metros_tropopausa=densidad_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_kilometros_metros-altura_frontera))
                 print(f"D= {densidad_kilometros_metros_tropopausa:.3f} km/m**3")



                 aviso_kilometros_metros_tropopausa_label=Label(ventana_geopotencial_,text="estas en tropopausa el gradiente termico es 0 y la temperatura es constante")
                 aviso_kilometros_metros_tropopausa_label.place(x=22,y=260)
               

                 presion_kilometros_metros_tropopausa_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
                 presion_kilometros_metros_tropopausa_label.place(x=22,y=300)
                 presion_kilometros_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"P= {presion_kilometros_metros_tropopausa:.3f} Pa")
                 presion_kilometros_metros_tropopausa_show_label.place (x=22,y=340)


                 temperatura_kilometros_metros_tropopausa_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
                 temperatura_kilometros_metros_tropopausa_label.place(x=22,y=380)
                 temperatura_kilometros_metros_tropopausa_show_label=Label(ventana_geopotencial_,text= f" T= {temperatura_tropopausa} k")
                 temperatura_kilometros_metros_tropopausa_show_label.place(x=22,y=420)


                 densidad_kilometros_metros_tropopausa_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
                 densidad_kilometros_metros_tropopausa_label.place(x=22,y=460)
                 densidad_kilometros_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"D= {densidad_kilometros_metros_tropopausa:.3f} km/m**3")
                 densidad_kilometros_metros_tropopausa_show_label.place(x=22,y=500)


                 altura_data_kilometros_metros_tropopausa_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
                 altura_data_kilometros_metros_tropopausa_label.place(x=22,y=540)
                 altura_data_kilometros_metros_tropopausa_show_label=Label(ventana_geopotencial_,text=f"altura= {altura_kilometros_metros} m")
                 altura_data_kilometros_metros_tropopausa_show_label.place(x=22,y=580)



            
              

            
           

       
       
       
           
    

    
    
    options = ["metros", "Pies", "kilometros"]
    selected_option = StringVar(ventana_geopotencial_)
    menu = OptionMenu(ventana_geopotencial_, selected_option, *options)
    menu.config(width=6,height=2)
    menu.place(x=120,y=100)



    submit_btn=Button (ventana_geopotencial_,text="submit info",command=lambda:print_selection(selected_option.get(),),width="30",height="2",bg="#4B0082")
    submit_btn.place(x=22,y=200)


def ventana_geometrica():
    ventana.destroy()
    ventana_geometrica_=Tk()
    ventana_geometrica_.geometry("750x550")
    ventana_geometrica_.title("ALTURA GEOMETRICA")
    ventana_geometrica_.config(background="#000000")
    userquestion_label=Label(text="Altura geometrica",font=("cambria",14),bg="#4B0082",width="200",height="3")
    userquestion_label.pack()
    useralturageopotencial_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="3")
    useralturageopotencial_label.place(x=22,y=100)
    usergradientegeopotencial_label=Label(text="Gradiente Termico",font=("arial",12),bg="#4B0082",width="15",height="3")
    usergradientegeopotencial_label.place(x=330,y=100)


    altura= DoubleVar()
    altura_entry=Entry(textvariable=altura,width=40)
    altura_entry.place(x=22,y=170)

    gradiente=DoubleVar()
    gradiente_entry=Entry(textvariable=gradiente,width=40)
    gradiente_entry.place(x=330,y=170)


    def altura_data ():
       altura_geometrica= altura_entry.get()
       data_sence_geometrica=float(altura_geometrica)
       data_sence_geopotencial=data_sence_geometrica*(radio_tierra/(radio_tierra+data_sence_geometrica))
       return data_sence_geopotencial
    
    def gradiente_data ():
       gradiente=gradiente_entry.get()
       data_sence=float(gradiente)
       return data_sence
    


    def print_selection (option):
        
        altura_data()
        gradiente_data()




        if altura_data()==0.0:
           messagebox.showerror("error","Tienes que llenar todos los datos")
        
        if gradiente_data()==0.0:
           messagebox.showerror("error","Tienes que llenar todos los datos")



        if option == "metros":
           altura_data_metros=altura_data()
           print(f"altura= {altura_data_metros} m")
           if altura_data_metros<=11000:
                temperatura_altura= temteratura_inicial + (gradiente_data()*altura_data_metros) 
                print(f"T={temperatura_altura:.2f} K")
                presion_altura= presion_inicial*(temperatura_altura/temteratura_inicial)**(-(gravedad/(constand_aire_seco*gradiente_data())))
                print(f"P= {presion_altura:.3f} Pa")
                densidad_altura=presion_altura/(constand_aire_seco*temperatura_altura)
                print(f"D= {densidad_altura:.2f} Km/m**3")
                
                temperatura_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
                temperatura_label.place(x=22,y=260)
                temperatura_altura_show_label=Label(ventana_geometrica_,text=f"T={temperatura_altura:.2f} K")
                temperatura_altura_show_label.place (x=22,y=300)


                presion_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
                presion_label.place(x=22,y=340)
                presion_altura_show_label=Label(ventana_geometrica_,text=f"P= {presion_altura:.3f} Pa")
                presion_altura_show_label.place (x=22,y=380)


                densidad_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
                densidad_label.place(x=22,y=420)
                densidad_altura_show_label=Label(ventana_geometrica_,text=f"D= {densidad_altura:.2f} Km/m**3")
                densidad_altura_show_label.place (x=22,y=460)


                altura_data_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
                altura_data_label.place(x=22,y=500)
                altura_data_show_label=Label(ventana_geometrica_,text=f"altura= {altura_data_metros} m")
                altura_data_show_label.place(x=22,y=540)


           if altura_data_metros>11000 and altura_data_metros<=20000:
               print("estas en tropopausa el gradiente termico es 0 y la temperatura es constante")

               presion_metros_tropopausa=presion_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_data_metros-altura_frontera))
               print(f"P= {presion_metros_tropopausa:.3f} Pa")

               densidad_metros_tropopausa=densidad_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_data_metros-altura_frontera))
               print(f"D= {densidad_metros_tropopausa:.3f} km/m**3")



               aviso_metros_tropopausa_label=Label(ventana_geometrica_,text="estas en tropopausa el gradiente termico es 0 y la temperatura es constante")
               aviso_metros_tropopausa_label.place(x=22,y=260)
               

               presion_metros_tropopausa_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
               presion_metros_tropopausa_label.place(x=22,y=300)
               presion_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"P= {presion_metros_tropopausa:.3f} Pa")
               presion_metros_tropopausa_show_label.place (x=22,y=340)


               temperatura_metros_tropopausa_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
               temperatura_metros_tropopausa_label.place(x=22,y=380)
               temperatura_metros_tropopausa_show_label=Label(ventana_geometrica_,text= f" T= {temperatura_tropopausa} k")
               temperatura_metros_tropopausa_show_label.place(x=22,y=420)


               densidad_metros_tropopausa_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
               densidad_metros_tropopausa_label.place(x=22,y=460)
               densidad_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"D= {densidad_metros_tropopausa:.3f} km/m**3")
               densidad_metros_tropopausa_show_label.place(x=22,y=500)


               altura_data_metros_tropopausa_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
               altura_data_metros_tropopausa_label.place(x=22,y=540)
               altura_data_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"altura= {altura_data_metros} m")
               altura_data_metros_tropopausa_show_label.place(x=22,y=580)





        if option == "Pies":
           altura_pies_metros=altura_data()*0.3048
           print(f"altura= {altura_pies_metros} m")
           if altura_pies_metros<=11000:
             temperatura_altura_pies_metro= temteratura_inicial + (gradiente_data()*altura_pies_metros) 
             print(f"k= {temperatura_altura_pies_metro:.2f} k")
             presion_altura_pies_metro= presion_inicial*(temperatura_altura_pies_metro/temteratura_inicial)**(-(gravedad/(constand_aire_seco*gradiente_data())))
             print(f"P= {presion_altura_pies_metro:.2f} Pa")
             densidad_altura_pies_metro=presion_altura_pies_metro/(constand_aire_seco*temperatura_altura_pies_metro)
             print(f"D= {densidad_altura_pies_metro:.2f} Km/m**3")



             temperatura_label_pies_metros=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
             temperatura_label_pies_metros.place(x=22,y=260)
             temperatura_altura_show_label_pies_metros=Label(ventana_geometrica_,text=f"k= {temperatura_altura_pies_metro:.2f} k")
             temperatura_altura_show_label_pies_metros.place (x=22,y=300)


             presion_label_pies_metros=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
             presion_label_pies_metros.place(x=22,y=340)
             presion_altura_show_label_pies_metros=Label(ventana_geometrica_,text=f"P= {presion_altura_pies_metro:.2f} Pa")
             presion_altura_show_label_pies_metros.place (x=22,y=380)


             densidad_label_pies_metros=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
             densidad_label_pies_metros.place(x=22,y=420)
             densidad_altura_show_label_pies_metros=Label(ventana_geometrica_,text=f"D= {densidad_altura_pies_metro:.2f} Km/m**3")
             densidad_altura_show_label_pies_metros.place (x=22,y=460)


             altura_data_label_pies_metros=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
             altura_data_label_pies_metros.place(x=22,y=500)
             altura_data_show_label_pies_metros=Label(ventana_geometrica_,text=f"altura= {altura_pies_metros} m")
             altura_data_show_label_pies_metros.place(x=22,y=540)



           if altura_pies_metros>11000 and altura_pies_metros<=20000:
                print("estas en tropopausa el gradiente termico es 0 y la temperatura es constante")

                presion_pies_metros_tropopausa=presion_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_pies_metros-altura_frontera))
                print(f"P= {presion_pies_metros_tropopausa:.3f} Pa")

                densidad_pies_metros_tropopausa=densidad_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_pies_metros-altura_frontera))
                print(f"D= {densidad_pies_metros_tropopausa:.3f} km/m**3")



                aviso_pies_metros_tropopausa_label=Label(ventana_geometrica_,text="estas en tropopausa el gradiente termico es 0 y la temperatura es constante")
                aviso_pies_metros_tropopausa_label.place(x=22,y=260)
               

                presion_pies_metros_tropopausa_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
                presion_pies_metros_tropopausa_label.place(x=22,y=300)
                presion_pies_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"P= {presion_pies_metros_tropopausa:.3f} Pa")
                presion_pies_metros_tropopausa_show_label.place (x=22,y=340)


                temperatura_pies_metros_tropopausa_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
                temperatura_pies_metros_tropopausa_label.place(x=22,y=380)
                temperatura_pies_metros_tropopausa_show_label=Label(ventana_geometrica_,text= f" T= {temperatura_tropopausa} k")
                temperatura_pies_metros_tropopausa_show_label.place(x=22,y=420)


                densidad_pies_metros_tropopausa_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
                densidad_pies_metros_tropopausa_label.place(x=22,y=460)
                densidad_pies_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"D= {densidad_pies_metros_tropopausa:.3f} km/m**3")
                densidad_pies_metros_tropopausa_show_label.place(x=22,y=500)
               

                altura_data_pies_metros_tropopausa_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
                altura_data_pies_metros_tropopausa_label.place(x=22,y=540)
                altura_data_pies_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"altura= {altura_pies_metros} m")
                altura_data_pies_metros_tropopausa_show_label.place(x=22,y=580)





        if option == "kilometros":
           altura_kilometros_metros=altura_data()*1000
           print(f"altura= {altura_kilometros_metros} m")
           if altura_kilometros_metros<=11000:
              temperatura_altura_kilometro_metro= temteratura_inicial + (gradiente_data()*altura_kilometros_metros) 
              print(f"k= {temperatura_altura_kilometro_metro:.2f} k")
              presion_altura_kilometro_metro= presion_inicial*(temperatura_altura_kilometro_metro/temteratura_inicial)**(-(gravedad/(constand_aire_seco*gradiente_data())))
              print(f"P= {presion_altura_kilometro_metro:.2f} Pa")
              densidad_altura_kilometro_metro= presion_altura_kilometro_metro/(constand_aire_seco*temperatura_altura_kilometro_metro)
              print(f"D= {densidad_altura_kilometro_metro:.2f} Km/m**3")


              temperatura_label_kilometros_metros=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
              temperatura_label_kilometros_metros.place(x=22,y=260)
              temperatura_altura_show_label_kilometros_metros=Label(ventana_geometrica_,text=f"k= {temperatura_altura_kilometro_metro:.2f} k")
              temperatura_altura_show_label_kilometros_metros.place (x=22,y=300)


              presion_label_kilometros_metros=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
              presion_label_kilometros_metros.place(x=22,y=340)
              presion_altura_show_label_kilometros_metros=Label(ventana_geometrica_,text=f"P= {presion_altura_kilometro_metro:.2f} Pa")
              presion_altura_show_label_kilometros_metros.place (x=22,y=380)


              densidad_label_kilometros_metros=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
              densidad_label_kilometros_metros.place(x=22,y=420)
              densidad_altura_show_label_kilometros_metros=Label(ventana_geometrica_,text=f"D= {densidad_altura_kilometro_metro:.2f} Km/m**3")
              densidad_altura_show_label_kilometros_metros.place (x=22,y=460)


              altura_data_label_kilometros_metros=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
              altura_data_label_kilometros_metros.place(x=22,y=500)
              altura_data_show_label_kilometros_metros=Label(ventana_geometrica_,text=f"altura= {altura_data_metros} m")
              altura_data_show_label_kilometros_metros.place(x=22,y=540)



           if altura_kilometros_metros>11000 and altura_kilometros_metros<=20000:
                 print("estas en tropopausa el gradiente termico es 0 y la temperatura es constante")

                 presion_kilometros_metros_tropopausa=presion_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_kilometros_metros-altura_frontera))
                 print(f"P= {presion_kilometros_metros_tropopausa:.3f} Pa")

                 densidad_kilometros_metros_tropopausa=densidad_frontera*euler**((-gravedad/(constand_aire_seco*temperatura_tropopausa))*(altura_kilometros_metros-altura_frontera))
                 print(f"D= {densidad_kilometros_metros_tropopausa:.3f} km/m**3")



                 aviso_kilometros_metros_tropopausa_label=Label(ventana_geometrica_,text="estas en tropopausa el gradiente termico es 0 y la temperatura es constante")
                 aviso_kilometros_metros_tropopausa_label.place(x=22,y=260)
               

                 presion_kilometros_metros_tropopausa_label=Label(text="Presion",font=("arial",12),bg="#4B0082",width="10",height="1")
                 presion_kilometros_metros_tropopausa_label.place(x=22,y=300)
                 presion_kilometros_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"P= {presion_kilometros_metros_tropopausa:.3f} Pa")
                 presion_kilometros_metros_tropopausa_show_label.place (x=22,y=340)


                 temperatura_kilometros_metros_tropopausa_label=Label(text="Temperatura",font=("arial",12),bg="#4B0082",width="10",height="1")
                 temperatura_kilometros_metros_tropopausa_label.place(x=22,y=380)
                 temperatura_kilometros_metros_tropopausa_show_label=Label(ventana_geometrica_,text= f" T= {temperatura_tropopausa} k")
                 temperatura_kilometros_metros_tropopausa_show_label.place(x=22,y=420)


                 densidad_kilometros_metros_tropopausa_label=Label(text="Densidad",font=("arial",12),bg="#4B0082",width="10",height="1")
                 densidad_kilometros_metros_tropopausa_label.place(x=22,y=460)
                 densidad_kilometros_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"D= {densidad_kilometros_metros_tropopausa:.3f} km/m**3")
                 densidad_kilometros_metros_tropopausa_show_label.place(x=22,y=500)


                 altura_data_kilometros_metros_tropopausa_label=Label(text="Altura",font=("arial",12),bg="#4B0082",width="10",height="1")
                 altura_data_kilometros_metros_tropopausa_label.place(x=22,y=540)
                 altura_data_kilometros_metros_tropopausa_show_label=Label(ventana_geometrica_,text=f"altura= {altura_kilometros_metros} m")
                 altura_data_kilometros_metros_tropopausa_show_label.place(x=22,y=580)












    options = ["metros", "Pies", "kilometros"]
    selected_option = StringVar(ventana_geometrica_)
    menu = OptionMenu(ventana_geometrica_, selected_option, *options)
    menu.config(width=6,height=2)
    menu.place(x=120,y=100)



    submit_btn=Button (ventana_geometrica_,text="submit info",command=lambda:print_selection(selected_option.get(),),width="30",height="2",bg="#4B0082")
    submit_btn.place(x=22,y=200)
    



    
    










    



user_ir= Button(ventana,text="ir",command= ventana_geopotencial,width="10",height="2",bg="#FFFFFF")
user_ir.place(x=170,y=285)

user_ir_geo=Button(ventana,text="ir",command= ventana_geometrica,width="10",height="2",bg="#FFFFFF")
user_ir_geo.place(x=490,y=285)





#altura= DoubleVar()
#altura_entry=Entry(textvariable=altura,width=40)
#altura_entry.place(x=22,y=170)

#temperature_=DoubleVar()
#temperature_entry=Entry(textvariable=temperature_ ,width=40)
#temperature_entry.place(x=330,y=170)


#def altura_data():
 #   altura= altura_entry.get()
  #  data_sence=float(altura)
   # return data_sence


#def temperature_data():
 #   temperature_=temperature_entry.get()
  #  data_sence=float(temperature_)
   # return data_sence


#def print_selection(option,option1):
 #   altura_data()
  #  temperature_data()
    

   # if altura_data()==0.0:
    #    messagebox.showerror("error","Tienes que llenar todos los datos")

    #if temperature_data()==0.0:
     #   messagebox.showerror("error","Tienes que llenar todos los datos")

    #if option == "metros":
     #   print(altura_data())
    #if option == "Pies":
      #  altura_pies_metros=altura_data()*0.3048
       # print(altura_pies_metros)
    #if option == "kilometros":
#        altura_kilometros_metros=altura_data()*1000
 #       print(altura_kilometros_metros)


#    if option1=="Kelvin":
#        print(temperature_data())

#    if option1=="Celcius":
#        celcius_kelvin=temperature_data()+273.15
#        print(f"{celcius_kelvin:.2f}")
    
#    if option1=="Farenheit":
#        farenheit_kelvin=(temperature_data()-32)* 5/9 + 273.15
#        print(f"{farenheit_kelvin:.3f}")

    


#options = ["metros", "Pies", "kilometros"]
#selected_option = StringVar(ventana)
#selected_option.set(options[0])
#menu = OptionMenu(ventana, selected_option, *options)
#menu.config(width=6,height=2)
#menu.place(x=120,y=100)

#temperatures=["Farenheit","Celcius","Kelvin"]
#selected_temperatures=StringVar(ventana)
#menut=OptionMenu(ventana,selected_temperatures,*temperatures)
#menut.config(width=6,height=2)
#menut.place(x=430,y=100)




#submit_btn=Button (ventana,text="submit info",command=lambda:print_selection(selected_option.get(),selected_temperatures.get()),width="30",height="2",bg="#4B0082")
#submit_btn.place(x=22,y=200)
    










    





ventana.mainloop()


