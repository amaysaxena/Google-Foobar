/**
 * Created by amaysaxena on 03/09/2017.
 */
import java.util.*;

class Answer {
    private static HashSet<Node> leafNodes = new HashSet<>();

    static class Node implements Comparable<Node> {
        private Set<Node> children;
        private Integer value;
        private int depth;
        private int minChild;

        Node(int i){
            value = i;
            children = new HashSet<>();
            minChild = Integer.MAX_VALUE;
        }

        public int compareTo(Node n) {
            return (this.value - n.value);
        }

        void makeRoot() {
            depth = 0;
        }

        void addChild(Node i) {
            this.children.add(i);
            i.depth = this.depth + 1;

            if (i.value < minChild) minChild = i.value;

            if (Answer.leafNodes.contains(this)) {
                Answer.leafNodes.remove(this);
            }

            Answer.leafNodes.add(i);
        }

        private Set<Node> getDivisibleChildren(int y) {
            //Set<Node> list = new TreeSet<>(this.children).headSet(new Node(y), true);
            Set<Node> list = this.children;
            Set<Node> returnList = new HashSet<>();
            for (Node x : list) {
                if (y % x.value == 0) returnList.add(x);
            }
            return returnList;
        }
    }

    public static void insert(Node sentinel, int y) {
        Deque<Node> fringe = new ArrayDeque<>();
        fringe.addFirst(sentinel);

        while(!fringe.isEmpty()) {
            Node currNode = fringe.removeFirst();

            if (y < currNode.minChild) {
                currNode.addChild(new Node(y));
                continue;
            }

            Set<Node> currChildren = currNode.getDivisibleChildren(y);

            if (currChildren.isEmpty()) {
                currNode.addChild(new Node(y));
            } else {
                fringe.addAll(currChildren);
            }
        }
    }

    public static int numTriplesInBranch(int n) {
        return (n * (n-1) * (n-2)) / 6;
    }

    public static int answer(int[] l) {
        //Arrays.sort(l);
        Node sentinel = new Node(Integer.MIN_VALUE); //assign any value to the sentinel node. This weill be the root
        sentinel.makeRoot();
        int numTriples = 0;

        for (int y : l) {
            insert(sentinel, y);
        }

        for (Node n : Answer.leafNodes) {
            numTriples += numTriplesInBranch(n.depth);
            System.out.print("(" + n.value.toString() + ", " + n.depth + ") ");
        }
        return numTriples;
    }

    public static void main(String[] args) {
        System.out.println(5/2);
    }
}