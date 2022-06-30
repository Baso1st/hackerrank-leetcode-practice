#https://leetcode.com/problems/search-suggestions-system/
#1268. Search Suggestions System


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        result = []
        
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            filtered = [x for x in products if x[:i] == prefix]
            filtered.sort()
            result.append(filtered[:3])
            
        return result
        



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        table = {}
        
        for prod in products:
            for i in range(1, len(prod)+1):
                prefix = prod[:i]
                if prefix in table:
                    table[prefix].append(prod)
                else:
                    table[prefix] = [prod]
        
        
        result = []
        
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            if prefix in table:
                sorted_words = sorted(table[prefix])[:3]
                result.append(sorted_words)
            else:
                result.append([])
        return result


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        self.prods = products

        result = []
        bs_start = 0
        prefix = ""
        for c in searchWord:
            prefix += c
            start = self.binary_search(bs_start, prefix)

            arr = []
            for prod in products[start:]:
                if not prod.startswith(prefix):
                    break
                if len(arr) == 3:
                    break
                arr.append(prod)
            
            result.append(arr)

            bs_start = start

        return result

        
    def binary_search(self, start, prefix):
        i = start
        j = len(self.prods)
        mid = 0
        while i < j:
            mid = (i + j) // 2
            if self.prods[mid] >= prefix:
                j = mid
            else:
                i = mid + 1

        return i





if __name__ == '__main__':
    prods = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    word = 'mouse'
    s = Solution()
    print(s.suggestedProducts(prods, word))
