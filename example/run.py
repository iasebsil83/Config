#!/usr/bin/python3




# ---- IMPORTATIONS ----

#add library path
import sys
sys.path.append("../lib")

#dreamlands
import config as cfg






# ---- EXECUTION ----

# EXAMPLE 1 : READING

#read a dreamlands file
myComputer_config = cfg.read("oldComputer.cfg")

#display parsed content
print("EXAMPLE 1 : Configuration read from \'oldComputer.cfg\' : ")
print(myComputer_config)
print()




# EXAMPLE 2 : WRITING

#create a new configuration
newComputer_config = {
	"CPU_ARCHITECTURE" : "x86_64",
	"GPU_MEMORY_TYPE"  : "GDDR5",
	"RAM_TYPE"         : "DDR5",
	"RAM_SIZE"         : "16GB"
}

#get Config text equivalent
print("EXAMPLE 2 : Writing :")
print(newComputer_config)
print("in file 'newComputer.cfg'.")

#write into a config file
cfg.write(newComputer_config, "newComputer.cfg")
