


from MicroWebSrv2  import *
from time          import sleep
from _thread       import allocate_lock
from lights import *



@WebRoute(GET, '/test')
def RequestTestGet(microWebSrv2, request):
    request.Response.ReturnOkJSON({
        'ClientAddr' : request.UserAddress,
        'Accept'     : request.Accept,
        'UserAgent'  : request.UserAgent
    })


@WebRoute(POST, '/lights', name='Lights')
def RequestTestPost(microWebSrv2, request) :
    data = request.GetPostedJSONObject()
    print(data)
    try :
        state = data['state']
        if 'interval' in data:
            interval = float(data['interval'])
        else:
            interval = None
        if 'colors' in data:
            colors = list(map(lambda c: (c['r'], c['g'], c['b']), data['colors']))
        else:
            colors = None
    except :
        print("Bad Request")
        request.Response.ReturnBadRequest()
        return
    if lights:
        if state == 'static':
            lights.state = STATIC
        elif state == 'marquee':
            lights.state = MARQUEE
        elif state == 'fade':
            lights.state = FADE
        elif state == 'rainbow':
            lights.state = RAINBOW
        else:
            lights.state = OFF
        if colors:
            lights.colors = colors
        if interval:
            lights.interval = interval

    request.Response.ReturnOk()

print()



mws2 = MicroWebSrv2()

# For embedded MicroPython, use a very light configuration,
mws2.SetEmbeddedConfig()
mws2._slotsCount = 4

# All pages not found will be redirected to the home '/',
mws2.NotFoundURL = '/'

mws2.StartManaged()

lights = Lights(pin=5, led_count=8)

try :
    while mws2.IsRunning :
        lights.run()
except KeyboardInterrupt :
    pass

# End,
print()
mws2.Stop()
print('Bye')
print()

# ============================================================================
# ============================================================================
# ============================================================================


