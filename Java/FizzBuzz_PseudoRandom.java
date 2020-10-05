// FizzBuzz using pseudorandom generated numbers
// Author: @pr1metine

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.Random;
import java.util.stream.Collectors;

/** "PSRF" */
public class PseudoRandomFizzBuzz {

    Map<Integer, String> fizzBuzzMap;
    static final long SEED = 694206942069420L;
    static final Path PATH_TO_CSV = FileSystems.getDefault().getPath("fizzBuzz.csv");

    public void initMap() throws IOException {
        fizzBuzzMap = Files.lines(PATH_TO_CSV)
            .filter(s -> s.matches("^\\d+,\\w+"))
            .collect(Collectors.toMap(k -> Integer.parseInt(k.split(",")[0]), v -> v.split(",")[1]));
    }

    public static void main(String[] args) {
        try {
            PseudoRandomFizzBuzz fizzBuzz = new PseudoRandomFizzBuzz();
            fizzBuzz.initMap();
            Random gen = new Random(SEED);
            gen.ints(100L, 0, 6942069)
                .mapToObj(fizzBuzz.fizzBuzzMap::get)
                .forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
            System.err.println("Does the CSV file containing the content of the HashMap exist, i. e. \"fizzBuzz.csv\"?");
            System.err.println("If that's not the case please run `java PRFBCSVGenerator.java`");
        }
    }

}
