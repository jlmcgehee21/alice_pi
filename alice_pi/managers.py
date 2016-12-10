
class Manager(object):
    """
    A Manager's job is to manage collections of Measurer's and Senders
    """

    def __init__(self, measurers_and_senders):
        self.measurers_and_senders = measurers_and_senders

    def run(self):
        """
        For every measurer, see if the value has changed, if it has,
        push to senders.
        """
