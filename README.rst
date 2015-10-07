ROBOTICS NETWORKING
===================

.. image:: https://travis-ci.org/space-concordia-robotics/robotics-networking.svg
  :target: https://travis-ci.org/space-concordia-robotics/robotics-networking

Robotics networking stuff.

To install, run:

    python2.7 setup.py install --user

This will make a user install. Make sure your environment sees executables in
the local path.

If you're developing, use the following command:

    python2.7 setup.py develop --user

Any changes you make will take effect immediately. No need to reinstall.

Then you can start the server using the following command (this is the
executable that comes along with this library):

    roboticsnet-server

And if you want to give a few things a shot manually, you can test with the
client executable. You can run help to see what kind of commands are currently
supported manually.


    usage: roboticsnet-client [-h] [--forward FORWARD] [--reverse REVERSE]
                              [--forwardLeft FORWARDLEFT] [--queryproc] [--graceful]
                              [--host HOST] [--port PORT] [--testall] [--startvid]
                              [--stopvid]

    optional arguments:
      -h, --help         	  show this help message and exit
      --forward FORWARD  	  send forward command, given a value from 1 to 63
      --reverse REVERSE  	  send reverse command, given a value from 1 to 63
      --forwardLeft FORWARDLEFT   send forwardLeft command, given a value from 1 to 63
      --forwardRight FORWARDRIGHT send forwardRight command, given a value from 1 to 63
      --reverseLeft REVERSELEFT   send reverseLeft command, given a value from 1 to 63
      --reverseRight REVERSERIGHT send reverseRight command, given a value from 1 to 63
      --queryproc        	  send query about what is currently running
      --graceful         	  shutdown server gracefully
      --host HOST        	  specify an alternate host to default localhost
      --port PORT        	  specify an alternate port to default 5000
      --testall          	  sends a command of each
      --startvid         	  request video to start running
      --stopvid          	  request video to stop running


So after running the server, with the above command (roboticsnet-server), you can
send a packet this way:

    $ roboticsnet-client --forward 23

    Using port:  5000

    Using host:  localhost

    Send move command...

    Done!

And on the server side you should get the following:

    Send things to motors

    Received:  0x1 0x17

    Make move command

    Send things to motors

Overall Setup
=============

For the moment this is how things should look like:

.. image:: doc/sc-dep-diag.png

Server Hooks
============

It is possible to use this module without actually altering it. The way that
this is done, is by providing hooks to the server's commands. The commands
execute whenever there is a request that is received and processed. After the
request is processed and matched against the proper command, the command is
executed. Each command is associated with a hook. So after the command (pattern)
is executed, the hook is executed right after.

There exists an example you can read in 'roboticsnet/examples/hook_example.py'.

We will go over segments of the above piece by piece in order for the reader to
have an easier time understanding what is happening.

.. code:: python

    import roboticsnet
    from roboticsnet.command_hook import CommandHook
    from roboticsnet.rover_listener import RoverListener

    def _forwardHook():
        ...

    def _turnHook():
        ...

    def _queryProcHook():
        ...

    def _reverse=_reverseHook():
        ...

    def _startVideo():
        ...

    # First you would need to define your hooks using CommandHook
    cmd_hook = CommandHook(
            forward=_forwardHook,
            turn=_turnHook,
            queryproc=_queryProcHook,
            reverse=_reverseHook,
            startVideo=_startVideoCount
            )

    l = RoverListener(hooks=cmd_hook)
    l.listen()

The above example starts a listening server with hooks. The 'def's prefixed with
'_' are our cutsom hooks. We can provide any method we want in order to get this
to execute arbitrary code. So for example, each time a 'forward' command is
received, then the '_forwardHook()' method will actually execute once the
request is done processing. This is how you attach your added, wanted behavior.

To do this we need an extra structure which stores this information (what hooks
to execute whenever a particular command is received). We use an object called
'CommandHook', and set each of these hooks individually. You can omit hooks, and
that will be fine - it simply means we do not want to bind any more behavior to
a command.

You could also create classes, and pass their methods as hooks as well. Here is
another example which is located in 'examples/hook_with_params.py'.

.. code:: python

    import roboticsnet
    from roboticsnet.command_hook import CommandHook
    from roboticsnet.rover_listener import RoverListener

    forward_count = 0

    class Counter:
        def __init__(self):
            self.count = 0

        def incr(self):
            self.count += 1

        def get(self):
            return self.count

    def _forwardHook(params):
        print "This is my custom forward hook!"
        print "And in my custom forward hook, the params I receive are: ", params
        print "And I extract the value of interest: ", params['value']

    def _turnHook():
        print "This is turn hook, where I don't care about the params (even though"
        print "we actually do receive params"

    myCounter = Counter()

    cmd_hook = CommandHook(
            forward=_forwardHook,
            turn=_turnHook,
            startVideo=myCounter.inrc
            )

    l = RoverListener(hooks=cmd_hook)
    l.listen()

    print "The startvideo command was received this many times: ", myCounter.get()

That should conclude most of what you need to know about hooks!

Polling Services
================

Polling services have been added to the networking library. What this means is
that you're able to pass code blocks, which will then be spawned as monitoring
services.

The way this is achieved is by creating a monitoring service object which
contains the code block you pass. It waits every specified time unit, and will
then invoke the code block.

Essentially the code block you pass must return the value you need. How this
ties all together in the end is that when the client will request for sensor
info (see sensinfo in PROTOCOL), the networking library will go over all the
monitoring services, and get the last value obtained from the polling. Then all
of that information is packaged appropriately, and sent back to the client for
consumption.

A sample file for these monitoring services may be found in

    robotics-networking/examples/service_example.py

.. code:: python

    import roboticsnet
    from roboticsnet.command_hook import CommandHook
    from roboticsnet.rover_listener import RoverListener

    forward_count = 0

    def _forwardHook():
        global forward_count
        print "This is my custom forward hook!"
        forward_count += 1

    def polling_service():
        """ Returns the same number all the time; for testing purposes """
        print "polling service 1 is executed!"
        return 42

    def polling_service_2():
        """ Just another service """
        print "Service 2!"
        return 24

    def cat():
        """ somehow a cat made it into the software! """
        print "MEW MEW MEW MEW"
        return 'cat'

    # You don't need hooks in this case, but just to show that you can use them
    # anyway.
    cmd_hook = CommandHook(
            forward=_forwardHook
            )

    l = RoverListener(\
            hooks=cmd_hook,
            # And again we bind the polling services here
            monitorProcs=[\
                polling_service,
                polling_service_2,
                cat])

    print roboticsnet.__appname__, " ",  roboticsnet.__version__
    print "Starting command dispatcher..."
    l.listen()

    print "The server is completely oblivious to the following information:"
    print "  - forward commands received: ", forward_count


