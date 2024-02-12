import datetime

from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    publish_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()
    video_id = models.CharField(max_length=150, unique=True)
    channel_id = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ', '.join(['title=' + self.title, 'description=' + self.description])


class APIAuthKey(models.Model):
    auth_key = models.CharField(max_length=250, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    exhausted = models.BooleanField(default=False)

    @classmethod
    def get_auth_key(cls):
        """
            This function returns the non-exhausted auth api key.
            The newest auth key is returned.
        """
        api_key = cls.objects.filter(exhausted=False).order_by('-created').values()
        if len(api_key):
            return api_key[0]['auth_key']
        return None

    @classmethod
    def mark_auth_key_exhausted(cls, auth_key):
        """
            This function marks the api auth key as exhausted
        """
        auth_key_object = cls.objects.get(auth_key=auth_key)
        auth_key_object.exhausted = True
        auth_key_object.updated = datetime.datetime.now()
        auth_key_object.save()
        return auth_key_object
