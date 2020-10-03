$LC1:
        .ascii  "Fizz\000"
$LC2:
        .ascii  "Buzz\000"
$LC0:
        .ascii  "FizzBuzz\000"
main:
        addiu   $sp,$sp,-64
        sw      $31,60($sp)
        sw      $fp,56($sp)
        move    $fp,$sp
        sw      $0,24($fp)
        li      $2,1181286400                 # 0x46690000
        ori     $2,$2,0x7a7a
        sw      $2,28($fp)
        sb      $0,32($fp)
        li      $2,1114963968                 # 0x42750000
        ori     $2,$2,0x7a7a
        sw      $2,36($fp)
        sb      $0,40($fp)
        lui     $2,%hi($LC0)
        lw      $4,%lo($LC0)($2)
        addiu   $3,$2,%lo($LC0)
        lw      $3,4($3)
        sw      $4,44($fp)
        sw      $3,48($fp)
        addiu   $2,$2,%lo($LC0)
        lbu     $2,8($2)
        nop
        sb      $2,52($fp)
$L7:
        lw      $2,24($fp)
        nop
        slt     $2,$2,100
        beq     $2,$0,$L2
        nop

        lw      $3,24($fp)
        li      $2,15                 # 0xf
        bne     $2,$0,1f
        div     $0,$3,$2
        break   7
        mfhi    $2
        bne     $2,$0,$L3
        nop

        addiu   $2,$fp,44
        move    $5,$2
        lui     $2,%hi($LC1)
        addiu   $4,$2,%lo($LC1)
        jal     printf
        nop

        b       $L4
        nop

$L3:
        lw      $3,24($fp)
        li      $2,3                        # 0x3
        bne     $2,$0,1f
        div     $0,$3,$2
        break   7
        mfhi    $2
        bne     $2,$0,$L5
        nop

        addiu   $2,$fp,28
        move    $5,$2
        lui     $2,%hi($LC1)
        addiu   $4,$2,%lo($LC1)
        jal     printf
        nop

        b       $L4
        nop

$L5:
        lw      $3,24($fp)
        li      $2,5                        # 0x5
        bne     $2,$0,1f
        div     $0,$3,$2
        break   7
        mfhi    $2
        bne     $2,$0,$L6
        nop

        addiu   $2,$fp,36
        move    $5,$2
        lui     $2,%hi($LC1)
        addiu   $4,$2,%lo($LC1)
        jal     printf
        nop

        b       $L4
        nop

$L6:
        lw      $5,24($fp)
        lui     $2,%hi($LC2)
        addiu   $4,$2,%lo($LC2)
        jal     printf
        nop

$L4:
        lw      $2,24($fp)
        nop
        addiu   $2,$2,1
        sw      $2,24($fp)
        b       $L7
        nop

$L2:
        move    $2,$0
        move    $sp,$fp
        lw      $31,60($sp)
        lw      $fp,56($sp)
        addiu   $sp,$sp,64
        j       $31
        nop