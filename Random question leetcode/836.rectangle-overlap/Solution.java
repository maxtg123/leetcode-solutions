class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        return !(rec1[2] <= rec2[0] ||  // rec1 hoàn toàn bên trái rec2
                 rec2[2] <= rec1[0] ||  // rec2 hoàn toàn bên trái rec1
                 rec1[3] <= rec2[1] ||  // rec1 hoàn toàn dưới rec2
                 rec2[3] <= rec1[1]);   // rec2 hoàn toàn dưới rec1
    }
}
