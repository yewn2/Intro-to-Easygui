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

for contact_id, contact_info in contact_list.items():
    print(f"\nContact ID: {contact_id}")

    for key in contact_info:
        print(f"{key}: {contact_info[key]}")
