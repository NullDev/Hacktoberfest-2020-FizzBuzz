#SGopinath89
#MIPS while loop code for FizzBuzz
	.text
main:
	li $t0,1
	li $t1,101
	li $t3,3
	li $t4,5
	li $t5,15
	loop:
		bge $t0,$t1,stop
			
			div	$t0, $t5
			mfhi $t2
			
			bne $t2,0,elseif2
			li $v0,4
			la $a0,msg3
			syscall
			j	stopif
			
			elseif2:
			div	$t0, $t4
			mfhi $t2
			bne $t2,0,elseif3
			li $v0,4
			la $a0,msg2
			syscall
			j	stopif
			
			elseif3:
			div	$t0, $t3
			mfhi $t2
			bne $t2,0,else
			li $v0,4
			la $a0,msg1
			syscall
			j	stopif
			
		else:
			li $v0,1
			move $a0,$t0
			syscall
			
		stopif:
			addi $t0,$t0,1

			li $v0,11
			li $a0,'\n'
			syscall

			j loop
	
	stop:
	jr $ra

	
	.data
 msg1: .asciiz "Fizz"
 msg2: .asciiz "Buzz"
 msg3: .asciiz "FizzBuzz"