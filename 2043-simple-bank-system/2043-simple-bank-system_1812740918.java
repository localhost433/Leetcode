class Bank {
    private long[] balance;
    
    public Bank(long[] balance) {
        this.balance = balance;
    }

    public boolean valid(int acc) {
        return 1 <= acc && acc <= balance.length;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if (!(valid(account1) && valid(account2))) return false;
        if (money < 0) return false;
        int a = account1 - 1, b = account2 - 1;
        if (balance[a] < money) return false;
        if (a == b) return true;
        balance[a] -= money;
        balance[b] += money;
        return true;
    }
    
    public boolean deposit(int account, long money) {
        if (!valid(account)) return false;
        if (money < 0) return false;
        balance[account - 1] += money;
        return true;
    }
    
    public boolean withdraw(int account, long money) {
        if (!valid(account)) return false;
        if (money < 0) return false;
        int a = account - 1;
        if (balance[a] < money) return false;
        balance[a] -= money;
        return true;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */