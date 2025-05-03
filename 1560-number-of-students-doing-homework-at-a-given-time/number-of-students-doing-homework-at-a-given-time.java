class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int sum = 0 , len = startTime.length;
        for(int i = 0; i < len;i++){
        if(startTime[i]<=queryTime && endTime[i] >= queryTime )sum+=1;
        }
        return sum; 
    }
}