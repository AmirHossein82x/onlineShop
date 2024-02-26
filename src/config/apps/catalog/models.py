from django.db import models
from treebeard.mp_tree import MP_Node

from config.apps.catalog.managers import CategoryQuerySet


# Create your models here.

class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class OptionGroup(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option Group'
        verbose_name_plural = 'Option Groups'


class OptionGroupValue(models.Model):
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option Group Value'
        verbose_name_plural = 'Option Group Values'


class ProductClass(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    track_stock = models.BooleanField(default=True)
    required_shipping = models.BooleanField(default=True)
    options = models.ManyToManyField('Option')

    def has_attribute(self):
        return self.attributes.exists()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductAttribute(models.Model):
    class AttributeTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    product = models.ForeignKey(ProductClass, on_delete=models.CASCADE, null=True, related_name='attributes')
    title = models.CharField(max_length=64)
    type = models.CharField(max_length=16, choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.text)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Attribute'
        verbose_name_plural = 'Product Attributes'


class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    title = models.CharField(max_length=64)
    type = models.CharField(max_length=16, choices=OptionTypeChoice.choices, default=OptionTypeChoice.text)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'

