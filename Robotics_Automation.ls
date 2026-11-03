/PROG  KUGANRAJ_ROBOTICS_AUTOMATION_PROJECT
/Organize_CODEALPHA_TASKS
/ATTR
OWNER		= MNEDITOR;
COMMENT		= "2026";
PROG_SIZE	= 10481;
CREATE		= DATE 26-04-03  TIME 12:37:16;
MODIFIED	= DATE 26-04-03  TIME 12:37:18;
FILE_NAME	= PY1BCOM_;
VERSION		= 0;
LINE_COUNT	= 162;
MEMORY_SIZE	= 10853;
PROTECT		= READ_WRITE;
TCD:  STACK_SIZE	= 0,
      TASK_PRIORITY	= 50,
      TIME_SLICE	= 0,
      BUSY_LAMP_OFF	= 0,
      ABORT_REQUEST	= 0,
      PAUSE_REQUEST	= 0;
DEFAULT_GROUP	= 1,1,*,*,*;
CONTROL_CODE	= 00000000 00000000;
/APPL
  SPOT : TRUE ; 
/MN
   1:  !BMA R1612 ;
   2:   ;
   3:  UFRAME_NUM=0 ;
   4:  UTOOL_NUM=1 ;
   5:  PAYLOAD[1] ;
   6:   ;
   7:J PR[1:HOME POSITION] 50% FINE    ;
   8:   ;
   9:  DO[36:NIZ TO R1614-1]=ON ;
  10:   ;
  11:  DO[1:CYCLE COMP]=OFF ;
  12:  DO[2:WELD COMP 1 TO S161]=OFF ;
  13:  DO[136:WT ISO CONTACTOR]=OFF ;
  14:   ;
  15:  DO[20:NIZ TO S161]=ON ;
  16:   ;
  17:J P[3] 100% CNT50 BREAK    ;
  18:   ;
  19:  WAIT DI[1:READY OK 1 FROM S161]=ON    ;
  20:  WAIT DI[20:NIZ FROM S161]=ON    ;
  21:  DO[20:NIZ TO S161]=OFF ;
  22:   ;
  23:  DO[136:WT ISO CONTACTOR]=ON ;
  24:  WAIT DI[136:WT ISO CONTACTED]=ON    ;
  25:   ;
  26:  TIMER[1]=RESET ;
  27:  TIMER[1]=START ;
  28:   ;
  29:J P[17] 100% CNT70    ;
  30:L P[18] 2000mm/sec CNT70    ;
  31:L P[5] 1500mm/sec CNT50    ;
  32:   ;
  33:L P[32] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  34:L P[35] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  35:L P[36] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  36:L P[40] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  37:L P[44] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  38:L P[45] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  39:L P[46] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  40:L P[47] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  41:L P[48] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  42:L P[49] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  43:L P[54] 2000mm/sec CNT70    ;
  44:L P[55] 2000mm/sec CNT70    ;
  45:L P[16] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  46:  WAIT   0.00(sec) ;
  47:L P[56] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  48:L P[57] 2000mm/sec CNT70    ;
  49:L P[13] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  50:L P[20] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  51:L P[21] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  52:L P[23] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  53:   ;
  54:L P[33] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  55:L P[38] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  56:L P[39] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  57:L P[61] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  58:L P[62] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  59:  //WAIT   0.00(sec) ;
  60:L P[63] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  61:   ;
  62:L P[64] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  63:L P[65] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  64:L P[66] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  65:  //WAIT   0.00(sec) ;
  66:L P[75] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  67:L P[67] 1500mm/sec CNT50    ;
  68:L P[82] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  69:L P[80] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  70:L P[83] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  71:L P[84] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  72:L P[93] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  73:   ;
  74:   ;
  75:   ;
  76:  //WAIT   0.00(sec) ;
  77:L P[81] 2000mm/sec CNT50
    :  SPOT[SD=3,P=14,t=4.0,S=6,ED=3]    ;
  78:L P[76] 1500mm/sec CNT50    ;
  79:L P[77] 1500mm/sec CNT50    ;
  80:L P[78] 1500mm/sec CNT50    ;
  81:L P[59] 2000mm/sec CNT70    ;
  82:J P[24] 100% CNT70    ;
  83:L P[25] 1500mm/sec CNT70    ;
  84:L P[26] 1500mm/sec CNT70    ;
  85:L P[27] 2000mm/sec CNT50
    :  SPOT[SD=3,P=11,t=4.0,S=2,ED=3]    ;
  86:L P[1] 1500mm/sec CNT70    ;
  87:L P[79] 1500mm/sec CNT70    ;
  88:L P[68] 2000mm/sec CNT50
    :  SPOT[SD=3,P=11,t=4.0,S=2,ED=3]    ;
  89:L P[70] 2000mm/sec CNT50
    :  SPOT[SD=3,P=11,t=4.0,S=2,ED=3]    ;
  90:   ;
  91:   ;
  92:L P[25] 1500mm/sec CNT70    ;
  93:L P[24] 1500mm/sec CNT30 BREAK    ;
  94:   ;
  95:  WAIT DI[36:NIZ FROM R1614-1]=ON    ;
  96:  DO[36:NIZ TO R1614-1]=OFF ;
  97:  WAIT    .30(sec) ;
  98:  WAIT DI[36:NIZ FROM R1614-1]=ON    ;
  99:   ;
 100:L P[28] 1500mm/sec CNT70    ;
 101:L P[29] 1500mm/sec CNT70    ;
 102:L P[30] 1500mm/sec CNT30    ;
 103:L P[8] 1500mm/sec CNT50    ;
 104:L P[31] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=4,ED=3]    ;
 105:L P[10] 1500mm/sec CNT70    ;
 106:L P[34] 1500mm/sec CNT70    ;
 107:L P[4] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=4,ED=3]    ;
 108:L P[11] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=4,ED=3]    ;
 109:L P[85] 1500mm/sec CNT50    ;
 110:L P[86] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=7,ED=3]    ;
 111:L P[87] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=7,ED=3]    ;
 112:L P[88] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=7,ED=3]    ;
 113:L P[90] 1500mm/sec CNT50    ;
 114:L P[91] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=7,ED=3]    ;
 115:L P[92] 2000mm/sec CNT50
    :  SPOT[SD=3,P=15,t=4.0,S=7,ED=3]    ;
 116:   ;
 117:L P[6] 1500mm/sec CNT100    ;
 118:   ;
 119:   ;
 120:  DO[2:WELD COMP 1 TO S161]=ON ;
 121:   ;
 122:L P[7] 1500mm/sec CNT70    ;
 123:L P[41] 3000mm/sec CNT70    ;
 124:J P[15] 100% CNT100    ;
 125:J P[42] 100% CNT70    ;
 126:J P[43] 100% CNT30    ;
 127:   ;
 128:  DO[36:NIZ TO R1614-1]=ON ;
 129:   ;
 130:  DO[1:CYCLE COMP]=PULSE,1.0sec ;
 131:  DO[20:NIZ TO S161]=ON ;
 132:   ;
 133:  DO[2:WELD COMP 1 TO S161]=OFF ;
 134:  DO[136:WT ISO CONTACTOR]=OFF ;
 135:  WAIT DI[136:WT ISO CONTACTED]=OFF    ;
 136:   ;
 137:  TIMER[1]=STOP ;
 138:   ;
 139:J P[2] 100% CNT30    ;
 140:   ;
 141:  DO[33:NIZ TO R1611-1]=ON ;
 142:  DO[35:NIZ TO R1613-1]=ON ;
 143:  DO[36:NIZ TO R1614-1]=ON ;
 144:  DO[41:NIZ TO R1611-2]=ON ;
 145:  DO[43:NIZ TO R1613-2]=ON ;
 146:  DO[44:NIZ TO R1614-2]=ON ;
 147:   ;
 148:  DO[1:CYCLE COMP]=OFF ;
 149:  DO[2:WELD COMP 1 TO S161]=OFF ;
 150:  DO[3:WELD COMP 2 TO S161]=OFF ;
 151:  DO[4:WELD COMP 3 TO S161]=OFF ;
 152:  DO[136:WT ISO CONTACTOR]=OFF ;
 153:   ;
 154:  DO[20:NIZ TO S161]=ON ;
 155:   ;
 156:  CALL _TEST_CT    ;
 157:   ;
 158:J PR[1:HOME POSITION] 50% FINE    ;
 159:   ;
 160:  UFRAME_NUM=0 ;
 161:  UTOOL_NUM=1 ;
 162:  PAYLOAD[1] ;
/POS
P[1]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2219.636  mm,	Y =   573.120  mm,	Z =   613.676  mm,
	W =    14.421 deg,	P =    -4.003 deg,	R =    -3.102 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -129.208  mm
};
P[2]{
   GP1:
	UF : 0, UT : 1,	
	J1=    10.000 deg,	J2=   -40.000 deg,	J3=     0.000 deg,
	J4=    90.000 deg,	J5=   -90.000 deg,	J6=     0.000 deg
   GP2:
	UF : 0, UT : 1,	
	J1=    -3.000  mm
};
P[3]{
   GP1:
	UF : 0, UT : 1,	
	J1=     2.806 deg,	J2=   -48.922 deg,	J3=    19.225 deg,
	J4=    52.795 deg,	J5=  -108.771 deg,	J6=    -3.397 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -109.664  mm
};
P[4]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2150.913  mm,	Y =  1138.324  mm,	Z =   700.274  mm,
	W =     4.430 deg,	P =    -5.035 deg,	R =   -22.000 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -36.121  mm
};
P[5]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1899.802  mm,	Y =   833.958  mm,	Z =   -16.581  mm,
	W =   -92.975 deg,	P =    13.900 deg,	R =    91.902 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -94.675  mm
};
P[6]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2096.188  mm,	Y =  1383.999  mm,	Z =   607.854  mm,
	W =     1.073 deg,	P =    -2.438 deg,	R =   -21.385 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.197  mm
};
P[7]{
   GP1:
	UF : 0, UT : 1,	
	J1=    27.407 deg,	J2=    21.853 deg,	J3=    13.340 deg,
	J4=   -84.247 deg,	J5=   -67.415 deg,	J6=  -191.844 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.197  mm
};
P[8]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2154.005  mm,	Y =  1038.184  mm,	Z =   651.143  mm,
	W =     4.716 deg,	P =    -5.035 deg,	R =   -40.822 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -108.885  mm
};
P[10]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2154.005  mm,	Y =  1038.184  mm,	Z =   651.143  mm,
	W =     4.716 deg,	P =    -5.036 deg,	R =   -40.822 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -108.885  mm
};
P[11]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2132.010  mm,	Y =  1137.368  mm,	Z =   697.631  mm,
	W =     3.152 deg,	P =    -1.834 deg,	R =   -21.686 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -62.852  mm
};
P[13]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2005.920  mm,	Y =   742.168  mm,	Z =   610.220  mm,
	W =   -11.212 deg,	P =   -64.527 deg,	R =    12.917 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -18.141  mm
};
P[15]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1452.513  mm,	Y =   522.208  mm,	Z =   587.297  mm,
	W =   -51.769 deg,	P =   -35.307 deg,	R =    48.962 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.197  mm
};
P[16]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2007.705  mm,	Y =   897.794  mm,	Z =   606.847  mm,
	W =   -60.367 deg,	P =   -34.975 deg,	R =    72.990 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -20.095  mm
};
P[17]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1030.271  mm,	Y =   293.479  mm,	Z =   304.031  mm,
	W =   -46.264 deg,	P =    13.171 deg,	R =   148.378 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -109.664  mm
};
P[18]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1457.779  mm,	Y =   639.061  mm,	Z =  -162.609  mm,
	W =   -52.925 deg,	P =    28.141 deg,	R =   129.801 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -109.664  mm
};
P[20]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2002.181  mm,	Y =   669.438  mm,	Z =   608.178  mm,
	W =   -10.810 deg,	P =   -64.714 deg,	R =    12.475 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -12.790  mm
};
P[21]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2001.509  mm,	Y =   637.253  mm,	Z =   604.046  mm,
	W =   -10.810 deg,	P =   -64.714 deg,	R =    12.475 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -13.846  mm
};
P[23]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1998.632  mm,	Y =   598.900  mm,	Z =   595.141  mm,
	W =   -10.560 deg,	P =   -64.079 deg,	R =    12.198 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -18.938  mm
};
P[24]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1771.754  mm,	Y =   596.947  mm,	Z =   525.096  mm,
	W =    14.818 deg,	P =    -2.057 deg,	R =   -10.562 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -120.000  mm
};
P[25]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1997.469  mm,	Y =   586.607  mm,	Z =   554.646  mm,
	W =    14.422 deg,	P =    -4.003 deg,	R =    -3.102 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -136.635  mm
};
P[26]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2215.395  mm,	Y =   574.251  mm,	Z =   572.018  mm,
	W =    14.421 deg,	P =    -4.003 deg,	R =    -3.102 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -136.635  mm
};
P[27]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2197.552  mm,	Y =   511.207  mm,	Z =   626.336  mm,
	W =    14.699 deg,	P =    -3.987 deg,	R =    -3.121 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[28]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1784.032  mm,	Y =  1162.136  mm,	Z =   520.010  mm,
	W =     4.716 deg,	P =    -5.037 deg,	R =   -40.822 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.000  mm
};
P[29]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2001.070  mm,	Y =  1225.025  mm,	Z =   573.626  mm,
	W =     4.716 deg,	P =    -5.036 deg,	R =   -40.822 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.000  mm
};
P[30]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2003.417  mm,	Y =  1187.482  mm,	Z =   570.173  mm,
	W =     4.716 deg,	P =    -5.036 deg,	R =   -40.822 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -130.301  mm
};
P[31]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2148.755  mm,	Y =  1035.350  mm,	Z =   700.069  mm,
	W =     4.657 deg,	P =    -5.025 deg,	R =   -40.817 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -33.998  mm
};
P[32]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1863.863  mm,	Y =   889.347  mm,	Z =   -18.521  mm,
	W =   -92.829 deg,	P =     5.000 deg,	R =    93.491 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -44.256  mm
};
P[33]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1994.515  mm,	Y =   569.490  mm,	Z =   587.773  mm,
	W =    -6.819 deg,	P =   -66.081 deg,	R =     1.696 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -17.118  mm
};
P[34]{
   GP1:
	UF : 0, UT : 1,	
	J1=    28.772 deg,	J2=    10.826 deg,	J3=    11.664 deg,
	J4=   -78.273 deg,	J5=   -30.208 deg,	J6=  -190.883 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.037  mm
};
P[35]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1863.887  mm,	Y =   901.398  mm,	Z =    26.543  mm,
	W =   -92.202 deg,	P =      .212 deg,	R =    92.544 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.759  mm
};
P[36]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1860.252  mm,	Y =   918.771  mm,	Z =    85.519  mm,
	W =   -93.489 deg,	P =    -2.442 deg,	R =    93.406 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -26.541  mm
};
P[38]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1991.150  mm,	Y =   548.449  mm,	Z =   578.129  mm,
	W =    -6.819 deg,	P =   -66.081 deg,	R =     1.696 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[39]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1985.363  mm,	Y =   532.670  mm,	Z =   571.466  mm,
	W =     3.262 deg,	P =   -70.635 deg,	R =    -5.930 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -26.614  mm
};
P[40]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1871.070  mm,	Y =   952.615  mm,	Z =   225.951  mm,
	W =   -84.495 deg,	P =    -5.332 deg,	R =    92.845 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -39.098  mm
};
P[41]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  1764.248  mm,	Y =  1404.618  mm,	Z =   557.867  mm,
	W =     -.591 deg,	P =    -2.597 deg,	R =    15.206 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.197  mm
};
P[42]{
   GP1:
	UF : 0, UT : 1,	
	J1=     7.547 deg,	J2=   -52.560 deg,	J3=    22.963 deg,
	J4=     -.368 deg,	J5=  -114.980 deg,	J6=  -109.548 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.197  mm
};
P[43]{
   GP1:
	UF : 0, UT : 1,	
	J1=     7.547 deg,	J2=   -53.850 deg,	J3=    22.963 deg,
	J4=    90.000 deg,	J5=  -106.176 deg,	J6=   -11.335 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.197  mm
};
P[44]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1885.096  mm,	Y =   966.652  mm,	Z =   281.456  mm,
	W =   -73.770 deg,	P =   -11.975 deg,	R =    84.707 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -39.083  mm
};
P[45]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1898.874  mm,	Y =   979.824  mm,	Z =   327.601  mm,
	W =   -73.684 deg,	P =   -13.235 deg,	R =    84.321 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -22.918  mm
};
P[46]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1918.307  mm,	Y =   992.337  mm,	Z =   384.743  mm,
	W =   -70.716 deg,	P =   -10.967 deg,	R =    82.703 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -23.347  mm
};
P[47]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1933.014  mm,	Y =  1005.386  mm,	Z =   431.981  mm,
	W =   -70.342 deg,	P =   -15.160 deg,	R =    83.532 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -27.238  mm
};
P[48]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1956.364  mm,	Y =  1015.123  mm,	Z =   486.718  mm,
	W =   -68.940 deg,	P =    -7.923 deg,	R =    87.902 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -29.321  mm
};
P[49]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1985.702  mm,	Y =  1025.984  mm,	Z =   555.706  mm,
	W =   -65.679 deg,	P =   -17.314 deg,	R =    84.551 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -33.431  mm
};
P[54]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2018.112  mm,	Y =   984.628  mm,	Z =   546.024  mm,
	W =   -73.115 deg,	P =   -21.355 deg,	R =    92.171 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -108.692  mm
};
P[55]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2046.280  mm,	Y =   887.038  mm,	Z =   589.170  mm,
	W =   -71.327 deg,	P =   -32.338 deg,	R =    78.437 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -108.692  mm
};
P[56]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2008.656  mm,	Y =   772.030  mm,	Z =   609.391  mm,
	W =   -61.332 deg,	P =   -34.955 deg,	R =    70.727 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -18.279  mm
};
P[57]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2027.959  mm,	Y =   779.651  mm,	Z =   598.470  mm,
	W =   -18.278 deg,	P =   -69.340 deg,	R =    16.867 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -108.692  mm
};
P[59]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1548.823  mm,	Y =   667.793  mm,	Z =   454.585  mm,
	W =   -28.639 deg,	P =   -34.457 deg,	R =    44.417 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -108.692  mm
};
P[61]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1984.334  mm,	Y =   501.629  mm,	Z =   556.956  mm,
	W =    -1.210 deg,	P =   -68.614 deg,	R =    -1.286 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -44.466  mm
};
P[62]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1978.617  mm,	Y =   486.236  mm,	Z =   550.010  mm,
	W =    34.203 deg,	P =   -65.199 deg,	R =   -36.347 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -19.362  mm
};
P[63]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1975.335  mm,	Y =   468.098  mm,	Z =   539.264  mm,
	W =    28.109 deg,	P =   -65.523 deg,	R =   -29.202 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -15.986  mm
};
P[64]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1969.509  mm,	Y =   442.807  mm,	Z =   526.587  mm,
	W =    34.061 deg,	P =   -65.065 deg,	R =   -35.728 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -16.604  mm
};
P[65]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1967.299  mm,	Y =   431.604  mm,	Z =   521.164  mm,
	W =    31.157 deg,	P =   -63.216 deg,	R =   -32.666 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[66]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1963.298  mm,	Y =   410.066  mm,	Z =   508.983  mm,
	W =    32.619 deg,	P =   -62.223 deg,	R =   -34.800 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -10.930  mm
};
P[67]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1960.564  mm,	Y =   359.891  mm,	Z =   471.191  mm,
	W =    56.319 deg,	P =   -56.928 deg,	R =   -63.397 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[68]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2055.213  mm,	Y =   752.023  mm,	Z =   664.550  mm,
	W =     8.829 deg,	P =      .524 deg,	R =    -2.397 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -129.208  mm
};
P[70]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2061.424  mm,	Y =   803.961  mm,	Z =   668.588  mm,
	W =     8.829 deg,	P =      .525 deg,	R =    -2.397 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[75]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1956.794  mm,	Y =   379.130  mm,	Z =   491.611  mm,
	W =    27.778 deg,	P =   -64.511 deg,	R =   -32.079 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -15.756  mm
};
P[76]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1935.330  mm,	Y =   190.948  mm,	Z =   369.611  mm,
	W =    13.152 deg,	P =   -68.378 deg,	R =   -20.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -64.761  mm
};
P[77]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1944.930  mm,	Y =   334.468  mm,	Z =   369.610  mm,
	W =    11.590 deg,	P =   -68.579 deg,	R =   -18.551 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -101.674  mm
};
P[78]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1970.475  mm,	Y =   470.866  mm,	Z =   397.594  mm,
	W =   -27.296 deg,	P =   -67.397 deg,	R =    29.625 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -103.832  mm
};
P[79]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2142.573  mm,	Y =   769.862  mm,	Z =   626.873  mm,
	W =     8.829 deg,	P =      .524 deg,	R =    -2.397 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -129.208  mm
};
P[80]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1947.988  mm,	Y =   340.422  mm,	Z =   468.293  mm,
	W =    57.673 deg,	P =   -57.801 deg,	R =   -64.581 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[81]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1909.849  mm,	Y =   156.022  mm,	Z =   352.919  mm,
	W =    57.853 deg,	P =   -54.955 deg,	R =   -67.836 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -15.897  mm
};
P[82]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1951.677  mm,	Y =   357.834  mm,	Z =   479.702  mm,
	W =    56.318 deg,	P =   -56.928 deg,	R =   -63.106 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -37.748  mm
};
P[83]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1940.450  mm,	Y =   306.314  mm,	Z =   447.055  mm,
	W =    57.016 deg,	P =   -57.139 deg,	R =   -64.071 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[84]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1936.958  mm,	Y =   287.779  mm,	Z =   436.546  mm,
	W =    56.953 deg,	P =   -57.233 deg,	R =   -63.812 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[85]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2090.456  mm,	Y =  1244.796  mm,	Z =   626.236  mm,
	W =     2.825 deg,	P =    -4.083 deg,	R =   -27.560 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.104  mm
};
P[86]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2071.458  mm,	Y =  1265.479  mm,	Z =   675.005  mm,
	W =     2.826 deg,	P =    -4.082 deg,	R =   -27.560 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.104  mm
};
P[87]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2073.003  mm,	Y =  1285.837  mm,	Z =   675.235  mm,
	W =     2.826 deg,	P =    -4.082 deg,	R =   -27.560 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.104  mm
};
P[88]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2073.177  mm,	Y =  1343.135  mm,	Z =   674.010  mm,
	W =     2.826 deg,	P =    -4.082 deg,	R =   -27.560 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.104  mm
};
P[90]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2085.449  mm,	Y =  1440.670  mm,	Z =   639.877  mm,
	W =     2.825 deg,	P =    -4.082 deg,	R =   -27.560 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -135.104  mm
};
P[91]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2079.247  mm,	Y =  1446.849  mm,	Z =   672.220  mm,
	W =     1.596 deg,	P =    -3.848 deg,	R =   -21.746 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -68.465  mm
};
P[92]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, -1',
	X =  2080.296  mm,	Y =  1509.866  mm,	Z =   669.793  mm,
	W =      .663 deg,	P =    -4.835 deg,	R =    -5.779 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[93]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  1931.583  mm,	Y =   267.935  mm,	Z =   424.930  mm,
	W =    58.019 deg,	P =   -57.478 deg,	R =   -64.405 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
/END
