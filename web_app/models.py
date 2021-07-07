from django.db import models

# Create your models here.


class TUser(models.Model):
    name = models.CharField('Имя', max_length=128, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_users'
        verbose_name = 'куратор'
        verbose_name_plural = 'кураторы'


class TProcedures(models.Model):
    xml_type = models.CharField(max_length=64, null=True, blank=True)
    purchase_number = models.CharField(max_length=64, null=True, blank=True)
    doc_publish_date = models.DateTimeField(null=True, blank=True)
    doc_publish_date_str = models.CharField(max_length=64, null=True, blank=True)
    purchase_object_info = models.CharField(max_length=256, null=True, blank=True)
    reg_num = models.CharField(max_length=64, null=True, blank=True)
    full_name = models.CharField(max_length=256, null=True, blank=True)
    max_price = models.IntegerField(null=True, blank=True)
    curator = models.ForeignKey(TUser, verbose_name='Куратор', on_delete=models.DO_NOTHING, max_length=64, null=True,
                                blank=True)

    def __str__(self):
        return self.purchase_number

    class Meta:
        db_table = 't_procedures'
        ordering = ['doc_publish_date']
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
