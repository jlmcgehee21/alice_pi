import unittest2 as unittest
import mock
from alice_pi import managers


class TestManager(unittest.TestCase):
    def test_run(self):
        count = 3

        measurer = mock.MagicMock(measure=mock.Mock(side_effect=lambda:  1))
        sender = mock.MagicMock(send=mock.Mock(side_effect=lambda x: 200))

        test = {'measurer': measurer,
                'senders': [sender]}

        man = managers.Manager([test])

        man.run(count=count)

        # assert we check the measurer every time
        self.assertEquals(measurer.measure.call_count, count)

        # since we are recording the same measurement, we will only send once
        self.assertEquals(sender.send.call_count, 1)


if __name__ == '__main__':
    unittest.main()
