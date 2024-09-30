from functools import wraps
import sys

def instrument(f):
    """Show call entry/exits on stderr

    Wrapper to instrument a function to show the
    call entry and exit from that function. Can
    customize view with global instrument_flags.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        call_depth = wrapper.call_count
        wrapper.call_count += 1
        arg_str = ', '.join([str(args[i]) for i in range(len(args))])
        if instrument.TRIM_ARGS is not None and len(arg_str) > instrument.TRIM_ARGS:
            arg_str = arg_str[:instrument.TRIM_ARGS] + " ..."
        if instrument.SHOW_CALL:
            sys.stderr.write("   "*call_depth + "call to " + f.__name__ + ": " + arg_str + "\n")
        result = f(*args, **kwargs)
        res_str = str(result)
        if instrument.TRIM_RET is not None and len(res_str) > instrument.TRIM_RET:
            res_str = res_str[:instrument.TRIM_RET] + " ..."
        if instrument.SHOW_RET:
            sys.stderr.write("   "*call_depth + f.__name__ + " returns: " +  res_str + "\n")
        wrapper.call_count -= 1
        return result
    wrapper.call_count = 0
    return wrapper

instrument.SHOW_CALL = True
instrument.SHOW_RET = True
instrument.TRIM_ARGS = 55  #None if no trimming
instrument.TRIM_RET = 60   #None if no trimming
