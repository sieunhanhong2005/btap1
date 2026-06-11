inventory_stock = 100
total_revenue = 0

def add_stock(amount):
    global inventory_stock
    inventory_stock += amount
    print(f"Da nhap kho thanh cong {amount} san pham")
    print(f"Ton kho hien tai: {inventory_stock}")
    
def process_sale(quantity):
    if quantity > inventory_stock:
        print(f"Khong con du hang ton khp. Trong kho chi con {inventory_stock}")
        return False
    return True

def calculate_final_price(quantity,price):
    subtotal = quantity * price
    discount = subtotal * 0.1 if subtotal >= 1000 else 0.0
    tax = (subtotal - discount) * 0.08
    final_total = subtotal - discount + tax
    print(f"Hoa don chi tiet: ")
    print(f"So luong: {quantity}   |   Don gia: {price}")
    print(f"Tam tinh: {subtotal}   |   Giam gia 10%: {discount}")
    print(f"Thue VAT 8%: {tax}   |   Tong thanh toan: {final_total}")
    return final_total

def print_report():
    print(f"---BAO CAO KINH DOANH---")
    print(f"Ton kho hien tai: {inventory_stock} san pham")
    print(f"Tong doanh thu: {total_revenue}")
    
while True:
    print(f"-----TECHSTORE MANAGEMENT SYSTEM-----")
    print(f"1. Nhap them hang vao kho")
    print(f"2. Ban hang ( tinh toan hoa don )")
    print(f"3. Xem bao cao tong quan")
    print(f"4. Thoat chuong trinh")
    
    choice = input("Moi ban lua chon chuc nang: ")
    
    if choice == "1":
        amount = int(input("Nhap so luong san pham muon them: "))
        if amount <= 0:
            print("Du lieu nhap vao phai lon hon 0")
        else:
            add_stock(amount)
            
    elif choice == "2":
        quantity = int(input("Nhap so luong muon mua: "))
        if quantity <= 0:
            print("Du lieu nhap vao phai lon hon 0")
            continue
        if process_sale(quantity):
            price = float(input("Nhap don gia: "))
            if price <= 0:
                print("So tien phai lon hon 0")
                continue
            final_price = calculate_final_price(quantity,price)
            inventory_stock -= quantity
            total_revenue += final_price
            print("Da ban thanh cong")
            
    elif choice == "3":
        print_report()
        
    elif choice == "4":
        print("Bye")
    else:
        print("Lua chon ko hop le. Nhap lai di ")