******************************************************************
  * Author:Srinjoy Bhuiya                                         *
  * Date:2015, Dec the 12th                                       *
  * Purpose:FizzBuzz,                                             *
  *                                                               *
  ******************************************************************
   IDENTIFICATION DIVISION.
  *-*-*-*-*-*-*-*-*-*-*-*-*-
   PROGRAM-ID. FIZZBUZZ.
  *-*-*-*-*-*-*-*-*-*-*--
   ENVIRONMENT DIVISION.
  *-*-*-*-*-*-*-*-*-*-*--
   CONFIGURATION SECTION.
  *----------------------
   INPUT-OUTPUT SECTION.
  *----------------------
   DATA DIVISION.
  *-*-*-*-*-*-*-*-
   FILE SECTION.
  *-------------------------
   WORKING-STORAGE SECTION.
  *-------------------------
   01  WS-DATA.
       05  WS-COUNTS.
           10  WS-FIRST        PIC 9(4)    VALUE ZERO.
           10  WS-LAST         PIC 9(4)    VALUE 20.
           10  WS-POSN         PIC 9(4).
       05  WS-RESULTS.
           10  WS-RS00         PIC 9(4).
           10  WS-RM05         PIC 9(4).
               88  WS-ML05                 VALUE ZERO.
           10  WS-RM03         PIC 9(4).
               88  WS-ML03                 VALUE ZERO.
       05  WS-DISPLAY-STRING   PIC X(10).
       05  WS-DISPLAY-NUM REDEFINES WS-DISPLAY-STRING.
           10  WS-FIZZBUZZ-PRI PIC X(3).
           10  WS-FIZZBUZZ-INT PIC Z(3)9.
           10  WS-FIZZBUZZ-SUI PIC X(3).
       05  WS-DISPLAY-ALPHA REDEFINES WS-DISPLAY-STRING.
           10  WS-FIZZBUZZ-STR PIC X(10).
               88  WS-IS-OTHER             VALUE "*  0000  *".
               88  WS-IS-FIZZ              VALUE "*  FIZZ  *".
               88  WS-IS-BUZZ              VALUE "*  BUZZ  *".
               88  WS-IS-FIZZBUZZ          VALUE "*FIZZBUZZ*".

  *-*-*-*-*-*-*-*-*-*-*
   PROCEDURE DIVISION.
  *-*-*-*-*-*-*-*-*-*-*
   MAIN-PROCEDURE.
        PERFORM    10000-BEGIN
        PERFORM    20000-MAIN
           VARYING WS-POSN FROM WS-FIRST BY 1
             UNTIL WS-POSN > WS-LAST
        PERFORM    30000-END
        .
        STOP RUN.
  *
   10000-BEGIN.
       DISPLAY "**********"
       .
  *
   20000-MAIN.
       PERFORM 40000-COMPUTE-FIZZBUZZ
       DISPLAY WS-DISPLAY-STRING
       .
  *
   30000-END.
       DISPLAY "**********"
       .
  *
   40000-COMPUTE-FIZZBUZZ.
       DIVIDE WS-POSN BY 5 GIVING WS-RS00 REMAINDER WS-RM05
       DIVIDE WS-POSN BY 3 GIVING WS-RS00 REMAINDER WS-RM03
       EVALUATE TRUE
           WHEN (WS-ML05 AND WS-ML03)
               SET WS-IS-FIZZBUZZ  TO TRUE
           WHEN WS-ML05
               SET WS-IS-BUZZ      TO TRUE
           WHEN WS-ML03
               SET WS-IS-FIZZ      TO TRUE
           WHEN OTHER
               SET WS-IS-OTHER     TO TRUE
               MOVE WS-POSN        TO WS-FIZZBUZZ-INT
       END-EVALUATE
       .
  *
   END PROGRAM FIZZBUZZ.