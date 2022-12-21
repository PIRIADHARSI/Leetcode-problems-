int findGCD(int* nums, int numsSize){
    int min=1000,max=0,gcd;
    for(int i=0;i<numsSize;i++){
        if(nums[i]<min){
            min=nums[i];
        }
        if(nums[i]>max){
            max=nums[i];
        }
    }
    for(int i=1;i<=min && i<=max;++i){
        if(min%i==0 && max%i==0){
            gcd=i;
        }
    }
    return gcd;
}
