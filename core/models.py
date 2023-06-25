from django.db import models
import uuid
from datetime import date
from django.contrib.auth.models import AbstractUser, BaseUserManager
from core.utils import get_current_user


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    mobile =  models.CharField(max_length=15, null=False)
    reporting_to = models.ForeignKey('User', null=True, on_delete=models.PROTECT)
    ROLES = (
        ("AGENT", "Agent"),
        ("AREA_MANAGER", "Area Manager"),
        ("REGIONAL_MANAGER", "Regional Manager"),
    )
    designation = models.CharField(max_length = 20, choices = ROLES, default = 'AGENT')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()



class BaseModel(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    created_by = models.ForeignKey(User, null=True, editable=False, related_name='%(class)s_created', on_delete=models.CASCADE)
    update_by = models.ForeignKey(User, null=True, editable=False, related_name='%(class)s_updated', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated():
            self.modified_by = user
            if not self.id:
                self.created_by = user
        super(BaseModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated():
            self.modified_by = user
            if not self.id:
                self.created_by = user
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Customer(BaseModel):
    name = models.CharField(max_length=100, null=False)
    address = models.TextField(max_length=500, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Customers"


class WareHouse(BaseModel):
    name = models.CharField(max_length=100, null=False)
    address = models.TextField(max_length=500, null=True, blank=True)
    longitude = models.CharField(max_length=10, null=True)
    latitude = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Warehouses"


class Asset(BaseModel):
    type = models.CharField(max_length=100, null=False)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    warehouse = models.ForeignKey(WareHouse, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Assets"


class Branch(BaseModel):
    name = models.CharField(max_length=100, null=False)
    ifsc = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Branches"


class Loan(BaseModel):
    loan_account_number = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=10, null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    loan_created_date = models.DateField(default=date.today)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, null=True, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.loan_account_number)

    class Meta:
        verbose_name_plural = "Loans"