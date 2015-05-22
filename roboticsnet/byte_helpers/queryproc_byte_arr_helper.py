class QueryprocByteArrHelper:
    """
    This has functionality to parse replies from the server, and show in human
    readable form, what exactly is happening. This is for debugging at the
    moment, but may have potential in the future, to be used as an utility

    Author:
        psyomn
    """

    _sids_to_label = ROBOTICSNET_PROCESS_IDS_TO_LABEL

    _statids_to_label = ROBOTICSNET_PROCESS_STATUS_IDS_TO_LABELS

    @staticmethod
    def format(reply):
        """
        Format the reply to human readable format, from a queryproc command issued.

        Parameters:
            reply - is the reply received from the server. See the PROTOCOL file for
            more information about the format received

        Return:
            A string, decribing the processes, and their status
        """

        ret = ""
        reply_a = list(reply)

        while len(reply_a) != 0:
            b1, b2 = ord(reply_a[0]), ord(reply_a[1])
            ret += "{}: {}\n".format(_sids_to_label[b1], _statids_to_label[b2])

        return ret
