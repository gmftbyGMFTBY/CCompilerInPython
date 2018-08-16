DATA     SEGMENT
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

	MOV      pausezone0,a
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      pausezone0,5
	MOV      AL,pausezone0
	MOV      parazone2,AL
	MOV    AL,parazone1
	CMP    AL,parazone2
	JZ    ETRUE1
	JMP    EFALSE1
	ETRUE1:
	EBEGIN0:
	MOV      pausezone0,a
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      pausezone0,20
	MOV      AL,pausezone0
	MOV      parazone2,AL
	MOV    AL,parazone1
	CMP    AL,parazone2
	JB    ETRUE0
	JMP    EFALSE0
	ETRUE0:
	MOV      pausezone0,a
	ADD      pausezone0,1
something wrong with the mov command, ['=', 'pausezone0', '_', 'a']
