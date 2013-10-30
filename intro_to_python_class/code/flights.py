def report_status(scheduled_time, estimated_time):
    ''' (number, number) -> string

    Return the flight status (on time, early or delayed)
    for a flight that was scheduled to arrive at
    scheduled time, but is now estimated to arrive
    at estimated time.

    Pre-condition: scheduled time and estimated time
    are both >= 0 and < 24.
    
    >>> report_status(14.3, 14.3)
    'on time'
    >>> report_status(12.5, 11.5)
    'early'
    >>> report_status(9.0, 9.5)
    'delayed'
    '''

    if scheduled_time == estimated_time:
        return 'on time'

    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'
