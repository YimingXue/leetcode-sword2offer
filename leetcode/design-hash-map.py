#
# @lc app=leetcode.cn id=706 lang=python
#
# [706] Design HashMap
#
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = list()
        self.values = list()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
            return 
        self.keys.append(key)
        self.values.append(value)
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.values.pop(index)
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# # C++写法
# class MyHashMap {
# public:
#     vector<int> keys;
#     vector<int> values;
#     /** Initialize your data structure here. */
#     MyHashMap() {
        
#     }
    
#     /** value will always be non-negative. */
#     void put(int key, int value) {
#         vector<int>::iterator iter = find(this->keys.begin(), this->keys.end(), key);
#         if (iter == this->keys.end()){
#             this->keys.push_back(key);
#             this->values.push_back(value);
#             return;
#         }
#         int index = iter - this->keys.begin();
#         this->values[index] = value;
#         return;
#     }
    
#     /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
#     int get(int key) {
#         vector<int>::iterator iter = find(this->keys.begin(), this->keys.end(), key);
#         if (iter == this->keys.end()) return -1;
#         int index = iter - this->keys.begin();
#         return this->values[index];
#     }
    
#     /** Removes the mapping of the specified value key if this map contains a mapping for the key */
#     void remove(int key) {
#         vector<int>::iterator iter = find(this->keys.begin(), this->keys.end(), key);
#         if (iter != this->keys.end()){
#             int index = iter - this->keys.begin();
#             this->keys.erase(iter);
#             this->values.erase(this->values.begin()+index);
#         }
#         return;
#     }
# };

# /**
#  * Your MyHashMap object will be instantiated and called as such:
#  * MyHashMap* obj = new MyHashMap();
#  * obj->put(key,value);
#  * int param_2 = obj->get(key);
#  * obj->remove(key);
#  */

