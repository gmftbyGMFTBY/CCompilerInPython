DATA     SEGMENT
a    DB  ?
pausezone0    DB      ?
pausezone1    DB      ?
pausezone2    DB      ?
pausezone3    DB      ?
pausezone4    DB      ?
pausezone5    DB      ?
pausezone6    DB      ?
pausezone7    DB      ?
pausezone8    DB      ?
pausezone9    DB      ?
parazone0     DW      ?
parazone1     DW      ?
parazone2     DW      ?
parazone3     DW      ?
parazone4     DW      ?
parazone5     DW      ?
parazone6     DW      ?
parazone7     DW      ?
parazone8     DW      ?
parazone9     DW      ?
DATA     ENDS

CODE     SEGMENT
MAIN    PROC    FAR
	ASSUME  CS:CODE,DS:DATA,ES:NOTHING
	PUSH    DS
	XOR     AX,AX
	PUSH    AX
	MOV     AX,DATA
	MOV     DS,AX
	MOV      pausezone0,1
	MOV      AL,pausezone0
	MOV      a,AL
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      BL,pausezone0
	MUL      BL
	MOV      pausezone0, AX
	MOV      pausezone1,8
	MOV      AL,pausezone1
	SUB      AL,pausezone1
	MOV      pausezone1,AX
	MOV      pausezone2,3
	MOV      AL,pausezone2
	MOV      BL,pausezone2
	MUL      BL
	MOV      pausezone2, AX
	MOV      AL,pausezone0
	ADD      AL,pausezone0
	MOV      pausezone0,AX
	MOV      AL,pausezone0
	MOV      a,AL
	MOV      parazone0,2
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      pausezone0,2
	MOV      AL,pausezone0
	ADD      AL,pausezone0
	MOV      pausezone0,AX
	MOV      AL,pausezone0
	MOV      parazone2,AL
	CALL     ADD
	MOV      AL,parazone0
	MOV      pausezone1,AL
	MOV      AL,pausezone1
	MOV      pausezone2,AL
	MOV      AL,pausezone2
	MOV      a,AL
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      parazone0,1
	MOV      AL,pausezone0
	MOV      parazone1,AL
MAIN    ENDP

ADD     PROC
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	ADD      AL,pausezone0
	MOV      pausezone0,AX
	MOV      parazone0,1
	MOV      AL,pausezone0
	MOV      parazone1,AL
ADD     ENDP