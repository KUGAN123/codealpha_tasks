/PROG  PICK_PLACE
/ATTR
OWNER        = MNEDITOR;
COMMENT      = "Basic conveyor pick and place";
DEFAULT_GROUP = 1,*,*,*,*;
/MN
   1:  ! DI[1] = PART PRESENT ;
   2:  ! DO[1] ON=CLOSE, OFF=OPEN ;
   3:  UTOOL_NUM=1 ;
   4:  UFRAME_NUM=1 ;
   5:  DO[1]=OFF ;
   6:  WAIT   .50(sec) ;
   7:  LBL[1] ;
   8:  WAIT DI[1]=ON ;
   9:  J P[1] 50% FINE ;
  10:  L P[2] 150mm/sec FINE ;
  11:  DO[1]=ON ;
  12:  WAIT   .50(sec) ;
  13:  L P[1] 150mm/sec FINE ;
  14:  J P[3] 50% FINE ;
  15:  L P[4] 150mm/sec FINE ;
  16:  DO[1]=OFF ;
  17:  WAIT   .50(sec) ;
  18:  L P[3] 150mm/sec FINE ;
  19:  JMP LBL[1] ;
/POS
P[1]{
 GP1:
 UF : 1, UT : 1, CONFIG : 'N U T, 0, 0, 0',
 X = 0.000 mm, Y = 0.000 mm, Z = 100.000 mm,
 W = 0.000 deg, P = 0.000 deg, R = 0.000 deg
};
P[2]{
 GP1:
 UF : 1, UT : 1, CONFIG : 'N U T, 0, 0, 0',
 X = 0.000 mm, Y = 0.000 mm, Z = 0.000 mm,
 W = 0.000 deg, P = 0.000 deg, R = 0.000 deg
};
P[3]{
 GP1:
 UF : 1, UT : 1, CONFIG : 'N U T, 0, 0, 0',
 X = 300.000 mm, Y = 0.000 mm, Z = 100.000 mm,
 W = 0.000 deg, P = 0.000 deg, R = 0.000 deg
};
P[4]{
 GP1:
 UF : 1, UT : 1, CONFIG : 'N U T, 0, 0, 0',
 X = 300.000 mm, Y = 0.000 mm, Z = 0.000 mm,
 W = 0.000 deg, P = 0.000 deg, R = 0.000 deg
};
