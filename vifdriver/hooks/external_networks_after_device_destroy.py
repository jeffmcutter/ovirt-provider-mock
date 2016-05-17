#!/usr/bin/python

import hooking
import os
import sys
sys.path.append("/usr/libexec/vdsm/hooks/vifdriver")
import vif_driver_hooking

reply = vif_driver_hooking.before_device_destroy(os.environ, hooking.read_domxml())
if reply:
    hooking.write_domxml(reply)
hooking.exit_hook("", return_code=0)
