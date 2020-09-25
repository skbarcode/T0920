# Generated by Django 2.2.15 on 2020-09-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_auto_20200925_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract_info',
            name='delivery_Method',
            field=models.CharField(choices=[('0', '快递发货'), ('1', '物流发货'), ('2', '送货上门'), ('3', '客户自提'), ('4', '无须运输')], max_length=24, verbose_name='交货方式'),
        ),
        migrations.AlterField(
            model_name='contract_info',
            name='delivery_dates',
            field=models.CharField(choices=[('0', '三个工作日内'), ('1', '七个工作日内'), ('2', '十个工作日内'), ('3', '两周内'), ('4', '四周内'), ('5', '四到六周'), ('6', '六到八周')], max_length=24, verbose_name='交货时间'),
        ),
        migrations.AlterField(
            model_name='contract_info',
            name='freight',
            field=models.CharField(choices=[('0', '甲方承担'), ('1', '乙方承担'), ('3', '无须运输')], max_length=24, verbose_name='运费'),
        ),
        migrations.AlterField(
            model_name='contract_info',
            name='invoice_info',
            field=models.CharField(choices=[('0', '13%增值税专用发票'), ('1', '6%增值税专用发票'), ('2', '6%增值税普通发票'), ('3', '收据')], max_length=24, verbose_name='发票税率'),
        ),
    ]
