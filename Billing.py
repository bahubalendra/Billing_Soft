from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        # self= Tk()
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing")
        bg_color = "#074463"
        titel = Label(self.root, text="Billing", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ====Variables====
        # ====cosmetis====
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        # ====Grocery===
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # ====cold drinks====
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        # ===Total product and tax variable==
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        # ===customer details==
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ===customer details frame===
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=5)

        cphn_lbl = Label(F1, text=" Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                            column=3,
                                                                                                            padx=10,
                                                                                                            pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, width=10, text="Search", command=self.find_bill, bd=7, font="arial 10 bold").grid(row=0,
                                                                                                                column=6,
                                                                                                                padx=10,
                                                                                                                pady=10)

        # =====cousmetics Frame====
        F2 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text="Bath soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1,
                                             padx=10, pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=1,
                                                   column=1,
                                                   padx=10,
                                                   pady=10)

        face_w_lbl = Label(F2, text="face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        face_w_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2,
                                               column=1,
                                               padx=10,
                                               pady=10)

        hair_s_lbl = Label(F2, text="Hair spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w"
        )
        hair_s_txt = Entry(F2, width=10, textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3,
                                               column=1,
                                               padx=10,
                                               pady=10)

        hair_g_lbl = Label(F2, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w"
        )
        hair_g_txt = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4,
                                               column=1,
                                               padx=10,
                                               pady=10)

        body_l_lbl = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w"
        )
        body_l_txt = Entry(F2, width=10, textvariable=self.loshan, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=5,
                                               column=1,
                                               padx=10,
                                               pady=10)

        # =====Grocery=====
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1,
                                           padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1,
                                           column=1,
                                           padx=10,
                                           pady=10)
        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        g3_txt = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2,
                                           column=1,
                                           padx=10,
                                           pady=10)
        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w"
        )
        g4_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3,
                                           column=1,
                                           padx=10,
                                           pady=10)
        g5_lbl = Label(F3, text="sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w"
        )
        g5_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4,
                                           column=1,
                                           padx=10,
                                           pady=10)
        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w"
        )
        g6_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5,
                                           column=1,
                                           padx=10,
                                           pady=10)

        # ====Cold Drinks===
        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        c1_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1,
                                           padx=10, pady=10)
        c2_lbl = Label(F4, text="Cock", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        c2_txt = Entry(F4, width=10, textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1,
                                           column=1,
                                           padx=10,
                                           pady=10)
        c3_lbl = Label(F4, text="frooti", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        c3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2,
                                           column=1,
                                           padx=10,
                                           pady=10)
        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w"
        )
        c4_txt = Entry(F4, width=10, textvariable=self.thumbs_up, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3,
                                           column=1,
                                           padx=10,
                                           pady=10)
        c5_lbl = Label(F4, text="limca", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w"
        )
        c5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4,
                                           column=1,
                                           padx=10,
                                           pady=10)
        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w"
        )
        c6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5,
                                           column=1,
                                           padx=10,
                                           pady=10)

        # ===Bill Area====
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
        bill_titel = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # ==Button Frame==
        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total Cosmetics Price", fg="white", bg=bg_color,
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=1, padx=10)

        m2_lbl = Label(F6, text="Total Grocery Price", fg="white", bg=bg_color,
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=1, padx=10)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", fg="white", bg=bg_color,
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, pady=1, padx=10)

        m1_lbl = Label(F6, text="Cosmetics Tax", fg="white", bg=bg_color, font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=1, padx=10)

        m2_lbl = Label(F6, text=" Grocery Tax", fg="white", bg=bg_color, font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, pady=1, padx=10)

        m3_lbl = Label(F6, text="Cold Drinks Tax", fg="white", bg=bg_color, font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, pady=1, padx=10)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", pady=15, bd=2, width=10,
                           font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, text="Genrate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15,
                           bd=2, width=10,
                           font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, bd=2,
                           width=10,
                           font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.exit_app, bg="cadetblue", fg="white", pady=15, bd=2,
                          width=10,
                          font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p = self.soap.get() * 10
        self.c_fw_p = self.face_wash.get() * 20
        self.c_fc_p = self.face_cream.get() * 30
        self.c_hs_p = self.spray.get() * 40
        self.c_hg_p = self.gell.get() * 50
        self.c_bl_p = self.loshan.get() * 60
        # ==total_cosmetic_price
        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fw_p +
            self.c_fc_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        # ===total_Grocery_price
        self.g_r_p = self.rice.get() * 70
        self.g_f_p = self.food_oil.get() * 80
        self.g_d_p = self.daal.get() * 90
        self.g_s_p = self.sugar.get() * 100
        self.g_w_p = self.wheat.get() * 110
        self.g_t_p = self.tea.get() * 120
        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_s_p +
            self.g_w_p +
            self.g_t_p
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        # total_cold drinks_price
        self.d_m_p = self.maza.get() * 10
        self.d_f_p = self.frooti.get() * 20
        self.d_c_p = self.cock.get() * 30
        self.d_t_p = self.thumbs_up.get() * 40
        self.d_s_p = self.sprite.get() * 50
        self.d_l_p = self.limca.get() * 60
        self.total_drinks_price = float(
            self.d_m_p +
            self.d_f_p +
            self.d_c_p +
            self.d_t_p +
            self.d_s_p +
            self.d_l_p
        )
        self.cold_drinks_price.set("Rs. " + str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price * 0.05), 2)
        self.cold_drinks_tax.set("Rs. " + str(self.d_tax))

        self.total_bill = float(self.total_cosmetic_price +
                                self.total_grocery_price +
                                self.total_drinks_price +
                                self.c_tax +
                                self.g_tax +
                                self.d_tax
                                )

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tWell come subhahsree Reatil\n")
        self.textarea.insert(END, f"\nBill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\nPhone Number : {self.c_phon.get()}")
        self.textarea.insert(END, f"\n======================================")
        self.textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n======================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer Details are must")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # ===Cosmetic===
            if self.soap.get() != 0:
                self.textarea.insert(END, f"\n Bath soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get() != 0:
                self.textarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.face_wash.get() != 0:
                self.textarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fc_p}")

            if self.spray.get() != 0:
                self.textarea.insert(END, f"\n Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")

            if self.gell.get() != 0:
                self.textarea.insert(END, f"\n Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")

            if self.loshan.get() != 0:
                self.textarea.insert(END, f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")

            # ===Grocery==
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.food_oil.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")

            if self.daal.get() != 0:
                self.textarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # ==cold drinks==
            if self.maza.get() != 0:
                self.textarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")

            if self.cock.get() != 0:
                self.textarea.insert(END, f"\n Cock\t\t{self.cock.get()}\t\t{self.d_c_p}")

            if self.frooti.get() != 0:
                self.textarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.sprite.get() != 0:
                self.textarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            if self.limca.get() != 0:
                self.textarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")

            if self.thumbs_up.get() != 0:
                self.textarea.insert(END, f"\n Thumbs Up\t\t{self.thumbs_up.get()}\t\t{self.d_t_p}")

            self.textarea.insert(END, f"\n--------------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drinks_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

            self.textarea.insert(END, f"\n--------------------------------------")
            self.textarea.insert(END, f"\n Total Bill : \t\t\tRs. {self.total_bill}")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "do You want to save the Bill?")
        if op > 0:
            self.bill_data = self.textarea.get("1.0", END)
            f1 = open("Bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Save", f"Bill No. : {self.bill_no.get()} Saved successful")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"Bills/{i}", "r")
                self.textarea.delete('1.0', END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to Clear Data?")
        if op > 0:
            # ====cosmetis====
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            # ====Grocery===
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ====cold drinks====
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            # ===Total product and tax variable==
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            # ===customer details==
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
