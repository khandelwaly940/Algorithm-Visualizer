from tkinter import *
import socket 
from tkinter import filedialog
from tkinter import messagebox
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
def load_image(image_path):
    try:
        return PhotoImage(file=image_path)
    except Exception as e:
        print(f"Error loading image '{image_path}': {e}")
        return None
    

root =Tk()
root.title("ShareMate")
root.geometry("460x550+500+190")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

def select_file():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image file', filetypes=(('file_type','.*txt'),('all files', '*.*')))

def sender():
    s=socket.socket()
    host=socket.gethostname()
    port=8080
    s.bind((host,port))
    s.listen(1)
    print(host)
    print('waiting for incoming conn')
    conn,addr=s.accept()
    file=open(filename,'rb')
    file_data=file.read(1024)
    conn.send(file_data)
    print("Data has been transmitted")

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry("460x550+500+190")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    window_image_icon_path=os.path.join(script_dir, 'assets', 'send.png')
    window_image_icon=load_image(window_image_icon_path)
    window.iconphoto(False,window_image_icon)

    background_send_image_path=os.path.join(script_dir, 'assets', 'sender.png')
    background_send_image=load_image(background_send_image_path)
    Label(window, image=background_send_image).place(x=-2,y=0)

    background_Mid_image_path=os.path.join(script_dir, 'assets', 'id.png')
    background_Mid_image=load_image(background_Mid_image_path)
    Label(window, image=background_Mid_image).place(x=100,y=290)

    host=socket.gethostname()
    Label(window,text=f'ID: {host}', bg='white',fg='black').place(x=170,y=320)


    Button(window, text="Select file", width=10,height=1, font='calibri', bg='#fff', fg="#000", command=select_file).place(x=160,y=150)
    Button(window, text="SEND",width=8, height=1, font='calibri', bg='#000', fg="#fff", command=sender).place(x=300, y=150)
    


    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry("460x550+500+190")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    def receiver_fun():
        ID=SenderID.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")


    # Load and set the window icon
    window_image_icon_path = os.path.join(script_dir, 'assets', 'receive.png')
    window_image_icon = load_image(window_image_icon_path)
    main.iconphoto(False, window_image_icon)

    # Load and place the background image
    Rbackground_image_path = os.path.join(script_dir, 'assets', 'receiver.png')
    Rbackground_image = load_image(Rbackground_image_path)
    Label(main, image=Rbackground_image, bg="#f4fdfe").place(x=0, y=-55)

    # Load and place the logo
    logo_path = os.path.join(script_dir, 'assets', 'profile.png')
    logo = load_image(logo_path)
    Label(main, image=logo, bg="#f4fdfe").place(x=180, y=220)

    # Title label
    Label(main, text="Receive", font=('calibri', 20, 'bold'), bg='#f4fdfe').place(x=190, y=320)

    # Sender ID input
    Label(main, text="Input sender ID:", font=('calibri', 10, 'bold'), bg="#f4fdfe").place(x=20, y=380)
    SenderID = Entry(main, width=25, fg="black", border=2, bg="white", font=("arial", 15))
    SenderID.place(x=20, y=400)
    SenderID.focus()

    # Incoming file name input
    Label(main, text="Filename for the incoming file:", font=('calibri', 10, 'bold'), bg="#f4fdfe").place(x=20, y=440)
    incoming_file = Entry(main, width=25, fg="black", border=2, bg="white", font=("arial", 15))
    incoming_file.place(x=20, y=460)

    """ # Receive button
    imageicon_path = os.path.join(script_dir, 'assets', 'arrow.png')
    imageicon = load_image(imageicon_path)"""
    rx = Button(main, text="Receive", compound=LEFT, width=13, bg="#39c790", font="calibri", command =receiver_fun)
    rx.place(x=20, y=500)

    main.mainloop()


icon_path = os.path.join(script_dir, 'assets', 'icon.png')
#icon_path = "assets/icon.png"
image_icon=load_image(icon_path)
root.iconphoto(False, image_icon)





Label(root, text="File Transfer", font=('calibri', 18, 'bold'), bg="#f4fdfe").place(x=20,y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)
image_send_path=os.path.join(script_dir, 'assets', 'send.png')
image_send=load_image(image_send_path)
send=Button(root, image=image_send, bg="#f4fdfe", bd=0, command= Send)
send.place(x=50,y =110)

receive_image_path=os.path.join(script_dir, 'assets', 'receive.png')
receive_image= load_image(receive_image_path)
send=Button(root, image=receive_image, bg="#f4fdfe", bd=0, command= Receive)
send.place(x=300,y =110)

Label(root, text="Send", font=('Calibri', 15, 'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root, text="Receive", font=('Calibri', 15, 'bold'),bg="#f4fdfe").place(x=300,y=200)

background_image_path=os.path.join(script_dir, 'assets', 'background.png')
background_image=load_image(background_image_path)
Label(root,image=background_image).place(x=-2,y=300)



root.mainloop()