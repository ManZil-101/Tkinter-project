from tkinter import *
from csv import DictWriter
from PIL import Image,ImageTk
import os
window = Tk()
window.title("Interest.APP")
window.geometry('870x880')
window.configure()

bg=ImageTk.PhotoImage(file="images/logo2.jpg")
fbg=ImageTk.PhotoImage(file="images/fr1.jpg")
bg1=Label(window,image=bg).place(x=0,y=8)





# DEFIND SECTION
def action():

# total saving of the year//
    b1=e1.get()
    b2=e2.get()
    b3=e3.get()
    b4=e4.get()
    b5=e5.get()
    b6=e6.get()
    b7=e7.get()
    b8=e8.get()
    b9=e9.get()
    b10=e10.get()
    b11=e11.get()
    b12=e12.get()
    acc=we.get()

    bts= int(b1)+int(b2)+int(b3)+int(b4)+int(b5)+int(b6)+int(b7)+int(b8)+int(b9)+int(b10)+int(b11)+int(b12)
    saving=int(bts)
    obl16 = Label(frame3, text=saving, font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=0)
    obl16 = Label(frame3, text="वर्षमा कुल बचत:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=0)
# interst section
    i1=(int(b1)*360*10)/36500
    i2=(int(b2)*330*10)/36500
    i3=(int(b3)*300*10)/36500
    i4=(int(b4)*270*10)/36500
    i5=(int(b5)*240*10)/36500
    i6=(int(b6)*210*10)/36500
    i7=(int(b7)*180*10)/36500
    i8=(int(b8)*150*10)/36500
    i9=(int(b9)*120*10)/36500
    i10=(int(b10)*90*10)/36500
    i11=(int(b11)*60*10)/36500
    i12=(int(b12)*30*10)/36500
    est= float(i1)+float(i2)+float(i3)+float(i4)+float(i5)+float(i6)+float(i7)+float(i8)+float(i9)+float(i10)+float(i11)+float(i12)



# Yearly Account section
    bbb=be10.get()
    bbb1=be11.get()
    bbb2=be12.get()

    bint=(int(bbb)*int(bbb1)*1)/100
    ttbl= int(bbb)+ int(bts)
    totlint= int(bint)+ int(est)


    obl20 = Label(frame3, text="पाउन पर्ने व्याज:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=4)
    obl20 = Label(frame3, text=totlint, font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=4)

#tax
    tax=(int(totlint))*(int(bbb2)/100)
    tax1= int(tax)
    totlint2= int(totlint)-float(tax)
    totlint3=int(totlint2)
#total balance in tne account
    blance=int(ttbl)+int(totlint2)

    obl21 = Label(frame3, text="घटाइएको कर:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=5)
    obl21 = Label(frame3, text=tax1, font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=5)
    obl22 = Label(frame3, text="पायको कुल ब्याज:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=6)
    obl22 = Label(frame3, text=totlint3, font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=6)
    obl22 = Label(frame3, text="खातामा कुल ब्लान्स:", font=("times", 14, "bold", "italic"), bd=10).grid(column=0, row=7)
    obl22 = Label(frame3, text=blance, font=("times", 14, "bold", "italic"), bd=10).grid(column=1, row=7)

    #database
# write to csv file code here
    with open('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['ACC_NO','Saving', 'pauna_parne_interest','Payako_interest','Tax','Balance'])
        if os.stat('file.csv').st_size == 0:  # if file is not empty than header write else not
             dict_writer.writeheader()
        dict_writer.writerow({
            'ACC_NO': acc,
            'Saving': saving,
            'pauna_parne_interest': totlint,
            'Payako_interest': totlint3,
            'Tax':tax1,
            'Balance':blance,

        })




# ttle frame

l2 = Label(window, text='हातेमालो बचत तथा ऋण सहकारी सस्था लि.', font=("himalaya", 16, "bold"), fg="black",bg='#D1F5FF', anchor=W,
           justify=LEFT, ).place(x=220, y=9)
l1 = Label(window, text='ग.न.पा - ७ ,बागलुङ्ग.', font=("himalaya", 12, "bold"), fg="black", anchor=W,bg='#D1F5FF', justify=CENTER,
           bd=10).place(x=310, y=38)
l3 = Label(window, text='ACCOUNT NO:', font=("himalaya", 12, "bold"),bg='#79BAEC',fg="black", anchor=W, justify=CENTER,
           bd=10,).place(x=170, y=80)
we= Entry(window, bd=5,)
we.place(x=320, y=86)
we.focus()

# months secction
frame1 = LabelFrame(window, text="महिनाको हिसाबले वर्षको बचत प्रविष्ट गर्नुहोस्", font=("times", 14, "bold"), padx=10,
                    pady=10, bd=5)
frame1.place(x=30, y=130)

# label section
l3 = Label(frame1, text="श्रावणको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                              row=3)
l4 = Label(frame1, text="भाद्रको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                             row=4)
l5 = Label(frame1, text="आश्विनको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                              row=5)
l6 = Label(frame1, text="कार्तिकको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                               row=6)
l7 = Label(frame1, text="मंसिरको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                             row=7)
l8 = Label(frame1, text="पौषको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                           row=8)
l9 = Label(frame1, text="माघको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                           row=9)
l10 = Label(frame1, text="फाल्गुणको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(
    column=0, row=10)
l11 = Label(frame1, text="चैत्रको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                              row=11)
l12 = Label(frame1, text="बैशाखको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                              row=12)
l13 = Label(frame1, text="जेष्ठको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                              row=13)
l14 = Label(frame1, text="आषाढको रकम प्रविष्ट गर्नुहोस्:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0,
                                                                                                             row=14)

# entery sectionमंसिर पौष  माघ  फाल्गुण चैत्र बैशाख

e1 = Entry(frame1, bd=5,)
e1.grid(column=1, row=3)
e2 = Entry(frame1, bd=5)
e2.grid(column=1, row=4)
e3 = Entry(frame1, bd=5)
e3.grid(column=1, row=5)
e4 = Entry(frame1, bd=5)
e4.grid(column=1, row=6)
e5 = Entry(frame1, bd=5)
e5.grid(column=1, row=7)
e6 = Entry(frame1, bd=5)
e6.grid(column=1, row=8)
e7 = Entry(frame1, bd=5)
e7.grid(column=1, row=9)
e8 = Entry(frame1, bd=5)
e8.grid(column=1, row=10)
e9 = Entry(frame1, bd=5)
e9.grid(column=1, row=11)
e10 = Entry(frame1, bd=5)
e10.grid(column=1, row=12)
e11 = Entry(frame1, bd=5)
e11.grid(column=1, row=13)
e12 = Entry(frame1, bd=5)
e12.grid(column=1, row=14)
#total saving iin the year


# balance section
frame2 = LabelFrame(window, text="वार्षिक खाताको विवरण ", font=("times", 14, "bold"), padx=10, pady=10, bd=5)
frame2.place(x=500, y=130)
bl14 = Label(frame2, text="खाताको कुल बचत:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=14)
bl15 = Label(frame2, text="ब्याजदर :", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=15)
bl16 = Label(frame2, text="कर दर:", font=("times", 10, "bold", "italic"), bd=10).grid(column=0, row=16)
be10 = Entry(frame2, bd=5)
be10.grid(column=1, row=14)
be11 = Entry(frame2, bd=5)
be11.grid(column=1, row=15)
be12 = Entry(frame2, bd=5)
be12.grid(column=1, row=16)
btn = Button(frame2, text="प्रविष्ट गर्नुहोस्", bd=10, command=action).grid(column=1, row=17)
#clear function

def clear():



    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    be10.delete(0, END)
    be11.delete(0, END)
    be12.delete(0, END)
    we.delete(0,END)


# output section
frame3 = LabelFrame(window, text="आउटपुट सेक्सन ", font=("times", 14, "bold"), padx=10, pady=10, bd=5, )
frame3.place(x=500, y=350)
btn1 = Button(frame3, text="NEXT", bd=10, command=clear).grid(column=1, row=17)





























window.mainloop()
