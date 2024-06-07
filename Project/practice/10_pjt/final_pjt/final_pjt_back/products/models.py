from django.db import models
from django.core.exceptions import ValidationError
from django.db import models

def validate_specific_number(value):
    if value not in (1, 2, 3):
        raise ValidationError('This field must be {}'.format((1, 2, 3)))

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField(
        validators=[validate_specific_number]
    )
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    mtrt_int = models.TextField()
    DSname = models.TextField()


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts,on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()