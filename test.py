# from git import Repo
import time
now = time.gmtime(time.time())
y, m, d  = now.tm_year, now.tm_mon, now.tm_mday 
msg  = "data update "+str(y)+str(m)+str(d)
# repo = Repo("./")
# repo.git.add(update=True)
# repo.index.commit(msg)
# origin = repo.remote(name="origin")
# branch = repo.head()
# origin.push("--set-upstream", origin.ma)

#-*- coding: utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import subprocess
import os

os.chdir('./')

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", msg])
subprocess.call(["git", "push", "-u", "origin", "master"])