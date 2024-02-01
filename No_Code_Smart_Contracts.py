import tkinter as tk

app = tk.Tk()
app.title("App NoCode Smart Contracts")
app.geometry("850x450")

code = ""

def add_spdx_pragma(contract_name):
    global code
    code = "/*SPDX-License-Identifier: MIT*/ pragma solidity ^0.8.0; contract " + contract_name + " {"

    print("Your contract is " + code)


def ini_contract():
    global contract
    global var_name
    global code
    contract.delete("1.0", tk.END)
    add_spdx_pragma("LFGCONTRACT")
    contract.insert(tk.END, code)
    # code = ""
    var_name.delete(0, tk.END)
    
vars = []

var_type = ""

def set_address():
    global var_type
    var_type = "address "


def set_uint():
    global var_type
    var_type = "uint "


def new_var():
    global code
    global var_type
    global var_name
    contract.delete("1.0", tk.END)
    var_name1 = var_name.get()
    my_new_var = var_type + var_name1
    print("new Var is " + var_type + " " + var_name1)
    code = code + " " + my_new_var + ";"    
    print("code is " + code)
    contract.insert(tk.END, code)
    var_name.delete(0, tk.END)


def add_deposit():
    global code
    code = code + " " + "uint amountDeposited; function deposit() public payable{amountDeposited = msg.value;}"
    contract.delete("1.0", tk.END)
    contract.insert(tk.END, code)



def close_contract():
    global code
    code = code + " }"
    contract.delete("1.0", tk.END)
    contract.insert(tk.END, code)

var_name = tk.Entry(app, width=15, font=('Arial', 10))
var_name.place(x=125, y=65)

var_type1 = tk.Button(app, text = "address", width=7, background='#377af4', foreground="white", font=('Arial', 10), cursor='hand2', command=set_address)
var_type1.place(x=50, y = 50)

var_type2 = tk.Button(text = "uint",  width=7, background='#377af4', foreground="white", font=('Arial', 10), cursor='hand2', command=set_uint)
var_type2.place(x=50, y = 80)

add_var_but = tk.Button(app, text= "Add Var",  width=7, background='#377af4', foreground="white", font=('Arial', 10), cursor='hand2', command=new_var)
add_var_but.place(x=240, y=61)

deposit = tk.Button(app, text="Add Deposit ETH",  width=10, background='#f90f04', foreground="white", font=('Arial', 13), cursor='hand2', command=add_deposit)
deposit.place(x=50, y=100)

contract = tk.Text(app, wrap="word", height=10, width=85, state="normal")
contract.place(x=50, y=250)

boton = tk.Button(app, text="Ini Contract",  width=10, background='#377af4', foreground="white", font=('Arial', 13), cursor='hand2', command=ini_contract)
boton.place(x=5, y=10)

close = tk.Button(app, text="close contract }",  width=10, background='#377af4', foreground="white", font=('Arial', 11), cursor='hand2', command=close_contract)
close.place(x=5, y=125)

app.mainloop() 
