# Autodock4 enhancement

Autodock4 is a freely available docking program. It's implementation is
limited to allowing for at most 32 flexible torsion angles in molecules.
However, some of the molecules we want to process are bigger than that,
and in that case the code would abort. The code authors actually do not
recommend running such large molecules with the code. Instead the 
recommend approaches that would dock such molecules in incremental ways.
As these approaches seem very labor intensive they seem impractical
for numbers of molecules we want to process. Hence, we choose to throw
caution to the wind and increase the maximum number of torsion angles.

To increase the number of torsion angles we need to update two header
files where compile time parameters are given:

- `constants.h`: Contains the `MAX_TORS` parameter and the `TOR_ARG_LIST`
  which is an argument list fragment listing all torsion angles.
- `autocomm.h`: Contains the `LINE_LEN` parameter which should at least 
  be `4+4*MAX_TORS` in size.

In addition there is a script `gen_tor_arg_list.sh` to generate `TOR_ARG_LIST`s
for arbitrary numbers of torsion angles should you need to adjust this.
