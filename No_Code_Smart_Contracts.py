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
    add_var(var_type, var_name.get())
    contract.insert(tk.END, code)
    code = ""
    var_name.delete(0, tk.END)
    

vars = []

def add_var(var_type, var_name):
    myVar = {
        "type" : "",
        "name" : ""
    }
    vars.append(myVar)
    global code
    code = code + " " + var_type + " " + var_name + ";"

var_name = tk.Entry(app, width=10)
var_name.place(x=130, y=100)

var_type = ""

def set_address():
    global var_type
    var_type = "address"

var_type1 = tk.Button(text = "address", command=set_address)
var_type1.place(x=190, y = 100)

def set_uint():
    global var_type
    var_type = "uint"

var_type2 = tk.Button(text = "uint", command=set_uint)
var_type2.place(x=250, y = 100)

contract = tk.Text(app, wrap="word", height=10, width=80, state="normal")
contract.place(x=50, y=150)

boton = tk.Button(app, text="Ini Contract", command=ini_contract)
boton.place(x=10, y=100)

app.mainloop() 
