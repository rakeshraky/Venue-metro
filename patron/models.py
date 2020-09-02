from django.db import models


class FactMembers(models.Model):
    aid = models.CharField(db_column='AID', max_length=20,primary_key=True)  # Field name made lowercase.
    mid = models.CharField(db_column='MID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid = models.CharField(db_column='CID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tl = models.CharField(db_column='TL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fn = models.CharField(db_column='FN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ln = models.CharField(db_column='LN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dob = models.CharField(db_column='DOB', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mp = models.CharField(db_column='MP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    eid = models.CharField(db_column='EID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tg = models.CharField(db_column='TG', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ms = models.CharField(db_column='MS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g = models.CharField(db_column='G', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pc = models.CharField(db_column='PC', blank=True,max_length=20, null=True)  # Field name made lowercase.
    ed = models.CharField(db_column='ED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=20,blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False 
        db_table = 'Fact_Members'

class Members(models.Model):
    accountid = models.BigAutoField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
    member_id = models.CharField(max_length=12, blank=True, null=True)
    firstname = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=6, blank=True, null=True)
    home_phone = models.CharField(db_column='Home_phone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    office_phone = models.CharField(max_length=16, blank=True, null=True)
    mobile_phone = models.CharField(max_length=16, blank=True, null=True)
    fax = models.CharField(max_length=16, blank=True, null=True)
    messenger_type = models.CharField(max_length=100, blank=True, null=True)
    messenger_name = models.CharField(max_length=200, blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)
    last_login = models.BigIntegerField(blank=True, null=True)
    value = models.DecimalField(db_column='Value', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    webaccess = models.CharField(db_column='WebAccess', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    membership_status = models.CharField(max_length=12, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    suburb = models.CharField(max_length=35, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=16, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    recordtype = models.CharField(db_column='RecordType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='TIMEZONE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isfirsttimelogin = models.CharField(db_column='IsFirstTimeLogin', max_length=1, blank=True, null=True)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rewardsflag = models.CharField(max_length=1, blank=True, null=True)
    groupcode = models.CharField(max_length=12, blank=True, null=True)
    categorycode = models.CharField(max_length=12, blank=True, null=True)
    lastreportdate = models.DateTimeField(db_column='LastReportDate', blank=True, null=True)  # Field name made lowercase.
    lastnewsletterdate = models.DateTimeField(db_column='LastNewsLetterDate', blank=True, null=True)  # Field name made lowercase.
    tiergamingcategory = models.CharField(db_column='TierGamingCategory', max_length=24, blank=True, null=True)  # Field name made lowercase.
    cscategoryid = models.IntegerField(db_column='CSCategoryID', blank=True, null=True)  # Field name made lowercase.
    dateregistered = models.DateTimeField(db_column='DateRegistered', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    udf1 = models.CharField(db_column='UDF1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf2 = models.CharField(db_column='UDF2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf3 = models.CharField(db_column='UDF3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf4 = models.CharField(db_column='UDF4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf5 = models.CharField(db_column='UDF5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf6 = models.CharField(db_column='UDF6', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf7 = models.CharField(db_column='UDF7', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf8 = models.CharField(db_column='UDF8', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf9 = models.CharField(db_column='UDF9', max_length=45, blank=True, null=True)  # Field name made lowercase.
    udf10 = models.CharField(db_column='UDF10', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tempmemberflag = models.CharField(db_column='TempMemberFlag', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unclaimedticketcounter = models.IntegerField(db_column='UnclaimedTicketCounter', blank=True, null=True)  # Field name made lowercase.
    facebook_uid = models.CharField(max_length=200, blank=True, null=True)
    lastupdatedtime = models.DateTimeField(db_column='LastUpdatedTime', blank=True, null=True)  # Field name made lowercase.
    updateflag = models.CharField(db_column='UPDATEFLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mmid = models.BigIntegerField(db_column='MMID', blank=True, null=True)  # Field name made lowercase.
    gpoptindate = models.DateTimeField(db_column='GPOptInDate', blank=True, null=True)  # Field name made lowercase.
    gpoptin = models.CharField(db_column='GPOptIn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    membershipcategories = models.CharField(db_column='MembershipCategories', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    photostatus = models.CharField(db_column='PhotoStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    appregistrationrequestdate = models.DateTimeField(db_column='appRegistrationRequestDate', blank=True, null=True)  # Field name made lowercase.
    language_preference = models.CharField(db_column='Language_Preference', max_length=32, blank=True, null=True)  # Field name made lowercase.
    optinoutid = models.IntegerField(db_column='OptInOutID', blank=True, null=True)  # Field name made lowercase.
    optinoutstatus = models.CharField(db_column='OptInOutStatus', max_length=3, blank=True, null=True)  # Field name made lowercase.
    optinoutdatetime = models.DateTimeField(db_column='OptInOutDateTime', blank=True, null=True)  # Field name made lowercase.
    documentnumber = models.CharField(db_column='DocumentNumber', max_length=24, blank=True, null=True)  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=24, blank=True, null=True)  # Field name made lowercase.
    documentissuedate = models.DateTimeField(db_column='DocumentIssueDate', blank=True, null=True)  # Field name made lowercase.
    documentexpirydate = models.DateTimeField(db_column='DocumentExpiryDate', blank=True, null=True)  # Field name made lowercase.
    qrcodepath = models.CharField(db_column='QRCodePath', max_length=256, blank=True, null=True)  # Field name made lowercase.
    updateprofilerequestdatetime = models.DateTimeField(db_column='updateProfileRequestDateTime', blank=True, null=True)  # Field name made lowercase.
    prefcontactmethod = models.CharField(db_column='PrefContactMethod', max_length=32, blank=True, null=True)  # Field name made lowercase.
    socialclub = models.CharField(db_column='SocialClub', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referredby = models.CharField(db_column='ReferredBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=64, blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=64, blank=True, null=True)  # Field name made lowercase.
    agegroup = models.CharField(db_column='AgeGroup', max_length=6, blank=True, null=True)  # Field name made lowercase.
    emailoptinoutstatus = models.CharField(db_column='EmailOptInOutStatus', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sendgridunsubscribeflag = models.CharField(db_column='sendGridUnsubscribeFlag', max_length=1, blank=True, null=True)  # Field name made lowercase.
    duetorenew = models.IntegerField(blank=True, null=True)
    ratecategoryid = models.IntegerField(db_column='RateCategoryID', blank=True, null=True)  # Field name made lowercase.
    tpticketslut = models.DateTimeField(db_column='TPTicketsLUT', blank=True, null=True)  # Field name made lowercase.
    idprooffrontpath = models.CharField(db_column='IDProofFrontPath', max_length=256, blank=True, null=True)  # Field name made lowercase.
    idproofbackpath = models.CharField(db_column='IDProofBackPath', max_length=256, blank=True, null=True)  # Field name made lowercase.
    membersignaturepath = models.CharField(db_column='MemberSignaturePath', max_length=256, blank=True, null=True)  # Field name made lowercase.
    staffsignaturepath = models.CharField(db_column='StaffSignaturePath', max_length=256, blank=True, null=True)  # Field name made lowercase.
    photopath = models.CharField(db_column='PhotoPath', max_length=256, blank=True, null=True)  # Field name made lowercase.
    documentstate = models.CharField(db_column='DocumentState', max_length=32, blank=True, null=True)  # Field name made lowercase.
    documentcountry = models.CharField(db_column='DocumentCountry', max_length=32, blank=True, null=True)  # Field name made lowercase.
    otherpreferences = models.CharField(db_column='OtherPreferences', max_length=32, blank=True, null=True)  # Field name made lowercase.
    addresstype = models.CharField(db_column='AddressType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    suspensionflag = models.CharField(db_column='SuspensionFlag', max_length=1, blank=True, null=True)  # Field name made lowercase.
    accountuid = models.CharField(db_column='AccountUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ismerge = models.CharField(db_column='IsMerge', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dsupdateddatetime = models.DateTimeField(db_column='DSUpdatedDateTime', blank=True, null=True)  # Field name made lowercase.
    rxaccountid = models.BigIntegerField(db_column='RXAccountID', blank=True, null=True)  # Field name made lowercase.
    preferredclub = models.CharField(db_column='PreferredClub', max_length=48, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Members'


class Australianpostcodes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    geopoint = models.CharField(db_column='GeoPoint', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=24, blank=True, null=True)  # Field name made lowercase.
    coordinates = models.TextField(db_column='Coordinates', blank=True, null=True)  # Field name made lowercase.
    postcode = models.IntegerField(db_column='Postcode', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=12, blank=True, null=True)  # Field name made lowercase.
    colour = models.CharField(db_column='Colour', max_length=12, blank=True, null=True)  # Field name made lowercase.
    opacity = models.DecimalField(db_column='Opacity', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Australianpostcodes'