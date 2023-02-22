# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjangoSummernoteAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=100)
    uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_summernote_attachment'


class ProductsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_category'


class ProductsProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    quantity_in_stock = models.IntegerField()
    in_stock = models.BooleanField()
    animal_choice = models.CharField(max_length=20)
    category = models.ForeignKey(ProductsCategory, models.DO_NOTHING, blank=True, null=True)
    has_color = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_product'


class ProfilesUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    default_phone_number = models.CharField(max_length=20, blank=True, null=True)
    default_country = models.CharField(max_length=2, blank=True, null=True)
    default_postcode = models.CharField(max_length=20, blank=True, null=True)
    default_town_or_city = models.CharField(max_length=40, blank=True, null=True)
    default_street_address1 = models.CharField(max_length=80, blank=True, null=True)
    default_street_address2 = models.CharField(max_length=80, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    default_email = models.CharField(max_length=254)
    full_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'profiles_userprofile'


class ProfilesUserwishlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    user = models.ForeignKey(ProfilesUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profiles_userwishlist'


class ReviewsComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField()
    approved = models.BooleanField()
    post = models.ForeignKey('ReviewsPost', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_comment'


class ReviewsPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=200)
    slug = models.CharField(unique=True, max_length=200)
    excerpt = models.TextField()
    updated_on = models.DateTimeField()
    content = models.TextField()
    created_on = models.DateTimeField()
    status = models.IntegerField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_post'


class ReviewsPostLikes(models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(ReviewsPost, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_post_likes'
        unique_together = (('post', 'user'),)


class ReviewsReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField()
    approved = models.BooleanField()
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    posted_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    dislike_count = models.IntegerField()
    like_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reviews_review'


class ReviewsReviewDislikes(models.Model):
    id = models.BigAutoField(primary_key=True)
    review = models.ForeignKey(ReviewsReview, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_review_dislikes'
        unique_together = (('review', 'user'),)


class ReviewsReviewLikes(models.Model):
    id = models.BigAutoField(primary_key=True)
    review = models.ForeignKey(ReviewsReview, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_review_likes'
        unique_together = (('review', 'user'),)


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
