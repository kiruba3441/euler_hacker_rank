package euler;

import java.util.ArrayList;
import java.util.List;

public class 8LargestContinousProduct {

	public static Integer maxContinousProduct(List<Integer>input, int k) {
		int kindex = 1, i = 0;
		int maxProduct = 0;
		int continProduct = 0;
		while (i < input.size()) {
			
			if (input.get(i) != 0) {
				if (continProduct == 0)
					continProduct = input.get(i);
				else {
					continProduct = (continProduct * input.get(i));
				}

				if (kindex == k) {
					maxProduct = Math.max(continProduct, maxProduct);
				} else if (kindex > k) {
					continProduct /= (input.get(i-k));
					maxProduct = Math.max(continProduct, maxProduct);
				}
				kindex++;
			} else {
				continProduct = 0;
				kindex = 1;
			}
			i++;
		}
		return maxProduct;
	}

	public static void main(String[] args) {
		List<Integer> inputList = new ArrayList<>();
		"2709360626".chars().forEach((c)->{
			inputList.add(c-'0');
		});
        //3675356291
		System.out.println(inputList);
		System.out.println(maxContinousProduct(inputList,5));
	}
}
