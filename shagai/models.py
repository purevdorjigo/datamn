from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Баг"
        verbose_name_plural = "Багууд"


class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Тамирчин"
        verbose_name_plural = "Тамирчид"


class ContestType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contest(models.Model):
    type = models.ForeignKey(ContestType, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.type, self.year)

    class Meta:
        verbose_name = "Тэмцээн"
        verbose_name_plural = "Тэмцээнүүд"


class SoloPerformance(models.Model):
    """
    Тамирчдын хувийн цувааны оноог хадгалах модель
    Эхний 12 суман дээр 16 хасаан дээр тавьсан бол
    sum16 талбарыг бөглөн 8 хасаан дээр тавьсан бол
    sum8 талбарыг бөглөнө
    12 суман дээр
        1. 16 хасаан дээр оноо авсан бол 1 оноо
        2. 8 хасаан дээр оноо авсан бол 2 оноо
    4 суман дээр
    """

    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    sum16 = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(12), MinValueValidator(0)]
    )
    sum8 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(12), MinValueValidator(0)],
        verbose_name="8 суманд",
    )
    sum4 = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(4), MinValueValidator(0)],
        verbose_name="4 суманд",
    )
    tulaa = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(4), MinValueValidator(0)],
        help_text="Тулаа хасаа",
        verbose_name="Тулаа хасаа",
    )

    class Meta:
        ordering = ("contest", "player", "-sum16", "-sum8", "-sum4", "-tulaa")
        verbose_name = "Хувийн цуваа"
        verbose_name_plural = "Хувийн цуваа"

    @property
    def total(self):
        return self.sum16 * 1 + self.sum8 * 2 + self.sum4 * 3 + self.tulaa * 4

    @property
    def score(self):
        return self.sum16 + self.sum8 + self.sum4 + self.tulaa

    def __str__(self):
        return "{} {} {}".format(self.player, self.contest, self.total)
