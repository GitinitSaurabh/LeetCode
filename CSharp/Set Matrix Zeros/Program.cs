public class Solution {
    public void SetZeroes(int[][] matrix) {
        int[] rowArr = new int[matrix.Length];
        int[] colArr = new int[matrix[0].Length];
        
        for(int i=0;i<matrix.Length;i++){
            for(int j=0; j<matrix[0].Length;j++){
                
                if(matrix[i][j] == 0){
                    rowArr[i] = -1; colArr[j] = -1;
                }
            }
        }
        for(int i=0;i<matrix.GetLength(0);i++){
            for(int j=0; j<matrix[i].Length;j++){
                
                if(rowArr[i] == -1 && colArr[j]==-1){
                    matrix = setColZero(j,matrix.Length,matrix);
                    matrix = setRowZero(i,matrix[0].Length,matrix);
                }
            }
        }
    }
public static int[][] setRowZero(int k, int len, int[][] mat){
    
    for(int c=0; c<len;c++ ){
        mat[k][c] = 0;
        }
    return mat;
    }
public static int[][] setColZero(int k, int len, int[][] mat){
    
    for(int r=0; r<len;r++ ){
        mat[r][k] = 0;
        }
    return mat;
    }
}