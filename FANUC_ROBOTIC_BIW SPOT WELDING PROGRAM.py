"""
Python representation of a FANUC LS robot program.

Source: PY1BRHD_35JPH_APR.LS
Purpose: Read and inspect the FANUC program's motion, I/O, wait, timer,
and spot-welding instructions in Python.

IMPORTANT:
- This is NOT a FANUC robot controller program.
- It does NOT connect to or move a robot.
- SPOT schedules, I/O mappings, frames, tools, payload and safety logic
  must be verified by a qualified FANUC integrator before any real use.
- The original FANUC position records are retained below as reference text.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class FanucInstruction:
    line: int
    source: str


PROGRAM_NAME = "PY1BRHD_35JPH_APR"
CONTROLLER_CONTEXT = "FANUC R-30iB (source-file context)"
SOURCE_FORMAT = "FANUC LS"

# Each item preserves the original FANUC instruction text.
# This is an inspectable representation, not executable robot motion.
INSTRUCTIONS: List[FanucInstruction] = [
    FanucInstruction(1, "!FMA R0403 ;"),
    FanucInstruction(2, "!***********************: ;"),
    FanucInstruction(3, "!***********************: ;"),
    FanucInstruction(4, "!       P  Y  1  B      : ;"),
    FanucInstruction(5, "!      2  A  S  D  U    : ;"),
    FanucInstruction(6, "!    R  N  T  B  C  I   : ;"),
    FanucInstruction(7, "!***********************: ;"),
    FanucInstruction(8, "!***********************: ;"),
    FanucInstruction(9, ";"),
    FanucInstruction(10, "UFRAME_NUM=0 ;"),
    FanucInstruction(11, "UTOOL_NUM=1 ;"),
    FanucInstruction(12, "PAYLOAD[1] ;"),
    FanucInstruction(13, ";"),
    FanucInstruction(14, "J PR[3] 50% FINE    ;"),
    FanucInstruction(15, ";"),
    FanucInstruction(16, "DO[33]=ON ;"),
    FanucInstruction(17, "DO[1]=OFF ;"),
    FanucInstruction(18, "DO[2]=OFF ;"),
    FanucInstruction(19, "DO[98]=OFF ;"),
    FanucInstruction(20, "DO[20]=ON ;"),
    FanucInstruction(21, ";"),
    FanucInstruction(22, "J P[1] 30% CNT30    ;"),
    FanucInstruction(23, "J P[17] 30% CNT30    ;"),
    FanucInstruction(24, "J P[51] 75% CNT30    ;"),
    FanucInstruction(25, ";"),
    FanucInstruction(26, "DO[98]=ON ;"),
    FanucInstruction(27, "WAIT DI[1]=ON    ;"),
    FanucInstruction(28, "WAIT DI[20]=ON    ;"),
    FanucInstruction(29, "WAIT DI[97]=ON    ;"),
    FanucInstruction(30, "DO[20]=OFF ;"),
    FanucInstruction(31, "WAIT   3.00(sec) ;"),
    FanucInstruction(32, "TIMER[1]=RESET ;"),
    FanucInstruction(33, "TIMER[1]=START ;"),
    FanucInstruction(34, ";"),
    FanucInstruction(35, "J P[60] 75% CNT70    ;"),
    FanucInstruction(36, ";"),
    FanucInstruction(37, "J P[59] 75% FINE    ;"),
    FanucInstruction(38, "WAIT DI[33]=ON    ;"),
    FanucInstruction(39, "DO[33]=OFF ;"),
    FanucInstruction(40, "WAIT DI[33]=ON    ;"),
    FanucInstruction(41, "WAIT DI[41]=ON    ;"),
    FanucInstruction(42, ";"),
    FanucInstruction(43, "J P[79] 75% CNT50    ;"),
    FanucInstruction(44, "L P[78] 2000mm/sec CNT50    ;"),
    FanucInstruction(45, "L P[80] 2000mm/sec CNT50    ;"),
    FanucInstruction(46, "L P[76] 2000mm/sec CNT50    ;"),
    FanucInstruction(47, "L P[84] 2000mm/sec CNT50    ;"),
    FanucInstruction(48, ";"),
    FanucInstruction(49, "L P[92:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=0,ED=3]    ;"),
    FanucInstruction(50, "!SPOT 36 ;"),
    FanucInstruction(51, ";"),
    FanucInstruction(52, "L P[91:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(53, "!SPOT 35 ;"),
    FanucInstruction(54, ";"),
    FanucInstruction(55, "L P[114] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(56, "!SPOT 34 ;"),
    FanucInstruction(57, ";"),
    FanucInstruction(58, "L P[113] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(59, "!SPOT 33 ;"),
    FanucInstruction(60, ";"),
    FanucInstruction(61, ";"),
    FanucInstruction(62, "L P[112] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(63, "!SPOT 32 ;"),
    FanucInstruction(64, ";"),
    FanucInstruction(65, "L P[16] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(66, "L P[110] 2000mm/sec CNT50    ;"),
    FanucInstruction(67, "L P[109] 1500mm/sec CNT50    ;"),
    FanucInstruction(68, ";"),
    FanucInstruction(69, ";"),
    FanucInstruction(70, "L P[19] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(71, ";"),
    FanucInstruction(72, "L P[69] 2000mm/sec CNT50    ;"),
    FanucInstruction(73, ";"),
    FanucInstruction(74, "L P[103] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(75, "!SPOT 27 ;"),
    FanucInstruction(76, ";"),
    FanucInstruction(77, "L P[102] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(78, "!SPOT 26 ;"),
    FanucInstruction(79, ";"),
    FanucInstruction(80, "L P[101] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(81, "!SPOT 25 ;"),
    FanucInstruction(82, ";"),
    FanucInstruction(83, "L P[87:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(84, "!SPOT 24 ;"),
    FanucInstruction(85, ";"),
    FanucInstruction(86, "L P[70:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=0,ED=3]    ;"),
    FanucInstruction(87, "!SPOT 23 ;"),
    FanucInstruction(88, ";"),
    FanucInstruction(89, "L P[89] 2000mm/sec CNT50    ;"),
    FanucInstruction(90, "L P[88] 2000mm/sec CNT50    ;"),
    FanucInstruction(91, "DO[33]=ON ;"),
    FanucInstruction(92, "L P[68:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(93, "!SPOT 22 ;"),
    FanucInstruction(94, "WAIT DI[41]=ON    ;"),
    FanucInstruction(95, "DO[41]=OFF ;"),
    FanucInstruction(96, "WAIT DI[41]=ON    ;"),
    FanucInstruction(97, "WAIT   1.00(sec) ;"),
    FanucInstruction(98, ";"),
    FanucInstruction(99, "L P[66:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=12,S=20,ED=3]    ;"),
    FanucInstruction(100, "!SPOT 21 ;"),
    FanucInstruction(101, ";"),
    FanucInstruction(102, "WAIT DI[41]=ON    ;"),
    FanucInstruction(103, "DO[41]=OFF ;"),
    FanucInstruction(104, "WAIT DI[41]=ON    ;"),
    FanucInstruction(105, ";"),
    FanucInstruction(106, "L P[23] 1500mm/sec CNT50    ;"),
    FanucInstruction(107, "L P[22] 2000mm/sec CNT50    ;"),
    FanucInstruction(108, ";"),
    FanucInstruction(109, "L P[27:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=12,S=20,ED=3]    ;"),
    FanucInstruction(110, "!SPOT 20 ;"),
    FanucInstruction(111, ";"),
    FanucInstruction(112, "L P[15:ID1788] 1000mm/sec CNT50 SPOT[SD=3,P=15,S=36,ED=3]    ;"),
    FanucInstruction(113, "!SPOT 19 ;"),
    FanucInstruction(114, "WAIT   1.00(sec) ;"),
    FanucInstruction(115, "L P[52] 2000mm/sec CNT50    ;"),
    FanucInstruction(116, "L P[26] 2000mm/sec CNT50    ;"),
    FanucInstruction(117, "DO[41]=ON ;"),
    FanucInstruction(118, "L P[25] 2000mm/sec CNT30    ;"),
    FanucInstruction(119, "L P[48] 2000mm/sec CNT30    ;"),
    FanucInstruction(120, "L P[55] 1500mm/sec CNT50    ;"),
    FanucInstruction(121, ";"),
    FanucInstruction(122, "L P[56:ID1788] 500mm/sec CNT50 SPOT[SD=3,P=10,S=20,ED=3]    ;"),
    FanucInstruction(123, "!SPOT 18 ;"),
    FanucInstruction(124, ";"),
    FanucInstruction(125, "L P[55] 1500mm/sec CNT50    ;"),
    FanucInstruction(126, "L P[54] 1500mm/sec CNT30    ;"),
    FanucInstruction(127, "L P[53] 1500mm/sec CNT50    ;"),
    FanucInstruction(128, "L P[9] 1500mm/sec CNT70    ;"),
    FanucInstruction(129, ";"),
    FanucInstruction(130, "L P[8:ID1789_a] 500mm/sec CNT50 SPOT[SD=3,P=10,S=20,ED=3]    ;"),
    FanucInstruction(131, "!SPOT 17 ;"),
    FanucInstruction(132, "WAIT   1.00(sec) ;"),
    FanucInstruction(133, "L P[95] 1500mm/sec CNT70    ;"),
    FanucInstruction(134, "L P[42] 1500mm/sec FINE    ;"),
    FanucInstruction(135, "L P[18] 1500mm/sec FINE SPOT[SD=3,P=11,S=2,ED=3]    ;"),
    FanucInstruction(136, ";"),
    FanucInstruction(137, "L P[20] 500mm/sec FINE SPOT[SD=3,P=11,S=2,ED=3]    ;"),
    FanucInstruction(138, ";"),
    FanucInstruction(139, "L P[6] 500mm/sec CNT30    ;"),
    FanucInstruction(140, "L P[21] 500mm/sec FINE SPOT[SD=3,P=11,S=2,ED=3]    ;"),
    FanucInstruction(141, ";"),
    FanucInstruction(142, ";"),
    FanucInstruction(143, ";"),
    FanucInstruction(144, ";"),
    FanucInstruction(145, "L P[14] 500mm/sec CNT10    ;"),
    FanucInstruction(146, ";"),
    FanucInstruction(147, "L P[13:ID1410_a] 500mm/sec FINE SPOT[SD=4,P=12,S=22,ED=4]    ;"),
    FanucInstruction(148, "!SPOT 13 ;"),
    FanucInstruction(149, "//WAIT   1.00(sec) ;"),
    FanucInstruction(150, "L P[12:ID1410_a] 500mm/sec FINE SPOT[SD=4,P=12,S=22,ED=4]    ;"),
    FanucInstruction(151, "!SPOT 12 ;"),
    FanucInstruction(152, ";"),
    FanucInstruction(153, "L P[73] 500mm/sec CNT50    ;"),
    FanucInstruction(154, "L P[11] 500mm/sec CNT30    ;"),
    FanucInstruction(155, "L P[72] 500mm/sec CNT10    ;"),
    FanucInstruction(156, "L P[10] 500mm/sec CNT20    ;"),
    FanucInstruction(157, "L P[44] 500mm/sec CNT50    ;"),
    FanucInstruction(158, "L P[43] 500mm/sec CNT50    ;"),
    FanucInstruction(159, "L P[41] 1000mm/sec CNT70    ;"),
    FanucInstruction(160, "J P[40] 75% CNT70    ;"),
    FanucInstruction(161, "J P[39] 75% CNT70    ;"),
    FanucInstruction(162, "J P[39] 75% CNT70    ;"),
    FanucInstruction(163, "L P[138] 500mm/sec CNT70    ;"),
    FanucInstruction(164, "L P[38] 1500mm/sec CNT70    ;"),
    FanucInstruction(165, "L P[37] 500mm/sec CNT70    ;"),
    FanucInstruction(166, "L P[36] 500mm/sec CNT70    ;"),
    FanucInstruction(167, ";"),
    FanucInstruction(168, "L P[35:ID1408_ap] 500mm/sec CNT50 SPOT[SD=3,P=12,S=22,ED=3]    ;"),
    FanucInstruction(169, "!SPOT 11 ;"),
    FanucInstruction(170, "WAIT   1.00(sec) ;"),
    FanucInstruction(171, "L P[34:ID1424_ap] 500mm/sec CNT50 SPOT[SD=3,P=17,S=104,ED=3]    ;"),
    FanucInstruction(172, "!SPOT 10 ;"),
    FanucInstruction(173, ";"),
    FanucInstruction(174, "L P[81:ID1424_ap] 500mm/sec CNT50 SPOT[SD=3,P=12,S=22,ED=3]    ;"),
    FanucInstruction(175, "!SPOT 9 ;"),
    FanucInstruction(176, "WAIT   1.00(sec) ;"),
    FanucInstruction(177, "L P[33] 500mm/sec CNT50    ;"),
    FanucInstruction(178, "L P[32] 500mm/sec CNT50    ;"),
    FanucInstruction(179, "L P[31] 500mm/sec CNT50    ;"),
    FanucInstruction(180, "L P[30] 500mm/sec CNT70    ;"),
    FanucInstruction(181, "L P[29] 500mm/sec CNT70    ;"),
    FanucInstruction(182, "L P[28] 500mm/sec CNT50    ;"),
    FanucInstruction(183, "L P[100] 500mm/sec CNT30    ;"),
    FanucInstruction(184, "L P[7] 1500mm/sec CNT70    ;"),
    FanucInstruction(185, "L P[123] 1500mm/sec CNT70    ;"),
    FanucInstruction(186, "L P[5] 500mm/sec CNT100    ;"),
    FanucInstruction(187, "DO[2]=ON ;"),
    FanucInstruction(188, ";"),
    FanucInstruction(189, "J P[4] 100% CNT100    ;"),
    FanucInstruction(190, "J P[3] 100% CNT100    ;"),
    FanucInstruction(191, ";"),
    FanucInstruction(192, "DO[33]=ON ;"),
    FanucInstruction(193, "DO[1]=PULSE,1.0sec ;"),
    FanucInstruction(194, "DO[20]=ON ;"),
    FanucInstruction(195, "DO[2]=OFF ;"),
    FanucInstruction(196, "DO[98]=OFF ;"),
    FanucInstruction(197, ";"),
    FanucInstruction(198, "TIMER[1]=STOP ;"),
    FanucInstruction(199, "J P[2] 75% CNT50    ;"),
    FanucInstruction(200, "J P[1] 75% CNT70    ;"),
    FanucInstruction(201, ";"),
    FanucInstruction(202, "DO[33]=ON ;"),
    FanucInstruction(203, "DO[34]=ON ;"),
    FanucInstruction(204, "DO[36]=ON ;"),
    FanucInstruction(205, "DO[41]=ON ;"),
    FanucInstruction(206, "DO[42]=ON ;"),
    FanucInstruction(207, "DO[44]=ON ;"),
    FanucInstruction(208, "DO[45]=ON ;"),
    FanucInstruction(209, ";"),
    FanucInstruction(210, "DO[1]=OFF ;"),
    FanucInstruction(211, "DO[2]=OFF ;"),
    FanucInstruction(212, "DO[3]=OFF ;"),
    FanucInstruction(213, "DO[4]=OFF ;"),
    FanucInstruction(214, "DO[98]=OFF ;"),
    FanucInstruction(215, ";"),
    FanucInstruction(216, "DO[20]=ON ;"),
    FanucInstruction(217, ";"),
    FanucInstruction(218, "CALL _TEST_CT    ;"),
    FanucInstruction(219, ";"),
    FanucInstruction(220, "J PR[3] 50% FINE    ;"),
    FanucInstruction(221, ";"),
    FanucInstruction(222, "OVERRIDE=100% ;"),
    FanucInstruction(223, "UFRAME_NUM=0 ;"),
    FanucInstruction(224, "UTOOL_NUM=1 ;"),
    FanucInstruction(225, "PAYLOAD[1] ;"),
]

# Original /POS section retained for reference.
# Teach and validate all positions on the actual robot cell.
POSITIONS_LS_REFERENCE = r"""
P[1]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -29.998 deg,	J2=   -24.590 deg,	J3=    30.779 deg,
	J4=    23.272 deg,	J5=  -102.789 deg,	J6=  -128.517 deg
   GP2:
	UF : 0, UT : 1,	
	J1=    -3.000  mm
};
P[2]{
   GP1:
	UF : 0, UT : 1,	
	J1=     5.402 deg,	J2=   -42.917 deg,	J3=    25.505 deg,
	J4=    34.695 deg,	J5=   -75.099 deg,	J6=   -77.709 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -50.000  mm
};
P[3]{
   GP1:
	UF : 0, UT : 1,	
	J1=     2.482 deg,	J2=   -47.461 deg,	J3=     2.002 deg,
	J4=    51.029 deg,	J5=   -18.581 deg,	J6=   -45.957 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -50.000  mm
};
P[4]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -25.244 deg,	J2=   -45.726 deg,	J3=    -8.128 deg,
	J4=    80.810 deg,	J5=    27.029 deg,	J6=   -76.061 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -50.000  mm
};
P[5]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -54.812 deg,	J2=   -36.773 deg,	J3=   -13.134 deg,
	J4=    88.105 deg,	J5=    71.274 deg,	J6=   -78.017 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -120.000  mm
};
P[6]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2423.526  mm,	Y =  1213.033  mm,	Z =   497.385  mm,
	W =    -3.461 deg,	P =     -.902 deg,	R =    52.460 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -82.231  mm
};
P[7]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -19.736 deg,	J2=   -50.386 deg,	J3=   -13.430 deg,
	J4=    79.387 deg,	J5=    50.935 deg,	J6=   -73.626 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -181.855  mm
};
P[8:"ID1789_a"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2481.460  mm,	Y =  1427.494  mm,	Z =   528.880  mm,
	W =      .780 deg,	P =    -5.511 deg,	R =    44.921 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.164  mm
};
P[9]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2494.376  mm,	Y =  1421.284  mm,	Z =   519.884  mm,
	W =      .000 deg,	P =    -4.999 deg,	R =    45.000 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -76.680  mm
};
P[10]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2454.877  mm,	Y =  1141.022  mm,	Z =   522.968  mm,
	W =    -3.426 deg,	P =     1.090 deg,	R =    50.059 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -100.000  mm
};
P[11]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, -1, 1',
	X =  2444.517  mm,	Y =  1123.174  mm,	Z =   517.754  mm,
	W =   -16.791 deg,	P =    -6.607 deg,	R =    23.150 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -128.777  mm
};
P[12:"ID1410_a"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, -1, 1',
	X =  2424.986  mm,	Y =  1122.992  mm,	Z =   542.910  mm,
	W =   -20.421 deg,	P =    -6.611 deg,	R =    23.169 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -10.868  mm
};
P[13:"ID1410_a"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, -1, 1',
	X =  2423.563  mm,	Y =  1155.255  mm,	Z =   533.708  mm,
	W =    -7.966 deg,	P =    -8.833 deg,	R =    21.909 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -11.151  mm
};
P[14]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, -1, 1',
	X =  2447.738  mm,	Y =  1160.582  mm,	Z =   508.529  mm,
	W =    -7.432 deg,	P =    -5.635 deg,	R =    21.191 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -128.777  mm
};
P[15:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2628.179  mm,	Y =  2161.657  mm,	Z =   390.387  mm,
	W =      .019 deg,	P =      .338 deg,	R =    44.963 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -35.499  mm
};
P[16]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2628.425  mm,	Y =  2598.684  mm,	Z =   397.611  mm,
	W =      .101 deg,	P =      .747 deg,	R =    46.198 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -70.605  mm
};
P[17]{
   GP1:
	UF : 0, UT : 1,	
	J1=    -5.001 deg,	J2=   -34.999 deg,	J3=    33.113 deg,
	J4=     -.001 deg,	J5=  -100.004 deg,	J6=   -79.997 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -50.000  mm
};
P[18]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2428.090  mm,	Y =  1294.046  mm,	Z =   528.539  mm,
	W =     1.455 deg,	P =    -4.231 deg,	R =    49.934 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -67.367  mm
};
P[19]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2529.677  mm,	Y =  2600.835  mm,	Z =   397.269  mm,
	W =      .107 deg,	P =      .475 deg,	R =    54.660 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -41.163  mm
};
P[20]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2425.235  mm,	Y =  1249.114  mm,	Z =   530.162  mm,
	W =     1.301 deg,	P =    -4.124 deg,	R =    49.388 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -93.869  mm
};
P[21]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2423.607  mm,	Y =  1212.999  mm,	Z =   537.255  mm,
	W =    -3.461 deg,	P =     -.902 deg,	R =    52.460 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -82.231  mm
};
P[22]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2639.998  mm,	Y =  1993.299  mm,	Z =   313.724  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -186.983  mm
};
P[23]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2518.946  mm,	Y =  1993.299  mm,	Z =   317.756  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -186.983  mm
};
P[25]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2454.154  mm,	Y =  1694.452  mm,	Z =   331.214  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -275.000  mm
};
P[26]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2646.700  mm,	Y =  2154.850  mm,	Z =   323.535  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -275.000  mm
};
P[27:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2628.179  mm,	Y =  2055.675  mm,	Z =   394.241  mm,
	W =      .019 deg,	P =      .338 deg,	R =    44.963 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -37.946  mm
};
P[28]{
   GP1:
	UF : 0, UT : 1,	
	J1=     8.073 deg,	J2=   -30.719 deg,	J3=   -25.959 deg,
	J4=    33.116 deg,	J5=    30.169 deg,	J6=   -29.428 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -200.801  mm
};
P[29]{
   GP1:
	UF : 0, UT : 1,	
	J1=    24.754 deg,	J2=   -42.659 deg,	J3=   -19.963 deg,
	J4=   -22.148 deg,	J5=    21.405 deg,	J6=    20.743 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -212.630  mm
};
P[30]{
   GP1:
	UF : 0, UT : 1,	
	J1=    39.586 deg,	J2=   -54.504 deg,	J3=   -17.636 deg,
	J4=   -50.665 deg,	J5=    33.693 deg,	J6=    48.018 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -200.000  mm
};
P[31]{
   GP1:
	UF : 0, UT : 1,	
	J1=    31.594 deg,	J2=   -45.734 deg,	J3=   -11.804 deg,
	J4=   -65.931 deg,	J5=    14.182 deg,	J6=    91.539 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -265.019  mm
};
P[32]{
   GP1:
	UF : 0, UT : 1,	
	J1=    29.365 deg,	J2=   -30.128 deg,	J3=   -20.095 deg,
	J4=   -37.581 deg,	J5=    17.741 deg,	J6=    62.747 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -265.019  mm
};
P[33]{
   GP1:
	UF : 0, UT : 1,	
	J1=    31.239 deg,	J2=   -29.873 deg,	J3=   -17.075 deg,
	J4=   -49.036 deg,	J5=    16.758 deg,	J6=    74.113 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -124.492  mm
};
P[34:"ID1424_ap"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'F U T, 0, 0, 0',
	X =  2469.642  mm,	Y =  1038.027  mm,	Z =   574.961  mm,

	W =   -24.177 deg,	P =     3.699 deg,	R =    19.531 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -33.925  mm
};
P[35:"ID1408_ap"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'F U T, 0, 0, 0',
	X =  2441.033  mm,	Y =  1073.883  mm,	Z =   557.752  mm,
	W =   -24.950 deg,	P =     3.447 deg,	R =    19.553 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -35.237  mm
};
P[36]{
   GP1:
	UF : 0, UT : 1,	
	J1=    29.369 deg,	J2=   -30.990 deg,	J3=   -22.643 deg,
	J4=   -27.771 deg,	J5=    21.422 deg,	J6=    50.432 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -244.630  mm
};
P[37]{
   GP1:
	UF : 0, UT : 1,	
	J1=    26.768 deg,	J2=   -42.149 deg,	J3=   -10.983 deg,
	J4=   -56.865 deg,	J5=     6.866 deg,	J6=    74.992 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -215.990  mm
};
P[38]{
   GP1:
	UF : 0, UT : 1,	
	J1=    27.476 deg,	J2=   -46.569 deg,	J3=   -11.002 deg,
	J4=   -58.302 deg,	J5=     9.637 deg,	J6=    68.378 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -271.270  mm
};
P[39]{
   GP1:
	UF : 0, UT : 1,	
	J1=    32.619 deg,	J2=   -54.436 deg,	J3=     1.002 deg,
	J4=  -125.006 deg,	J5=    18.427 deg,	J6=   127.310 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -220.000  mm
};
P[40]{
   GP1:
	UF : 0, UT : 1,	
	J1=     4.572 deg,	J2=   -54.004 deg,	J3=   -16.998 deg,
	J4=  -128.797 deg,	J5=   -30.579 deg,	J6=   134.586 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -220.000  mm
};
P[41]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -18.630 deg,	J2=   -43.535 deg,	J3=   -27.802 deg,
	J4=  -105.721 deg,	J5=   -67.911 deg,	J6=   126.506 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -260.000  mm
};
P[42]{
   GP1:
	UF : 0, UT : 1,	
	J1=      .251 deg,	J2=    -6.779 deg,	J3=   -36.549 deg,
	J4=  -120.254 deg,	J5=   -61.677 deg,	J6=   134.452 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[43]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -13.099 deg,	J2=   -11.899 deg,	J3=   -31.174 deg,
	J4=  -103.797 deg,	J5=   -66.452 deg,	J6=   147.020 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -241.619  mm
};
P[44]{
   GP1:
	UF : 0, UT : 1,	
	J1=    -6.993 deg,	J2=    -5.367 deg,	J3=   -31.653 deg,
	J4=  -107.787 deg,	J5=   -61.779 deg,	J6=   149.924 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -205.291  mm
};
P[48]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2369.357  mm,	Y =  1431.871  mm,	Z =   333.210  mm,
	W =      .002 deg,	P =    -3.338 deg,	R =    41.363 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -275.520  mm
};
P[51]{
   GP1:
	UF : 0, UT : 1,	
	J1=    -8.455 deg,	J2=   -50.117 deg,	J3=    26.846 deg,
	J4=    -9.713 deg,	J5=   -74.601 deg,	J6=   -47.795 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -50.000  mm
};
P[52]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2635.680  mm,	Y =  2161.669  mm,	Z =   377.454  mm,
	W =      .019 deg,	P =      .337 deg,	R =    44.963 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -67.987  mm
};
P[53]{
   GP1:
	UF : 0, UT : 1,	
	J1=    14.052 deg,	J2=    -7.972 deg,	J3=   -43.718 deg,
	J4=  -145.038 deg,	J5=   -53.068 deg,	J6=   155.487 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -200.551  mm
};
P[54]{
   GP1:
	UF : 0, UT : 1,	
	J1=    16.101 deg,	J2=   -14.047 deg,	J3=   -42.177 deg,
	J4=  -146.730 deg,	J5=   -50.952 deg,	J6=   155.967 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -200.551  mm
};
P[55]{
   GP1:
	UF : 0, UT : 1,	
	J1=    15.992 deg,	J2=   -17.620 deg,	J3=   -36.820 deg,
	J4=  -143.927 deg,	J5=   -46.591 deg,	J6=   151.823 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -108.987  mm
};
P[56:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2360.845  mm,	Y =  1424.379  mm,	Z =   527.519  mm,
	W =      .002 deg,	P =    -3.338 deg,	R =    41.363 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -42.364  mm
};
P[59]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -19.877 deg,	J2=   -50.701 deg,	J3=     1.611 deg,
	J4=   -72.850 deg,	J5=   -66.270 deg,	J6=    81.397 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -50.000  mm
};
P[60]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -11.312 deg,	J2=   -43.531 deg,	J3=    26.567 deg,
	J4=   -17.747 deg,	J5=   -85.928 deg,	J6=   -21.157 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -50.000  mm
};
P[66:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2536.875  mm,	Y =  2057.099  mm,	Z =   395.140  mm,
	W =      .001 deg,	P =      .000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -27.714  mm
};
P[68:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2536.875  mm,	Y =  2159.623  mm,	Z =   395.140  mm,
	W =      .001 deg,	P =      .000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -27.714  mm
};
P[69]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2518.590  mm,	Y =  2556.626  mm,	Z =   382.080  mm,
	W =      .067 deg,	P =      .401 deg,	R =    51.890 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -63.417  mm
};
P[70:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2529.987  mm,	Y =  2291.114  mm,	Z =   391.579  mm,
	W =      .027 deg,	P =      .486 deg,	R =    44.952 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -35.318  mm
};
P[72]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2445.850  mm,	Y =  1127.801  mm,	Z =   504.132  mm,
	W =   -13.494 deg,	P =    -2.860 deg,	R =    30.397 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -138.910  mm
};
P[73]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, -1, 1',
	X =  2442.182  mm,	Y =  1117.037  mm,	Z =   530.043  mm,
	W =   -16.791 deg,	P =    -6.606 deg,	R =    23.149 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -34.000  mm
};
P[76]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2513.283  mm,	Y =  1987.252  mm,	Z =   309.272  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -251.846  mm
};
P[78]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2178.453  mm,	Y =  1649.523  mm,	Z =   320.271  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -275.000  mm
};
P[79]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2178.454  mm,	Y =  1353.838  mm,	Z =   359.630  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -220.000  mm
};
P[80]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2505.220  mm,	Y =  1813.680  mm,	Z =   309.273  mm,
	W =      .001 deg,	P =     -.000 deg,	R =    45.005 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -264.250  mm
};
P[81:"ID1424_ap"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'F U T, 0, 0, 0',
	X =  2505.594  mm,	Y =  1040.968  mm,	Z =   578.470  mm,
	W =   -27.602 deg,	P =     5.765 deg,	R =    18.599 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -28.567  mm
};
P[84]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2645.479  mm,	Y =  2293.780  mm,	Z =   319.948  mm,
	W =      .019 deg,	P =      .338 deg,	R =    44.963 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -226.941  mm
};
P[87:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2535.363  mm,	Y =  2327.016  mm,	Z =   391.579  mm,
	W =      .027 deg,	P =      .486 deg,	R =    44.952 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -35.318  mm
};
P[88]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2534.507  mm,	Y =  2196.344  mm,	Z =   369.100  mm,
	W =      .019 deg,	P =      .338 deg,	R =    44.963 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -202.198  mm
};
P[89]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2534.507  mm,	Y =  2314.037  mm,	Z =   369.101  mm,
	W =      .019 deg,	P =      .338 deg,	R =    44.963 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -153.409  mm
};
P[91:"ID1788"]{

   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2628.550  mm,	Y =  2326.444  mm,	Z =   392.355  mm,
	W =      .101 deg,	P =      .747 deg,	R =    46.198 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -22.881  mm
};
P[92:"ID1788"]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2629.988  mm,	Y =  2291.308  mm,	Z =   392.355  mm,
	W =      .101 deg,	P =      .747 deg,	R =    46.198 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -36.626  mm
};
P[95]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2468.326  mm,	Y =  1335.450  mm,	Z =   480.226  mm,
	W =      .000 deg,	P =    -2.999 deg,	R =    45.001 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -85.402  mm
};
P[100]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'F U T, 0, 0, 0',
	X =  2425.361  mm,	Y =   803.795  mm,	Z =   491.247  mm,
	W =      .071 deg,	P =     1.378 deg,	R =    29.782 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -243.821  mm
};
P[101]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2535.363  mm,	Y =  2379.813  mm,	Z =   391.579  mm,
	W =      .027 deg,	P =      .486 deg,	R =    44.952 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -35.318  mm
};
P[102]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2535.363  mm,	Y =  2436.642  mm,	Z =   391.579  mm,
	W =      .027 deg,	P =      .486 deg,	R =    44.952 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -35.318  mm
};
P[103]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2532.868  mm,	Y =  2486.752  mm,	Z =   391.579  mm,
	W =      .027 deg,	P =      .486 deg,	R =    44.952 deg
   GP2:
	UF : 0, UT : 1,	
	J1=    -8.995  mm
};
P[109]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2523.778  mm,	Y =  2601.606  mm,	Z =   332.923  mm,
	W =      .076 deg,	P =      .404 deg,	R =    53.481 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -150.074  mm
};
P[110]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2633.084  mm,	Y =  2597.551  mm,	Z =   332.461  mm,
	W =      .028 deg,	P =      .752 deg,	R =    49.886 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -148.825  mm
};
P[112]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2628.552  mm,	Y =  2496.071  mm,	Z =   392.354  mm,
	W =      .101 deg,	P =      .747 deg,	R =    46.198 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -22.881  mm
};
P[113]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2628.551  mm,	Y =  2438.184  mm,	Z =   392.354  mm,
	W =      .101 deg,	P =      .747 deg,	R =    46.198 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -22.881  mm
};
P[114]{
   GP1:
	UF : 0, UT : 1,		CONFIG : 'N U T, 0, 0, 0',
	X =  2628.550  mm,	Y =  2383.178  mm,	Z =   392.354  mm,
	W =      .101 deg,	P =      .747 deg,	R =    46.198 deg
   GP2:
	UF : 0, UT : 1,	
	J1=   -22.881  mm
};
P[123]{
   GP1:
	UF : 0, UT : 1,	
	J1=   -37.311 deg,	J2=   -42.666 deg,	J3=   -16.403 deg,
	J4=    83.104 deg,	J5=    65.244 deg,	J6=   -73.082 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -183.296  mm
};
P[138]{
   GP1:
	UF : 0, UT : 1,	
	J1=    27.476 deg,	J2=   -46.569 deg,	J3=   -11.002 deg,
	J4=   -58.302 deg,	J5=     9.637 deg,	J6=    68.378 deg
   GP2:
	UF : 0, UT : 1,	
	J1=  -271.270  mm
};
"""


def show_program_summary() -> None:
    """Print a compact summary of the imported FANUC program."""
    print(f"Program: {PROGRAM_NAME}")
    print(f"Controller context: {CONTROLLER_CONTEXT}")
    print(f"Instructions imported: {len(INSTRUCTIONS)}")
    print("Instruction categories:")
    categories = {
        "joint_moves": 0,
        "linear_moves": 0,
        "spot_commands": 0,
        "digital_io": 0,
        "waits": 0,
        "timers": 0,
        "other": 0,
    }

    for instruction in INSTRUCTIONS:
        command = instruction.source.upper()
        if command.startswith("J "):
            categories["joint_moves"] += 1
        elif command.startswith("L "):
            categories["linear_moves"] += 1
        elif "SPOT[" in command:
            categories["spot_commands"] += 1
        elif "DO[" in command:
            categories["digital_io"] += 1
        elif command.startswith("WAIT"):
            categories["waits"] += 1
        elif "TIMER[" in command:
            categories["timers"] += 1
        else:
            categories["other"] += 1

    for name, count in categories.items():
        print(f"  {name}: {count}")


def print_instructions() -> None:
    """Display the FANUC instruction list with original line numbers."""
    for instruction in INSTRUCTIONS:
        print(f"{instruction.line:>3}: {instruction.source}")


if __name__ == "__main__":
    show_program_summary()
    print("\nImported FANUC instruction sequence:")
    print_instructions()
