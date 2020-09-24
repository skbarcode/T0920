from django.db import models


class company(models.Model):
    title = models.CharField(max_length=24, verbose_name='公司名称')
    title_en = models.CharField(verbose_name='公司名称英文', max_length=64)
    address = models.CharField(verbose_name='地址', max_length=32)
    telphone = models.CharField(verbose_name='电话', max_length=12)
    fax = models.CharField(verbose_name='传真', max_length=12)
    email = models.EmailField(verbose_name='邮件', max_length=24)
    url = models.URLField(verbose_name='网址', max_length=24)
    bank = models.CharField(verbose_name='对公银行', max_length=24)
    bank_no = models.CharField(verbose_name='银行帐号', max_length=24)
    logo = models.ImageField(verbose_name='LOGO')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '甲方公司'
        verbose_name_plural = '甲方公司'


class contact_information(models.Model):  # 联系信息
    person = models.CharField(verbose_name='联系人', max_length=12)
    address = models.CharField(verbose_name='联系地址', max_length=64)
    phone = models.CharField(verbose_name='联系手机', max_length=12)
    tel = models.CharField(verbose_name='联系电话', max_length=12)
    fax = models.CharField(verbose_name='联系传真', max_length=12)

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = '联系信息'
        verbose_name_plural = '联系信息'


class client(models.Model):  # 客户信息
    title = models.CharField(max_length=24, verbose_name='公司名称')
    address = models.CharField(verbose_name='地址', max_length=32)
    telphone = models.CharField(verbose_name='电话', max_length=12)
    fax = models.CharField(verbose_name='传真', max_length=12)
    bank = models.CharField(verbose_name='对公银行', max_length=24)
    bank_no = models.CharField(verbose_name='银行帐号', max_length=24)
    person = models.ForeignKey(contact_information, verbose_name='联系人', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = '客户信息'


class unit(models.Model):
    name = models.CharField(max_length=36, verbose_name='单位')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '单位'
        verbose_name_plural = '单位'


class Brand(models.Model):
    name = models.CharField(max_length=24, verbose_name='品牌')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class type(models.Model):
    name = models.CharField(max_length=24, verbose_name='分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Supplier(models.Model):  # 供应商
    name = models.CharField(max_length=64, verbose_name='供应商', unique=True)
    advantage = models.CharField(max_length=256, verbose_name='优势品牌', blank=True, null=True)
    advantage = models.CharField(max_length=64, verbose_name='联系人', blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name='联系手机', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'


class product(models.Model):
    name = models.CharField(verbose_name='品名规格', max_length=36, unique=True)
    brand = models.ForeignKey(to='Brand', verbose_name='品牌', on_delete=models.CASCADE)
    nickname = models.CharField(verbose_name='供应商型号', max_length=36, blank=True, null=True)
    unit = models.ForeignKey(unit, on_delete=models.CASCADE, verbose_name='单位')
    type = models.ForeignKey(type, verbose_name='分类', default=0, on_delete=models.CASCADE)
    cost_price = models.FloatField(verbose_name='产品进价', default=0)
    min_selling_price = models.FloatField(verbose_name='最低售价', default=0)
    meno = models.TextField(verbose_name='备注', default='', blank=True, null=True)
    supplier = models.ForeignKey(to='Supplier', verbose_name='供应商', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品资料'
        verbose_name_plural = '产品资料'


class product_info(models.Model):
    product = models.ForeignKey(product, verbose_name='品名规格', on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name='数量')
    price = models.FloatField(verbose_name='单价', default=0)
    amount = models.FloatField(verbose_name='金额')
    meno = models.CharField(max_length=64, verbose_name='备注')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = '产品明细'
        verbose_name_plural = '产品明细'


class payment_info(models.Model):
    name = models.CharField(max_length=36, verbose_name='付款方式')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '付款方式'
        verbose_name_plural = '付款方式'


class contract_info(models.Model):
    name = models.CharField(verbose_name='合同名称', max_length=12, default='产品购销合同')
    company = models.ForeignKey(company, verbose_name='甲方公司', default=0, on_delete=models.CASCADE)
    client = models.ForeignKey(client, verbose_name='乙方公司', on_delete=models.CASCADE)
    contract_no = models.CharField(verbose_name='合同编号', max_length=16, )
    product_info = models.ForeignKey(to='product_info', verbose_name='产品明细表', on_delete=models.CASCADE)
    total_amount = models.FloatField(verbose_name='总金额', max_length=12)
    delivery_date = [
        (0, '三个工作日内'),
        (1, '七个工作日内'),
        (2, '十个工作日内'),
        (3, '两周内'),
        (4, '四周内'),
        (5, '四到六周'),
        (6, '六到八周'),
    ]
    freight_choices = [
        (0, '甲方承担'),
        (1, '乙方承担'),
        (3, '无须运输'),
    ]
    delivery_Method_choices = [
        (0, '快递发货'),
        (1, '物流发货'),
        (2, '送货上门'),
        (3, '客户自提'),
        (4, '无须运输'),

    ]
    invoice_info_choices = [
        (0, '13%增值税专用发票'),
        (1, '6%增值税专用发票'),
        (2, '6%增值税普通发票'),
        (3, '收据'),
    ]
    delivery_dates = models.CharField(choices=delivery_date, verbose_name='交货时间', default=1, max_length=1)
    freight = models.CharField(choices=freight_choices, verbose_name='运费', default=0, max_length=1)
    delivery_Method = models.CharField(choices=delivery_Method_choices, verbose_name='交货方式', default=0, max_length=1)
    invoice_info = models.CharField(choices=invoice_info_choices, verbose_name='发票税率', default=0, max_length=1)
    payment_info = models.ForeignKey(payment_info, verbose_name='付款信息', on_delete=models.CASCADE, default=0, )
    add_info = models.CharField(max_length=256, verbose_name='补充协议',
                                default='打印头质保三个月或三十公里，先到为准，人为或物理损坏不在质保范围（包含但不限于打印头表面有白点、磨伤、损坏、变形、烧头等）')
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期')

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = '合同信息'
        verbose_name_plural = '合同信息'

class Model_record(models.Model):
    sk_model = models.CharField(max_length=32,verbose_name='公司型号')
    sp_model = models.CharField(max_length=32,verbose_name='供应商型号')
    supplier = models.ForeignKey(Supplier,verbose_name='供应商',on_delete=models.CASCADE)
    meno = models.CharField(max_length=128,verbose_name='备注',blank=True,null=True)

    def __str__(self):
        return self.sk_model
    class Meta:
        verbose_name='型号登记'
        verbose_name_plural ='型号登记'