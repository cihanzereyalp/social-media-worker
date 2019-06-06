import unittest
from unittest import mock

from .. import login_with_creds
from .. import main


class TestSMWorker(unittest.TestCase):
    @mock.patch.object(login_with_creds.LoginWithCreds, '__init__')
    @mock.patch('social-media-worker.main.get_inputs')
    def test_main_start_instagram(self, mock_get_inputs, mock_class):
        mock_get_inputs.return_value = 'instagram', 'instagram', 'instagram'
        mock_class.return_value = None

        main.start()
        mock_get_inputs.assert_called()
        mock_class.assert_called_once_with('instagram', 'instagram', 'instagram')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
