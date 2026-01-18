

# שאלה 2 סעיפים א, ב, ג 

class City:
    def _init_(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population

    def describe(self):
        return f"{self.name}, {self.country} (population: {self.population})"


class Marina(City):
    def _init_(self, name, country, population, docks_count):
        super()._init_(name, country, population)
        self.docks_count = docks_count

    def marina_info(self):
        return f"Marina docks: {self.docks_count}"


class Park(City):
    def _init_(self, name, country, population, area_km2):
        super()._init_(name, country, population)
        self.area_km2 = area_km2

    def park_info(self):
        return f"Park area: {self.area_km2} km^2"


class Amphitheater(City):
    def _init_(self, name, country, population, seats):
        super()._init_(name, country, population)
        self.seats = seats

    def amphitheater_info(self):
        return f"Amphitheater seats: {self.seats}"


def main():
    name = input("Enter city name for Marina: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    docks = int(input("Enter docks count: "))
    m = Marina(name, country, population, docks)

    print("\n--- Marina Object ---")
    print(m.describe())
    print(m.marina_info())

    name = input("\nEnter city name for Park: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    area = float(input("Enter park area (km^2): "))
    p = Park(name, country, population, area)

    print("\n--- Park Object ---")
    print(p.describe())
    print(p.park_info())

    name = input("\nEnter city name for Amphitheater: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    seats = int(input("Enter seats count: "))
    a = Amphitheater(name, country, population, seats)

    print("\n--- Amphitheater Object ---")
    print(a.describe())
    print(a.amphitheater_info())


if __name__ == "__main__":
    main()
    
    
# שאלה 2 סעיף ד 
"""
מטרת ההורשה היא לאפשר יצירת מחלקות חדשות המבוססות על מחלקה קיימת, תוך שימוש חוזר בתכונות ובמתודות שכבר הוגדרו בה.
עיקרון זה נועד לצמצם כפילויות בקוד, לשמר היררכיה לוגית בין מחלקות,
לאפשר הרחבה והתאמה של פונקציונליות קיימת באמצעות הוספת תכונות ומתודות ייחודיות למחלקות היורשות.
תוצאת ההורשה היא קוד מאורגן, קריא וקל יותר לתחזוקה,
המאפשר הרחבה של המערכת ללא שינוי במחלקות הבסיס, ובכך תורם לגמישות
ולשימוש יעיל בעקרונות התכנות מונחה העצמים.

"""



