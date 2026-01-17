# שאלה 1 סעיף א 

class Invoice:
    def __init__(self, invoice_number, customer_name, product_name, quantity, price_per_unit):
        self.invoice_number = invoice_number
        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        self.__price_per_unit = price_per_unit  

    @property
    def price_per_unit(self):
        return self.__price_per_unit

    @price_per_unit.setter
    def price_per_unit(self, value):
        if value > 0:
            self.__price_per_unit = value
        else:
            raise ValueError("Price must be a positive number")

    def calculate_total(self):
        return self.quantity * self.__price_per_unit

    def display_invoice(self):
        return (
            f"Invoice Number: {self.invoice_number}\n"
            f"Customer Name: {self.customer_name}\n"
            f"Product Name: {self.product_name}\n"
            f"Quantity: {self.quantity}\n"
            f"Total Price: {self.calculate_total()}"
        )

# שאלה 1 סעיף ב 

invoice_number = input("Enter invoice number: ")
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price_per_unit = float(input("Enter price per unit: "))

invoice = Invoice(
    invoice_number,
    customer_name,
    product_name,
    quantity,
    price_per_unit
)

print(invoice.display_invoice())


# שאלה 1 סעיף ג 

"""
מטרת הכימוס היא להסתיר את המימוש הפנימי של האובייקט
ולהגביל את הגישה הישירה לנתוניו, תוך חשיפת ממשק מבוקר וברור לשימוש חיצוני. 
עיקרון זה נועד להגן על שלמות הנתונים, למנוע שימוש שגוי בתכונות האובייקט
, ולאכוף כללי גישה ולוגיקה פנימית דרך מתודות ייעודיות.

תוצאת הכימוס היא יצירת קוד מאורגן, בטוח וקל יותר לתחזוקה, 
, שבו השינויים במימוש הפנימי אינם משפיעים על אופן השימוש באובייקט, ובכך משתפרת היציבות, 
המודולריות והאמינות של המערכת.

"""