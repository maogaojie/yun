# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class OcAccounts(models.Model):
#     uid = models.CharField(primary_key=True, max_length=64)
#     data = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'oc_accounts'

# class OcUsers(models.Model):
#     uid = models.CharField(primary_key=True, max_length=64)
#     displayname = models.CharField(max_length=64, blank=True, null=True)
#     password = models.CharField(max_length=255)
#     uid_lower = models.CharField(max_length=64, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oc_users'


# class OcActivity(models.Model):
#     activity_id = models.BigAutoField(primary_key=True)
#     timestamp = models.IntegerField()
#     priority = models.IntegerField()
#     type = models.CharField(max_length=255, blank=True, null=True)
#     user = models.CharField(max_length=64, blank=True, null=True)
#     affecteduser = models.CharField(max_length=64)
#     app = models.CharField(max_length=32)
#     subject = models.CharField(max_length=255)
#     subjectparams = models.TextField()
#     message = models.CharField(max_length=255, blank=True, null=True)
#     messageparams = models.TextField(blank=True, null=True)
#     file = models.CharField(max_length=4000, blank=True, null=True)
#     link = models.CharField(max_length=4000, blank=True, null=True)
#     object_type = models.CharField(max_length=255, blank=True, null=True)
#     object_id = models.BigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'oc_activity'

# class OcStorages(models.Model):
#     numeric_id = models.BigAutoField(primary_key=True)
#     id = models.CharField(unique=True, max_length=64, blank=True, null=True)
#     available = models.IntegerField()
#     last_checked = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oc_storages'

# class OcMounts(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     storage_id = models.IntegerField()
#     root_id = models.IntegerField()
#     user_id = models.CharField(max_length=64)
#     mount_point = models.CharField(max_length=4000)
#     mount_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'oc_mounts'
#         unique_together = (('user_id', 'root_id'),)

class OcActivityMq(models.Model):
    mail_id = models.BigAutoField(primary_key=True)
    amq_timestamp = models.IntegerField()
    amq_latest_send = models.IntegerField()
    amq_type = models.CharField(max_length=255)
    amq_affecteduser = models.CharField(max_length=64)
    amq_appid = models.CharField(max_length=255)
    amq_subject = models.CharField(max_length=255)
    amq_subjectparams = models.CharField(max_length=4000)
    object_type = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_activity_mq'


class OcAddressbookchanges(models.Model):
    id = models.BigAutoField(primary_key=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    synctoken = models.PositiveIntegerField()
    addressbookid = models.BigIntegerField()
    operation = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_addressbookchanges'


class OcAddressbooks(models.Model):
    id = models.BigAutoField(primary_key=True)
    principaluri = models.CharField(max_length=255, blank=True, null=True)
    displayname = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    synctoken = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_addressbooks'
        unique_together = (('principaluri', 'uri'),)


class OcAppconfig(models.Model):
    appid = models.CharField(primary_key=True, max_length=32)
    configkey = models.CharField(max_length=64)
    configvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_appconfig'
        unique_together = (('appid', 'configkey'),)


class OcAuthtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=64)
    login_name = models.CharField(max_length=64)
    password = models.TextField(blank=True, null=True)
    name = models.TextField()
    token = models.CharField(unique=True, max_length=200)
    type = models.PositiveSmallIntegerField()
    remember = models.PositiveSmallIntegerField()
    last_activity = models.PositiveIntegerField()
    last_check = models.PositiveIntegerField()
    scope = models.TextField(blank=True, null=True)
    expires = models.PositiveIntegerField(blank=True, null=True)
    private_key = models.TextField(blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    version = models.PositiveSmallIntegerField()
    password_invalid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_authtoken'


class OcBruteforceAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=64)
    occurred = models.PositiveIntegerField()
    ip = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)
    metadata = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_bruteforce_attempts'


class OcCalendarInvitations(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=255)
    recurrenceid = models.CharField(max_length=255, blank=True, null=True)
    attendee = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    sequence = models.BigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=60)
    expiration = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_calendar_invitations'


class OcCalendarResources(models.Model):
    id = models.BigAutoField(primary_key=True)
    backend_id = models.CharField(max_length=64, blank=True, null=True)
    resource_id = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    displayname = models.CharField(max_length=255, blank=True, null=True)
    group_restrictions = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_calendar_resources'


class OcCalendarRooms(models.Model):
    id = models.BigAutoField(primary_key=True)
    backend_id = models.CharField(max_length=64, blank=True, null=True)
    resource_id = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    displayname = models.CharField(max_length=255, blank=True, null=True)
    group_restrictions = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_calendar_rooms'


class OcCalendarchanges(models.Model):
    id = models.BigAutoField(primary_key=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    synctoken = models.PositiveIntegerField()
    calendarid = models.BigIntegerField()
    operation = models.SmallIntegerField()
    calendartype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_calendarchanges'


class OcCalendarobjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    calendardata = models.TextField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    calendarid = models.BigIntegerField()
    lastmodified = models.PositiveIntegerField(blank=True, null=True)
    etag = models.CharField(max_length=32, blank=True, null=True)
    size = models.BigIntegerField()
    componenttype = models.CharField(max_length=8, blank=True, null=True)
    firstoccurence = models.BigIntegerField(blank=True, null=True)
    lastoccurence = models.BigIntegerField(blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    calendartype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_calendarobjects'
        unique_together = (('calendarid', 'calendartype', 'uri'),)


class OcCalendarobjectsProps(models.Model):
    id = models.BigAutoField(primary_key=True)
    calendarid = models.BigIntegerField()
    objectid = models.BigIntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    parameter = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    calendartype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_calendarobjects_props'


class OcCalendars(models.Model):
    id = models.BigAutoField(primary_key=True)
    principaluri = models.CharField(max_length=255, blank=True, null=True)
    displayname = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    synctoken = models.PositiveIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    calendarorder = models.PositiveIntegerField()
    calendarcolor = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.TextField(blank=True, null=True)
    components = models.CharField(max_length=64, blank=True, null=True)
    transparent = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_calendars'
        unique_together = (('principaluri', 'uri'),)


class OcCalendarsubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    principaluri = models.CharField(max_length=255, blank=True, null=True)
    displayname = models.CharField(max_length=100, blank=True, null=True)
    refreshrate = models.CharField(max_length=10, blank=True, null=True)
    calendarorder = models.PositiveIntegerField()
    calendarcolor = models.CharField(max_length=255, blank=True, null=True)
    striptodos = models.SmallIntegerField(blank=True, null=True)
    stripalarms = models.SmallIntegerField(blank=True, null=True)
    stripattachments = models.SmallIntegerField(blank=True, null=True)
    lastmodified = models.PositiveIntegerField(blank=True, null=True)
    synctoken = models.PositiveIntegerField()
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_calendarsubscriptions'
        unique_together = (('principaluri', 'uri'),)


class OcCards(models.Model):
    id = models.BigAutoField(primary_key=True)
    addressbookid = models.BigIntegerField()
    carddata = models.TextField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    lastmodified = models.BigIntegerField(blank=True, null=True)
    etag = models.CharField(max_length=32, blank=True, null=True)
    size = models.BigIntegerField()
    uid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_cards'


class OcCardsProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    addressbookid = models.BigIntegerField()
    cardid = models.BigIntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    preferred = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_cards_properties'


class OcCollresAccesscache(models.Model):
    user_id = models.CharField(max_length=64)
    collection_id = models.BigIntegerField(blank=True, null=True)
    resource_type = models.CharField(max_length=64, blank=True, null=True)
    resource_id = models.CharField(max_length=64, blank=True, null=True)
    access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_collres_accesscache'
        unique_together = (('user_id', 'collection_id', 'resource_type', 'resource_id'),)


class OcCollresCollections(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_collres_collections'


class OcCollresResources(models.Model):
    collection_id = models.BigIntegerField()
    resource_type = models.CharField(max_length=64)
    resource_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_collres_resources'
        unique_together = (('collection_id', 'resource_type', 'resource_id'),)


class OcComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.BigIntegerField()
    topmost_parent_id = models.BigIntegerField()
    children_count = models.PositiveIntegerField()
    actor_type = models.CharField(max_length=64)
    actor_id = models.CharField(max_length=64)
    message = models.TextField(blank=True, null=True)
    verb = models.CharField(max_length=64, blank=True, null=True)
    creation_timestamp = models.DateTimeField(blank=True, null=True)
    latest_child_timestamp = models.DateTimeField(blank=True, null=True)
    object_type = models.CharField(max_length=64)
    object_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_comments'


class OcCommentsReadMarkers(models.Model):
    user_id = models.CharField(max_length=64)
    marker_datetime = models.DateTimeField(blank=True, null=True)
    object_type = models.CharField(max_length=64)
    object_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_comments_read_markers'
        unique_together = (('user_id', 'object_type', 'object_id'),)


class OcCredentials(models.Model):
    user = models.CharField(primary_key=True, max_length=64)
    identifier = models.CharField(max_length=64)
    credentials = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_credentials'
        unique_together = (('user', 'identifier'),)


class OcDavShares(models.Model):
    id = models.BigAutoField(primary_key=True)
    principaluri = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    access = models.SmallIntegerField(blank=True, null=True)
    resourceid = models.BigIntegerField()
    publicuri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_dav_shares'
        unique_together = (('principaluri', 'resourceid', 'type', 'publicuri'),)


class OcDirectlink(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    file_id = models.BigIntegerField()
    token = models.CharField(max_length=60, blank=True, null=True)
    expiration = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_directlink'


class OcFederatedReshares(models.Model):
    share_id = models.IntegerField(unique=True)
    remote_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_federated_reshares'


class OcFileLocks(models.Model):
    id = models.BigAutoField(primary_key=True)
    lock = models.IntegerField()
    key = models.CharField(unique=True, max_length=64)
    ttl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_file_locks'


class OcFilecache(models.Model):
    fileid = models.BigAutoField(primary_key=True)
    storage = models.BigIntegerField()
    path = models.CharField(max_length=4000, blank=True, null=True)
    path_hash = models.CharField(max_length=32)
    parent = models.BigIntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)
    mimetype = models.BigIntegerField()
    mimepart = models.BigIntegerField()
    size = models.BigIntegerField()
    mtime = models.BigIntegerField()
    storage_mtime = models.BigIntegerField()
    encrypted = models.IntegerField()
    unencrypted_size = models.BigIntegerField()
    etag = models.CharField(max_length=40, blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_filecache'
        unique_together = (('storage', 'path_hash'),)


class OcFilesTrash(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=250)
    user = models.CharField(max_length=64)
    timestamp = models.CharField(max_length=12)
    location = models.CharField(max_length=512)
    type = models.CharField(max_length=4, blank=True, null=True)
    mime = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_files_trash'


class OcFlowChecks(models.Model):
    class_field = models.CharField(db_column='class', max_length=256)  # Field renamed because it was a Python reserved word.
    operator = models.CharField(max_length=16)
    value = models.TextField(blank=True, null=True)
    hash = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_flow_checks'


class OcFlowOperations(models.Model):
    class_field = models.CharField(db_column='class', max_length=256)  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=256)
    checks = models.TextField(blank=True, null=True)
    operation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_flow_operations'


class OcGroupAdmin(models.Model):
    gid = models.CharField(primary_key=True, max_length=64)
    uid = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_group_admin'
        unique_together = (('gid', 'uid'),)


class OcGroupUser(models.Model):
    gid = models.CharField(primary_key=True, max_length=64)
    uid = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_group_user'
        unique_together = (('gid', 'uid'),)


class OcGroups(models.Model):
    gid = models.CharField(primary_key=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_groups'


class OcJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    argument = models.CharField(max_length=4000)
    last_run = models.IntegerField(blank=True, null=True)
    last_checked = models.IntegerField(blank=True, null=True)
    reserved_at = models.IntegerField(blank=True, null=True)
    execution_duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_jobs'


class OcLoginFlowV2(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.BigIntegerField()
    started = models.PositiveSmallIntegerField()
    poll_token = models.CharField(unique=True, max_length=255)
    login_token = models.CharField(unique=True, max_length=255)
    public_key = models.TextField()
    private_key = models.TextField()
    client_name = models.CharField(max_length=255)
    login_name = models.CharField(max_length=255, blank=True, null=True)
    server = models.CharField(max_length=255, blank=True, null=True)
    app_password = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_login_flow_v2'


class OcMigrations(models.Model):
    app = models.CharField(primary_key=True, max_length=255)
    version = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_migrations'
        unique_together = (('app', 'version'),)


class OcMimetypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    mimetype = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_mimetypes'

class OcNotifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=32)
    user = models.CharField(max_length=64)
    timestamp = models.IntegerField()
    object_type = models.CharField(max_length=64)
    object_id = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    subject_parameters = models.TextField(blank=True, null=True)
    message = models.CharField(max_length=64, blank=True, null=True)
    message_parameters = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=4000, blank=True, null=True)
    icon = models.CharField(max_length=4000, blank=True, null=True)
    actions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_notifications'


class OcNotificationsPushtokens(models.Model):
    uid = models.CharField(max_length=64)
    token = models.IntegerField()
    deviceidentifier = models.CharField(max_length=128)
    devicepublickey = models.CharField(max_length=512)
    devicepublickeyhash = models.CharField(max_length=128)
    pushtokenhash = models.CharField(max_length=128)
    proxyserver = models.CharField(max_length=256)
    apptype = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_notifications_pushtokens'
        unique_together = (('uid', 'token'),)


class OcOauth2AccessTokens(models.Model):
    token_id = models.IntegerField()
    client_id = models.IntegerField()
    hashed_code = models.CharField(unique=True, max_length=128)
    encrypted_token = models.CharField(max_length=786)

    class Meta:
        managed = False
        db_table = 'oc_oauth2_access_tokens'


class OcOauth2Clients(models.Model):
    name = models.CharField(max_length=64)
    redirect_uri = models.CharField(max_length=2000)
    client_identifier = models.CharField(unique=True, max_length=64)
    secret = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_oauth2_clients'


class OcPreferences(models.Model):
    userid = models.CharField(primary_key=True, max_length=64)
    appid = models.CharField(max_length=32)
    configkey = models.CharField(max_length=64)
    configvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_preferences'
        unique_together = (('userid', 'appid', 'configkey'),)


class OcPrivacyAdmins(models.Model):
    displayname = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_privacy_admins'


class OcProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(max_length=64)
    propertypath = models.CharField(max_length=255)
    propertyname = models.CharField(max_length=255)
    propertyvalue = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_properties'


class OcSchedulingobjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    principaluri = models.CharField(max_length=255, blank=True, null=True)
    calendardata = models.TextField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    lastmodified = models.PositiveIntegerField(blank=True, null=True)
    etag = models.CharField(max_length=32, blank=True, null=True)
    size = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_schedulingobjects'


class OcShare(models.Model):
    id = models.BigAutoField(primary_key=True)
    share_type = models.SmallIntegerField()
    share_with = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    uid_owner = models.CharField(max_length=64)
    uid_initiator = models.CharField(max_length=64, blank=True, null=True)
    parent = models.BigIntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=64)
    item_source = models.CharField(max_length=255, blank=True, null=True)
    item_target = models.CharField(max_length=255, blank=True, null=True)
    file_source = models.BigIntegerField(blank=True, null=True)
    file_target = models.CharField(max_length=512, blank=True, null=True)
    permissions = models.SmallIntegerField()
    stime = models.BigIntegerField()
    accepted = models.SmallIntegerField()
    expiration = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)
    mail_send = models.SmallIntegerField()
    share_name = models.CharField(max_length=64, blank=True, null=True)
    password_by_talk = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    hide_download = models.SmallIntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_share'


class OcShareExternal(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    share_type = models.IntegerField(blank=True, null=True)
    remote = models.CharField(max_length=512)
    remote_id = models.IntegerField()
    share_token = models.CharField(max_length=64)
    password = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64)
    owner = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    mountpoint = models.CharField(max_length=4000)
    mountpoint_hash = models.CharField(max_length=32)
    accepted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_share_external'
        unique_together = (('user', 'mountpoint_hash'),)

class OcSystemtag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    visibility = models.SmallIntegerField()
    editable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_systemtag'
        unique_together = (('name', 'visibility', 'editable'),)


class OcSystemtagGroup(models.Model):
    systemtagid = models.BigIntegerField()
    gid = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_systemtag_group'
        unique_together = (('gid', 'systemtagid'),)


class OcSystemtagObjectMapping(models.Model):
    objectid = models.CharField(max_length=64)
    objecttype = models.CharField(max_length=64)
    systemtagid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_systemtag_object_mapping'
        unique_together = (('objecttype', 'objectid', 'systemtagid'),)


class OcTrustedServers(models.Model):
    url = models.CharField(max_length=512)
    url_hash = models.CharField(unique=True, max_length=255)
    token = models.CharField(max_length=128, blank=True, null=True)
    shared_secret = models.CharField(max_length=256, blank=True, null=True)
    status = models.IntegerField()
    sync_token = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_trusted_servers'


class OcTwofactorBackupcodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=64)
    code = models.CharField(max_length=128)
    used = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_twofactor_backupcodes'


class OcTwofactorProviders(models.Model):
    provider_id = models.CharField(primary_key=True, max_length=32)
    uid = models.CharField(max_length=64)
    enabled = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'oc_twofactor_providers'
        unique_together = (('provider_id', 'uid'),)





class OcVcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    category = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_vcategory'


class OcVcategoryToObject(models.Model):
    objid = models.BigIntegerField()
    categoryid = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_vcategory_to_object'
        unique_together = (('categoryid', 'objid', 'type'),)


class OcWhatsNew(models.Model):
    version = models.CharField(unique=True, max_length=64)
    etag = models.CharField(max_length=64)
    last_check = models.PositiveIntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_whats_new'
