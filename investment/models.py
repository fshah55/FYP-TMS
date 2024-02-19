from django.db import models

# Create your models here.
class Invest(models.Model):
    account = models.ForeignKey('accounts.Staff', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=30)
    shares = models.DecimalField(max_digits=10, decimal_places=2)
    spot_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return str(self.id)
