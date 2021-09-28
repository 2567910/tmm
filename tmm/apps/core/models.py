from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        verbose_name_plural = "People"

class Course(models.Model):

    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        verbose_name = _("Cource")
        verbose_name_plural = _("Countries")
    def __str__(self):
        return self.name

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Test(TranslatableModel):
    translations = TranslatedFields(
        name = models.TextField(),
        year = models.IntegerField()
    )

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Test")
    def __str__(self):
        return self.name