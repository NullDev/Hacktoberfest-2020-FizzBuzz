// Creates a CSV file with pairs of pseudorandom integers and FizzBuzz
// Author: @pr1metine

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Random;

public class PRFBCSVGenerator {
    static final long SEED = 694206942069420L;
    static final Path PATH_TO_CSV = FileSystems.getDefault().getPath("fizzBuzz.csv");

    private PRFBCSVGenerator() {
    }

    public static void generateCSV() throws IOException {
        Random gen = new Random(SEED);
        StringBuilder builder = new StringBuilder();

        for (int i = 1; i <= 100; i++) {
            builder.append(gen.nextInt(6942069));
            builder.append(',');
            if (i % 3 == 0 || i % 5 == 0) {
                if (i % 3 == 0)
                    builder.append("fizz");
                if (i % 5 == 0)
                    builder.append("buzz");
            } else {
                builder.append(i);
            }
            builder.append('\n');
        }

        Files.writeString(PATH_TO_CSV, builder);
        System.out.println("CSV file generated and stored in:");
        System.out.println(PATH_TO_CSV.toAbsolutePath().toString());
        System.out.println("Now run `java PseudoRandomFizzBuzz.java` again.");
    }

    public static void main(String[] args) {
        try {
            generateCSV();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
