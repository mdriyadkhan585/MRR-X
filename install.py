# Tool Name :-  MRR-X
# Author        :-  RIYAD KHAN
# Date            :-  8/24/2022
#Category     :-  root@MRR#>

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install MRR-X [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          
          if os.path.exists(system.conf_dir+"/MRR-X"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/MRR-X")
          os.system(system.sudo+" cp -r modules core MRR-X.py "+system.conf_dir+"/MRR-X")
          os.system(system.sudo+" cp -r core/MRR-X "+system.bin)
          os.system(system.sudo+" cp -r core/mrrx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/MRR-X")
          os.system(system.sudo+" chmod +x "+system.bin+"/mrrx")
          os.system("cd .. && "+system.sudo+" rm -rf MRR-X")
          if os.path.exists(system.bin+"/MRR-X") and os.path.exists(system.conf_dir+"/MRR-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m root@MRR#> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m root@MRR#> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/MRR-X"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/MRR-X")
          os.system("cp -r modules core MRR-X.py "+system.conf_dir+"/MRR-X")
          os.system("cp -r core/MRR-X "+system.bin)
          os.system("cp -r core/mrrx "+system.bin)
          os.system("chmod +x "+system.bin+"/MRR-X")
          os.system("chmod +x "+system.bin+"/mrrx ")
          os.system("cd .. && rm -rf MRR-X")
          if os.path.exists(system.bin+"/MRR-X") and os.path.exists(system.conf_dir+"/MRR-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m root@MRR#> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m root@MRR#> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
