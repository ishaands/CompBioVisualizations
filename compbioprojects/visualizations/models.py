from django.db import models

# Create your models here.


class DemoDNA(models.Model):
    # string is the dna string itself. The string can be as long as possible.
    string = models.TextField()
    # module represents the module that this dna is from.
    module = models.TextField()

    def __repr__(self):
        return "Module: {} DNA: {}".format(module, string)

    def __str__(self):
        print("Module: {} DNA: {}".format(module, string))
