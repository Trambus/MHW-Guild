# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class weapon(models.Model):
    className = models.CharField(max_length=50, default="Weapon")
    url = models.CharField(max_length=5, default="wep")
    category = models.CharField(max_length=30, default="Light")
    damageType = models.CharField(max_length=30, default="Cutting")

    def __str__(self):
        return self.className + ' - ' + self.category + ' - id: ' + str(self.id)

# swordShield.id: 1
class swordShield(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# dualBlades.id: 2
class dualBlades(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# longsword.id: 3
class longsword(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# lightBowgun.id: 4
class lightBowgun(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# greatsword.id: 5
class greatsword(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# hammer.id: 6
class hammer(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# lance.id: 7
class lance(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# gunlance.id: 8
class gunlance(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# heavyBowgun.id: 9
class heavyBowgun(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# huntingHorn.id: 10
class huntingHorn(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# switchAxe.id: 11
class switchAxe(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# chargeBlade.id: 12
class chargeBlade(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# insectGlaive.id: 13
class insectGlaive(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()

# bow.id: 14
class bow(models.Model):
    weapon = models.ForeignKey(weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    raw = models.IntegerField()
    element = models.IntegerField()
    elementType = models.CharField(max_length=30)
    status = models.IntegerField()
    statusType = models.CharField(max_length=30)
    affinity = models.IntegerField()
    sharpness = models.IntegerField()
