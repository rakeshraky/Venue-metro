# Generated by Django 2.1.15 on 2020-08-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patron', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('accountid', models.BigAutoField(db_column='AccountID', primary_key=True, serialize=False)),
                ('member_id', models.CharField(blank=True, max_length=12, null=True)),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=6, null=True)),
                ('home_phone', models.CharField(blank=True, db_column='Home_phone', max_length=16, null=True)),
                ('office_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=16, null=True)),
                ('fax', models.CharField(blank=True, max_length=16, null=True)),
                ('messenger_type', models.CharField(blank=True, max_length=100, null=True)),
                ('messenger_name', models.CharField(blank=True, max_length=200, null=True)),
                ('welcome_message', models.TextField(blank=True, null=True)),
                ('last_login', models.BigIntegerField(blank=True, null=True)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=13, null=True)),
                ('webaccess', models.CharField(blank=True, db_column='WebAccess', max_length=1, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=1, null=True)),
                ('membership_status', models.CharField(blank=True, max_length=12, null=True)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('address3', models.CharField(blank=True, max_length=100, null=True)),
                ('suburb', models.CharField(blank=True, max_length=35, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=16, null=True)),
                ('dob', models.DateTimeField(blank=True, db_column='DOB', null=True)),
                ('recordtype', models.CharField(blank=True, db_column='RecordType', max_length=10, null=True)),
                ('timezone', models.CharField(blank=True, db_column='TIMEZONE', max_length=10, null=True)),
                ('isfirsttimelogin', models.CharField(blank=True, db_column='IsFirstTimeLogin', max_length=1, null=True)),
                ('accounttype', models.CharField(blank=True, db_column='AccountType', max_length=20, null=True)),
                ('rewardsflag', models.CharField(blank=True, max_length=1, null=True)),
                ('groupcode', models.CharField(blank=True, max_length=12, null=True)),
                ('categorycode', models.CharField(blank=True, max_length=12, null=True)),
                ('lastreportdate', models.DateTimeField(blank=True, db_column='LastReportDate', null=True)),
                ('lastnewsletterdate', models.DateTimeField(blank=True, db_column='LastNewsLetterDate', null=True)),
                ('tiergamingcategory', models.CharField(blank=True, db_column='TierGamingCategory', max_length=24, null=True)),
                ('cscategoryid', models.IntegerField(blank=True, db_column='CSCategoryID', null=True)),
                ('dateregistered', models.DateTimeField(blank=True, db_column='DateRegistered', null=True)),
                ('expirydate', models.DateTimeField(blank=True, db_column='ExpiryDate', null=True)),
                ('udf1', models.CharField(blank=True, db_column='UDF1', max_length=45, null=True)),
                ('udf2', models.CharField(blank=True, db_column='UDF2', max_length=45, null=True)),
                ('udf3', models.CharField(blank=True, db_column='UDF3', max_length=45, null=True)),
                ('udf4', models.CharField(blank=True, db_column='UDF4', max_length=45, null=True)),
                ('udf5', models.CharField(blank=True, db_column='UDF5', max_length=45, null=True)),
                ('udf6', models.CharField(blank=True, db_column='UDF6', max_length=45, null=True)),
                ('udf7', models.CharField(blank=True, db_column='UDF7', max_length=45, null=True)),
                ('udf8', models.CharField(blank=True, db_column='UDF8', max_length=45, null=True)),
                ('udf9', models.CharField(blank=True, db_column='UDF9', max_length=45, null=True)),
                ('udf10', models.CharField(blank=True, db_column='UDF10', max_length=45, null=True)),
                ('tempmemberflag', models.CharField(blank=True, db_column='TempMemberFlag', max_length=1, null=True)),
                ('unclaimedticketcounter', models.IntegerField(blank=True, db_column='UnclaimedTicketCounter', null=True)),
                ('facebook_uid', models.CharField(blank=True, max_length=200, null=True)),
                ('lastupdatedtime', models.DateTimeField(blank=True, db_column='LastUpdatedTime', null=True)),
                ('updateflag', models.CharField(blank=True, db_column='UPDATEFLAG', max_length=1, null=True)),
                ('mmid', models.BigIntegerField(blank=True, db_column='MMID', null=True)),
                ('gpoptindate', models.DateTimeField(blank=True, db_column='GPOptInDate', null=True)),
                ('gpoptin', models.CharField(blank=True, db_column='GPOptIn', max_length=1, null=True)),
                ('membershipcategories', models.CharField(blank=True, db_column='MembershipCategories', max_length=1024, null=True)),
                ('photostatus', models.CharField(blank=True, db_column='PhotoStatus', max_length=1, null=True)),
                ('appregistrationrequestdate', models.DateTimeField(blank=True, db_column='appRegistrationRequestDate', null=True)),
                ('language_preference', models.CharField(blank=True, db_column='Language_Preference', max_length=32, null=True)),
                ('optinoutid', models.IntegerField(blank=True, db_column='OptInOutID', null=True)),
                ('optinoutstatus', models.CharField(blank=True, db_column='OptInOutStatus', max_length=3, null=True)),
                ('optinoutdatetime', models.DateTimeField(blank=True, db_column='OptInOutDateTime', null=True)),
                ('documentnumber', models.CharField(blank=True, db_column='DocumentNumber', max_length=24, null=True)),
                ('documenttype', models.CharField(blank=True, db_column='DocumentType', max_length=24, null=True)),
                ('documentissuedate', models.DateTimeField(blank=True, db_column='DocumentIssueDate', null=True)),
                ('documentexpirydate', models.DateTimeField(blank=True, db_column='DocumentExpiryDate', null=True)),
                ('qrcodepath', models.CharField(blank=True, db_column='QRCodePath', max_length=256, null=True)),
                ('updateprofilerequestdatetime', models.DateTimeField(blank=True, db_column='updateProfileRequestDateTime', null=True)),
                ('prefcontactmethod', models.CharField(blank=True, db_column='PrefContactMethod', max_length=32, null=True)),
                ('socialclub', models.CharField(blank=True, db_column='SocialClub', max_length=64, null=True)),
                ('referredby', models.CharField(blank=True, db_column='ReferredBy', max_length=128, null=True)),
                ('language', models.CharField(blank=True, db_column='Language', max_length=64, null=True)),
                ('occupation', models.CharField(blank=True, db_column='Occupation', max_length=64, null=True)),
                ('agegroup', models.CharField(blank=True, db_column='AgeGroup', max_length=6, null=True)),
                ('emailoptinoutstatus', models.CharField(blank=True, db_column='EmailOptInOutStatus', max_length=3, null=True)),
                ('sendgridunsubscribeflag', models.CharField(blank=True, db_column='sendGridUnsubscribeFlag', max_length=1, null=True)),
                ('duetorenew', models.IntegerField(blank=True, null=True)),
                ('ratecategoryid', models.IntegerField(blank=True, db_column='RateCategoryID', null=True)),
                ('tpticketslut', models.DateTimeField(blank=True, db_column='TPTicketsLUT', null=True)),
                ('idprooffrontpath', models.CharField(blank=True, db_column='IDProofFrontPath', max_length=256, null=True)),
                ('idproofbackpath', models.CharField(blank=True, db_column='IDProofBackPath', max_length=256, null=True)),
                ('membersignaturepath', models.CharField(blank=True, db_column='MemberSignaturePath', max_length=256, null=True)),
                ('staffsignaturepath', models.CharField(blank=True, db_column='StaffSignaturePath', max_length=256, null=True)),
                ('photopath', models.CharField(blank=True, db_column='PhotoPath', max_length=256, null=True)),
                ('documentstate', models.CharField(blank=True, db_column='DocumentState', max_length=32, null=True)),
                ('documentcountry', models.CharField(blank=True, db_column='DocumentCountry', max_length=32, null=True)),
                ('otherpreferences', models.CharField(blank=True, db_column='OtherPreferences', max_length=32, null=True)),
                ('addresstype', models.CharField(blank=True, db_column='AddressType', max_length=32, null=True)),
                ('suspensionflag', models.CharField(blank=True, db_column='SuspensionFlag', max_length=1, null=True)),
                ('accountuid', models.CharField(blank=True, db_column='AccountUID', max_length=36, null=True)),
                ('ismerge', models.CharField(blank=True, db_column='IsMerge', max_length=1, null=True)),
                ('dsupdateddatetime', models.DateTimeField(blank=True, db_column='DSUpdatedDateTime', null=True)),
                ('rxaccountid', models.BigIntegerField(blank=True, db_column='RXAccountID', null=True)),
                ('preferredclub', models.CharField(blank=True, db_column='PreferredClub', max_length=48, null=True)),
                ('latitude', models.FloatField(blank=True, db_column='Latitude', null=True)),
                ('longitude', models.FloatField(blank=True, db_column='Longitude', null=True)),
            ],
            options={
                'db_table': 'Members',
                'managed': False,
            },
        ),
    ]