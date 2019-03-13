import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Entry


class EntryModelTests(TestCase):
    def test_was_published_recently_with_old_entry(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_entry = Entry(date_published=time)
        self.assertIs(old_entry.was_published_recently(), False)

        def test_was_published_recently_with_recent_entry(self):
            time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
            recent_entry = Entry(date_published=time)
            self.assertIs(recent_entry.was_published_recently(), True)

            def test_was_published_recently_with_future_entry(self):
                time = timezone.now() + datetime.timedelta(days=30)
                future_entry = Entry(date_published=time)
                self.assertIs(future_entry.was_published_recently(), False)
