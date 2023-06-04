"""
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь один метод экземпляра:

shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif,
при четвертом — paf, и так далее
"""

class Gun:
    def __init__(self):
        self.flag = True

    def shoot(self):
        self.flag = not self.flag
        print(('pif', 'paf')[self.flag])


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()