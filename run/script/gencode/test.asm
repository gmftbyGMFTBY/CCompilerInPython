DATA     SEGMENT
b    DB  ?
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
parazone0     DB      ?
parazone1     DB      ?
parazone2     DB      ?
parazone3     DB      ?
parazone4     DB      ?
parazone5     DB      ?
parazone6     DB      ?
parazone7     DB      ?
parazone8     DB      ?
parazone9     DB      ?
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
	MOV      BL,2
	MUL      BL
	MOV      pausezone0, AL
	MOV      pausezone1,8
	SUB      pausezone1,6
	MOV      pausezone2,3
	MOV      AL,pausezone2
	MOV      BL,pausezone1
	MUL      BL
	MOV      pausezone2, AL
	MOV      AL,pausezone0
	ADD      AL,pausezone2
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      a,AL
	MOV      parazone0,2
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      pausezone0,2
	ADD      pausezone0,3
	MOV      AL,pausezone0
	MOV      parazone2,AL
	CALL     FOOL
	MOV      AL,parazone1
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
	RET
MAIN    ENDP

FOOL     PROC
	MOV      AL,parazone1
	MOV      a,AL
	MOV      AL,parazone2
	MOV      b,AL
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	ADD      AL,b
	MOV      pausezone0,AL
	MOV      parazone0,1
	MOV      AL,pausezone0
	MOV      parazone1,AL
	RET
FOOL     ENDP

CODE     ENDS
		END     MAIN
