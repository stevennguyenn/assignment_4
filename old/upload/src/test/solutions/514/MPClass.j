.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	putstatic MPClass/a I
Label2:
	getstatic MPClass/a I
	iconst_5
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MPClass/a I
	iconst_1
	iadd
	putstatic MPClass/a I
	goto Label2
Label3:
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
