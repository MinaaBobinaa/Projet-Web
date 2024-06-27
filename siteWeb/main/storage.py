from django.core.files.storage import FileSystemStorage
import os

class UniqueFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        if self.exists(name):
            base, extension = os.path.splitext(name)
            counter = 1
            while self.exists(name):
                name = f"{base}_{counter}{extension}"
                counter += 1
        return name
