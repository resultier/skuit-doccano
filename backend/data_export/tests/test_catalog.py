import unittest

from ..pipeline.catalog import Options
from projects.models import (
    BOUNDING_BOX,
    DOCUMENT_CLASSIFICATION,
    IMAGE_CAPTIONING,
    IMAGE_CLASSIFICATION,
    INTENT_DETECTION_AND_SLOT_FILLING,
    SEGMENTATION,
    SEQ2SEQ,
    SEQUENCE_LABELING,
    SPEECH2TEXT,
)


class TestOptions(unittest.TestCase):
    def test_return_at_least_one_option(self):
        tasks = [
            BOUNDING_BOX,
            DOCUMENT_CLASSIFICATION,
            IMAGE_CAPTIONING,
            IMAGE_CLASSIFICATION,
            INTENT_DETECTION_AND_SLOT_FILLING,
            SEGMENTATION,
            SEQ2SEQ,
            SEQUENCE_LABELING,
            SPEECH2TEXT,
        ]
        for task in tasks:
            with self.subTest(task=task):
                options = Options.filter_by_task(task)
                self.assertGreaterEqual(len(options), 1)
