from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Contract(models.Model):
    contractid = models.BigAutoField(db_column='contractId', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    managerid = models.BigIntegerField(db_column='managerId')  # Field name made lowercase.
    contractstartdate = models.DateTimeField(db_column='contractStartDate')  # Field name made lowercase.
    contractenddate = models.DateTimeField(db_column='contractEndDate', blank=True,
                                           null=True)  # Field name made lowercase.
    roomid = models.BigIntegerField(db_column='roomId')  # Field name made lowercase.
    contractdeposit = models.IntegerField(db_column='contractDeposit')  # Field name made lowercase.
    contractrent = models.IntegerField(db_column='contractRent')  # Field name made lowercase.
    contractpaytype = models.SmallIntegerField(db_column='contractPayType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contract'
        app_label = 'MainDashboard'


class Electricity(models.Model):
    electricityid = models.BigAutoField(db_column='electricityId', primary_key=True)  # Field name made lowercase.
    electricitynumber = models.FloatField(db_column='electricityNumber')  # Field name made lowercase.
    electricitydate = models.DateTimeField(db_column='electricityDate')  # Field name made lowercase.
    roomid = models.BigIntegerField(db_column='roomId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Electricity'
        app_label = 'MainDashboard'


class Managers(models.Model):
    managersid = models.BigAutoField(db_column='managersId', primary_key=True)  # Field name made lowercase.
    managersname = models.CharField(db_column='managersName', max_length=50)  # Field name made lowercase.
    managersaccount = models.CharField(db_column='managersAccount', max_length=45, blank=True,
                                       null=True)  # Field name made lowercase.
    managerspassword = models.CharField(db_column='managersPassword', max_length=45, blank=True,
                                        null=True)  # Field name made lowercase.
    managerskeyindate = models.DateTimeField(db_column='managersKeyinDate', blank=True,
                                             null=True)  # Field name made lowercase.
    managerslogindate = models.DateTimeField(db_column='managersLoginDate', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Managers'
        app_label = 'MainDashboard'


class Rent(models.Model):
    rentid = models.BigIntegerField(db_column='rentId', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    managerid = models.BigIntegerField(db_column='managerId')  # Field name made lowercase.
    rentamount = models.IntegerField(db_column='rentAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rent'
        app_label = 'MainDashboard'


class Room(models.Model):
    roomid = models.BigAutoField(db_column='roomId', primary_key=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='roomName', max_length=50)  # Field name made lowercase.
    roommanagersid = models.BigIntegerField(db_column='roomManagersId')  # Field name made lowercase.
    roomordername = models.CharField(db_column='roomOrderName', max_length=60)  # Field name made lowercase.
    roomordermemo = models.TextField(db_column='roomOrderMemo')  # Field name made lowercase.
    roomlastmodifydatetime = models.DateTimeField(db_column='roomLastModifyDatetime', blank=True,
                                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Room'
        app_label = 'MainDashboard'


class Users(models.Model):
    userid = models.BigAutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=60)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=120)  # Field name made lowercase.
    userclass = models.CharField(db_column='userClass', max_length=60)  # Field name made lowercase.
    usertel = models.CharField(db_column='userTel', max_length=45)  # Field name made lowercase.
    useraddress = models.CharField(db_column='userAddress', max_length=120)  # Field name made lowercase.
    userkeyindate = models.DateTimeField(db_column='userKeyinDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
        app_label = 'MainDashboard'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = 'MainDashboard'
