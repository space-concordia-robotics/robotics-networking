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

    $ roboticsnet-client --help
    usage: Manually send commands to listener. [-h] [--move MOVE] [--turn TURN]
                                               [--queryproc QUERYPROC]

    optional arguments:
      -h, --help            show this help message and exit
      --move MOVE           send move command, given a value from 0 to 255
      --turn TURN           send turn command, given a value from 0 to 255
      --queryproc QUERYPROC
                            send query about what is currently running


So after running the server, with the above command (roboticsnet-server), you can
send a packet this way:

    $ roboticsnet-client --move 23

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
