.source String.src
.class  public String
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static main([Ljava/lang/String;)V

    ; constant

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc    "enter something:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    ; input

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokestatic Runtime/readString()Ljava/lang/String;
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    ; variable

    ldc    "bye!"
    astore 0

    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload  0
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    return
    .limit stack  2
    .limit locals 1
.end method

