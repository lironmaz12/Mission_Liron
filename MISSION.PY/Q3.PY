# שאלה 3 סעיף א 

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def main():
    animals = [Dog(), Cat()]

    for animal in animals:
        print(animal.speak())

if __name__ == "__main__":
    main()

# שאלה 3 סעיף ב 
"""
   בפייתוןDuck Typing הביטוי מתייחס לעקרון 
הכוונה היא שבפייתון לא חשוב מהו הטיפוס הפורמלי של האובייקט / מאיזו מחלקה הוא, 
אלא אילו פעולות הוא יודע לבצע בפועל. 
כלומר, כאשר אובייקט מתנהג כמו אובייקט מסוג מסוים - יש לו את המתודות וההתנהגות המצופה מממנו 
אז ניתן להתייחס אליו ככזה, גם אם אינו שייך לאותה מחלקה.
 עיקרון זה מבטא את הגישה הדינמית של פייתון,
המעודדת כתיבת קוד גמיש וממוקד ביכולת ובפונקציונליות ולא בהגדרות טיפוס קשיחות. 

"""

# שאלה 3 סעיף ג 

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

def main():
    animals = [Dog(), Cat()]

    for animal in animals:
        if isinstance(animal, Animal):
            print(animal.speak())
        else:
            print("Not an Animal")

if __name__ == "__main__":
    main()
    
# שאלה 3 סעיף ד 

"""
מטרת רב צורתיות היא לאפשר שימוש אחיד בממשק משותף עבור אובייקטים מסוגים שונים, 
כך שניתן להפעיל עליהם את אותן פעולות מבלי להזדקק לידיעה מוקדמת על מימושם הספציפי. 
עקרון זה מאפשר כתיבת קוד כללי, גמיש ומודולרי, המתמקד בהתנהגות ולא בסוג האובייקט.

תוצאת הרב צורתיות היא שיפור בקריאות הקוד, הפחתת תלות בין רכיבי המערכת, 
הגברת יכולת ההרחבה והתחזוקה של התוכנה, 
שכן ניתן להוסיף מימושים חדשים ללא צורך בשינוי הקוד הקיים.

"""