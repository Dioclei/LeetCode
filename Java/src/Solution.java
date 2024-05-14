import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.SortedMap;
import java.util.Stack;
import java.util.TreeMap;
import java.util.concurrent.atomic.AtomicBoolean;

import javafx.util.Pair;

class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        // sort the array
        Arrays.sort(nums);
        // starting from both ends, find suitable sum nearest to k but lower than k.
        int i = 0;
        int j = nums.length - 1;
        int sum = -1;
        int finalSum = -1;
        while (i < j) {
            // get a sum. doesn't matter if it's more than k or not.
            sum = nums[i] + nums[j];
            // if sum is valid and more than finalSum, update finalSum
            if (sum < k && sum > finalSum) {
                finalSum = sum;
            }
            // get a next sum close to k
            if (sum < k) {
                // add to try to get a higher sum
                i += 1;
            } else {
                // subtract to try to get a lower sum
                j -= 1;
            }
        }
        return finalSum;
    }

    public int maxWidthOfVerticalArea(int[][] points) {
        // Runtime: O(nlogn), Memory: O(n)
        int[] xValues = new int[points.length];
        int answer = 0;
        // index all the x values
        for (int i = 0; i < points.length; i++) {
            xValues[i] = points[i][0];
        }
        // sort
        Arrays.sort(xValues);
        // find max distance between each value
        for (int z = 1; z < xValues.length; z++) {
            int dist = xValues[z] - xValues[z - 1];
            if (dist > answer) {
                answer = dist;
            }
        }
        return answer;
    }

    public int lengthOfLongestSubstringTwoDistinct(String s) {
        LinkedList<Character> q = new LinkedList<>();
        int count = 0;
        int backCharacterCount = 0;
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (q.size() == 0) {
                q.add(c);
                count += 1;
            } else if (q.size() == 1) {
                if (q.peek() == c) {
                    count += 1;
                } else {
                    q.add(c);
                    count += 1;
                    backCharacterCount += 1;
                }
            } else {
                if (q.peek() == c) {
                    q.remove();
                    q.add(c);
                    count += 1;
                    backCharacterCount = 1;
                } else if (q.peekLast() == c) {
                    count += 1;
                    backCharacterCount += 1;
                } else {
                    // new character
                    q.remove();
                    q.add(c);
                    count = backCharacterCount + 1;
                    backCharacterCount = 1;
                }
            }
            answer = Math.max(answer, count);
        }
        return answer;
    }

    public int maxScore(String s) {
        int left = s.charAt(0) == '0' ? 1 : 0;
        // initialise right
        int right = 0;
        for (int z = 1; z < s.length(); z++) {
            if (s.charAt(z) == '1') {
                right += 1;
            }
        }
        // initialise answer
        int answer = left + right;
        // count zeroes
        for (int i = 1; i < s.length() - 1; i++) {
            char c = s.charAt(i);
            if (c == '0') {
                left += 1;
            } else {
                right -= 1;
            }
            answer = Math.max(answer, (left + right));
        }
        return answer;
    }

    public boolean isPathCrossing(String path) {
        HashMap<Coordinate, Integer> crossedCoordinates = new HashMap<>();
        Coordinate currentCoordinate = new Coordinate(0, 0);
        crossedCoordinates.put(currentCoordinate, 1);
        for (int i = 0; i < path.length(); i++) {
            char direction = path.charAt(i);
            if (direction == 'N') {
                currentCoordinate = currentCoordinate.moveNorth();
            } else if (direction == 'S') {
                currentCoordinate = currentCoordinate.moveSouth();
            } else if (direction == 'E') {
                currentCoordinate = currentCoordinate.moveEast();
            } else {
                currentCoordinate = currentCoordinate.moveWest();
            }
            // log coordinate in hashmap
            if (crossedCoordinates.containsKey(currentCoordinate)) {
                return true;
            } else {
                crossedCoordinates.put(currentCoordinate, 1);
            }
        }
        return false;
    }

    class Coordinate {
        private int x;
        private int y;
        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public Coordinate moveNorth() {
            return new Coordinate(this.x, this.y + 1);
        }
        public Coordinate moveSouth() {
            return new Coordinate(this.x, this.y - 1);
        }
        public Coordinate moveEast() {
            return new Coordinate(this.x + 1, this.y);
        }
        public Coordinate moveWest() {
            return new Coordinate(this.x - 1, this.y);
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == null) {
                return false;
            } else if (obj instanceof Coordinate) {
                Coordinate c = (Coordinate) obj;
                return this.x == c.x && this.y == c.y;
            } else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            return 10 * this.x + this.y;
        }
    }

    public int minOperations(String s) {
        int operations = 0; // ideal: 0101010...
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ((i % 2 == 0 && c == '1') || (i % 2 == 1 && c == '0')) {
                operations += 1;
            }
        }
        return Math.min(operations, s.length() - operations);
    }

    public int numDecodings(String s) {
        // recursive, O(2^n) solution, gives Time Limit Exceeded
        HashMap<String, Boolean> check = new HashMap<>();
        check.put("10", true);
        check.put("11", true);
        check.put("12", true);
        check.put("13", true);
        check.put("14", true);
        check.put("15", true);
        check.put("16", true);
        check.put("17", true);
        check.put("18", true);
        check.put("19", true);
        check.put("20", true);
        check.put("21", true);
        check.put("22", true);
        check.put("23", true);
        check.put("24", true);
        check.put("25", true);
        check.put("26", true);
        return numDecodingsHelper(s, 0, s.length(), check);
    }

    private int numDecodingsHelper(String s, int startIndex, int totalLength, HashMap<String, Boolean> check) {
        int realLength = totalLength - startIndex;
        if (s.charAt(0 + startIndex) == '0') { // rubbish input
            return 0;
        } else if (realLength == 1) {
            return 1;
        } else if (realLength == 2) {
            return check.containsKey(s.substring(startIndex)) ? 1 + numDecodingsHelper(s, startIndex + 1, totalLength, check) : 1;
        }
        // check if first two characters are possible number
        if (check.containsKey(s.substring(0 + startIndex, 2 + startIndex))) {
            return numDecodingsHelper(s, startIndex + 1, totalLength, check) + numDecodingsHelper(s, startIndex + 2, totalLength, check);
        }
        return numDecodingsHelper(s, startIndex + 1, totalLength, check);
    }

    public int minCost(String colors, int[] neededTime) {
        int result = 0;
        char currentColor = colors.charAt(0);
        int currentColorTotalTime = neededTime[0];
        int currentKeptBalloonTime = neededTime[0];
        for (int i = 1; i < colors.length(); i++) {
            char color = colors.charAt(i);
            int time = neededTime[i];
            if (color == currentColor) {
                currentColorTotalTime += time;
                // keep the balloon which takes the longest time to remove
                currentKeptBalloonTime = Math.max(currentKeptBalloonTime, time);
            } else {
                // new color, need to log the minimum time needed to remove the previous color
                // difference between currentColorTotalTime and currentKeptBalloonTime is the time needed to remove the balloons
                if (color != currentColor) {
                    result += (currentColorTotalTime - currentKeptBalloonTime);
                }
                // initialise new color by resetting values
                currentColor = color;
                currentColorTotalTime = time;
                currentKeptBalloonTime = time;
            }
        }
        // log the final minimum time for the last color
        result += (currentColorTotalTime - currentKeptBalloonTime);
        return result;
    }

    /*
    public int getLengthOfOptimalCompression(String s, int k) {
        return getLengthOfOptimalCompression(s.toCharArray(), k);
    }
    private int getLengthOfOptimalCompression(char[] cs, int k) {
        int minimum = runLengthEncodeLength(cs);
        if (k == 0) {
            return minimum;
        }
        ArrayList<Integer> possibleRemovedIntegers = new ArrayList<>();
        for (int i = 0; i < cs.length; i++) {
            // remove the character
            if (cs[i] == 0) {
                continue;
            }
            char removedChar = cs[i];
            cs[i] = 0;
            int length = runLengthEncodeLength(cs);
            if (length < minimum) {
                possibleRemovedIntegers.clear();
                possibleRemovedIntegers.add(i);
                minimum = length;
            } else if (length == minimum) {
                possibleRemovedIntegers.add(i);
            }
            // restore the character
            cs[i] = removedChar;
        }
        // find the minimum from the possible options
        for (int z = 0; z < possibleRemovedIntegers.size(); z++) {
            char[] next = Arrays.copyOf(cs, cs.length);
            next[possibleRemovedIntegers.get(z)] = 0;
            int length = getLengthOfOptimalCompression(next, k - 1);
            if (length < minimum) {
                minimum = length;
            }
        }
        return minimum;
    }
    */

    private int runLengthEncodeLength(char[] s) {
        int count = 0;
        int result = 0;
        char currentCharacter = s[0];
        for (int i = 0; i < s.length; i++) {
            char c = s[i];
            if (c == 0) { // skip character
                continue;
            }
            if (c == currentCharacter) {
                count += 1;
            } else {
                result += count > 1 ? 1 + Integer.toString(count).length() : 1;
                currentCharacter = c;
                count = 1;
            }
        }
        if (count == 0) {
            return 0;
        }
        result += count > 1 ? 1 + Integer.toString(count).length() : 1;
        return result;
    }

    public int getLengthOfOptimalCompression(String s, int k) {
        char[] original = s.toCharArray();
        char[] current = new char[original.length];
        HashMap<DP, Integer> hash = new HashMap<>();
        return getLengthOfOptimalCompressionHelper(hash, original, current, 0, k);
    }

    private int getLengthOfOptimalCompressionHelper(
            HashMap<DP, Integer> hash,
            char[] original,
            char[] current,
            int currentIndex,
            int k) {
        DP dp = new DP(current, currentIndex, k);
        if (hash.containsKey(dp)) {
            return hash.get(dp);
        }
        if (currentIndex == original.length) {
            int result = runLengthEncodeLength(current);
            hash.put(dp, result);
            return result;
        }
        if (k == 0) {
            // could be more efficient by taking the rest of the string
            char[] choice = current.clone();
            choice[currentIndex] = original[currentIndex];
            return getLengthOfOptimalCompressionHelper(hash, original, choice, currentIndex + 1, k);
        }
        char[] choice1 = current.clone();
        choice1[currentIndex] = 0;
        char[] choice2 = current.clone();
        choice2[currentIndex] = original[currentIndex];
        return Math.min(
                getLengthOfOptimalCompressionHelper(hash, original, choice1, currentIndex + 1, k - 1),
                getLengthOfOptimalCompressionHelper(hash, original, choice2, currentIndex + 1, k)
        );
    }

    class DP {
        char[] current;
        int currentIndex;
        int k;
        DP(char[] current, int currentIndex, int k) {
            this.current = current;
            this.currentIndex = currentIndex;
            this.k = k;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == null) {
                return false;
            } else if (obj instanceof DP) {
                return this.k == ((DP) obj).k
                        && this.currentIndex == ((DP) obj).currentIndex
                        && this.current.equals(((DP) obj).current);
            } else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            int result = Objects.hash(currentIndex, k);
            result = 31 * result + Arrays.hashCode(current);
            return result;
        }
    }

    public boolean makeEqual(String[] words) {
        HashMap<Character, Integer> hash = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                Character c = words[i].charAt(j);
                hash.put(c, hash.getOrDefault(c, 0) + 1);
            }
        }
        return hash.values().stream().reduce(true, (bool, i) -> bool && (i % words.length == 0), (a, b) -> a && b);
    }

    public int maxLengthBetweenEqualCharacters(String s) {
        int longestLength = -1;
        int[] earliest = new int[26];
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (earliest[c] == 0) {
                earliest[c] = i;
            } else {
                longestLength = Math.max(i - earliest[c] - 1, longestLength);
            }
        }
        return longestLength;
    }

    public List<List<Integer>> findWinners(int[][] matches) {
        TreeMap<Integer, Integer> losses = new TreeMap<>();
        for (int i = 0; i < matches.length; i++) {
            int winner = matches[i][0];
            int loser = matches[i][1];
            losses.putIfAbsent(winner, 0);
            losses.putIfAbsent(loser, 0);
            losses.put(loser, losses.get(loser) + 1);
        }
        List<Integer> players = new ArrayList<Integer>(losses.keySet());
        List<Integer> zeros = new ArrayList<>();
        List<Integer> ones = new ArrayList<>();
        for (int i = 0; i < players.size(); i++) {
            int player = players.get(i);
            int loss = losses.get(player);
            if (loss == 0) {
                zeros.add(player);
            } else if (loss == 1) {
                ones.add(player);
            }
        }
        ArrayList<List<Integer>> result = new ArrayList<>();
        result.add(zeros);
        result.add(ones);
        return result;
    }

    public boolean isInteger(String s) {
        try {
            Integer.parseInt(s);
            return true;
        } catch(NumberFormatException e) {
            return false;
        }
    }

    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ']') {
                // pop everything until [, then multiply by the number
                StringBuilder sb = new StringBuilder();
                while (!stack.peek().equals("[")) {
                    sb.insert(0, stack.pop());
                }
                stack.pop(); // remove the [
                StringBuilder n = new StringBuilder();
                while (!stack.isEmpty() && isInteger(stack.peek())) {
                    n.insert(0, stack.pop());
                }
                StringBuilder f = new StringBuilder();
                int num = Integer.parseInt(n.toString());
                for (int j = 0; j < num; j++) {
                    f.append(sb);
                }
                stack.push(f.toString());
            } else {
                stack.push(String.valueOf(c));
            }
        }
        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.insert(0, stack.pop());
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.decodeString("3[a]2[bc]"));
    }
}
