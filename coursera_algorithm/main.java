class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
    QF QquickFind = new QF(10);
    QquickFind.union(4, 3);
    QquickFind.union(4, 3);
    QquickFind.union(3, 8);
    QquickFind.union(6, 5);
    // 0 1 2 3 4
    // 5 6 7 8 9
    QquickFind.union(9, 4);
    QquickFind.union(2, 1);
    // QquickFind.connected(0, 7);
    System.out.println("QquickFind.connected(0, 7) " + QquickFind.connected(0, 7));
    System.out.println("QquickFind.connected(8, 9) " + QquickFind.connected(8, 9));
    QquickFind.union(5, 0);
    QquickFind.union(7, 2);
    QquickFind.union(6, 1);
    QquickFind.union(1, 0);
    System.out.println("QquickFind.connected(0, 7) " + QquickFind.connected(0, 7));
  }
  
}

class QF {
  private int[] ids;
  
  // constructor with number of elements
  public QF(int N){
    ids = new int[N];
    for(int i = 0; i < N; i++){
      ids[i] = i;
    }  
  }
  
  public boolean connected(int p, int q){
    for (int i:ids)
      System.out.print(i + " ");
    System.out.println("");
    
    return ids[p] == ids[q];
  }
  
  public void union(int p, int q){
    if(connected(p, q)) return; // guard clouse
    // p & q connected means have same ids
    System.out.println("union of " + p + " and " + q);
    int pId = ids[p];
    
    for(int i =0; i < ids.length; i++){
      if(ids[i] == pId)
        ids[i] = ids[q];
    }
    
  }
  
}
