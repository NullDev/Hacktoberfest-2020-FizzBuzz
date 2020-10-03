// Mix of Numbers
// Author: @kp7742

fn main() {
	fbz := [0b1000110, 0o151, 122, 0x7A, 0x42, 117, 0o172, 0b1111010]
	for i in 0..0x65 {
		x3 := i % 0x3 == 0b00000000
		x5 := i % 0b00000101 == 0x0
		if x3 && x5 {
			for n in fbz {print(byte(n).str())}println('')
		}
		else if x3 {
			for n in fbz[0..(fbz.len/2)] {print(byte(n).str())}println('')
		}
		else if x5 {
			for n in fbz[(fbz.len/2)..(fbz.len)] {print(byte(n).str())}println('')
		}
		else {
			println(i)
		}
	}
}
