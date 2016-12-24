import asyncio


class Manager(object):
    """
    A Manager's job is to manage collections of Measurer's and Senders
    """

    def __init__(self, measurers_and_senders):
        self.measurers_and_senders = measurers_and_senders

    def __init_measurements(self):
        for measurer_group in self.measurers_and_senders:
            measurer_group['measurement'] = None

    def run(self, count=None):
        """
        For every measurer, see if the value has changed, if it has,
        push to senders.
        """

        async def check_status(measurer_group):
            new_status = measurer_group['measurer'].measure()

            if new_status != measurer_group['measurement']:
                return new_status
            else:
                return None

        async def send_measurement(sender, measurement):
            sender.send(measurement)

        async def my_coroutine():
            loop_count = 0
            self.__init_measurements()
            while True:
                for measurer_group in self.measurers_and_senders:  # async for
                    meas_status = await check_status(measurer_group)
                    if meas_status is not None:
                        measurer_group['measurement'] = meas_status
                        for sender in measurer_group['senders']:  # async for
                            await send_measurement(sender,
                                                   measurer_group['measurement'])

                if count is not None:
                    loop_count += 1
                    if loop_count >= count:
                        break

        loop = asyncio.get_event_loop()
        loop.run_until_complete(my_coroutine())


if __name__ == '__main__':
    Manager('').run()
