public class FizzBuzz {
	
	private Integer qtdCount;

	public FizzBuzz(Integer qtdCount) {
		this.qtdCount = qtdCount;
	}
	
	public void fizzBuzz() {
		for(int i = 1; i <= qtdCount; ++i)
			System.out.println(i % 3 == 0 && i % 5 == 0 ? "FizzBuzz" : 
								i % 3 == 0 && i % 5 != 0 ? "Fizz" : 
								i % 3 != 0 && i % 5 == 0 ? "Buzz" : i);
	}
  
	public static void main(String[] args) {
		FizzBuzz fb = new FizzBuzz(100);
		fb.fizzBuzz();
	}

}
