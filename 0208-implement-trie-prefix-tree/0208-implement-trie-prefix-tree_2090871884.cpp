struct TrieNode {
    TrieNode* children[26] = {nullptr};
    bool isEnd = false;
};

class Trie {
private:
    TrieNode* head;
public:
    Trie() {
        head = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* cur = head;
        for (char c: word) {
            int idx = c - 'a';
            if (cur->children[idx] == nullptr) {
                cur->children[idx] = new TrieNode();
            }
            cur = cur->children[idx];
        }
        cur->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* cur = head;
        for (char c: word) {
            int idx = c - 'a';
            if (cur->children[idx] == nullptr) {
                return false;
            }
            cur = cur->children[idx];
        }
        return cur->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = head;
        for (char c: prefix) {
            int idx = c - 'a';
            if (cur->children[idx] == nullptr) {
                return false;
            }
            cur = cur->children[idx];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */