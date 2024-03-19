import easygui


def contact_program():
    contact_list = {
        "1":
            {"First Name": "John",
             "Last Name": "Matua",
             "Mobile": "027 121 1245",
             "Email": "matua_j@maximail.com"},
        "2":
            {"First Name": "Smith",
             "Last Name": "Pearson",
             "Mobile": "029 127 1247",
             "Email": "selat@maximail.co.lt"}
    }
    stop = "No"
    while stop != "Quit":
        stop = easygui.buttonbox("Would you like to search for a contact, "
                                 "print the contact list or add a contact?",
                                 "Actions", ["Search for contact", "Print list",
                                             "Add contact", "Quit"])
        if stop == "Search for contact":
            name_search(contact_list)
        elif stop == "Print list":
            contact_prnt(contact_list)
        elif stop == "Add contact":
            add_contact(contact_list)


def name_search(lst):
    name_type = easygui.buttonbox("Search for first name or last name?",
                                  "Search type",
                                  ["First Name", "Last Name"])
    search = easygui.enterbox(f"What {name_type} would you like to search for?",
                              "Search")
    if name_type == "Last Name":
        for contact_id, contact_info in lst.items():
            if contact_info['Last Name'] == search:
                info_list = []
                for key in contact_info:
                    info_list.append(f"{key}: {contact_info[key]}\n")
                easygui.msgbox("".join(info_list),
                               f"Contact ID: {contact_id}")
                break
            else:
                if contact_id == len(lst):
                    easygui.msgbox("Person not in contact list",
                                   "Not found")
    else:
        for contact_id, contact_info in lst.items():
            if contact_info['First Name'] == search:
                info_list = []
                for key in contact_info:
                    info_list.append(f"{key}: {contact_info[key]}\n")
                easygui.msgbox("".join(info_list),
                               f"Contact ID: {contact_id}")
                break
            else:
                if contact_id == len(lst):
                    easygui.msgbox("Person not in contact list",
                                   "Not found")


def contact_prnt(lst):
    for contact_id, contact_info in lst.items():
        info_list = []
        for key in contact_info:
            info_list.append(f"{key}: {contact_info[key]}\n")
        easygui.msgbox("".join(info_list),
                       f"Contact ID: {contact_id}")


def add_contact(lst):
    cont_id = easygui.enterbox("Enter contact ID: ", "Contact ID")
    lst[cont_id] = {}

    first_name = easygui.enterbox("Enter First name:", "First Name")
    lst[cont_id]['First Name'] = first_name

    last_name = easygui.enterbox("Enter Last name:", "Last Name")
    lst[cont_id]['Last Name'] = last_name

    mobile = easygui.enterbox("Enter Mobile:", "Mobile")
    lst[cont_id]['Mobile'] = mobile

    email = easygui.enterbox("Enter Email:", "Email")
    lst[cont_id]['Email'] = email


contact_program()
