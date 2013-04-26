import sys
import os


def makeJob(n):
    run = "MW"
    path = os.getcwd() +"/"+run+"/"+str(n)+"/"
    print path
    os.system("mkdir -p "+path)
    fileOut = open(path+"jobScript", "w")
    fileOut.write("#!/bin/bash \n")
    fileOut.write("#    Begin PBS directives \n")
    fileOut.write("#PBS -A ast032 \n")
    fileOut.write("#PBS -N run_" + run + "\n")
    fileOut.write("#PBS -j oe \n")
    fileOut.write("#PBS -l walltime=00:10:00,nodes="+str(n) +" \n")
    fileOut.write("#PBS -l gres=widow2%widow3 \n")
    fileOut.write("#    End PBS directives and begin shell commands \n")

    fileOut.write("module load cmake\n")
    fileOut.write("module load vim/7.3\n")
    fileOut.write("module load cudatoolkit\n")
    fileOut.write("module load git\n")

    fileOut.write("module swap PrgEnv-pgi PrgEnv-gnu\n")
    fileOut.write("cd " + path +" \n")
    fileOut.write("export OMP_SET_NUM_THREADS=16\n")
    fileOut.write("date\n")
    fileOut.write("aprun -n${PBS_NUM_NODES} -d16 -cc 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15  -N 1 ");
    
    fileOut.write("/lustre/widow2/scratch/jbedorf/BonsaiGitStrong/runtime/bonsai2_slowdust_run ");
    fileOut.write("-i  /tmp/work/jbedorf/1BTest/IC/WPD09_test3_1B.tipsy ")
    fileOut.write("-T 2 -r 1 -o 0.4 -t 0.000001 -e 0.01 --prepend-rank\n")

    fileOut.close()

makeJob(1)
makeJob(2)
makeJob(4)
makeJob(16)
makeJob(64)
makeJob(128)
makeJob(256)
makeJob(512)
makeJob(1024)
makeJob(2048)
makeJob(4096)
makeJob(8192)
makeJob(16384)
makeJob(18600)

