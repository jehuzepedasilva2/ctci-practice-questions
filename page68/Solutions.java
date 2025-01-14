package page68;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class Solutions {


  public void printIntegerSolutions() {
   int n = 2;
   HashMap<Integer, ArrayList<ArrayList<Integer>>> map = new HashMap<>();
   for (int c = 1; c <= n; c++) {
    for (int d = 1; d <= n; d++) {
      int result = (c*c*c) + (d*d*d);
      ArrayList<Integer> pair = new ArrayList<>();
      pair.add(c);
      pair.add(d);
      if (map.containsKey(result)) {
        map.get(result).add(pair);
      } else {
        ArrayList<ArrayList<Integer>> newArray = new ArrayList<>();
        newArray.add(pair);
        map.put(result, newArray);
      }
    }
   }

   //  2,011,808

   int  countPairs = 0;

   for (Map.Entry<Integer, ArrayList<ArrayList<Integer>>> entry : map.entrySet()) {
    for (ArrayList<Integer> pair1 : entry.getValue()) {
      for (ArrayList<Integer> pair2 : entry.getValue()) {
        countPairs += 1;
        System.out.print(pair1);
        System.out.print(" ");
        System.out.print(pair2);
        System.out.println("");
      }
    }
   }

   System.out.println(countPairs);

  } 

  public static void main(String[] args) {
    Solutions test = new Solutions();
    test.printIntegerSolutions();
    System.out.println("Done");
  }

}