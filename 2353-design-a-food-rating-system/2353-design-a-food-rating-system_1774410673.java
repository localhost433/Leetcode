class FoodRatings {
    private static final class FoodKey {
        String name;
        int rating;
        FoodKey(String name, int rating) {
            this.name = name;
            this.rating = rating;
        }
    }

    private final Map<String, String> foodToCuisine = new HashMap<>();
    private final Map<String, Integer> foodToRating = new HashMap<>();
    private final Map<String, TreeSet<FoodKey>> cuisineToSet = new HashMap<>();
    private final Map<String, FoodKey> foodToNode = new HashMap<>();
    private static final Comparator<FoodKey> BY_RATING_DESC_NAME_ASC =
        (a, b) -> {
            if (a.rating != b.rating) return Integer.compare(b.rating, a.rating);
            return a.name.compareTo(b.name);
        };

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        int n = foods.length;
        for (int i = 0; i < n; i++) {
            String f = foods[i];
            String c = cuisines[i];
            int r = ratings[i];

            foodToCuisine.put(f, c);
            foodToRating.put(f, r);

            FoodKey node = new FoodKey(f, r);
            foodToNode.put(f, node);

            cuisineToSet
                .computeIfAbsent(c, k -> new TreeSet<>(BY_RATING_DESC_NAME_ASC))
                .add(node);
        }
    }

    public void changeRating(String food, int newRating) {
        int old = foodToRating.get(food);
        if (old == newRating) return; // no-op

        String cuisine = foodToCuisine.get(food);
        TreeSet<FoodKey> set = cuisineToSet.get(cuisine);

        FoodKey node = foodToNode.get(food);

        set.remove(node);
        node.rating = newRating;
        set.add(node);

        foodToRating.put(food, newRating);
    }

    public String highestRated(String cuisine) {
        return cuisineToSet.get(cuisine).first().name;
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */