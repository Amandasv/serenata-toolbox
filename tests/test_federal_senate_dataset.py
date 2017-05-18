from tempfile import gettempdir
from unittest import TestCase
from unittest.mock import patch


from serenata_toolbox.federal_senate.federal_senate_dataset import FederalSenateDataset


class TestFederalSenateDataset(TestCase):
    @patch("serenata_toolbox.federal_senate.federal_senate_dataset.urlretrieve")
    def test_fetch_files_from_S3(self, mockedUrlRetrieve):
        self.path = gettempdir()
        self.subject = FederalSenateDataset(self.path)

        self.subject.fetch()
        self.assertTrue(mockedUrlRetrieve.called)

    def test_translate(self):
        self.subject = FederalSenateDataset('tests/fixtures/csv/')

        self.subject.translate()

        self.assertTrue(True) # What should be asserted here?
