// Link - https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

int subtractProductAndSum(int num){
    int sum = 0, product = 1;
    int mod, result;

    while(num > 0){
        mod = num%10;
        sum += mod;
        product *= mod;
        num /= 10;
    }

    result = product - sum;

    return result;
}

