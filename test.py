from git import Repo
import time
now = time.gmtime(time.time())
y, m, d  = now.tm_year, now.tm_mon, now.tm_mday 
msg  = "data update "+str(y)+str(m)+str(d)
repo = Repo("./")
repo.git.add(update=True)
repo.index.commit(msg)
origin = repo.remote(name="origin")
repo.push("--set-upstream", 'origin', "master")