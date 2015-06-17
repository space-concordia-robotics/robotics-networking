from roboticsnet.roboticsnet_exception import RoboticsnetException

class Commandable:
    """ Interface for anything that may be executed """

    def execute(self):
        raise NotImplementedError("You need to implement this functionality")

    def _runHook(self, hook, params):
        if not hook: return

        argc = hook.func_code.co_argcount

        def isInstanceMethod():
            return hook.func_code.co_varnames[0] == 'self' and argc == 2

        if argc == 0:
            hook()
        elif argc == 1 or isInstanceMethod():
            hook(params)
        else:
            raise RoboticsnetException(
                "You can only supply hooks with 0, or 1 parameter. Read the documentation.")
