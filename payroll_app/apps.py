'''
We hereby attest to the truth of the following facts:

We have not discussed the HTML/CSS/Bootstrap/Python/Django language code in our program with anyone other than our instructor or the teaching assistants assigned to this course.

We have not used HTML/CSS/Bootstrap/Python/Django language code obtained from another student, or any other unauthorized source, either modified or unmodified

If any HTML/CSS/Bootstrap/Python/Django language code or docomentation used in our program was obtained from another source, such as a textbook or course notes, that has been clearly noted with a proper citation in the comments of our program.

Bootstrap. (n.d.). Navbar. Bootstrap. https://getbootstrap.com/docs/5.0/components/navbar/.
Bootstrap. (n.d.). Select. Bootstrap. https://getbootstrap.com/docs/5.0/forms/select/.
Bootstrap. (n.d.). Spacing. Bootstrap. https://getbootstrap.com/docs/5.0/utilities/spacing/.
Chapagain, S. (2023, July 6). How to Use a Foreign Key to Create Many-to-One Relationships in Django. Free Code Camp. https://www.freecodecamp.org/news/what-is-one-to-many-relationship-in-django/
Django. (n.d.). Many-to-one relationships. Django. https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_one/
W3Schools. (n.d.). CSS3 Borders. W3Schools. https://www.w3schools.com/css/css3_borders.asp.
W3Schools. (n.d.). CSS3 Images. W3Schools. https://www.w3schools.com/css/css3_images.asp.
W3Schools. (n.d.). CSS3 Shadows. W3Schools. https://www.w3schools.com/css/css3_shadows.asp.
W3Schools. (n.d.). CSS3 Text Justify. W3Schools. https://www.w3schools.com/cssref/css3_pr_text-justify.php.
W3Schools. (n.d.). CSS Text Spacing. W3Schools. https://www.w3schools.com/css/css_text_spacing.asp.
W3Schools. (n.d.). HTML <input> placeholder Attribute. W3Schools. https://www.w3schools.com/tags/att_input_placeholder.asp.
yuvi. (2013, October 28). django difference between - one to one, many to one and many to many. Stack Overflow. https://stackoverflow.com/questions/19641841/django-difference-between-one-to-one-many-to-one-and-many-to-many
'''

from django.apps import AppConfig


class PayrollAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "payroll_app"
