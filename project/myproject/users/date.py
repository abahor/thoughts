import datetime

def date(value):
    # if value == datetime.datetime.utcnow():
    #     return 'now'
    if value > datetime.datetime.utcnow() - datetime.timedelta(minutes=59):
        if datetime.datetime.utcnow().minute - value.minute == 0:
            return 'now'
        # if value.minute - datetime.datetime.utcnow().minute == 0:
            # v = datetime.datetime.utcnow().seconds - value.seconds
            # return str(value.seconds) + ' seconds'
        # print(str(datetime.datetime.utcnow().minute) + '     ' + str(value.minute))
        i = datetime.datetime.utcnow() - value
        print(i)
        YY = datetime.datetime.utcnow() - i
        # print('h')
        print(datetime.datetime.utcnow())
        print(value)
        print(YY)
        rqq = divmod(i.seconds,60)[0]
        return str(rqq) + ' min'

    p = datetime.datetime.now() - datetime.timedelta(days=1)

    if value > p:
        # print('hello')
        # print(datetime.datetime.utcnow().hour ,'  - ', value.hour)
        # return str(datetime.datetime.utcnow().hour - value.hour) + ' hour'
        rd = datetime.datetime.utcnow() - value
        print('ss')
        print(rd.seconds)
        t = divmod(divmod(rd.seconds,60)[0],60)[0]
        print(t,'   ', divmod(rd.seconds,60)[0])
        if t == 0:
            return 1 + ' hours'
        return str(t) + ' hours'
