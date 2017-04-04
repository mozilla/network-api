from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class S3MediaStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        super(S3MediaStorage, self).__init__(*args, **kwargs)

    def isfile(self, name):
        return self.exists(name)

    def isdir(self, name):
        if not name:
            return True

        if self.isfile(name):
            return False

        dirlist = self.bucket.objects.filter(Prefix=self._encode_name(name))

        for item in dirlist:
            return True

        return False

    def move(self, old_file_name, new_file_name, allow_overwrite=False):

        if self.exists(new_file_name):
            if allow_overwrite:
                self.delete(new_file_name)
            else:
                raise "The destination file '%s' exists and allow_overwrite is False" % new_file_name

        old_key_name = self._encode_name(self._normalize_name(self._clean_name(old_file_name)))
        new_key_name = self._encode_name(self._normalize_name(self._clean_name(new_file_name)))

        k = self.bucket.copy_key(new_key_name, self.bucket.name, old_key_name)

        if not k:
            raise "Couldn't copy '%s' to '%s'" % (old_file_name, new_file_name)

        self.delete(old_file_name)

    def makedirs(self, name):
        pass

    def rmtree(self, name):
        name = self._normalize_name(self._clean_name(name))
        dirlist = self.bucket.list(self._encode_name(name))
        for item in dirlist:
            item.delete()