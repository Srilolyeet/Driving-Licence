import tkinter as tk

root = tk.Tk()

root.title("Driving License Information")

root.geometry("400x300")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

label_id = tk.Label(root, text="Driving License ID:")
label_name = tk.Label(root, text="Name:")
label_dob = tk.Label(root, text="Date of Birth:")
label_pin = tk.Label(root, text="Pincode:")
label_address = tk.Label(root, text="Address:")
label_vehicle_type = tk.Label(root, text="Vehicles authorized to drive:")



def update_labels():
    # Define variables
    license_id = 6236803598     
    name = "Sriram Makam"  
    dob = "08/15/2009"  
    pincode =  812804  
    address = "18 Saunders St, Salem"  
    vehicle_types = ["Two-wheeler", "Four-wheeler"]
    
    print(type(license_id))
    print(type(name))
    print(type(dob))
    print(type(pincode))
    print(type(address))
    print(type(vehicle_types))
    
    label_id.config(text="Driving License ID: " + str(license_id))
    label_name.config(text="Name: " + name)
    label_dob.config(text="Date of Birth: " + dob)
    label_pin.config(text="Pincode: " + str(pincode))
    label_address.config(text="Address: " + address)
    label_vehicle_type.config(text="Vehicles authorized to drive: " + ", ".join(vehicle_types))

    
    
update_button = tk.Button(root, text="Update Information", command=update_labels)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

label_id.pack()
label_name.pack()
label_dob.pack()
label_pin.pack()
label_address.pack()
label_vehicle_type.pack()
.....update_button.pack()

root.mainloop()
