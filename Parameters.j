.source Parameters.src
.class  public Parameters
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static sum(II)V
    ; c = a + b
    iload 0
    iload 1
    iadd
    istore 2

    ; print(c)
    
    getstatic java/lang/System/out Ljava/io/PrintStream;
    iload 2
    invokevirtual java/io/PrintStream/print(I)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    return
.limit locals 3
.limit stack  2
.end method

.method public static main([Ljava/lang/String;)V
    ; x = 3
    ldc 3
    istore 0

    ; sum(x, 5)
    iload 0
    ldc 5
    invokestatic Parameters/sum(II)V ; delta = -2

    return
    .limit locals 1
    .limit stack  2
.end method

