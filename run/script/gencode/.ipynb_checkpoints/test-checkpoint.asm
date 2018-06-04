DATA     SEGMENT
c    DB  ?
d    DB  ?
count    DB  ?
b    DB  ?
a    DB  ?
w    DB  ?
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
	MOV    AL,parazone1
	CMP    AL,parazone2
	JA    ETRUE0
	JMP    EFALSE0
	ETRUE0:
	MOV      pausezone0,1
	MOV      AL,pausezone0
	MOV      a,AL
	JMP    ENEXT0
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
	MOV      AL,pausezone0
	MOV      parazone2,AL
	CALL     FOOL
	MOV      AL,parazone1
	MOV      pausezone1,AL
	MOV      AL,pausezone1
	MOV      pausezone2,AL
	MOV      AL,pausezone2
	MOV      a,AL
	MOV      pausezone0,2
	MOV      AL,pausezone0
	MOV      b,AL
	EBEGIN2:
	MOV      AL,b
	MOV      pausezone0,AL
	MOV    AL,0
	CMP    AL,pausezone0
	JNZ    ETRUE2
	JMP    EFALSE2
	ETRUE2:
	MOV      AL,b
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      pausezone0,1
	MOV      AL,pausezone0
	MOV      parazone2,AL
	MOV    AL,parazone1
	CMP    AL,parazone2
	JZ    ETRUE1
	JMP    EFALSE1
	ETRUE1:
	MOV      AL,a
	MOV      pausezone0,AL
	ADD      pausezone0,2
	MOV      AL,pausezone0
	MOV      a,AL
	JMP    ENEXT1
	EFALSE1:
	MOV      AL,a
	MOV      pausezone0,AL
	SUB      pausezone0,2
	MOV      AL,pausezone0
	MOV      a,AL
	MOV      parazone0,2
	MOV      pausezone0,1
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      pausezone0,1
	MOV      AL,pausezone0
	MOV      parazone2,AL
	CALL     FOOL
	MOV      AL,parazone1
	MOV      pausezone1,AL
	MOV      AL,a
	MOV      pausezone2,AL
	MOV      AL,pausezone2
	ADD      AL,pausezone1
	MOV      pausezone2,AL
	MOV      AL,pausezone2
	MOV      a,AL
	ENEXT1:
	MOV      AL,b
	MOV      pausezone0,AL
	SUB      pausezone0,1
	MOV      AL,pausezone0
	MOV      b,AL
	JMP    EBEGIN2
	EFALSE2:
	MOV      AL,a
	MOV      pausezone0,AL
	MOV      parazone0,1
	MOV      AL,pausezone0
	MOV      parazone1,AL
    
    mov ah,2
    add al,30h
    mov dl,al
    int 21h
	RET
MAIN    ENDP

FOOL     PROC
	MOV      AL,parazone1
	MOV      c,AL
	MOV      AL,parazone2
	MOV      d,AL
	MOV      pausezone0,0
	MOV      AL,pausezone0
	MOV      count,AL
	MOV      pausezone0,0
	MOV      AL,pausezone0
	MOV      w,AL
	LL13:
	MOV      AL,w
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      parazone1,AL
	MOV      AL,c
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      parazone2,AL
	MOV    AL,parazone1
	CMP    AL,parazone2
	JNA    LL23
	JMP    LL33
	LL43:
	MOV      AL,w
	MOV      pausezone0,AL
	ADD      pausezone0,1
	MOV      AL,pausezone0
	MOV      w,AL
	JMP    LL13
	LL23:
	MOV      AL,count
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	ADD      AL,d
	MOV      pausezone0,AL
	MOV      AL,pausezone0
	MOV      count,AL
	JMP    LL43
	LL33:
	MOV      AL,count
	MOV      pausezone0,AL
	MOV      parazone0,1
	MOV      AL,pausezone0
	MOV      parazone1,AL
	RET
FOOL     ENDP

CODE     ENDS
		END     MAIN
