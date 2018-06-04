[['F', 'main'],
 ['D', '_', '_', 'a'],
 ['=', '1', '_', 'pausezone0'],
 ['=', 'pausezone0', '_', 'a'],
 ['=', 'a', '_', 'pausezone0'],
 ['*', 'pausezone0', '2', 'pausezone0'],
 ['=', '8', '_', 'pausezone1'],
 ['-', 'pausezone1', '6', 'pausezone1'],
 ['=', '3', '_', 'pausezone2'],
 ['*', 'pausezone2', 'pausezone1', 'pausezone2'],
 ['+', 'pausezone0', 'pausezone2', 'pausezone0'],
 ['=', 'pausezone0', '_', 'a'],
 ['=', 'a', '_', 'pausezone0'],
 ['=', 'pausezone0', '_', 'parazone1'],
 ['=', '1', '_', 'pausezone0'],
 ['=', 'pausezone0', '_', 'parazone2'],
 ['CMP', 'parazone1', 'parazone2', '_'],
 ['JA', '_', '_', 'ETRUE0'],
 ['JMP', '_', '_', 'EFALSE0'],
 ['L', '_', '_', 'ETRUE0'],
 ['=', '1', '_', 'pausezone0'],
 ['=', 'pausezone0', '_', 'a'],
 ['JMP', '_', '_', 'ENEXT0'],
 ['L', '_', '_', 'EFALSE0'],
 ['=', '2', '_', 'pausezone0'],
 ['=', 'pausezone0', '_', 'a'],
 ['L', '_', '_', 'ENEXT0'],
 ['=', '2', '_', 'parazone0'],
 ['=', 'a', '_', 'pausezone0'],
 ['=', 'pausezone0', '_', 'parazone1'],
 ['=', '2', '_', 'pausezone0'],
 ['+', 'pausezone0', '3', 'pausezone0'],
 ['=', 'pausezone0', '_', 'parazone2'],
 ['C', '_', '_', 'fool'],
 ['=', 'parazone1', '_', 'pausezone1'],
 ['=', 'pausezone1', '_', 'pausezone2'],
 ['=', 'pausezone2', '_', 'a'],
 ['=', 'a', '_', 'pausezone0'],
 ['=', '1', '_', 'parazone0'],
 ['=', 'pausezone0', '_', 'parazone1'],
 ['R', '_', '_', '_'],
 ['F', 'a', 'b', 'fool'],
 ['=', 'parazone1', '_', 'a'],
 ['D', '_', '_', 'a'],
 ['=', 'parazone2', '_', 'b'],
 ['D', '_', '_', 'b'],
 ['=', 'a', '_', 'pausezone0'],
 ['+', 'pausezone0', 'b', 'pausezone0'],
 ['=', '1', '_', 'parazone0'],
 ['=', 'pausezone0', '_', 'parazone1'],
 ['R', '_', '_', '_']]
DATA     SEGMENT
a    DB  ?
b    DB  ?
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
    
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      pausezone0,1
	MOV      AL,pausezone0
	MOV      parazone2,AL
	MOV      AL,parazone1
	CMP      AL,parazone2
	JA       ETRUE0
	JMP      EFALSE0
	ETRUE0:
	MOV      pausezone0,1
	MOV      AL,pausezone0
	MOV      a,AL
	JMP      ENEXT0
	EFALSE0:
	MOV      pausezone0,2
	MOV      AL,pausezone0
	MOV      a,AL
	ENEXT0:
    
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
