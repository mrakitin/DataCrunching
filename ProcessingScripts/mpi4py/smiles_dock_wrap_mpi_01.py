#-------------------------------------------------------------
# MPI wrapper of smiles_dock.sh (or derived) script
# v 0.1
#
# Usage examples:
# On NERSC cluster (.sh script for slurm to be started by sbatch)
##!/bin/bash -l
##SBATCH -L SCRATCH
##SBATCH -C haswell
##SBATCH --constraint=haswell
##SBATCH -q debug
##SBATCH -N 20
##SBATCH -t 00:30:00
#module load python
#source activate /global/common/software/m2173/anhe-py3
#srun -n 640 python3 ./smiles_dock_wrap_mpi_01.py PLPro_chainsAB ena+db.can '-11.849,39.742,-39.838' '90,136,82' 0 2000
#
# On an isolated server:
# mpiexec -n 5 python smiles_dock_wrap_mpi_01.py 3CLPro_protein ena+db.sorted '-10.520,-2.322,-20.631' '54,52,60' 1,3,5,7,9,11,13,15
# mpiexec -n 11 python smiles_dock_wrap_mpi_01.py 3CLPro_protein ena+db.sorted '-10.520,-2.322,-20.631' '54,52,60' 0 15
#
#-------------------------------------------------------------

from mpi4py import MPI
from array import *
import subprocess
import sys
import time

#-------------------------------------------------------------

comMPI = MPI.COMM_WORLD #MPI stuff
rank = comMPI.Get_rank()
nProc = comMPI.Get_size()

len_argv = len(sys.argv)
if(len_argv < 5): raise Exception('Insufficient number of arguments were supplied.')

nmCoreScript = 'smiles_dock_01.sh' #'smiles_dock.sh'

nmProtein = sys.argv[1] #./smiles_dock.sh script arguments
nmFile2Proc = sys.argv[2] #Main file to process
sCrd = sys.argv[3] #Grid Center Coordinates
sGrid = sys.argv[4] #Grid Numbers of Points
#The next one or two arguments, sys.argv[5] and sys.argv[6], are used to define line numbers of the nmFile2Proc, see examples above

listIndLines2Proc = None
if(len_argv > 5):
    sLineFile2ProcInit = sys.argv[5] #Initial (0-based) line number of the Main File, or coma-separated individual line numbers to be processed

    argv5_isString = isinstance(sLineFile2ProcInit, str) if(sys.version_info[0] == 3) else isinstance(sLineFile2ProcInit, basestring)
    if(argv5_isString):
        sLineFile2ProcInit = sLineFile2ProcInit.replace('\'', '')
        commaInd = sLineFile2ProcInit.find(',')
        lineFile2ProcInit = None
        lineFile2ProcFin = None
        if((commaInd >= 0) and (commaInd < len(sLineFile2ProcInit) - 1)): #List of line numbers is submitted
            listStrIndLines2Proc = sLineFile2ProcInit.split(',')
            listIndLines2Proc = [int(listStrIndLines2Proc[i]) for i in range(len(listStrIndLines2Proc))]
        else: lineFile2ProcInit = int(sLineFile2ProcInit)
    else: lineFile2ProcInit = int(sLineFile2ProcInit)

    #lineFile2ProcInit = int(sys.argv[5])
    if((listIndLines2Proc is None) and (lineFile2ProcInit is not None)):
        if(len_argv > 6):
            sLineFile2ProcFin = sys.argv[6]
            argv6_isString = isinstance(sLineFile2ProcFin, str) if(sys.version_info[0] == 3) else isinstance(sLineFile2ProcFin, basestring)
            if(argv6_isString): sLineFile2ProcFin = sLineFile2ProcFin.replace('\'', '')
            lineFile2ProcFin = int(sLineFile2ProcFin) #Final (0-based) line of the Main File to be processed (to be taken into account only if sys.argv[5] doesn't define list of lines)
            if(lineFile2ProcFin < lineFile2ProcInit): raise Exception('Incorrect definition of initial and final string indexes to be processed.')
            listIndLines2Proc = [i for i in range(lineFile2ProcInit, lineFile2ProcFin + 1)]
        else: listIndLines2Proc = [lineFile2ProcInit]

arInds = array('i', [0])
arRes = array('i', [0])

if(rank == 0): #Master
    if(nProc == 1): #There are no Workers, do all the work for them
        if(listIndLines2Proc is None): #No line-related arguments submitted - process entire nmFile2Proc at once
            s2run = './' + nmCoreScript + ' ' + nmProtein + ' ' + nmFile2Proc + ' ' + sCrd + ' ' + sGrid
            #s2run = './' + nmCoreScript + ' ' + nmProtein + ' ' + nmFile2Proc + ' \'' + sCrd + '\' \'' + sGrid + '\''
            #s2run = './smiles_dock_01.sh ' + nmProtein + ' ' + nmFile2Proc + ' \'' + sCrd + '\' \'' + sGrid + '\''
            #s2run = './smiles_dock.sh ' + nmProtein + ' ' + nmFile2Proc + ' \'' + sCrd + '\' \'' + sGrid + '\''
            print('rank/size', rank, '/', nProc, ' command to run: ', s2run)

            subprocess.run(['./' + nmCoreScript, nmProtein, nmFile2Proc, sCrd, sGrid]) #Do Processing

            #subprocess.run(['./smiles_dock_01.sh', nmProtein, nmFile2Proc, sCrd, sGrid]) #Do Processing
            #subprocess.run(['./smiles_dock.sh', nmProtein, nmFile2Proc, sCrd, sGrid]) #Do Processing

        else:  #Line-related arguments submitted - process nmFile2Proc line by line
            f = open(nmFile2Proc, 'r')
            lines = f.readlines()
            f.close()
            nLines = len(lines)

            if(listIndLines2Proc is None): listIndLines2Proc = [i for i in range(nLines)]
            nLines2Proc = len(listIndLines2Proc)
           
            for i in range(nLines2Proc):
                curIndLine = listIndLines2Proc[i]
                if((curIndLine >= 0) and (curIndLine < nLines)):
                    nmSubFile = nmFile2Proc + '.' + repr(curIndLine)
                    fs = open(nmSubFile, 'w')
                    fs.write(lines[curIndLine])
                    fs.close()
                    
                    s2run = './' + nmCoreScript + ' ' + nmProtein + ' ' + nmSubFile + ' ' + sCrd + ' ' + sGrid
                    #s2run = './' + nmCoreScript + ' ' + nmProtein + ' ' + nmSubFile + ' \'' + sCrd + '\' \'' + sGrid + '\''
                    print('rank/size', rank, '/', nProc, ' command to run: ', s2run)

                    subprocess.run(['./' + nmCoreScript, nmProtein, nmSubFile, sCrd, sGrid]) #Do Processing

                else:
                    print('WARNING: Line with (0-based) index', curIndLine, 'was not found in', nmFile2Proc, 'file')
        exit()

    #split the main input file, save sub-files, send job orders to Workers, and receive reports from them
    f = open(nmFile2Proc, 'r')
    lines = f.readlines()
    f.close()
    nLines = len(lines)

    #if(lineFile2ProcFin > nLines - 1): lineFile2ProcFin = nLines - 1
    #nLines = lineFile2ProcFin - lineFile2ProcInit + 1

    if(listIndLines2Proc is None): listIndLines2Proc = [i for i in range(nLines)]
    nLines2Proc = len(listIndLines2Proc)
    #print('rank/size', rank, '/', nProc, ' nLines2Proc =', repr(nLines2Proc))
    
    nWorkersBusy = 0
    for i in range(nLines2Proc):
    #for i in range(nLines): #Send messages to Workers to process sub-files
        curIndLine = listIndLines2Proc[i]
        if((curIndLine >= 0) and (curIndLine < nLines)):
            nmSubFile = nmFile2Proc + '.' + repr(curIndLine)
            #nmSubFile = nmFile2Proc + '.' + repr(i + lineFile2ProcInit)
            #nmSubFile = nmFile2Proc + '.' + repr(i)
            
            fs = open(nmSubFile, 'w')
            fs.write(lines[curIndLine])
            #fs.write(lines[i + lineFile2ProcInit])
            #fs.write(lines[i])
            fs.close()

            arInds[0] = curIndLine
            #arInds[0] = i + lineFile2ProcInit
            #arInds[0] = i
            if(i < nProc - 1): #First, just send sub-file index to a Worker
                comMPI.Send([arInds, MPI.INT], dest=i+1)
                nWorkersBusy += 1
                #print('rank/size', rank, '/', nProc, ' job sent to dest:', repr(i+1))
            else: #If there are more sub-files than Workers, wait to hear from anyone that his previous job is done, and send a new one
                comMPI.Recv([arRes, MPI.INT], source=MPI.ANY_SOURCE) #Receive OK from any Worker that sub-file is processed
                rankWorker = arRes[0]
                comMPI.Send([arInds, MPI.INT], dest=rankWorker)
        else:
            print('WARNING: Line with (0-based) index', curIndLine, 'was not found in', nmFile2Proc, 'file')

    arInds[0] = -1
    for i in range(nWorkersBusy): #Wait for Workers to finish thier jobs and send them messages to exit 
        comMPI.Recv([arRes, MPI.INT], source=MPI.ANY_SOURCE) #Receive OK from any Worker that sub-file is processed
        rankWorker = arRes[0]
        comMPI.Send([arInds, MPI.INT], dest=rankWorker)

    for i in range(nLines2Proc, nProc): #Send messages to exit to those Workers who did not have chance to work
    #for i in range(nLines, nProc): #Send messages to exit to those Workers who did not have chance to work
        comMPI.Send([arInds, MPI.INT], dest=i)

else: #Workers: receive job orders from Master and report back after each job is done
    arRes[0] = rank
    maxNumSubFiles = 10000000 #Very Large Number
    for i in range(maxNumSubFiles):
        
        comMPI.Recv([arInds, MPI.INT], source=0) #Receive next job order from Master
        if(arInds[0] < 0): #Order to exit
            print('rank/size', rank, '/', nProc, ' exiting')
            break
        else:
            nmSubFile = nmFile2Proc + '.' + repr(arInds[0])
            s2run = './' + nmCoreScript + ' ' + nmProtein + ' ' + nmSubFile + ' ' + sCrd + ' ' + sGrid
            #s2run = './' + nmCoreScript + ' ' + nmProtein + ' ' + nmSubFile + ' \'' + sCrd + '\' \'' + sGrid + '\''
            #s2run = './smiles_dock_01.sh ' + nmProtein + ' ' + nmSubFile + ' \'' + sCrd + '\' \'' + sGrid + '\''
            #s2run = './smiles_dock.sh ' + nmProtein + ' ' + nmSubFile + ' \'' + sCrd + '\' \'' + sGrid + '\''
            print('rank/size', rank, '/', nProc, ' command to run: ', s2run)

            subprocess.run(['./' + nmCoreScript, nmProtein, nmSubFile, sCrd, sGrid]) #Do Processing

            #subprocess.run(['./smiles_dock_01.sh', nmProtein, nmSubFile, sCrd, sGrid]) #Do Processing
            #subprocess.run(['./smiles_dock.sh', nmProtein, nmSubFile, sCrd, sGrid]) #Do Processing
            #Analyze results? 
            #time.sleep(2.) #Mimic execution (for debugging)

            comMPI.Send([arRes, MPI.INT], dest=0) #Report to Master that job was done
