  class Solution {
      public List<List<Integer>> generate(int numRows) {
          List<List<Integer>> total = new ArrayList<>(numRows);
          total.add(List.of(1));
          if (numRows == 1) return total;
          total.add(List.of(1,1));
          for (int i=2; i< numRows; i++){
              List<Integer> last = total.get(total.size()-1);
              ArrayList<Integer> cur = new ArrayList<>(i);
              cur.add(1);
              for (int j=0; j<i-1; j++){
                  cur.add(last.get(j) + last.get(j+1));
              }
              cur.add(1);
              total.add(cur);
          }
          return total;
      }
  }